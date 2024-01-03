import streamlit as st
import random

def generate_random_key(length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = list(alphabet)
    random.shuffle(key)
    return "".join(key[:length])

def triple_encrypt_auto_key_user_input(message):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Generate three random keys based on the length of the message
    key_length = len(message) // 2
    key1 = generate_random_key(key_length)
    key2 = generate_random_key(key_length)
    key3 = generate_random_key(key_length)
    
    # Display the generated keys
    st.write("\nGenerated Keys:")
    st.write("Key 1:", key1)
    st.write("Key 2:", key2)
    st.write("Key 3:", key3)
    
    # Apply the first columnar transposition with key1
    first_transposition = encrypt(message, key1)
    
    # Apply the second columnar transposition with key2
    second_transposition = encrypt(first_transposition, key2)
    
    # Apply the third columnar transposition with key3
    triple_transposition = encrypt(second_transposition, key3)
    
    return triple_transposition

def main():
    st.title("Triple Columnar Transposition Encryption App")

    # User input for the message
    message = st.text_input("Enter your message:")

    if st.button("Encrypt"):
        if message:
            # Perform triple columnar transposition and display the result
            result = triple_encrypt_auto_key_user_input(message.upper())
            st.write("\nTriple Encrypted Message:")
            st.write(result)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
