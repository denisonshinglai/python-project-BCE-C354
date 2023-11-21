def decrypt_caesar_ciper(cliphertext,shift):
    plaintext=""
    for char in cliphertext:
        if char.isalpha():
            shift_amount= shift%26
            if char.islower():
                decrypt_char=chr(((ord(char)-ord('a')-shift_amount+26)%26)+ord('a'))
            else:
                decrypt_char=chr(((ord(char)-ord('A')-shift_amount+26)%26)+ord('A'))
            plaintext+=decrypt_char 
        else:
            plaintext +=char
    return plaintext

encrypted_message=input("Enter The encrypted message:")
shift=int(input("enter the shift:"))

decrypt_message=decrypt_caesar_ciper(encrypted_message,shift)
print("DECRYPTED MESSAGE:",decrypt_message)
