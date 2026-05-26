import math__utils
from math__utils import square
import string__utils

a=int(input("Enter first No: "))
b=int(input("Enter second No: "))
n=int(input("Enter a number to find the square:"))
print("Sum is: ",math__utils.add(a,b))
print("Square is :",square(n))

str=input("Enter a string to Capitalize: ")
strcap=string__utils.capitalize_words(str)
print("Capitalized string: ",strcap)

str1=input("Enter a string to reverse: ")
strrev=string__utils.reverse_string(str1)
print("Reversed String is: ",strrev)

str2=input("Enter a string to count words: ")
strcount=string__utils.word_count(str2)
print("Count of words in the string is: ",strcount)
