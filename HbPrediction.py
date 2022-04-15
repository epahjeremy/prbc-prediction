#Description: This programm predicits hemoglobin content in a given pRBC unit

#import necessary libaries
import pandas as pd
from sklearn.linear_model import LinearRegression

from PIL import Image
import streamlit as st


#Create a title and a subtitel for the programm
st.write('''
# Hemoglobin and iron content prediction tool 
Predict the hemoglobin content of a given pRBC unit in g/unit using machine learning and python
''')

#open and display an image
st.image( "https://raw.githubusercontent.com/epahjeremy/prbc-prediction/main/Hb_ML6.png")

#Get the feature imput from the data

def get_user_input():
   volume = st.sidebar.slider('Volume in mL', 200.0, 400.0, 300.0)
   hb_fingertip = st.sidebar.slider('Hb fingertip in g/dL', 12.5, 18.0, 14.0)
   male = st.sidebar.slider('Male', 0, 1, 1)
   female = st.sidebar.slider('Female', 0, 1, 0)
         
   if male and female == 1:
      st.write('WARNING: Must be EITHER male OR female!')
             
  #Store a dictionary into a variable
   user_data = {'Volume in mL': volume,
                 'Hb fingertip in g/dL': hb_fingertip,
                 'Female': female,
                  'Male': male
                }
        
   #Transform the data into a data frame
   features = pd.DataFrame(user_data, index =[0])
   return features



data_up = st.file_uploader("Here you can upload your own tranining data set as a csv-file -Hb in unit (g), volume (mL), Hb fingertip (g/dL), sex (male/female)- for prediction:")
if data_up is not None:
   df_up = pd.read_csv(data_up)
        
   #Create dummie variables
   df_up_dummies_all = pd.get_dummies(df_up, prefix='', prefix_sep='')

   #Set a subheader
   st.subheader('This is Your training data:')
   #Show the data as a table
   st.dataframe(df_up_dummies_all)
   #Show statistics on the data
   st.subheader('Statistical overview of Your data set:')
   st.write(df_up_dummies_all.describe())

   #Split the data into independent 'X' and dependent 'y' variables
   X_up = df_up_dummies_all.iloc[:, [False, True, True, True, True]]
   y_up = df_up.iloc[:, 0]
   
   #Store the user input into a varaible
   user_input = get_user_input()

   #Set a subheader an display the users input
   st.subheader('User input:')
   st.write(user_input)
      
   #Creat and train the model
   MLR_model_up = LinearRegression()
   MLR_model_up.fit(X_up,y_up)
   
  #Store the models predictions in a variable
   prediction_up = MLR_model_up.predict(user_input)
   iron_up = prediction_up/66.458*4*55.845

   #Set a subheader and display the predicion
   st.subheader('Predicted Hb content in g per unit:')
   st.write(prediction_up)

   #Set a subheader and display the predicion
   st.subheader('Predicted iron content in mg per unit:')
   st.write(iron_up)
   
   
   data2 = st.file_uploader("You can upload a csv-file -volume (mL), Hb fingertip (g/dL), sex (male/female)- for prediction:")
   if data2 is not None:
     df2 = pd.read_csv(data2)
     X2 =  pd.get_dummies(df2, prefix='', prefix_sep='')
     file_pred = MLR_model.predict(X2)
     iron_file = file_pred/66.458*4*55.845
      
    #Set a subheader and display the predicion
     st.subheader('Predicted Hb content in g per unit of uploaded file:')
     st.write(file_pred)
      
     #Set a subheader and display the predicion
     st.subheader('Predicted iron content in mg per unit of uploaded file:')
     st.write(iron_file)

   

#Get the data
#data = st.file_uploader("Upload the training data set - csv:")
df = pd.read_csv("https://raw.githubusercontent.com/Jayremi21/HbPrediction/main/Training_Data_WebApp.csv")


# If a dataset is uploaded, show a preview
if data_up is None:
   # df = pd.read_csv(data)
        
    #Create dummie variables
    df_dummies_all = pd.get_dummies(df, prefix='', prefix_sep='')

    #Set a subheader
    st.subheader('Training data of German Red Cross Ba-Wü-Hessen gGmbH:')
    #Show the data as a table
    st.dataframe(df_dummies_all)
    #Show statistics on the data
    st.subheader('Statistical overview of training data:')
    st.write(df_dummies_all.describe())
    #Show the data as a chart
    #chart = st.bar_chart(df_dummies_all)

    #Split the data into independent 'X' and dependent 'y' variables
    X = df_dummies_all.drop(['UNIT_HB'], axis='columns')
    y = df.UNIT_HB

    
    #Store the user input into a varaible
    user_input = get_user_input()

    #Set a subheader an display the users input
    st.subheader('User input:')
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
   
    data2 = st.file_uploader("You can upload a csv-file -volume (mL), Hb fingertip (g/dL), sex (male/female)- for prediction:")
    if data2 is not None:
      df2 = pd.read_csv(data2)
      X2 =  pd.get_dummies(df2, prefix='', prefix_sep='')
      file_pred = MLR_model.predict(X2)
      iron_file = file_pred/66.458*4*55.845
      
     #Set a subheader and display the predicion
      st.subheader('Predicted Hb content in g per unit of uploaded file:')
      st.write(file_pred)
      
      #Set a subheader and display the predicion
      st.subheader('Predicted iron content in mg per unit of uploaded file:')
      st.write(iron_file)
      











