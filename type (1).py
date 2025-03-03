import tkinter as tk
import random
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Cybersecurity is the future of technology.",
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath."
]

class TypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mavis Typing Tutor")
        self.root.geometry("700x400")
        
        self.sentence = random.choice(sentences)
        self.start_time = None
        
        self.label = tk.Label(root, text=self.sentence, font=("Arial", 18), wraplength=600)
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result = tk.Label(root, text="", font=("Arial", 16))
        self.result.pack(pady=20)

        self.button = tk.Button(root, text="Check Speed", command=self.calculate_speed, font=("Arial", 16))
        self.button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            typed_text = self.entry.get()
            word_count = len(typed_text.split())
            speed = round((word_count / elapsed_time) * 60)
            
            
            correct_words = sum(1 for a, b in zip(typed_text.split(), self.sentence.split()) if a == b)
            accuracy = round((correct_words / len(self.sentence.split())) * 100)

            self.result.config(text=f"Speed: {speed} WPM | Accuracy: {accuracy}%")
        else:
            self.result.config(text="Start typing first!")

root = tk.Tk()
app = TypingApp(root)
root.mainloop()
