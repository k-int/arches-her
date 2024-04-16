# Arches for HERs

## What is Arches for HERs

Arches for HERs is a comprehensive data management platform for UK Historic Environment Records (HERs). Arches for HERs is purpose-built for HERs and any organization that conforms to the standards specified by the Forum for Information Standards in Heritage (FISH), including MIDAS Heritage.

You can find out more about Arches for HERs at [https://www.archesproject.org/arches-for-hers/](https://www.archesproject.org/arches-for-hers/)


## How Do I Set Up Arches for HERs

Arches for HERs requires Arches 7.5.1

1. To install Core Arches, follow the [Installing Core Arches](https://arches.readthedocs.io/en/latest/installing/installation/) instructions in the Arches Documentation Guide to install Arches 7.5.1.

2. Once you have installed Core Arches at the correct version, clone the arches-her repo as a folder named arches_her.

``` 
git clone https://github.com/archesproject/arches-her.git arches_her
```

2a. If you are installing Arches for HERs on Windows, follow the [instructions relating to the GDAL_LIBRARY_PATH](https://arches.readthedocs.io/en/latest/installing/installation/#common-errors) detailed in the Installing Core Arches documentation.  You will need to create a settings_local.py file with the following contents:

```
try:
    from .arches_her.settings import *
except ImportError:
    pass
```

3. Set up your database with the following command in the arches_her directory:

```
python manage.py setup_db`
```

4. Follow the instructions in Install Core Arches to [Build a Frontend Asset Bundle](https://arches.readthedocs.io/en/latest/installing/installation/#build-a-frontend-asset-bundle).

5. Load the package within the arches_her directory to register the components and graphs, and run required SQL against the database:

```
python manage.py packages -o load_package -s <path_to_arches_her_directory>/arches_her/arches_her/pkg
```


## How Do I Configure Arches for HERs

Administrators of an instance of Arches for HERs can configure their implementation having installed the out-of-the-box version.  Ways in which you can configure and customise an instance include:

- Configuring functions against specific graphs.  The initial installation of Arches for HERs includes the following functions:
    - BNG Point to GeoJSON function
    - GeoJSON to BNG Point function
    - Consultation Status function
- Branding the landing page of the instance
- Branding emails sent by the application
- Setting Accessibility mode to be on
- Configuring basemaps available in your Arches for HERs instance (using the instructions in the [Core Arches Documentation](https://arches.readthedocs.io/en/latest/administering/managing-map-layers/#basemaps-and-overlays)).




