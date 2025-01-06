def reverse_string(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) == 0 or len(s) == 1:
        return s
    # Recursive case: reverse the rest of the string and append the first character at the end
    return reverse_string(s[1:]) + s[0]


input_string = "hello"
output_string = reverse_string(input_string)
print(output_string)



def recuriveRealNumber(n):
    if n<=0:
        return 0
    else:
        return n + recuriveRealNumber(n-1)

inputNumber = 5
print(recuriveRealNumber(inputNumber))

