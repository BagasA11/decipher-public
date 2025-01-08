import pandas as pd
import numpy as np
import streamlit as st
import joblib
import matplotlib
from collections import Counter

MODEL = joblib.load("new_model.joblib")
FRQ = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]

# method to encrypt character
def encrypt_caesar(text, shift):
    text = str(text).lower()
    result = ""
    for char in text:
        if char.isalpha():
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted 
            
    return result

# method to count frequency each characters
def extact_feature(ciphertext):
     # a => 3, e => 5
    frequency = Counter(ciphertext)

    total = sum(frequency.values())
    features = [frequency.get(chr(i), 0) / total for i in range(ord('a'), ord('z') + 1)]
    # [0.2, 0.4]
    return features

# function to decrypt cipher text
def decrypt(cipertxt: str):
    np_cipher = np.array([extact_feature(cipertxt)])
    key = MODEL.predict(np_cipher)[0]
    return key

# txt = st.text_area(label="", value="", height=None, 
# max_chars=None, key=None, help=None, 
# on_change=None, args=None, 
# kwargs=None, *, placeholder=None, 
# disabled=False, label_visibility="visible")

# render tab
tab1, tab2 = st.tabs(["decrypt cipher-text", "get cipher-text"])

with tab1:
    # tab untuk menerjemahkan ciphertext
    st.header("ini tab untuk mendekripsi cipher text")
    cipherTxt = st.text_area(label="input cipher text")
    # predict result
    if len(cipherTxt) > 0:
        predict_shift = decrypt(cipherTxt)
        plaintext = encrypt_caesar(cipherTxt, -predict_shift)
        # count frequency
        cipher_freq = extact_feature(cipherTxt)
        st.write(f'predicted shift: {predict_shift}')
        st.write(f'result: {plaintext}')
    
   
    

with tab2:
    # tab untuk mendapatkan ciphertext dari bahasa inggris
    st.header("inputkan kalimat berbahasa inggris untuk mendapatkan cipher text")
    txtEnglish = st.text_area(label="input:")
    shift = st.number_input(label="input shift:", min_value=0, max_value=25)
    cipher = encrypt_caesar(txtEnglish, int(shift))
    st.code(body=cipher, wrap_lines=True)