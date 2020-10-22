# word = 'Hello Bob'
# num = int(word)


# Using try / except
word = 'Hello Bob'

try:
    num = int(word)
except:
    num = -1

print("First Try:", num)


####################################


word = '123'

try:
    num = int(word)
except:
    num = -1

print("Second Try:", num)


################################################


word = input("Enter a number: ")

try:
    num = int(word)
except:
    num = -1

if num > 0:
    print("It is a number")
else:
    print("It is not a number")