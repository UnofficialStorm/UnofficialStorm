
num = input("Enter a 3 digit number")
length = len(num) 

if length != 3:
    num = input("Enter a 3 digit number")
else:
    print("Processing...")

count = 0
word_p = 0
lst = ["hundreds", "tenths", "units"]

while count != length:
    print(num[count], lst[word_p])
    word_p = word_p + 1
    count = count + 1

