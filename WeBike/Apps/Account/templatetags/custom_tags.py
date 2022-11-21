from django import template

register = template.Library()


@register.simple_tag
def define_break(value=None):
    return value
