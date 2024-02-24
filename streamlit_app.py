import streamlit as st
x = st.slider('Select a value: ')
z = st.slider('Select a value: ',key='new3')
y = st.number_input("Enter number", 0, 25, 6, 2)
st.write(f'{x} + {z} = {x+z}')
st.write(f'{x} - {z} = {x-z}')
st.write(f'{x} * {z} = {x*z}')
st.write(f'{x} / {z} = {x/z}')

y1 = st.text_input("Enter your name")
st.title(y1)

#########################  date 

my_date1 = st.date_input("Select date") 
st.write(my_date1)

######################## time 

my_time = st.time_input("Select time")
st.write(my_time)

###################

color = st.color_picker("Select Colour")
st.title(color)

#############  read CSV file and display records or data 

import streamlit as st
import pandas as pd

df = pd.read_csv("Salary.csv")
st.dataframe(df)

####################### button 

name = "DSU"
st.write(name)


if st.button ("Submit"):
	st.write ("Name: {}".format(name.upper()))

if st.button ("Submit", key='new2'):
	st.write ("Name: {}".format(name.lower()))
###################################################  video adding 
video_file = open("karnataka.mp3", "rb").read()
st.video(video_file, start_time = 3)

st.video("https://www.youtube.com/watch?v=DrKLYvLPidw")
st.video("https://www.youtube.com/watch?v=WJ3M7Keivm0")

##########################

from PIL import Image
st.write("## Dayananda Sagar University --------- ")

img = Image.open("DSU.PNG")
st.image(img)
