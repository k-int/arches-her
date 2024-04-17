# Arches for HERs

## What is Arches for HERs

Arches for HERs is a comprehensive data management platform for UK Historic Environment Records (HERs). Arches for HERs is purpose-built for HERs and any organization that conforms to the standards specified by the Forum for Information Standards in Heritage (FISH), including MIDAS Heritage.

You can find out more about Arches for HERs at [https://www.archesproject.org/arches-for-hers/](https://www.archesproject.org/arches-for-hers/)


## How Do I Set Up Arches for HERs

Arches for HERs requires Arches 7.5.1

1. To install Core Arches clone the arches-her repo as **arches_her** and then run pip install:

```
git clone https://github.com/archesproject/arches-her.git arches_her
pip install -r ./arches_her/arches_her/install/requirements.txt
```


**❗️ If you need to make changes to the Arches Core code, follow the [Installing Core Arches](https://arches.readthedocs.io/en/latest/installing/installation/) instructions in the Arches Documentation Guide to install Arches 7.5.1.

Once you have installed Core Arches at the correct version, clone the arches-her repo as a folder named arches_her

``` 
git clone https://github.com/archesproject/arches-her.git arches_her
```

and comment out the arches=7.5.1 requirement in <path_to_arches_her_directory>/arches_her/arches_her/install/requirements.txt

If you are installing Arches for HERs on Windows, follow the [instructions relating to the GDAL_LIBRARY_PATH](https://arches.readthedocs.io/en/latest/installing/installation/#common-errors) detailed in the Installing Core Arches documentation.  You will need to create a settings_local.py file with the following contents:

```
try:
    from .arches_her.settings import *
except ImportError:
    pass
```

2. Set up your database and load the package with the following command in the arches_her directory:

```
python manage.py packages -o load_package -s <path_to_arches_her_directory>/arches_her/arches_her/pkg -db -y
```

3. Start the Arches for HERs project

```
python manage.py runserver
```

4. Install and build front-end dependencies:

```
cd arches_her
yarn install
yarn build_development
```



## How Do I Configure Arches for HERs

Administrators of an instance of Arches for HERs can configure their implementation having installed the out-of-the-box version.  Ways in which you can configure and customise an instance include:

- Configuring functions against specific graphs.  The initial installation of Arches for HERs includes the following functions:
    - BNG Point to GeoJSON function
    - GeoJSON to BNG Point function
    - Consultation Status function
- Branding and the highlighted content and images on the landing page of the instance
- Branding emails sent by the application
- Setting Accessibility mode to be on
- Configuring basemaps available in your Arches for HERs instance (using the instructions in the [Core Arches Documentation](https://arches.readthedocs.io/en/latest/administering/managing-map-layers/#basemaps-and-overlays)).

**❗️ Please note: you will need to configure a MapBox key in the user interface for the default mapping to appear, as per the [Default Map Settings](https://arches.readthedocs.io/en/latest/configuring/arches-system-settings/#default-map-settings) Core Arches documentation.




