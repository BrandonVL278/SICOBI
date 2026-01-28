
from django.utils.html import format_html
from django import template

register = template.Library()


@register.filter(name='custom_label')
def custom_label(field):
    return field.label_tag(attrs={'class': "w-fit pl-0.5 text-sm"})

@register.filter(name='custom_errors')
def custom_errors(field):
    html = ''
    if field.errors:
        html += f'<div class="text-sm text-red-600 mt-2">'
        for error in field.errors:
            html += f'<p>{error}</p>'
        html += '</div>'
    return format_html(html)

@register.filter(name='custom_text')
def custom_text(field):
    custom = "w-full rounded-radius border border-outline bg-surface-alt px-2 py-2 text-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:cursor-not-allowed disabled:opacity-75"
    if field.errors: custom = "w-full rounded-radius border border-danger bg-surface-alt px-2 py-2 text-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:cursor-not-allowed disabled:opacity-75" 

    if field.field.__class__.__name__ == 'BooleanField':
        custom = "text-primary focus:ring-primary"

    return field.as_widget(attrs={'class': custom})

@register.inclusion_tag('widgets/custom_multiselect_field.html')
def custom_multiselect_field(field):
    return {
        'field': field,
    }
