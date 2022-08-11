from tkinter import *
import time
def click():
   exec(open('StopWatch.py').read())
print('Fuck')
window = Tk()
button = Button(window, text = 'Do it, Kass. \n You know you want to.')
button.config(command=click) #performs callback of fcn
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