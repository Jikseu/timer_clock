# cd OneDrive/Desktop/TimerClock
# python timer_clock.py

from tkinter import *
from tkinter import ttk, Text, font
import time
from pygame import mixer

global times 

def countdowntimer():
	global times 
	times = int(hrs.get())*3600+ int(mis.get())*60 + int(sec.get())
	while times > -1:
		second = (times % 60)
		minute = (times // 60)
		hour = 0

		if minute > 60:
			minute = (minute % 60)
			hour = (minute // 60)

		sec.set(str(second).zfill(2))
		mis.set(str(minute).zfill(2))
		hrs.set(str(hour).zfill(2))
		
		if second == 10:
			pass

		root.update()
		time.sleep(1)
		times -= 1

def countuptimer():
	global times
	times = 0
	minute = 0
	hour = 0
	while times > -1:
		second = times 

		if second == 59:
			minute += 1
			times, second = 0, 0
		if minute == 59:
			hour += 1
			mis.set('00')

		sec.set(str(second).zfill(2))
		mis.set(str(minute).zfill(2))
		hrs.set(str(hour).zfill(2))

		root.update()
		time.sleep(1)
		times += 1
		
def stop():
	global times
	times = -2

def clear():
	sec.set('00')
	mis.set('00')
	hrs.set('00')

root = Tk()
root.title("Timer Clock")
rw = 294
rh = 103
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw/2) - (rw/2) + 640
y = (sh/2) - (rh/2) - 520
root.geometry('%dx%d+%d+%d' % (rw, rh, x, y))
root.config(bg="#B8CFEC")

null_l = Label(root,text=' '*32,bg='#B8CFEC').grid(row=0,column=0)
one_l = Label(root,text='',bg='#B8CFEC').grid(row=0,column=1)
two_l = Label(root,text='',bg='#B8CFEC').grid(row=0,column=2)
three_l = Label(root,text='',bg='#B8CFEC').grid(row=0,column=3)
four_l = Label(root,text='',bg='#B8CFEC').grid(row=0,column=4)
five_l = Label(root,text='',bg='#B8CFEC').grid(row=0,column=5)
six_l = Label(root,text=' '*32,bg='#B8CFEC').grid(row=0,column=6)

sec = StringVar()
mis = StringVar()
hrs = StringVar()
var = IntVar()

Entry(root, textvariable=hrs, width=2, font='Castellar 14', bg='#B8CFEC').grid(column=2,row=2)
Entry(root, textvariable=mis, width=2, font='Castellar 14', bg='#B8CFEC').grid(column=3,row=2)
Entry(root, textvariable=sec, width=2, font='Castellar 14', bg='#B8CFEC').grid(column=4,row=2)

sec.set('00'.zfill(2))
mis.set('00'.zfill(2))
hrs.set('00'.zfill(2))

countup_b = Button(root, text='Countup', command=countuptimer,bg='#B8CFEC',font='Castellar 10').grid(columnspan=4,row=1,sticky=E+W)
countdown_b = Button(root, text='Countdown', command=countdowntimer,bg='#B8CFEC',font='Castellar 10').grid(column=4,columnspan=3,row=1,sticky=E+W)
stop_b = Button(root, text='Stop', command=stop,bg='#B8CFEC',font='Castellar 10').grid(columnspan=4,row=3,sticky=E+W)
clear_b = Button(root, text='Clear', command=clear,bg='#B8CFEC',font='Castellar 10').grid(column=4,columnspan=3,row=3,sticky=E+W)

root.mainloop()