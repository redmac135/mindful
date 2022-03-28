from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='placeholder_classes')
def placeholder_class(value, args):
    placeholder, classes = args.split(',', 1)
    return value.as_widget(attrs={'placeholder': placeholder, 'class': classes})