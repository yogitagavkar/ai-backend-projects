import requests
import pandas as pd

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
print(f"total is {total}")

"""-------------------------------"""
"reverse string"

s = "yogita"
print(s[::-1])

""""""""""""
s = "madam"
print(s == s[::-1])
""""""

nums = [1,2,2,3,4]
print(set(nums))

""""""""
nums = [1,2,3,4,5,6]

y = [x for x in nums if x % 2 == 0]
print(y)

""""""""

response = requests.get("https://github.com/")
print(response)

if response.status_code == 200:
    print(response.json)

""""""

data = [{"name":"abc","salary":1000},{"name":"abc","salary":2000}]
df = pd.DataFrame(data)


df.to_csv("data/sales.csv",index = False)
df.to_json("data/sales_json.json")
print(df.groupby("name")['salary'].sum())

