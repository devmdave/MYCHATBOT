import tkinter as tk
from tkinter import scrolledtext
import requests
import os


def generate_response(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False

    }

    # Make the POST request
    response = requests.post(url, json=payload)
    return response.json()["response"]
        


def send_message():
    user_message = user_input.get()
    if user_message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_message + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.see(tk.END)
        user_input.delete(0, tk.END)
        # Here, you can add the AI response logic
        chat_response(user_message)

def chat_response(user_message):
    response = generate_response(user_message)
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, response + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

app = tk.Tk()
app.title("Madhav's AI")

# image = tk.PhotoImage(file=os.getcwd() + "/logo.png")
# # Create a Label widget with the image
# image_label = tk.Label(app, image=image,height=200)
# image_label.pack(pady=20)

chat_window = scrolledtext.ScrolledText(app, state='disabled', wrap='word',height=18)
chat_window.pack(pady=10)

user_input = tk.Entry(app, width=50)
user_input.pack(side=tk.LEFT, padx=450, pady=10)

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

app.mainloop()
