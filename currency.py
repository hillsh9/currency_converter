"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: SCOTT HILLMAN
Date: 12/23/20
"""
import introcs

APIKEY = 'uKGDs5s85CpZ9zv93I9guuZSOlQOTdGzmDMvtSH3sLce'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    # Enforce the precondition
    assert type(s) == str, repr(s)+(' is not a string')
    assert ' ' in s, repr(s)+(' is missing a space')

    # find the first space
    first_space = introcs.find_str(s," ")

    # slice the string s from the beginning of s up to first_space
    return s[:first_space]


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    assert ' ' in s, repr(s)+' is missing a space'

    # find the first space
    first_space = introcs.find_str(s," ")

    # slice the string s starting from first_space to the end
    return s[first_space+1:]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is
    a precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it
    only picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside
    """

    # Enforce the precondition
    assert type(s) == str, repr(s)+' is not a string'
    assert introcs.count_str(s,'\"') >= 2

    # find initial quotation mark
    first_quote = introcs.find_str(s,'\"')

    # find complementary quotation mark
    second_quote = introcs.find_str(s,'\"',first_quote+1)

    #returns first_inside_quotes
    return s[first_quote+1:second_quote]


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the
    string inside string quotes (") immediately following the substring '"src"'.
    For example, if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814'
        +'Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States
    Dollars"'). On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is
        invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons.
    The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814
        Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the
    type)
    """

    #Enforce the precondition

    # Find '"src":'
    find_src = introcs.find_str(json, '"src":')

    # Slice off everything before the colon
    new_string = json[find_src+5:]

    #use first_inside_quotes on new_string

    return first_inside_quotes(new_string)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns
    the string inside string quotes (") immediately following the substring
    '"dst"'. For example,if the json is

    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814
    Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"').
    On the other hand if the json is

    '{"success":false,"src":"","dst":"","error":"Source currency code is
    invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons.
    The JSON

    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros",
    "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the
    type)
    """

    #Enforce precondition

    # Find '"dst":'
    find_dst = introcs.find_str(json,'"dst":')

    # Slice off everything before the colon
    new_string_dst = json[find_dst+5:]

    #use first_inside_quotes on new_string
    return first_inside_quotes(new_string_dst)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    #Determine if JSON ends with 'false'
    json = introcs.join(introcs.split(json,' '))
    x = introcs.endswith_str(json,'false',0,16)

    return x


def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    #Enforce preconditions
    assert type(src) == str
    assert type(dst) == str
    assert (type(amt) == float or type(amt) == int) == True

    assert introcs.isalpha(src) == True
    assert introcs.isalpha(dst) == True
    assert (introcs.isfloat(amt) or introcs.isint(amt)) == True

    # pass function parameters into URL string and save in variable q
    p = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='+str(src)
    q = '&dst='+str(dst)+'&amt='+str(amt)+'&key='+str(APIKEY)
    return(introcs.urlread(p+q))


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """

    #Enforce preconditions
    '''currency is a nonempty string with only letters'''
    introcs.isalpha(currency)

    # Because the parameter for has_error is a json string, and the return
    # output of service_response is a json string, we can plug service response
    # into has_error as its parameter. Currency parameter for iscurrency then
    # becomes the src parameter for service_response. We want has_error to return
    # false because this means the web service call worked properly

    return not has_error(service_response(currency,'USD',0))


def exchange(src,dst,amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    #Enforce preconditions
    ''' src is a string for valid currency code '''
    ''' dst is a string for valid currency code '''
    ''' amt is a float or int'''

    assert type(src) == str and iscurrency(src) == True
    assert type(dst) == str and iscurrency(dst) == True
    assert (type(amt) == float or type(amt) == int) == True

    # Use service_response to return the JSON string which contains the info
    # to be extracted using string functions

    # service_response returns JSON in this format
    #'{"success": true, "src": "2 United States Dollars", "dst": "1.772814
    # Euros", "error": ""}'
    # we want to grab the dst amount

    # get_dst extracts '1.772814 Euros' from the json string

    # before_space extracts '1.772814' from the json string

    # float ensures that the type for json_parse is float

    json_parse = float(before_space(get_dst(service_response(src,dst,amt))))
    return json_parse
