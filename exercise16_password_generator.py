import random
import string

def prompt_bool(prompt: str) -> bool:
    while True:
        user_input = input(prompt)
        if user_input.lower().startswith("y"):
            return True
        if user_input.lower().startswith("n"):
            return False

uppercase = prompt_bool("Should the password include uppercase letters?: ")
lowercase = prompt_bool("Should the password include lowercase letters?: ")
numbers = prompt_bool("Should the password include numbers?: ")
special = prompt_bool("Should the password include special characters?: ")
length = int(input("How long should the password be?: "))

random_letter_upper = string.ascii_uppercase
random_letter_lower = string.ascii_lowercase
random_integer = list(map(str, range(10)))
special_characters = string.punctuation

char_list = []

if uppercase:
    char_list += random_letter_upper
if lowercase:
    char_list += random_letter_lower
if numbers:
    char_list += random_integer
if special:
    char_list += special_characters

print(''.join(random.SystemRandom().choices(char_list, k=length)))