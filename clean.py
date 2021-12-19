#!/usr/bin/python3

data = input()

index = data.find('[{')

print(data[index:])