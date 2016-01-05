# Django Dropimages #
Uses [Dropzone.js](http://www.dropzonejs.com/) and [django-braces](https://github.com/brack3t/django-braces) to simplify the upload of multiple images into a collection object.

! warning, this will become production code but it's still in its early development (code isn't packaged yet)

## Documentation
Add 'django_dropimages' to the list of installed apps.

Add *{% load drop_images %}* at the start of the template, *{% drop_images_js %}* where the javascripts are loaded,
and *{% drop_images  %}* where you want the dropzone to show.

Each image file dropped into the dropzone will create a *DropimagesImage* model, contained in a *DropimagesGallery* unique for every dropzone instance.

## Installation
Install from PyPI with `pip`:
`pip install django-dropimages`

## Examples
To navigate the example page (assuming you use [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)) :

    mkvirtualenv django-dropimages
    pip install example/requirements.txt
    add2virtualenv .
    python example/manage.py migrate
    python example/manage.py runserver