import streamlit as st

st.title('Deploy APP')
st.write('My First Deploy APP !')

import os

key= os.environ.get('MY_SECRET','NOT SET YET')
st.write(f'Server Key: {key}')

#git pull origin master
#Merge ----
#:q


#git push origin master