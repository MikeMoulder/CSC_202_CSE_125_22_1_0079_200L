#PyPassword Generator
import string
import random
print("An UnHackable Password Generator")

capitalLetter = string.ascii_uppercase
smallLetter = string.ascii_lowercase
symbol = string.punctuation
digit = string.digits

combo = capitalLetter + smallLetter + symbol + digit
shuffledCombo = random.sample(combo, len(combo))


length = int(input("How long do you want your password to be? "))
cl = 0
password = ""

while cl < length:
    password += shuffledCombo[cl]
    cl += 1

print("Your password is: " + password)


