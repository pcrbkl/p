from collections import Counter
value = input("Enter a value : ")
if value == value[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

for i in range(10):
    if value.count(str(i)) > 0:
        print(f'{str(i)} appears {value.count(str(i))} times')
