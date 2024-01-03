import streamlit as st
import random
import string

def generate_random_key(length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = list(alphabet)
    random.shuffle(key)
    return "".join(key[:length])

def double_encrypt(message):
    # Generate two keys based on the length of the message
    key1 = generate_random_key(len(message))
    key2 = generate_random_key(len(message))
    
    # Apply the first columnar transposition
    first_encrypted = encrypt(message, key1)
    
    # Apply the second columnar transposition to the result of the first
    double_encrypted = encrypt(first_encrypted, key2)
    
    return double_encrypted, key1, key2

def double_decrypt(ciphertext, key1, key2):
    # Apply the second columnar transposition in reverse order
    first_decrypted = decrypt(ciphertext, key2)
    
    # Apply the first columnar transposition to the result of the second
    double_decrypted = decrypt(first_decrypted, key1)
    
    return double_decrypted

def encrypt(message, key):
 # Remove spaces and convert to uppercase
    message = message.replace(" ", "").upper()
    
    # Calculate the number of columns based on the key length
    num_columns = len(key)
    
    # Calculate the number of rows needed
    num_rows = -(-len(message) // num_columns)  # Ceil division
    
    # Fill in the matrix with the message characters
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    k = 0
    
    for i in range(num_rows):
        for j in range(num_columns):
            if k < len(message):
                matrix[i][j] = message[k]
                k += 1
    
    # Create a dictionary to store the column order based on the key
    key_order = {key[i]: i for i in range(num_columns)}
    
    # Read out the matrix column by column based on the key order
    encrypted_text = ""
    for col in sorted(key_order.keys()):
        col_index = key_order[col]
        for row in range(num_rows):
            encrypted_text += matrix[row][col_index]
    
    return encrypted_text

def decrypt(ciphertext, key):
    # Calculate the number of columns based on the key length
    num_columns = len(key)
    
    # Calculate the number of rows needed
    num_rows = -(-len(ciphertext) // num_columns)  # Ceil division
    
    # Create a dictionary to store the column order based on the key
    key_order = {key[i]: i for i in range(num_columns)}
    
    # Calculate the number of characters in the last column
    last_col_chars = len(ciphertext) % num_columns
    
    # Initialize variables for matrix and counters
    matrix = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    k = 0
    
    # Fill in the matrix column by column based on the key order
    for col in sorted(key_order.keys()):
        col_index = key_order[col]
        for row in range(num_rows):
            if col_index == num_columns - 1 and row >= num_rows - last_col_chars:
                matrix[row][col_index] = ciphertext[k]
                k += 1
            else:
                matrix[row][col_index] = ciphertext[k]
                k += 1
    
    # Read out the matrix row by row to get the decrypted text
    decrypted_text = ""
    for i in range(num_rows):
        for j in range(num_columns):
            decrypted_text += matrix[i][j]
    
    return decrypted_text

def main():
    st.title("Double Columnar Transposition Cipher")

    user_message = st.text_input("Enter the message to encrypt:", "")
    double_encrypted_message = ""  # Initialize here to ensure it's available in the broader scope

    if st.button("Encrypt"):
        double_encrypted_message, generated_key1, generated_key2 = double_encrypt(user_message)
        st.write("Generated Key 1:", generated_key1)
        st.write("Generated Key 2:", generated_key2)
        st.write("Double Encrypted:", double_encrypted_message)

    if st.button("Decrypt"):
        double_decrypted_message = double_decrypt(double_encrypted_message, generated_key1, generated_key2)
        st.write("Double Decrypted:", double_decrypted_message)

if __name__ == "__main__":
    main()
