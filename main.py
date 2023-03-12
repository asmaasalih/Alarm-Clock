from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

from datetime import datetime

from playsound import playsound

# Main function for alarm clock
def alarm():
    alarm_hour = hours.get()
    alarm_min = minutes.get()
    alarm_sec = seconds.get()
    print(alarm_hour+":"+alarm_min+":"+alarm_sec)
    while True:
        now = datetime.now()
        if alarm_hour == now.strftime("%H") and alarm_min == now.strftime("%M") and alarm_sec == now.strftime("%S"):
            print("Playing.....")
            playsound("Alarm.mp3")
            break
        
# Set up the window
window = Tk()
window.title("Alarm Clock")
window.geometry("400x200")
window.configure(bg="#ffffff")

# Create frames for layout the window
frm_line = Frame(master=window, width=400,height=5,bg="#da6a63")
frm_line.grid(row=0,column=0)
frm_mid = Frame(master=window, width=400,height=40,bg="white")
frm_mid.grid(row=2,column=0)
frm_end = Frame(master=window, width=400,height=6,bg="#da6a63")
frm_end.grid(row=3,column=0)
frm_body = Frame(master=window,width=350,height=150,bg="white")
frm_body.grid(row=1,column=0)

# Adding a logo for my app
img = Image.open('Alarm.png')
img.resize((150, 150))
img = ImageTk.PhotoImage(img)

lbl_image = Label(frm_body,height=120,image=img,bg="white")
lbl_image.place(x=10,y=20)

app_name = Label(frm_body,text="Alarm",height=2,font=("Warp 18 bold"),bg="white")
app_name.place(x=100,y=10)

# Layout hours, minutes, and seconds labels and entry widgets
lbl_hour = Label(frm_body,text="Hour",height=1,font=("Warp 10 bold"),bg="white",fg="#da6a63")
lbl_hour.place(x=102,y=60)
hours = Combobox(frm_body,width=2,font=('Arial 12'))
hours['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23')
hours.current(0)
hours.place(x=106,y=85)

lbl_minute = Label(frm_body,text="Min",height=1,font=("Warp 10 bold"),bg="white",fg="#da6a63")
lbl_minute.place(x=162,y=60)
minutes = Combobox(frm_body,width=2,font=('Arial 12'))
minutes['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
minutes.current(0)
minutes.place(x=166,y=85)

lbl_second = Label(frm_body,text="Sec",height=1,font=("Warp 10 bold"),bg="white",fg="#da6a63")
lbl_second.place(x=222,y=60)
seconds = Combobox(frm_body,width=2,font=('Arial 12'))
seconds['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
seconds.current(0)
seconds.place(x=226,y=85)

# Create Alarm button 
set_btn = Button(frm_body,text="Set Alarm",width=8,bg="#da6a63",fg="white",font=("Warp 10 bold"),command=alarm)
set_btn.place(x=140,y=124)

# Run the application
window.mainloop()