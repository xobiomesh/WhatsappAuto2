import tkinter as tk
from tkinter import messagebox
from crontab import CronTab
import os

def schedule_message():
    recipient = recipient_entry.get()
    message = message_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if not recipient or not message or not date or not time:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    # Create the cron job
    cron = CronTab(user=True)
    job = cron.new(command=f'python /home/xo/Desktop/VScodeProjects/WhatsappAuto2/src/script.py "{recipient}" "{message}"', comment="WhatsApp Scheduler")
    job.setall(f'{time} {date} * * *')
    
    cron.write()
    messagebox.showinfo("Success", "Message scheduled successfully.")

# Create the GUI window
window = tk.Tk()
window.title("WhatsApp Scheduler")

tk.Label(window, text="Recipient Name").grid(row=0, column=0)
recipient_entry = tk.Entry(window)
recipient_entry.grid(row=0, column=1)

tk.Label(window, text="Message").grid(row=1, column=0)
message_entry = tk.Entry(window)
message_entry.grid(row=1, column=1)

tk.Label(window, text="Date (DD)").grid(row=2, column=0)
date_entry = tk.Entry(window)
date_entry.grid(row=2, column=1)

tk.Label(window, text="Time (HH:MM)").grid(row=3, column=0)
time_entry = tk.Entry(window)
time_entry.grid(row=3, column=1)

schedule_button = tk.Button(window, text="Schedule Message", command=schedule_message)
schedule_button.grid(row=4, columnspan=2)

window.mainloop()
