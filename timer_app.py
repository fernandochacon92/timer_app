#C:\Users\ThinkPad X1 Carbon\Documents\Fernando\Work\Python\timer>streamlit run timer_app.py


#cd Documents\Fernando\Work\Python\timer\timer_app
#pipreqs Documents\Fernando\Work\Python\timer\timer_app

#https://github.com/fernandochacon92/timer_app.git


import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

from datetime import datetime


import time
#import winsound

st.set_page_config(
     page_title="Timer workout",
     page_icon=":sunny:",
     initial_sidebar_state="expanded",
     layout="centered",
 )

#markdown cheatsheet
st.title('Workout Timer')

workout = st.slider('Work time in seconds',0, 100, 45)

pause = st.slider('Break time in seconds',0, 100, 15)

rounds = st.slider('Rounds',0, 20, 10)

rounds_1=rounds+1

st.markdown('**Work**.')
workout_bar = st.progress(0)

st.markdown('**Break**.')
pause_bar = st.progress(0)

st.markdown('**Rounds**.')
rounds_bar = st.progress(0)

workout_time = workout/100

pause_time = pause/100

round_time = 0.1

values = [1,2]


def circlek (valuesk):
    labels = ['Oxygen','Hydrogen']

    fig = go.Figure(data=[go.Pie(labels=labels, values=valuesk, hole=.9)])

    circle=st.plotly_chart(fig, use_container_width=True)
    
    return

#st.write(workout_time)
#st.write(pause_time)


if st.button('Start'):
    
    time.sleep(10)
    
    #winsound.Beep(800,1000)
    #winsound.Beep(800,1000)
    #winsound.Beep(800,1000)

    for completed_rounds in range(1,rounds_1):
        
        for percent_complete_work in range(100):
            time.sleep(workout_time)
            workout_bar.progress(percent_complete_work + 1)
            
            #if percent_complete_work == 99:
                #winsound.Beep(800,1000)
            workout_bar = st.progress(0)

        for percent_complete_pause in range(100):
            time.sleep(pause_time)
            pause_bar.progress(percent_complete_pause + 1)
            
            #if percent_complete_pause == 99:
                #winsound.Beep(800,1000)
        #st.write(rounds)
        #st.write(completed_rounds)
        rounds_bar.progress((completed_rounds) * 1/rounds)
        #st.write((completed_rounds)  * 1/rounds)
        
        #rounds_bar.progress((completed_rounds) * rounds*10)
        #st.write((completed_rounds) * rounds*10)
        


    #winsound.Beep(800,1000)
    st.balloons()
#winsound.MessageBeep()
#winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
#winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)  
