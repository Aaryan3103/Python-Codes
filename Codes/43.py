# Write a python program to determine whether the given String is a palindrome or not

def main():
    user_string = input("Enter String: ")
    if user_string == user_string[::-1]:
        print(f"User entered string is palindrome")
    else:
        print(f"User entered strign is not a palindrome")

if __name__ == "__main__":
    main()
print("THIS PROGRAM IS WRITTEN BY Aaryan ERP :- 0221BCA163")