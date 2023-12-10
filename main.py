import requests
from tkinter import messagebox


HOST = "http://127.0.0.1:5600"
AFK_BUCKET = "<your_afk_bucket>"

NO_AFK_MAX_TIME = 25 * 60

r = requests.get(f"{HOST}/api/0/buckets/{AFK_BUCKET}/events")

last_event = r.json()[0]

if last_event["data"]["status"] == "not-afk":
    no_afk_time = last_event["duration"]
    if no_afk_time > NO_AFK_MAX_TIME:
        # Popup Message
        minutes = round(no_afk_time / 60)
        snooze = messagebox.showinfo(
            message=f"You have been focussing for {minutes} minutes, "
            "maybe you should consider tot take a break!\n\n",
            title="Maybe you should take a break?")
