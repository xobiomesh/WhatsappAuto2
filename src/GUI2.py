import tkinter as tk
from tkinter import messagebox
from crontab import CronTab
import os

def schedule_message():
    recipient = recipient_entry.get()
    message = message_entry.get()
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    time = time_entry.get()

    if not recipient or not message or not day or not month or not year or not time:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    # Split the time into hours and minutes
    try:
        hour, minute = time.split(":")
    except ValueError:
        messagebox.showerror("Input Error", "Time must be in HH:MM format.")
        return

    # Create the cron job
    cron = CronTab(user=True)
    log_file = "/path/to/log_file.log"
    job = cron.new(command=f'/home/xo/Desktop/VScodeProjects/WhatsappAuto2/src/wrapper.sh "{recipient}" "{message}" >> {log_file} 2>&1', comment="WhatsApp Scheduler")
    job.setall(f'{minute} {hour} {day} {month} *')
    
    cron.write()
    messagebox.showinfo("Success", "Message scheduled successfully.")
    list_cron_jobs()


def list_cron_jobs():
    cron = CronTab(user=True)
    job_listbox.delete(0, tk.END)
    for job in cron:
        job_listbox.insert(tk.END, f"{job}")

def delete_selected_job():
    selected_job = job_listbox.get(tk.ACTIVE)
    if not selected_job:
        messagebox.showerror("Selection Error", "No job selected.")
        return

    cron = CronTab(user=True)
    for job in cron:
        if str(job) == selected_job:
            cron.remove(job)
            cron.write()
            messagebox.showinfo("Success", "Job deleted successfully.")
            list_cron_jobs()
            return

    messagebox.showerror("Deletion Error", "Selected job not found.")

# Create the GUI window
window = tk.Tk()
window.title("WhatsApp Scheduler")

tk.Label(window, text="Recipient Name").grid(row=0, column=0)
recipient_entry = tk.Entry(window)
recipient_entry.grid(row=0, column=1)

tk.Label(window, text="Message").grid(row=1, column=0)
message_entry = tk.Entry(window)
message_entry.grid(row=1, column=1)

tk.Label(window, text="Day (DD)").grid(row=2, column=0)
day_entry = tk.Entry(window)
day_entry.grid(row=2, column=1)

tk.Label(window, text="Month (MM)").grid(row=3, column=0)
month_entry = tk.Entry(window)
month_entry.grid(row=3, column=1)

tk.Label(window, text="Year (YYYY)").grid(row=4, column=0)
year_entry = tk.Entry(window)
year_entry.grid(row=4, column=1)

tk.Label(window, text="Time (HH:MM)").grid(row=5, column=0)
time_entry = tk.Entry(window)
time_entry.grid(row=5, column=1)

schedule_button = tk.Button(window, text="Schedule Message", command=schedule_message)
schedule_button.grid(row=6, columnspan=2)

tk.Label(window, text="Active Cron Jobs").grid(row=7, columnspan=2)

job_listbox = tk.Listbox(window, width=50)
job_listbox.grid(row=8, columnspan=2)

delete_button = tk.Button(window, text="Delete Selected Job", command=delete_selected_job)
delete_button.grid(row=9, columnspan=2)

# Initially list the active cron jobs
list_cron_jobs()

window.mainloop()
