import streamlit as st
x = st.slider('Select a value: ')
y = st.number_input("Enter number", 0, 25, 6, 2)
st.write(f'{x} + {y} = {x+y}')
st.write(f'{x} - {y} = {x-y}')
st.write(f'{x} * {y} = {x*y}')
st.write(f'{x} / {y} = {x/y}')
