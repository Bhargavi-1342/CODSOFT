import tkinter as tk
from tkinter import messagebox
import random
import time

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice_handler(choice):
    global user_score, computer_score, tie_score
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}", fg="#f0f0f0")
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    else:
        tie_score += 1
    update_score_labels()
    animate_computer_choice(computer_choice)

def animate_computer_choice(computer_choice):
    for _ in range(5):
        result_label.config(text=f"Computer chose: {random.choice(choices)}", fg="#555")
        root.update()
        time.sleep(0.1)
    result_label.config(text=f"Computer chose: {computer_choice}", fg="#f0f0f0")

def update_score_labels():
    user_score_label.config(text=f"Your score: {user_score}", fg="#ffdfdf")
    computer_score_label.config(text=f"Computer score: {computer_score}", fg="#dfdfdf")
    tie_score_label.config(text=f"Ties: {tie_score}", fg="#d0d0d0")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
tie_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x400")
root.configure(bg="#282c34")

title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 22, "bold"), pady=10, bg="#282c34", fg="#61afef")
title_label.pack()

button_frame = tk.Frame(root, bg="#282c34")
button_frame.pack(pady=20)

button_style = {
    "font": ("Arial", 14),
    "width": 10,
    "padx": 15,
    "pady": 10,
    "bg": "#61afef",
    "activebackground": "#528bff",
    "fg": "#282c34",
    "bd": 0,
    "relief": tk.RAISED
}

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice_handler("rock"), **button_style)
rock_button.grid(row=0, column=0, padx=15)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice_handler("paper"), **button_style)
paper_button.grid(row=0, column=1, padx=15)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice_handler("scissors"), **button_style)
scissors_button.grid(row=0, column=2, padx=15)

result_label = tk.Label(root, text="", font=("Arial", 18), pady=20, bg="#282c34", fg="#abb2bf")
result_label.pack()

score_frame = tk.Frame(root, bg="#282c34")
score_frame.pack()

user_score_label = tk.Label(score_frame, text=f"Your score: {user_score}", font=("Arial", 16), bg="#282c34", fg="#ffdfdf")
user_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text=f"Computer score: {computer_score}", font=("Arial", 16), bg="#282c34", fg="#dfdfdf")
computer_score_label.grid(row=0, column=1, padx=20)

tie_score_label = tk.Label(score_frame, text=f"Ties: {tie_score}", font=("Arial", 16), bg="#282c34", fg="#d0d0d0")
tie_score_label.grid(row=0, column=2, padx=20)

root.mainloop()
