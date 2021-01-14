# currency_converter
Implementation of a functional currency converter that utilizes Python to work with a REST web api 

This project was completed as part of the eCornell certificate "Building a Currency Converter," which is course 3 of 6 towards their "Python Programming"
certificate.

This repository consists of three modules
1) currency.py  ->  contains all of the functions used in the currency converter
2 testcurrency.py -> contains all of the unit testing functions for currency.py
3) exchangeit.py -> a simple user interface, which when run as script prompts the user for two currencies and an amount to be converted. 
   Finally, the script prints out the result of converting the first currency to the second.

I organized this project into 7 steps:
1) Implement the space breaking functions
2) Implement the quote extracting functions
3) Implement the JSON extracting functions
4) Implement the Web Service function. In this project I connect to the Open Exchange Rates web api
   https://docs.openexchangerates.org/docs/api-introduction
5) Implement the currency functions
6) Implement a simple application that leverages the functions in currency.py to allow a user to interact with it

The specification for each function in this project was provided to me. I had to figure out how to write the code to achieve the function spec.

Before creating each function I created the test script equivalent in testcurrency.py. By working backwards to establish test cases before actually writing 
the corresponsing function in in currency.py, I was forced to think through the function specification completely. This made writing the function much
easier and also ensured that everything worked properly when I integrated everything in the application exchangeit.py 
