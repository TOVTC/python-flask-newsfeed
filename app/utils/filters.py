# here, we will write Jinja (the templating engine for Python in this project) filters as regular Python functions
# expects to receive a datetime object and then use strftime() to convert it to a string (e.g. 01/01/20)
def format_date(date):
    return date.strftime('%m/%d/%y')

# use the following to test this function by running the file directly
# python app/utils/filters.py
# from datetime import datetime
# print(format_date(datetime.now()))

def format_url(url):
    # remove all extraneous information, leaving only the domain name
    # .replace() and .split() function the same as they do in JavaScript
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# use the following to test this function by running the file directly
# python app/utils/filters.py
# print(format_url("http://google.com/test"))
# print(format_url("https://google.com?q=test"))

def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    
    return word

# use the following to test this function by running the file directly
# python app/utils/filters.py
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))