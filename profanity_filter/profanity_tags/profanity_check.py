from django import template
from profanity_filter import ProfanityFilter

pf_check = ProfanityFilter()
register = template.Library()

def word_filter(value):
    value = pf_check.censor(value)
    return value

register.filter('word_filter', word_filter)