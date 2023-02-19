def reverse(input):
    reverse_string=""
    for i in range(len(input)-1,-1,-1):
        reverse_string += input[i]
    return reverse_string
input=input("Enter string:- ")
reverse_string=reverse(input)
print(reverse_string)    
