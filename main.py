print("Hello My bro")

# Taking the message input
msg = input("Enter your message: ")

# Taking the password input
password = input("Enter your password: ")

# Encrypting the message
encrypted_msg = []
for i in range(len(msg)):
    encrypted_char = (ord(msg[i]) + 4) * 16 + len(msg)
    encrypted_msg.append(encrypted_char)

print("Your message has been encrypted:")


# Decrypting the message
print("Enter password to decrypt the message")
re_pass = input("Enter your password: ")

if re_pass == password:
    decrypted_msg = ""
    for i in range(len(encrypted_msg)):
        decrypted_char = chr((encrypted_msg[i] - len(encrypted_msg)) // 16 - 4)
        decrypted_msg += decrypted_char

    print("Your message has been decrypted:")
    print(decrypted_msg)
else:
    print("Wrong password")
