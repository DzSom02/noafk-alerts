import tkinter as tk
from tkinter import messagebox
from datetime import timedelta


class CountdownTimerApp:
    def __init__(self, master, minutes):
        self.master = master
        self.master.title("Maybe you should take a break?")
        self.message_text = f"You have been focusing for {minutes} minutes, maybe you should consider to take a break!\n\n"

        base = 20
        width = int(base * 20)
        height = int(base * 11)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2

        self.master.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.time_left = timedelta(minutes=3)
        self.timer_running = False

        self.info_label = tk.Label(master, text=self.message_text, font=("Helvetica", 14), wraplength=width - 20)
        self.info_label.pack(pady=(10, 0))  # Adjusted pady value

        self.label = tk.Label(master, font=("Helvetica", 38))
        self.label.pack(pady=0)

        self.start_timer()

        self.exit_button = tk.Button(master, text="OK", command=self.close_application, width=6)
        self.exit_button.pack(side=tk.BOTTOM, pady=20)
        self.master.bind('<Return>', lambda event=None: self.close_application())  # Bind Enter key to Exit button

        self.update_display()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        self.time_left -= timedelta(seconds=1)
        self.update_display()
        self.master.after(1000, self.update_timer)

    def update_display(self):
        minutes, seconds = divmod(int(self.time_left.total_seconds()), 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.label.config(text=time_str)

    def clear_info_label(self):
        # Clear the info_label text and reset the text color
        self.info_label.config(text="", fg="blue")

    def close_application(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root, 100)
    root.mainloop()
