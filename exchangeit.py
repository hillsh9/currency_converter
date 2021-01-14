"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: SCOTT HILLMAN
Date:   12/31/20
"""

import currency


# 1) Ask the the user for a first currency code

ask_src = input('3-letter code for original currency: ')
currency.iscurrency(ask_src)


# 2) Ask the the user for a second currency code

ask_dst = input('3-letter code for the new currency: ')
currency.iscurrency(ask_dst)


# 3) Ask the the user for an amount (of the first currency)

ask_amt = float(input('Amount of the original currency: '))


# 4) Prints the conversion to the second currency rounded to 3 digits
x = round(float(currency.exchange(ask_src,ask_dst,ask_amt)),3)
print('You can exchange '+str(ask_amt)+' '+ask_src +' for '+str(x)+' '
+ask_dst+'.')



