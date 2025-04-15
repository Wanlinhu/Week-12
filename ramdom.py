import string
import random

random_string = ''.join(random.choices(string.ascii_lowercase, k=12))

print("Random string:", random_string)
