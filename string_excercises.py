# Question 1: take an input string from the user and create a new string with the first, middle, and last characters of the input string
from operator import index

first_input = input("Enter a String")
first_character = (first_input[0])
print(first_character)
middle_character = (int(len(first_input) / 2))
print(first_input[middle_character])
last_char = first_input[-1]
print(last_char)