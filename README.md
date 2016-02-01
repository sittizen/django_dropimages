# Django Dropimages #
Uses [Dropzone.js](http://www.dropzonejs.com/) and [django-braces](https://github.com/brack3t/django-braces) to simplify the upload of multiple images into a collection object.


## Installation
Install from PyPI with `pip`:

`pip install --pre django-dropimages`


## Documentation
Add 'django_dropimages' to the list of installed apps.

Add `url(r'^__dropimages__/', include(django_dropimages.urls)),` to your urls.py

Add `{% load drop_images %}` at the start of the template, `{% drop_images_js %}` where the javascripts are loaded, 
and `{% drop_images  %}` where you want the dropzone to show.

Each image file dropped into the dropzone will create a `DropimagesImage` model, contained in a `DropimagesGallery` 
unique for every dropzone instance.
You can customize in order to specify which model will hold the image instead of `DropimagesImage`, 
or completely override the called urls and use your own logic.

## Configuration
Provides a setting dictionary that you can add in your project’s settings module to customize its behavior.

### DROP_IMAGES_CONFIG

#### keys:

+ `SHOW_ID_ON_COMPLETE`

    Specify a DOM node id which will be set to 'display: block' once all the files are processed, useful to integrate
    the dropzone into another modelform or wizard (see the examples).
    
+ `GALLERY_FIELD_ID`

    Specify the id of a select field to be filled with the `DropimagesGallery` Django instance pk once the upload is 
    complete, useful to integrate the dropzone into another modelform or wizard (see the examples).
    
+ `UPLOAD_URL`

    Overrides the url where file data is POSTed, so you can use your own view to save the data.
    An option `?gallery_id` is automatically appended to the url, which is the same  for every file uploaded but unique 
    among different dropzone instances.

+ `DELETE_URL`

    Overrides the url to ask for immediate image removal from the dropzone, so you can use your own view.
    Two options are automatically appended to the url; `?gallery_id` which is the same for every file into the dropzone 
    but unique among different dropzone instances, and `original_filename` which should be saved into `DropimagesImage`
    or whichever model you use to save images in order to identify them.
    
+ `DROPIMAGE_MODEL`

    Use the specified model ( must be a `appname.ModelName` string ) to save the uploaded images.
    Model must have a ForeignKey to `dropimages.DropImagesGallery` called `dropimages_gallery` and a 
    `dropimages_original_filename` `CharField`.

+ `DROPIMAGE_FIELD`

    Save the image into the specified field name of the `DROPIMAGE_MODEL` model.


+ `DICT_DEFAULT_MESSAGE`

    The message that gets displayed before any files are dropped.
    

## Example
To navigate the example page (assuming you use [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)) :

    mkvirtualenv django-dropimages
    pip install example/requirements.txt
    add2virtualenv .
    python example/manage.py migrate
    python example/manage.py runserver
    