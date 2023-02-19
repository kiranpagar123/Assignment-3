def count(string):
    upper_count=0
    lower_count=0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("no of Upper case char is:-",upper_count)
    print("no of Lower case char is:-",lower_count)
string=input("Enter string:-")
count(string)           