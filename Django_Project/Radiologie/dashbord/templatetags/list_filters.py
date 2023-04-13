from django import template

register = template.Library()

@register.filter
def at_index(lst, index):
    return lst[index]