#!/usr/bin/env python3
# -------------------------------------------
# Exercise: Learn about input() and arithmetic operators in Python
# -------------------------------------------
# This starter program asks for a name and age and prints a short message.
# Your tasks (below) will ask you to extend and experiment with the program.

# --------------------
# Step 1: Run this program as it is first:
name = input("Enter your name: ")

# This code asks for age and converts it to an integer so we can do arithmetic.
# If the user types something invalid, we ask again.
while True:
    try:
        age = int(input("Enter your age (whole number): "))
        break
    except ValueError:
        print("Please enter your age as a whole number, e.g. 25")

print(f"Hello, {name}! This year you are {age}.")

# This will just add an empty line for space

food = input("What is your favorite food?")
print(f"That's a nice choice, {name.capitalize()}.  {food.capitalize()} is delicious.")
music = input("And how about music? What is your favorite song?")
print(f"{music}? You sure do have great taste!")

# --------------------
# Step 2: Customise the program
# 1) Ask the user for their favourite food and favourite song.
# 2) Print friendly messages that use those variables.
# 3) Keep all prints using f-strings so the output is neat.

# Example (you can write similar code for food and song):
colour = input("What's your favourite colour? ")

# Example (you can write similar code for food and song)
print(f"{colour.capitalize()} is a lovely colour, {name}!")

# --------------------
# Step 3: Arithmetic experiments
# Try the examples below. Change numbers, try new operations, and see what happens.

print("")  # spacing
print(f"You were born in either {2025-age} or {2024-age}")
print(f"In 5 years you will be {age+5}.")
print(f"You are approximately {age*12} months old.")
print(f"If we count in dog years (x7), you'd be {age/7} years old.")
print(f"Twice your age is {age*2}.")
print(f"Half your age is {age/2}.")


# A small example using the length of the name (string -> numeric)
print(f"Your name has {len(name)} characters.")

# --------------------
# Once you are done, please run the following commands (one by one) in the terminal:
# git add Ex2_input.py
# git commit -m "Completed input and arithmetic exercise"
# git push origin main
