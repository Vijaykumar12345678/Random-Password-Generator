import streamlit as st  
import random as _random
import string 
import pyttsx3


#Title of your app + one whitespace
st.markdown("<h1 style='text-align: center; color: black;'>Random Password Generator </h1>", unsafe_allow_html=True)
st.text(" \n")
st.text(" \n")


length = st.number_input('How many characters do you want your password to have? (8-100)', min_value=8, max_value=100)


st.text(" \n")


title = st.write('What should your password include?')

st.text(" \n")

cb1 = st.checkbox('Include Numbers')
cb2 = st.checkbox('Include Uppercase Letters')
cb4=st.checkbox("Include LowerCase Letters")
cb3 = st.checkbox('Include Special Characters ')


empty = st.empty()
ok=st.button("Generate Password")
if ok:
    if cb1 == True:
        #numbers = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
        numbers=string.digits   
    else:
        numbers = ""


    if cb2 == True:
        #letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" 
         letter=string.ascii_uppercase
    else:
        letter = ""


    if cb3 == True:
        symbols = string.punctuation
    else:
        symbols = ""
    if cb4==True:
        #letters="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        letters=string.ascii_lowercase   
    else:
        letters=""

    if cb1 and cb1 and cb3 and cb4 == None: 
        st.write("Check")

        
        
    all = letter+letters + str(numbers) + symbols



    try:
            temp = _random.sample(all, length)
    except ValueError:
        pass
                



    try:
        password = "".join(temp)
    except ValueError and NameError:
        pass




    try: 
        title2 = st.write('Password Generated is : ')
    except:
        NameError
        st.write(" ")
        
    st.text(" \n")
    try:
         st.code(password)
         engine=pyttsx3.init()

         engine.say(f"The password generated is {password}")

         engine.runAndWait()

       
     

    except ValueError and NameError:
        st.write("Select a box")       




        
    st.text(" \n")
    






