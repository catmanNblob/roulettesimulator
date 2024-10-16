import streamlit as st
import random

# Function to determine the color of the number
def get_color(number):
    if number == 0:
        return "green"
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    return "red" if number in red_numbers else "black"

# Title of the app
st.title("Roulette Game")

# User inputs for betting
bet_amount = st.number_input("Enter your bet amount:", min_value=1)
bet_type = st.selectbox("Choose your bet type:", ["Number (0-36)", "Red", "Black"])
bet_number = st.number_input("Enter a number (0-36):", min_value=0, max_value=36, value=0)

if st.button("Place Bet"):
    winning_number = random.randint(0, 36)  # Random number between 0-36
    winning_color = get_color(winning_number)
    
    st.write(f"Winning Number: **{winning_number}** ({winning_color})")
    
    if bet_type == "Number (0-36)" and bet_number == winning_number:
        st.success(f"You win! You get **{bet_amount * 35}** chips!")
    elif bet_type == "Red" and winning_color == "red":
        st.success(f"You win! You get **{bet_amount * 2}** chips!")
    elif bet_type == "Black" and winning_color == "black":
        st.success(f"You win! You get **{bet_amount * 2}** chips!")
    else:
        st.error("You lost!")
