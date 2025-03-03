import streamlit as st
import random 
import pandas as pd
st.header("Rock Paper Scissors Game");
rand_num = random.randint(1,3);
first = st.button("Rock", key="rock");
second = st.button("Paper", key="paper");
third = st.button("Scissors", key="scissors");
def Comp_Move():
    comp_num:int = rand_num;
    if(comp_num==1):
        st.text("Computer Move is Rock")
    elif(comp_num==2):
        st.text("Computer Move is Paper");
    elif(comp_num==3):
        st.text("Computer Move is Scissors");

def User_Move():
    

  if first :
    st.write("You clicked Rock")
    Comp_Move()

  if second:
    st.write("You clicked Paper")
    Comp_Move()

  if third:
    st.write("You clicked Scissors")
    Comp_Move()


def Compare():
    if((rand_num==1 and first) or (rand_num==2 and second) or (rand_num==3 and third)):
        User_Move();
        st.write("Match Tie");
        
    if((rand_num==2 and first) or (rand_num==3 and second) or (rand_num==1 and third)):
        User_Move();
        st.write("Computer Win and You Lose");
    if((rand_num==3 and first) or (rand_num==1 and second) or (rand_num==2 and third)):
        User_Move();
        st.write("Computer Lose and You Win");


Compare();
  