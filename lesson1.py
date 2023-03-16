import tkinter

def m():
	v1 = int(var1.get())
	v2 = int(var2.get())
	v3 = int(var3.get())
	v4 = int(var4.get())

	if (v1 > v2) and (v1 > v3) and (v1 > v4):
		edit1['bg']='red'
	if (v2>v1) and (v2>v3) and (v2>v4):
		edit2['bg']='red'

	if (v3>v2) and (v3>v1) and (v3>v4):
		edit3['bg']='red'
	if (v4>v2) and (v4>v3) and (v4>v1):
  		edit4['bg']='red' 
 
window = tkinter.Tk()
 
var1 = tkinter.StringVar()   
var2 = tkinter.StringVar()
var3 = tkinter.StringVar()
var4 = tkinter.StringVar()


edit1 = tkinter.Entry(window, textvariable= var1)
edit1.pack()

edit2 = tkinter.Entry(window, textvariable=var2)
edit2.pack()

edit3 = tkinter.Entry(window, textvariable=var3)
edit3.pack()

edit4 = tkinter.Entry(window, textvariable=var4)
edit4.pack()

button = tkinter.Button(text="Визначити", command=m)
button.pack()

window.mainloop()   