import tkinter as tk
from tkinter import messagebox
import random

WORD_LIST = [
    "argentina", "belgium", "india", "turkey", "germany",
    "finland", "germany", "australia", "iceland", "france",
    "canada", "china", "malaysia", "nepal", "oman",
    "portugal", "pakistan", "spain", "korea", "japan", "apple"
]


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("400x300")

        self.word = random.choice(WORD_LIST)
        self.guessed_letters = set()
        self.remaining_attempts = 6

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="_ " * len(self.word), font=("Helvetica", 18))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.master)
        self.entry.pack()
        self.entry.bind("<Return>", self.check_letter)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_letter)
        self.guess_button.pack(pady=10)

        self.attempts_label = tk.Label(self.master, text=f"Remaining Attempts: {self.remaining_attempts}", font=("Helvetica", 12))
        self.attempts_label.pack(pady=10)

        self.guessed_label = tk.Label(self.master, text="Guessed Letters: ", font=("Helvetica", 12))
        self.guessed_label.pack(pady=10)

    def check_letter(self, event=None):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        if not letter.isalpha() or len(letter) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single alphabetic character.")
            return

        if letter in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You have already guessed this letter.")
            return

        self.guessed_letters.add(letter)
        if letter in self.word:
            self.update_display()
            if all(letter in self.guessed_letters for letter in self.word):
                messagebox.showinfo("Congratulations!", "You have won the game!")
                self.reset_game()
        else:
            self.remaining_attempts -= 1
            self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
            if self.remaining_attempts == 0:
                messagebox.showinfo("Game Over", f"You have lost the game! The word was '{self.word}'.")
                self.reset_game()

    def update_display(self):
        display_word = ' '.join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_label.config(text=display_word)
        self.guessed_label.config(text=f"Guessed Letters: {', '.join(self.guessed_letters)}")

    def reset_game(self):
        self.word = random.choice(WORD_LIST)
        self.guessed_letters.clear()
        self.remaining_attempts = 6
        self.update_display()
        self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()