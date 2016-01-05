# Django Dropimages #
Uses [Dropzone.js](http://www.dropzonejs.com/) and [django-braces](https://github.com/brack3t/django-braces) to simplify the upload of multiple images into a collection object.


## Documentation
Add 'django_dropimages' to the list of installed apps.

Add `{% load drop_images %}` at the start of the template, `{% drop_images_js %}` where the javascripts are loaded,
and `{% drop_images  %}` where you want the dropzone to show.

Each image file dropped into the dropzone will create a `DropimagesImage` model, contained in a `DropimagesGallery` unique for every dropzone instance.

## Installation
Install from PyPI with `pip`:

`pip install --pre django-dropimages`

## Configuration
Provides a setting dictionary that you can add in your project’s settings module to customize its behavior.

### DROP_IMAGES_CONFIG

#### keys:

+ `SHOW_ID_ON_COMPLETE`

    Specify a DOM node id which will be set to 'display: block' once all the files are processed, useful to integrate
    the dropzone into another modelform (see the example).
    
+ `GALLERY_FIELD_ID`

    Specify the id of a select field to be filled with the `DropimagesGallery` Django pk once the upload is complete,
    useful to integrate the dropzone into another modelform (see the example).
    
+ `UPLOAD_URL`

    Overrides the url where file data is POSTed, so you can use your own view to save the data.
    An option `?gallery_id` is automatically appended to the url, which is the same  for every file uploaded but unique 
    among different dropzone instances.

+ `DELETE_URL`

    Overrides the url to ask for immediate image removal from the dropzone, so you can use your own view.
    Two optione are automatically appended to the url; `?gallery_id` which is the same for every file into the dropzone 
    but unique among different dropzone instances, and `original_filename` which should be saved into `DropimagesImage`
    objects to identify them.

+ `DICT_DEFAULT_MESSAGE`

    The message that gets displayed before any files are dropped.
    

## Example
To navigate the example page (assuming you use [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)) :

    mkvirtualenv django-dropimages
    pip install example/requirements.txt
    add2virtualenv .
    python example/manage.py migrate
    python example/manage.py runserver
    
