import requests
import popup
from tkinter import messagebox
import tkinter as tk

HOST = "http://127.0.0.1:5600"
AFK_BUCKET = "aw-watcher-afk_albert-XPS-13-7390"

NO_AFK_MAX_TIME = 25 * 60

r = requests.get(f"{HOST}/api/0/buckets/{AFK_BUCKET}/events")

# print(r.json())
last_event = r.json()[0]

if last_event["data"]["status"] == "not-afk":
    no_afk_time = last_event["duration"]
    if no_afk_time > NO_AFK_MAX_TIME:
        # Popup Message
        minutes = round(no_afk_time / 60)

        # snooze = messagebox.showinfo(
        #     message=f"You have been focusing for {minutes} minutes, "
        #     "maybe you should consider to take a break!\n\n",
        #     title="Maybe you should take a break?")
        root = tk.Tk()
        app = popup.CountdownTimerApp(root, minutes)
        root.mainloop()
