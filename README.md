# Arches for HERs

## What is Arches for HERs

Arches for HERs is a comprehensive data management platform for UK Historic Environment Records (HERs). Arches for HERs is purpose-built for HERs and any organization that conforms to the standards specified by the Forum for Information Standards in Heritage (FISH), including MIDAS Heritage.

You can find out more about Arches for HERs at [https://www.archesproject.org/arches-for-hers/](https://www.archesproject.org/arches-for-hers/)


## How do I get started with Arches for HERs


1. Clone the arches-her repo, making sure to change the default target folder to **arches_her** and then run pip install:

   ```
   pip install -r ./arches_her/arches_her/install/requirements.txt
   ```

   If you are installing Arches for HERs on Windows, follow the [instructions relating to the GDAL_LIBRARY_PATH](https://arches.readthedocs.io/en/latest/installing/installation/#common-errors) detailed in the Installing Core Arches documentation.  

1. Set up your database and load the package with the following command in the arches_her directory:

   ```
   python manage.py packages -o load_package -s <path_to_arches_her_directory>/arches_her/arches_her/pkg -db -y
   ```

1. Start the Arches for HERs project

   ```
   python manage.py runserver
   ```

1. Install and build front-end dependencies

   Before you can use browse the application you will need to build the front end asset bundle. From the directory containing the package.json file ([workspace]/arches_her/arches_her)

   ```
   yarn install
   yarn build_development
   ```

This will allow you to run the application locally, but is not suitable for running on a web server. Please see the guidance for deploying an Arches project like Arches for HERs into a server environment.

   https://arches.readthedocs.io/en/latest/deployment/
   

### Setting up a development environment

If you are setting up a development enviornment then please see the Arches documentation on how to do this:

   https://arches.readthedocs.io/en/latest/installing/installation/

You will need to use the dev/7.5.x branch for the arches repository.

The **arches_her/install/requirements.txt** file will also need to be edited in order to remove the `arches==7.5.1` requirement, as you will have cloned and installed the arches core code seperately.



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




