import uipath
import tkinter as tk
from tkinter import ttk

# Initialize UiPath application outside
app = uipath.Application()

# Open time and attendance tracking application
self.app.start("C:\\Program Files\\ManicTime\\ManicTime.exe")

class TimeAndAttendance:
    def __init__(self):
        
        self.app = app
        self.window = tk.Tk()        

        # Create the tkinter UI
        self.root = tk.Tk()
        self.root.title("Time and Attendance Tracking")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Create the clock in/out buttons
        self.clock_in_button = ttk.Button(self.root, text="Clock In", command=self.clock_in)
        self.clock_out_button = ttk.Button(self.root, text="Clock Out", command=self.clock_out)

        # Place the buttons in the UI
        self.clock_in_button.pack(pady=20)
        self.clock_out_button.pack()

        # Run the tkinter mainloop
        self.root.mainloop()

    def clock_in(self):
        # Clock in using UiPath
        self.app.window("Time and Attendance Application").click("clock_in_button")

    def clock_out(self):
        # Clock out using UiPath
        self.app.window("Time and Attendance Application").click("clock_out_button")

    def __del__(self):
        # Close the time and attendance tracking application
        self.app.quit()

if __name__ == '__main__':
    TimeAndAttendance()
