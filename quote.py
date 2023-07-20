import tkinter as tk
from tkinter import messagebox
import random

quotes = {
    "life": [ "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "Life is either a daring adventure or nothing at all. - Helen Keller",
        "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
        "The biggest adventure you can ever take is to live the life of your dreams. - Oprah Winfrey",
        "Life isn't about finding yourself. It's about creating yourself. - George Bernard Shaw",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"],
    "inspiration": ["Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "It always seems impossible until it is done. - Nelson Mandela",
        "The future depends on what you do today. - Mahatma Gandhi"],
    "funny": ["I'm sorry, if you were right, I'd agree with you. - Robin Williams",
        "The best way to appreciate your job is to imagine yourself without one. - Oscar Wilde",
        "I always wanted to be somebody, but now I realize I should have been more specific. - Lily Tomlin",
        "I dream of a better tomorrow, where chickens can cross the road and not be questioned about their motives. - Ralph Waldo Emerson",
        "I'm not superstitious, but I am a little stitious. - Michael Scott",
        "I like long walks, especially when they are taken by people who annoy me. - Fred Allen",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "The only mystery in life is why the kamikaze pilots wore helmets. - Al McGuire",
        "The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it. - Terry Pratchett",
        "Always borrow money from a pessimist. He won't expect it back. - Oscar Wilde"],
    "love": ["The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart. - Helen Keller",
        "Love is not only something you feel, it is something you do. - David Wilkerson",
        "Love is an endless act of forgiveness. Forgiveness is an endless act of love. - Beyoncé" ],
    "success": ["Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will. - Vince Lombardi",
        "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
        "Success is not in what you have, but who you are. - Bo Bennett"],
    }

def get_random_quote(category):
    if category in quotes:
        return random.choice(quotes[category])
    else:
        return "Category not found. Please try a different one."

def show_random_quote():
    category = category_var.get()
    quote = get_random_quote(category)
    messagebox.showinfo(f"{category.capitalize()} Quote", quote)

root = tk.Tk()
root.title("Random Quote Generator")

title_label = tk.Label(root, text="Random Quote Generator", font=("Helvetica", 16))
title_label.pack(pady=10)

category_var = tk.StringVar(root)
category_entry = tk.Entry(root, textvariable=category_var)
category_entry.pack(pady=5)


quote_button = tk.Button(root, text="Get Random Quote", command=show_random_quote)
quote_button.pack(pady=5)


quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=5)


root.mainloop()
