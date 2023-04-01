import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import ttk
import requests

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("DSU Social Media")

        # create a menu bar
        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        # create a file menu item
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Post", command=self.create_post)
        self.file_menu.add_command(label="Edit Post", command=self.edit_post)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # create an edit menu item
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Edit Profile", command=self.edit_profile)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # create a help menu item
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # create a toolbar
        self.toolbar = ttk.Frame(master, padding=2, relief=tk.RAISED)
        self.toolbar.grid(row=0, column=0, sticky=tk.W)

        self.new_post_icon = tk.PhotoImage(file='new_post.gif')
        self.new_post_button = ttk.Button(self.toolbar, image=self.new_post_icon, command=self.create_post)
        self.new_post_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.edit_post_icon = tk.PhotoImage(file='edit_post.gif')
        self.edit_post_button = ttk.Button(self.toolbar, image=self.edit_post_icon, command=self.edit_post)
        self.edit_post_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.edit_profile_icon = tk.PhotoImage(file='edit_profile.gif')
        self.edit_profile_button = ttk.Button(self.toolbar, image=self.edit_profile_icon, command=self.edit_profile)
        self.edit_profile_button.pack(side=tk.LEFT, padx=2, pady=2)

        # create the main content area
        self.main_content = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=10)
        self.main_content.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S, padx=10, pady=10)

        # set up the default view
        self.load_posts()

    def load_posts(self):
        # clear the main content area
        self.main_content.delete('1.0', tk.END)

        # get the posts from the server
        try:
            response = requests.get('http://localhost:8080/api/posts')
            if response.status_code == 200:
                posts = response.json()
                for post in posts:
                    self.main_content.insert(tk.END, f"{post['title']}\n\n{post['content']}\n\nPosted by: {post['author']}\n\n")
            else:
                messagebox.showerror("Error", f"Could not retrieve posts from server. Server returned error code: {response.status_code}")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Could not connect to server. Please check your network connection and try again.")

    def create_post(self, post=None):
        # create a top-level window for the post
        post_window = Toplevel()
        post_window.title("Create Post")

        # create a text box for the post title
        title_label = Label(post_window, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        title_entry = Entry(post_window, width=50)
        title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    
        # create a text box for the post body
        body_label = Label(post_window, text="Body:")
        body_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        body_text = Text(post_window, width=60, height=15)
        body_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # populate the post fields if editing an existing post
        if post:
            title_entry.insert(0, post["title"])
            body_text.insert("1.0", post["body"])
        
    
    def edit_post(self):
        # create a top-level window for the post editor
        top = tk.Toplevel()
        top.title("Edit Post")

        # create a label and entry for the post id
        id_label = tk.Label(top, text="Post ID:")
        id_label.grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(top)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # create a label and entry for the post title
        title_label = tk.Label(top, text="Title:")
        title_label.grid(row=1, column=0, padx=5, pady=5)
        title_entry = tk.Entry(top)
        title_entry.grid(row=1, column=1, padx=5, pady=5)

        # create a label and entry for the post content
        content_label = tk.Label(top, text="Content:")
        content_label.grid(row=2, column=0, padx=5, pady=5)
        content_entry = tk.Text(top, width=30, height=10)
        content_entry.grid(row=2, column=1, padx=5, pady=5)

        # create a button to submit the edited post
        submit_button = tk.Button(top, text="Submit",
                                  command=lambda: self.submit_edited_post(top, id_entry.get(), title_entry.get(), content_entry.get("1.0", "end-1c")))
        submit_button.grid(row=3, column=1, padx=5, pady=5)

    def submit_edited_post(self, top, post_id, post_title, post_content):
        # send a request to the server to edit the post
        response = requests.put(f"{self.server_url}/posts/{post_id}", json={"title": post_title, "content": post_content})

        # check if the request was successful
        if response.status_code == 200:
            messagebox.showinfo("Success", "Post edited successfully.")
            top.destroy()
        else:
            messagebox.showerror("Error", f"Failed to edit post: {response.text}")

    def change_server_url(self):
        # create a top-level window for the server URL editor
        top = tk.Toplevel()
        top.title("Change Server URL")

        # create a label and entry for the server URL
        url_label = tk.Label(top, text="Server URL:")
        url_label.grid(row=0, column=0, padx=5, pady=5)
        url_entry = tk.Entry(top, width=30)
        url_entry.grid(row=0, column=1, padx=5, pady=5)

        # create a button to submit the new server URL
        submit_button = tk.Button(top, text="Submit",
                                  command=lambda: self.submit_server_url_change(top, url_entry.get()))
        submit_button.grid(row=1, column=1, padx=5, pady=5)

    def submit_server_url_change(self, top, new_url):
        # change the server URL
        self.server_url = new_url

        # update the status bar
        self.status_text.set(f"Server URL: {self.server_url}")

        # close the top-level window
        top.destroy()

