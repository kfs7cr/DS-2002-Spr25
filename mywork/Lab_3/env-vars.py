#!/home/codespace/.python/current/bin/python3

import os

FAV_SODA = input('What is your favorite soda? ')
MAJOR = input('What is your major? ')
BIRTH_MONTH = input('What is your birthday month? ')

os.environ["FAV_SODA"] = FAV_SODA
os.environ["MAJOR"] = MAJOR
os.environ["BIRTH_MONTH"] = BIRTH_MONTH

print(os.getenv("FAV_SODA"))
print(os.getenv("MAJOR"))
print(os.getenv("BIRTH_MONTH"))