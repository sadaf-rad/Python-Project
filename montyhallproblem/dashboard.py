import streamlit as st 
from montyhallproblem.main  import simulate_game
import time 
st.title (':zap: Monty Hall Simulation')

num_games = st.number_input ('Enter number of games to simiulate ',min_value = 1 , max_value= 100000 , value = 100)

col1 , col2 = st.columns(2)
col1.subheader('Number of wins without switching the choice')
col2.subheader('number of wins after switching the choice')

chart1 = col1.line_chart(x=None , y = None , height = 400)
chart2 = col2.line_chart(x=None , y = None , height = 400)

no_switch = 0 
switch = 0 

for i in range (num_games):
    win_no_switch, win_switch = simulate_game(1)
    no_switch += win_no_switch
    switch += win_switch
    chart1.add_rows ([no_switch / (i + 1)])
    chart2.add_rows ([switch / (i + 1)])
    time.sleep(0.01)


    

