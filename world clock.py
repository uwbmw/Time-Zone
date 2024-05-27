from datetime import datetime
from tkinter import PhotoImage, Tk, Frame, Label
import pytz

root = Tk()

root.geometry("1200x400")
image_icon = PhotoImage(file="WorldClock.png")
root.iconphoto(False, image_icon)

def update_time(clock, name, timezone, city):
    home = pytz.timezone(timezone)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clock.config(text=current_time)
    name.config(text=city)
    clock.after(200, update_time, clock, name, timezone, city)

# First time zone
f = Frame(root, bd=5)
f.place(x=10, y=118, width=220, height=150)

name = Label(f, font=("Helvetica", 30, "bold"))
name.place(x=50, y=10)

logo = PhotoImage(file="in.png")
image_label = Label(root, image=logo)
image_label.place(x=20, y=150)

clock = Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

# Second time zone
f2 = Frame(root, bd=5)
f2.place(x=300, y=118, width=220, height=150)

name2 = Label(f2, font=("Helvetica", 30, "bold"))
name2.place(x=30, y=10)

logo2 = PhotoImage(file="us.png")
image_label2 = Label(root, image=logo2)
image_label2.place(x=290, y=150)

clock2 = Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

# Third time zone
f3 = Frame(root, bd=5)
f3.place(x=600, y=118, width=220, height=150)

name3 = Label(f3, font=("Helvetica", 30, "bold"))
name3.place(x=50, y=10)

logo3 = PhotoImage(file="gb.png")
image_label3 = Label(root, image=logo3)
image_label3.place(x=600, y=150)

clock3 = Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

# Fourth time zone
f4 = Frame(root, bd=5)
f4.place(x=900, y=118, width=220, height=150)

name4 = Label(f4, font=("Helvetica", 30, "bold"))
name4.place(x=50, y=10)

logo4 = PhotoImage(file="jp.png")
image_label4 = Label(root, image=logo4)
image_label4.place(x=900, y=150)

clock4 = Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

update_time(clock, name, "Asia/Kolkata", "India")
update_time(clock2, name2, "America/New_York", "New York")
update_time(clock3, name3, "Europe/London", "London")
update_time(clock4, name4, "Asia/Tokyo", "Tokyo")

root.mainloop()
