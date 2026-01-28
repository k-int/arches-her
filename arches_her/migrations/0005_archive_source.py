from django.db import migrations, models
from django.utils.translation import gettext as _


class Migration(migrations.Migration):

    dependencies = [("arches_her", "0004_update_plugins")]

    def add_reports(apps, schema_editor):
        ReportTemplate = apps.get_model("models", "ReportTemplate")

        ReportTemplate.objects.update_or_create(
            name="Archive Source Template",
            component="views/components/reports/archive-source",
            defaultconfig={"uncompacted_reporting": True},
            description="Archive source report",
            componentname="archive-source-report",
            templateid="75e5968a-72cf-4a07-8e0d-1cc3e81d34c8",
            preload_resource_data=False,
        )

    def update_graph_template(apps, schema_editor):
        """
        UPDATE graphs SET templateid = '75e5968a-72cf-4a07-8e0d-1cc3e81d34c8' WHERE graphid = 'b07cfa6f-894d-11ea-82aa-f875a44e0e11';
        """


    operations = [
        migrations.RunPython(add_reports, reverse_code=migrations.RunPython.noop),
        migrations.RunSQL(update_graph_template, reverse_code=migrations.RunPython.noop),
    ]
