import tkinter as Tkinter
from datetime import datetime
counter = 99993600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter==99993600:
                display=" "
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
            
            label['text']=display
            label.after(1000, count)
            counter += 1
			
    
    count()

		

def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	pause['state']='normal'
	reset['state']='normal'

def Pause():
	global running
	start['state']='normal'
	pause['state']='disabled'
	reset['state']='normal'
	running = False



def Reset(label):
	global counter
	counter=99993600

	if running==False:	
		reset['state']='disabled'
		label['text']='Timer'

	else:			
		label['text']=' '

window = Tkinter.Tk()
window.title("Countdown Timer")
window.geometry("400x150")
window.resizable(0,0)
label = Tkinter.Label(window, text="Timer", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(window)
start = Tkinter.Button(f, text='Start/Resume', width=10, command=lambda:Start(label))
pause = Tkinter.Button(f, text='Pause',width=10,state='disabled', command=Pause)
reset = Tkinter.Button(f, text='Reset',width=10, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
pause.pack(side ="left")
reset.pack(side="left")
window.mainloop()