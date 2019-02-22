from django import template

register = template.Library()

@register.filter(name='replace')
def replacement(value,arg):
    """
    REPLACE GIVEN VALUE in arg  FORM STRING

    """

    return value.replace(arg,'')
