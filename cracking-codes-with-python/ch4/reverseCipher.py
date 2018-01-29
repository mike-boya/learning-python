# Reverse Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

message = input('Enter Message: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
