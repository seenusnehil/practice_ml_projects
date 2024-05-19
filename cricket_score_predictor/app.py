import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = ['New Zealand', 'Canada', 'Afghanistan', 'West Indies',
         'Papua New Guinea', 'India', 'Bangladesh', 'Sri Lanka', 'England',
         'Scotland', 'South Africa', 'Netherlands', 'Pakistan', 'Oman',
         'Australia', 'Ireland', 'Namibia', 'Nepal',
         'United States of America']

cities = ['Wellington', 'Abu Dhabi', 'Nagpur', 'Barbados', 'Dubai', 'Durban',
          'Mirpur', 'Delhi', 'Colombo', 'London', 'St Kitts', 'Auckland',
          'Melbourne', 'Cape Town', 'Hamilton', 'Lahore', 'St Lucia',
          'Edinburgh', 'Johannesburg', 'Pallekele', 'Sharjah', 'Nottingham',
          'Dublin', 'Cardiff', 'Chittagong', 'Adelaide', 'Mumbai',
          'Centurion', 'Kolkata', 'Manchester', 'Chandigarh', 'Sydney',
          'Southampton', 'Trinidad', 'Greater Noida', 'Mount Maunganui',
          'Lauderhill', 'Christchurch', 'Bangalore', 'Al Amarat']

st.title('Cricket Predictor')

col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city', sorted(cities))

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', key='col3')
with col4:
    overs = st.number_input('Overs done (works for more than 5', key='col4')
with col5:
    wickets = st.number_input('Wickets', key='col5')
    
last_five = st.number_input('Runs scored in last 5 overs', key='last_five')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'city':city, 
      'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'crr': [crr], 'last_five_over_runs': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
