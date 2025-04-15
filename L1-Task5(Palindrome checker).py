original_string=input("Enter the string: ").lower()
rev_string=original_string[::-1]
print("Reversed string :",rev_string)

def is_palindrome():
    if rev_string==original_string:
        print(f"{original_string} is a palindrome.")
    else:
        print(f"{original_string} is not a palindrome.")
    return 0

is_palindrome()
