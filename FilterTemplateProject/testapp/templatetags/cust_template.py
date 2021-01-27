from django import template
register=template.Library()

def truncate5(value):
    result=value[0:5]
    return 'keshava'

register.filter('truncate5',truncate5)
