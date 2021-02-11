#Github
#Branch circle
#cd Documents\Fernando\Work\Python\timer\timer_app
#streamlit run timer_app.py

#git add . #git commit -m "circle" #git push origin circle

#C:\Users\ThinkPad X1 Carbon\Documents\Fernando\Work\Python\timer>streamlit run timer_app.py


#cd Documents\Fernando\Work\Python\timer\timer_app
#pipreqs Documents\Fernando\Work\Python\timer\timer_app

#https://github.com/fernandochacon92/timer_app.git


import streamlit as st
import os
import plotly.graph_objects as go
import time 
#import winsound

st.set_page_config(
     page_title="Timer workout",
     page_icon=":muscle:",
     initial_sidebar_state="expanded",
     layout="centered",
 )

st.markdown("<h1 style='text-align: center; color: Black;'>Workout Timer</h1>", unsafe_allow_html=True)

workout = st.slider('Work time in seconds',0, 100, 45)

pause = st.slider('Break time in seconds',0, 100, 15)

rounds = st.slider('Rounds',0, 20, 10) 

rounds_str= str(rounds)

rounds_bar = st.progress(100)

workout_time = workout/100

pause_time = pause/100


#winsound.MessageBeep()
#winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
#winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)  


values = [100,0]

colors_1= ['rgb(33, 75, 99)',  'rgb(151, 179, 100)']

colors_2= ['rgb(56, 75, 126)', 'rgb(18, 36, 37)']

trace= go.Pie( values=values, hole=.8,showlegend=False, sort=False, marker_colors=colors_1, textinfo='none', hoverinfo='skip')

data1=[trace]

fig = go.Figure(data=data1)

fig.update_layout(annotations=[dict(text='READY!', x=0.5, y=0.5, font_size=20, showarrow=False)])

circle=st.plotly_chart(fig, use_container_width=True)

def animate_1(i):  # update the y values (every 1000ms)
    
    values= [t1,t2]
    trace= go.Pie( values=values, hole=.8, showlegend=False, sort=False, marker_colors=colors_1, textinfo='none',hoverinfo='skip')
    data1=[trace]
    fig = go.Figure(data=data1)
    fig.update_layout(annotations=[dict(text='GO! - '+ round_str+"/"+rounds_str ,
                                        x=0.5, y=0.5, font_size=20, showarrow=False)])
    
    circle.plotly_chart(fig)
    
def animate_2(i):  # update the y values (every 1000ms)
    
    values= [t1,t2]
    trace= go.Pie( values=values, hole=.8, showlegend=False, sort=False, marker_colors=colors_2, textinfo='none',hoverinfo='skip')
    data1=[trace]
    fig = go.Figure(data=data1)
    fig.update_layout(annotations=[dict(text='BREAK -' + round_str+"/"+rounds_str,
                                        x=0.5, y=0.5, font_size=20, showarrow=False)])
    
    circle.plotly_chart(fig)

if st.button('Start Workout'):
    
    for j in range(rounds):

        rounds_bar.progress((j+1)/rounds)
        
        round_str= str(j+1)

        for i in range(101):
            t1=100-i
            t2=100-t1
            animate_1(i)
            time.sleep(workout_time)

        if j < rounds-1:
        
            for i in range(101):
                t1=100-i
                t2=100-t1
                animate_2(i)
                time.sleep(pause_time)
                
    fig.update_layout(annotations=[dict(text='Well Done',x=0.5, y=0.5, font_size=20, showarrow=False)])
    
    circle.plotly_chart(fig)

    st.balloons()  
    