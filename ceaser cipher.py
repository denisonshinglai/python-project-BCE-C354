def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character by the specified amount
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            
            result += shifted_char
        else:
            # Preserve non-alphabetic characters
            result += char
    
    return result

if __name__ == "__main__":
    # Example usage
    text_input = input("Enter the text to encrypt: ")
    shift_input = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text_input, shift_input)
    print(f"The encrypted text is: {encrypted_text}")

