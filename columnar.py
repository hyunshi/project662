import streamlit as st
import random
import string

# Global dictionary to store generated keys
generated_keys = {}

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
    
    # Store generated keys in the global dictionary
    generated_keys['key1'] = key1
    generated_keys['key2'] = key2
    
    return double_encrypted

def double_decrypt(ciphertext):
    # Retrieve keys from the global dictionary
    key1 = generated_keys.get('key1', '')
    key2 = generated_keys.get('key2', '')

    if not key1 or not key2:
        st.warning("Please encrypt the message first.")
        return
    
    # Apply the second columnar transposition in reverse order
    first_decrypted = decrypt(ciphertext, key2)
    
    # Apply the first columnar transposition to the result of the second
    double_decrypted = decrypt(first_decrypted, key1)
    
    return double_decrypted

def encrypt(message, key):
    # Your existing encrypt function

def decrypt(ciphertext, key):
    # Your existing decrypt function

def main():
    st.title("Double Columnar Transposition Cipher")

    user_message = st.text_input("Enter the message to encrypt:", "")
    double_encrypted_message = ""

    if st.button("Encrypt"):
        double_encrypted_message = double_encrypt(user_message)
        st.write("Generated Key 1:", generated_keys.get('key1', ''))
        st.write("Generated Key 2:", generated_keys.get('key2', ''))
        st.write("Double Encrypted:", double_encrypted_message)

    if st.button("Decrypt"):
        double_decrypted_message = double_decrypt(double_encrypted_message)
        if double_decrypted_message:
            st.write("Double Decrypted:", double_decrypted_message)

if __name__ == "__main__":
    main()
