import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

SERVER_IP = "192.168.0.106"
PORT = 2222

# Socket erzeugen

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))
 
# GUI-Fenster erstellen
root = tk.Tk()
root.title("Chat Client")
 
# Textfeld für Chatverlauf
chat_area = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_area.pack(padx=10, pady=10)
 
# Eingabefeld für Nachrichten
message_entry = tk.Entry(root, width=40)
message_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))
 
def send_message():
    message = message_entry.get()
    if message:
        client.send(message.encode("UTF-8"))
        chat_area.configure(state='normal')
        chat_area.insert(tk.END, f"Client: {message}\n")
        chat_area.configure(state='disabled')

        message_entry.delete(0, tk.END)
 
send_button = tk.Button(root, text="Senden", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))
 
def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break

            chat_area.configure(state='normal')
            chat_area.insert(tk.END, f"Server: {data.decode('UTF-8')}\n")
            chat_area.configure(state='disabled')

        except:
            break
 
# Thread starten, um Nachrichten zu empfangen
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()
 
# GUI starten
root.mainloop()
client.close()
 

print("test")