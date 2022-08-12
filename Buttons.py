from tkinter import *
import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

start_time = time.time()

end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
def onclick(args):
   if args == 1:
      start_time = time.time()
   if args == 2:
      end_time = time.time()

print('Fuck')
window = Tk()
button = Button(window, text = 'Start', command=lambda:onclick(1))
button1 = Button(text = "Stop",command=lambda:onclick(2))
#button.config(command=click) #performs callback of fcn
button.config(font=('Ink Free', 60, 'bold'))
button.config(bg='#fffb1f') #bg color/might be borked atm
button.config(fg='#fffb1f') #text color
button.config(activebackground='#FF0000') #colors active bg
button.config(activeforeground='#FF0000') #colors active text
# upload card images here image = PhotoImage(file='file_name.extension')
#button.config(image = image) --the name of the variable image that is under the same main folder ad the project
#button.config(compound='top') replaces text on top and image on bottom. Works for putting text in whatever area you set-- top bottom left right
#button.config(state=DISABLED) #sets state of button. ACTIVE or DISABLED
#label = Label(window, text = whatever youre text it here)
#label.pack()
button.pack()
window.mainloop()