from tkinter import *
from datetime import datetime
from ds_client import DSClient

class Post:
    def __init__(self, username, message):
        self.username = username
        self.message = message
        self.timestamp = datetime.now()

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("DS Blog App")

        self.username_label = Label(master, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = Entry(master)
        self.username_entry.grid(row=0, column=1)

        self.message_label = Label(master, text="Message:")
        self.message_label.grid(row=1, column=0)
        self.message_entry = Entry(master)
        self.message_entry.grid(row=1, column=1)

        self.save_button = Button(master, text="Save Post", command=self.save_post)
        self.save_button.grid(row=2, column=1)

        self.footer_label = Label(master, text="Offline")
        self.footer_label.grid(row=3, column=0)

        self.online_checkbox = Checkbutton(master, text="Online", command=self.toggle_online)
        self.online_checkbox.grid(row=3, column=1)

        self._is_online = False
        self.ds_client = None

    def toggle_online(self):
        if self._is_online == False:
            self.ds_client = DSClient()
        self._is_online = not self._is_online
        self.set_footer_label()

    def set_footer_label(self):
        if self._is_online == True:
            self.footer_label.config(text="Online")
        else:
            self.footer_label.config(text="Offline")

    def save_post(self):
        username = self.username_entry.get()
        message = self.message_entry.get()
        post = Post(username, message)

        with open('blog.dsu', 'a') as f:
            f.write(f"{post.username}\n{post.message}\n{post.timestamp}\n")

        if self._is_online == True:
            self.publish(post)

    def publish(self, post:Post):
        self.ds_client.send(post)

root = Tk()
app = MainApp(root)
root.mainloop()
