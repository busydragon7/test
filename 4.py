
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

list1 = list(str1)
list2 = list(str2)

list1.sort()
list2.sort()

if list1 == list2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
