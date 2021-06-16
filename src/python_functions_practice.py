def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string_length):
    return len(string_length)

def join_string(string_1,string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

# def number_to_full_month_name(month_num):
#     if month_num == 1:
#         return "January"
#     elif month_num == 2:
#         return "February"
#     elif month_num == 3:
#         return "March"
#     elif month_num == 4:
#         return "April"
#     elif month_num == 5:
#         return "May"
#     elif month_num == 6:
#         return "June"
#     elif month_num == 7:
#         return "July"
#     elif month_num == 8:
#         return "August"
#     elif month_num == 9:
#         return "September"
#     elif month_num == 10:
#         return "October"
#     elif month_num == 11:
#         return "November"
#     elif month_num == 12:
#         return "December"

def number_to_full_month_name(month_num):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[month_num-1]
   
def number_to_short_month_name(month_num):
    return number_to_full_month_name(month_num)[:3]

def volume_calc(length,width,height):
    return length * width * height

def string_reverser(string):
    return string[::-1]

def farenheit_conv(farenheit):
    return ((farenheit - 32)*5)/9