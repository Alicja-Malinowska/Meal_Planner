import datetime
from urllib.parse import urlparse, urljoin
from flask import Flask, request

WEEK_DAYS = {
    '0': 'Monday',
    '1': 'Tuesday',
    '2': 'Wednesday',
    '3': 'Thursday',
    '4': 'Friday',
    '5': 'Saturday',
    '6': 'Sunday'
}

# this snippet is taken from stack overflow as the link in the offical Flask documentation doesn't work
def is_safe_url(target):
    '''this is used to check if the url is dafe before redirecting to "next"'''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc


def get_week(start_date):
    '''given a start date in datetime format, returns an array of 7 tuples
    each tuple includes a day and day of the week'''
    the_week = [(start_date, WEEK_DAYS[str(start_date.weekday())])]
    for i in range(1, 7):
        next_day = start_date + datetime.timedelta(days=i)
        the_week.append((next_day, WEEK_DAYS[str(next_day.weekday())]))
    return the_week

def get_tags(all_recipes):
    '''gathers tags from the recipes given, without duplicates, sorted alphabetically'''
    all_tags = []
    for recipe in all_recipes:
        tags = recipe["tags"]
        all_tags += tags
    all_recipes.rewind()
    tag_set = sorted(set(all_tags))
    return tag_set
