# Django Dropimages #
Uses [Dropzone.js](http://www.dropzonejs.com/) and [django-braces](https://github.com/brack3t/django-braces) to simplify the upload of multiple images into a collection object.

! warning, this will become production code but it's still in its early development (won't work)

## Documentation
todo

## Installation
Install from PyPI with `pip`:
`pip install django-dropimages`

## Examples
To navigate the examples pages (assuming you use virtualenvwrapper) :

    mkvirtualenv django-dropimages
    pip install example/requirements.txt
    add2virtualenv .
    python example/manage.py migrate
    python example/manage.py runserver