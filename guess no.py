import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.button.pack(pady=5)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
        
    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1
            
            if user_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", fg="red")
            elif user_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", fg="red")
            else:
                self.result_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.", fg="green")
                self.button.config(state=tk.DISABLED)  # Disable button after correct guess
        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
