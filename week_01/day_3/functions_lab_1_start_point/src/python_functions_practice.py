def return_10():
      return 10

def add(first, second):
    return first + second

def subtract(first, second):
     return first - second

def multiply(first, second):
     return first * second

def divide(first, second):
     return first / second

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
     return string_1 + string_2

def add_string_as_number(int_1, int_2):
     return int(int_1) + int(int_2)

def number_to_full_month_name(first):
     months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
     return months[first -1]

def number_to_short_month_name(first):
     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
     return months [first-1]

def volume_of_a_cube (length):
     return length ** 3      
     
def reverse_string (string): 
     return string.reverse()

def fahrenheit_to_celsius(fahrenheit, celsius):
     return celsius == 5/9 * (fahrenheit -  32)