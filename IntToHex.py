def int_to_hex(n):
    if n == 0:
        return ""
    hex_characters = "0123456789ABCDEF"
    return int_to_hex(n // 16) + hex_characters[n % 16]

number = int(input("Enter a positive integer: "))
while (number <= 0):
    print("Please enter a positive integer.")
    number = int(input("Enter a positive integer: "))

result = int_to_hex(number)
print(f"The hexadecimal representation of {number} is: {result}")