# Activity Watcher NOAFK Alert

This is simply a tool that uses: https://activitywatch.net/ to monitor the time
I stay in the computer and after 25 minutes of using the computer it pops up 
a message to remind me to move.

Use this line for the crontab:

```
* * * * * export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus && export XAUTHORITY=/run/user/1001/gdm/Xauthority && export DISPLAY=:1 && python3 <path_to_main>/main.py
```

You will still need to autostart the server, more info here:

https://docs.activitywatch.net/en/latest/getting-started.html#autostart
