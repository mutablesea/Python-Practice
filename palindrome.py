string = input("Enter a string: ")
# Remove spaces and convert to lowercase
processed_string = string.replace(" ", "").lower()

# Check if the processed string is a palindrome
if processed_string == processed_string[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
