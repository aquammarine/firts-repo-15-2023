book = 'Harry Potter'
print(book)

print("----------------------------------------------------")

is_adult = True
is_child = False
if is_adult:
    print("kid")
else:
    print("adult")

print("----------------------------------------------------")

is_sunny = True
is_warm = True
if is_warm and is_sunny:
    print("weather")

print("----------------------------------------------------")

import math

x = 12.394
y = 7.193
sum = (math.sqrt(math.tanh(x)) + (x + y)**math.log(x))
print(sum)

print("----------------------------------------------------")

import requests

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
response = requests.get(url)
print(response.text)
