from django.views.generic import View
from django.db import connection
from django.http import HttpResponse


class ApplicationAreas(View):
    def get(self, request, zoom, x, y):
        nodeid = '1909956f-3a3b-11eb-ae99-f875a44e0e11'
        if hasattr(request.user, "userprofile") is not True:
            models.UserProfile.objects.create(user=request.user)
        viewable_nodegroups = request.user.userprofile.viewable_nodegroups
        
        try:
            node = models.Node.objects.get(nodeid=nodeid, nodegroup_id__in=viewable_nodegroups)
            resource_ids = get_restricted_instances(request.user, allresources=True)
            if len(resource_ids) == 0:
                resource_ids.append("10000000-0000-0000-0000-000000000001")  # This must have a uuid that will never be a resource id.
            resource_ids = tuple(resource_ids)
            
            with connection.cursor() as cursor:
                result = cursor.execute(
                    """SELECT ST_AsMVT(tile, 'app-area', 4096, 'geom', 'id') FROM (SELECT tileid,
                        id,
                        resourceinstanceid,
                        nodeid,
                        ST_AsMVTGeom(
                            geom,
                            TileBBox(%s, %s, %s, 3857)
                        ) AS geom,
                        1 AS total
                    FROM geojson_geometries
                    WHERE nodeid = %s and and resourceinstanceid not in %s (geom && ST_TileEnvelope(%s, %s, %s))) AS tile;""",
                    [zoom, x, y, nodeid, resource_ids, zoom, x, y],
                )
                result = bytes(cursor.fetchone()[0]) if result is None else result
            return HttpResponse(result, content_type="application/x-protobuf")
        
        except models.Node.DoesNotExist:
            raise Http404()