#Description: This programm predicits hemoglobin content in a given pRBC unit

#import necessary libaries
import pandas as pd
from sklearn.linear_model import LinearRegression

from PIL import Image
import streamlit as st

#Create a title and a subtitel for the programm
st.write('''
# Hemoglobin and iron content prediction tool 
Predict the hemoglobin and iron content of a given pRBC unit in g/unit using machine learning and python
''')

#open and display an image
image = Image.open('HB_ML2.png')
st.image(image, caption='ML', use_column_width=True)

#Get the data

df = pd.read_excel('Training_Data_WebApp.xlsx')

#Create dummie variables
df_dummies_all = pd.get_dummies(df, prefix='', prefix_sep='')

#Set a subheader
st.subheader('Data information')
#Show the data as a table
st.dataframe(df_dummies_all)
#Show statistics on the data
st.subheader('Statistics')
st.write(df_dummies_all.describe())
#Show the data as a chart
#chart = st.bar_chart(df_dummies_all)

#Split the data into independent 'X' and dependent 'y' variables
X = df_dummies_all.drop(['UNIT_HB'], axis='columns')
y = df.UNIT_HB

#Get the feature imput from the data


def get_user_input():
    volume = st.sidebar.slider('Volume in mL', 200.0, 400.0, 300.0)
    hb_fingertip = st.sidebar.slider('Hb fingertip in g/dL', 12.5, 18.0, 14.0)
    male = st.sidebar.slider('Male', 0, 1, 1)
    female = st.sidebar.slider('Female', 0, 1, 0)
    if male == 1:
        female = 0
    else:
        female = 1
    if female == 1:
        male = 0
    else:
        male = 1




    #Store a dictionary into a variable
    user_data = {'Volume in mL': volume,
                 'Hb fingertip in g/dL': hb_fingertip,
                 'Female': female,
                 'Male': male
                 }



    #Transform the data into a data frame
    features = pd.DataFrame(user_data, index =[0])
    return features

#Store the user input into a varaible
user_input = get_user_input()

#Set a subheader an display the users input
st.subheader('User Input:')
st.write(user_input)

#Creat and train the model
MLR_model = LinearRegression()
MLR_model.fit(X,y)


#Store the models predictions in a variable
prediction = MLR_model.predict(user_input)
iron = prediction/66.458*4*55.845

#Set a subheader and display the predicion
st.subheader('Predicted Hb content in g per unit:')
st.write(prediction)

#Set a subheader and display the predicion
st.subheader('Predicted iron content in mg per unit:')
st.write(iron)











