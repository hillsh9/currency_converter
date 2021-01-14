"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: SCOTT HILLMAN
Date:   12/23/2020
"""

import introcs
import currency


def test_before_space():
    '''
    Test procedure for before_space
    '''
    print('Testing before_space')

    # Test case 1
    result = currency.before_space('hello world')
    introcs.assert_equals('hello',result)

    # Test case 2
    result = currency.before_space('hello  world')
    introcs.assert_equals('hello',result)

    # Test case 3
    result = currency.before_space('hello big world')
    introcs.assert_equals('hello',result)

    # Test case 4
    result = currency.before_space(' hello_big_world')
    introcs.assert_equals('',result)

    # Test case 5
    result = currency.before_space('hello_big_world ')
    introcs.assert_equals('hello_big_world',result)


def test_after_space():
    '''
    Test procedure for after_space
    '''
    print('Testing after_space')

    # Test case 1
    result = currency.after_space('hello world')
    introcs.assert_equals('world', result)

    # Test case 2
    result = currency.after_space('hello  world')
    introcs.assert_equals(' world', result)

    # Test case 3
    result = currency.after_space(' helloworld')
    introcs.assert_equals('helloworld', result)

    # Test case 4
    result = currency.after_space('helloworld ')
    introcs.assert_equals('', result)

    # Test case 5
    result = currency.after_space('hello big world ')
    introcs.assert_equals('big world ', result)


def test_first_inside_quotes():
    '''
    Test procedure for first_inside_quotes
    '''
    print('Testing first_inside_quotes')

    # Test case 1
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    # Test case 2
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    # Test case 3
    result = currency.first_inside_quotes('"A B C D E F G"')
    introcs.assert_equals('A B C D E F G', result)

    # Test case 4
    result = currency.first_inside_quotes('A "" B C D E F G')
    introcs.assert_equals('', result)


def test_get_src():
    '''
    Test procedure for get_src
    '''
    print('Testing get_src')

    # Test case 1
    result = currency.get_src('{"success": true, "src": "2 United States ' 
    +'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("2 United States Dollars", result)

    # Test case 2
    result = currency.get_src('{"success": true, "src":"2 United States ' 
    +'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals("2 United States Dollars", result)

    # Test case 3
    result = currency.get_src('{"success":false,"src":"","dst":"","error":'
    +'"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    # Test case 4
    result = currency.get_src('{"success":false,"src": "","dst":"","error":'
    +'"Source currency code isinvalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    '''
    Test procedure for get_dst
    '''
    print('Testing get_dst')

    # Test case 1
    result = currency.get_dst('{"success": true, "src": "2 United States ' 
    +'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    # Test case 2
    result = currency.get_dst('{"success": true, "src":"2 United States ' 
    +'Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    # Test case 3
    result = currency.get_dst('{"success":false,"src":"","dst":"","error":' 
    +'Source currency code is invalid."}')
    introcs.assert_equals('',result)

    # Test case 4
    result = currency.get_dst('{"success":false,"src": "","dst": "","error":'
    +'Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_has_error():
    '''
    Test procedure for has_error
    '''
    print('Testing has_error')

    # Test case 1
    result = currency.has_error('{"success":false,"src":"","dst":"","error":'
    +'"Source currency code is invalid."}')
    introcs.assert_equals (True,result)

    # Test case 2
    result = currency.has_error('{"success": true, "src": "2 United States '
    +'Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals (False, result)

    # Test case 3
    result = currency.has_error('{"success":false,"src":"","dst":"","error": '
    +'"Source currency code is invalid."}')
    introcs.assert_equals (True,result)

    # Test case 4
    result = currency.has_error('{"success":true, "src": "2 United States '
    +'Dollars", "dst": "1.772814 Euros", "error":""}')
    introcs.assert_equals (False, result)


def test_service_response():
    '''
    Test procedure for service_response
    '''
    print('Testing service_response')

    # Test case 1
    result = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars"'
    +', "dst": "2.2160175 Euros", "error": ""}', result)

    # Test case 2
    result = currency.service_response('USD','EUR',0.0)
    introcs.assert_equals('{"success": true, "src": "0.0 United States Dollars"'
    +', "dst": "0.0 Euros", "error": ""}', result)
    
    # Test case 3
    result = currency.service_response('USD','EUR',-2.0)
    introcs.assert_equals('{"success": true, "src": "-2.0 United States' + 
    'Dollars", "dst": "-1.772814 Euros", "error": ""}', result)
    
    # Test case 4
    result = currency.service_response('ZZZ','EUR',-2.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'
    +'"The rate for currency ZZZ is not present."}', result)

    # Test case 5
    result = currency.service_response('USD','ZZZ',1.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":'
    +' "The rate for currency ZZZ is not present."}', result)
    
    
def test_iscurrency():
    '''
    Test procedure for iscurrency
    '''
    print('Testing iscurrency')

    # Test case 1
    result = currency.iscurrency ('USD')
    introcs.assert_equals(True,result)

    # Test case 2
    result = currency.iscurrency ('ZZZ')
    introcs.assert_equals(False,result)


def test_exchange():
    '''
    Test procedure for exchange
    '''
    print('Testing exchange')

    # Test case 1
    result = currency.exchange('USD','GBP',1.0)
    introcs.assert_floats_equal(0.79542,result)

    # Test case 2
    result = currency.exchange('USD','GBP',-1)
    introcs.assert_floats_equal(-0.79542,result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()


print("All tests completed successfully.")
