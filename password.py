# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:59:15 2023

@author: Kumail
"""

import random 

pass1 = ['a','b','c','d','e','f','g','h','i','j','k','l',
        'm','n','o','p','q','r','s','t','u','v','w','x','y'
        ,'z','A','B','C','D','E','F','G','H','I','J','K',
        'L','M','N','O','P','Q','R','S','T','U','V','W','X'
        ,'Y','Z','1','2','3','4','5','6','7','8','9','0','!'
        ,'@','#','$','%','^','&','*','(',')']

# declaring the empty string
password = ""

#loop to generate the random password of the length entered by the 
for x in range (16):
    password = password + random.choice(pass1)[0]
    
print('Your New Password is :\n', password)    






















#(how to explain this code)
#The import statement on line 8 brings in the random module, which contains functions for generating random numbers and choosing random elements from a list.

#On line 10, a list called pass1 is defined that contains all the characters that can be used to create the password. These characters include lowercase and uppercase letters, digits, and various symbols.

#Line 13 initializes an empty string called password, which will store the generated password.

#The for loop on lines 16-18 repeats 16 times (the length of the desired password) and each time through the loop, it chooses a random character from the pass1 list using the random.choice() function, and appends it to the password string.

#Finally, on line 20, the script prints the generated password to the console.

















