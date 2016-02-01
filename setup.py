from io import open

from setuptools import find_packages, setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    print "README.md succesfully converted"
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='django-dropimages',
    version='0.1.5',
    description='Uses Dropzone.js and django-braces to simplify the upload of multiple images into a collection object.',
    long_description=long_description,
    author='Simone Cittadini',
    author_email='simone@sig-c.com',
    url='https://github.com/sittizen/django_dropimages',
    download_url='https://pypi.python.org/pypi/django-dropimages',
    license='MIT',
    packages=find_packages(exclude=('tests.*', 'tests', 'example')),
    install_requires=[
        'Django>=1.7',
        'django-braces<1.9',
        'Pillow'
    ],
    include_package_data=True,
    zip_safe=False,                 # because we're including static files
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
