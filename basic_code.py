import requests
import pandas as pd
import helper
import sys

name = "yogita"
age = 15

print(f"Hi my name is{name} and my age is {age}")

if age > 18:
     print("You are eligibile for vote")
else:
     print("You are not eligible")

"""--------------------------------"""
numbers = [1,2,3,4,5]

total = sum(numbers)
#print(f"total is {total}")

"""-------------------------------"""
"reverse string"

s = "yogita"
#print(s[::-1])

""""""""""""
s = "madam"
#print(s == s[::-1])
""""""

nums = [1,2,2,3,4]
#rint(set(nums))

""""""""
nums = [1,2,3,4,5,6]

y = [x for x in nums if x % 2 == 0]
#print(y)

""""""""

response = requests.get("https://github.com/")
#print(response)

if response.status_code == 200:
    print(response.json)

""""""

data = [{"name":"abc","salary":1000},{"name":"abc","salary":2000}]
df = pd.DataFrame(data)


df.to_csv("data/sales.csv",index = False)
df.to_json("data/sales_json.json")
# print(df.groupby("name")['salary'].sum())

""""""
# simple calculator

number1 = input("Enter first number")
number2 = input("Enter second number")

if(number1 == "" or number2 == ""):
     print("Number1 Or Number2 are should not be empty")
     sys.exit()

try :
    number1 = float(number1)
    number2 = float(number2)
except ValueError:
     print("Number1 Or Number2 are should be numbers")
     sys.exit()


if(number1 < 0 or number2 < 0):
     print("Number1 Or Number2 are should not be negative")
     sys.exit()


operation = input("Enter operation(+,-,/,*)")

if operation == "/" and number2 == 0:
        print("Cannot divide by zero")
        sys.exit()

result = helper.calculation(operation,number1,number2)
print("Calculation result is ",result)
