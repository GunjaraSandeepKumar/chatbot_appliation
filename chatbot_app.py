import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button, END

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")

        self.chat_history = Text(root, width=50, height=15, wrap=tk.WORD)
        self.scrollbar = Scrollbar(root, command=self.chat_history.yview)
        self.chat_history.config(yscrollcommand=self.scrollbar.set)
        self.chat_history.pack(pady=10)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_entry = Entry(root, width=50)
        self.message_entry.pack(pady=10)

        self.send_button = Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.chat_history.insert(tk.END, "Chatbot: Hello! How can I help you?\n")
        self.message_entry.focus_set()

    def send_message(self):
        message = self.message_entry.get()
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "You: " + message + "\n")
        self.message_entry.delete(0, tk.END)
        self.chat_history.configure(state='disabled')

        response = self.get_chatbot_response(message)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        self.chat_history.configure(state='disabled')

        self.chat_history.see(END)

    def get_chatbot_response(self, message):
        # Replace this function with your actual chatbot logic
        if message.lower() == "hello":
            return "Hello there! How can I assist you today?"
        elif message.lower() == "bye":
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = ChatbotApp(root)
    root.mainloop()
