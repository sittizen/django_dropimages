import uuid

from django import template
from django.template import Context

from django_dropimages import settings as di_settings

register = template.Library()


@register.tag(name="drop_images_js")
def drop_images_js(parser, token):
    return DropImagesJSNode()


class DropImagesJSNode(template.Node):
    def render(self, context):
        t = template.loader.get_template('django_dropimages/dropimagesjs.html')
        return t.render(Context({
            'gallery_id': uuid.uuid4(),
            'dict_default_message': di_settings.CONFIG['DICT_DEFAULT_MESSAGE'],
        }))


@register.tag(name="drop_images")
def drop_images(parser, token):
    return DropImagesNode()


class DropImagesNode(template.Node):
    def render(self, context):
        t = template.loader.get_template('django_dropimages/dropimages.html')
        return t.render(Context({}))
