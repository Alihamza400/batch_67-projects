import streamlit as st
import random
st.write("Hangman Game");
def choose_word():
    
    words = ["Person","Animal","Developers","Designers","Doctors","Engineers"]
    random.choice(words);
def display(word,guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
def hangman():
    word = choose_word();
    guessed_letters = set();
    attempts = 6;
    print("Welcome to Hangman");
    while attempts>0:
        print("\n"+ display(word,guessed_letters));
        guess = input("Guess a letter = ");
        if guess in guessed_letters:
            print("You Already guessed that letter")
            continue
        guessed_letters.add(guess);
        if guess not in word:
            attempts = attempts - 1;
            print(f"wrong guess!attempts left : {attempts}");
        if set(word).issubset(guessed_letters):
            print(f"You guessed the word : {word}")
    print(f"Game Over! The word was: {word}");
    if _name_ == "_main_":
     hangman();