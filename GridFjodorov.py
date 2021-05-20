from tkinter import *
list_ = ["2","3","4","6","5.1"]
foto_list=["2.png","3.png","4.png","6.png"]
global can, pc
def list_to_txt(event):
	global can, pc
	txt.delete(0.0,END)
	valik=lbox.curselection()
	txt.insert(END,lbox.get(valik[0]))
	print(lbox.get(valik[0]))
	can.delete(ALL)
	pc = PhotoImage(file=foto_list[valik[0]])
	print(foto_list[valik[0]])
	can.create_image(0,0,image=pc,anchor=NW)


def txt_to_list(event):
	text=text.get(0.0,END)
	text=text[-2:-1]
	if text--"/n":
		pass
	else:
		foto_list.append(text)
	lbox.config(height=len(foto_list))
	lbox.insert(END,text)
	txt.delete(0.0,END)
	text-""

def opisanie():
	text = txt.get(0.0, END)
	print(list(text))
	if text=="11.png\n":
		ttt="i9 10900kf \n rtx 3070 gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 2000 Euro "
	elif text=="12.png\n":
		ttt="i7 10700f \n rtx 3060ti gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 1500 Euro "
	elif text=="13.png\n":
		ttt="i5 10600\n rtx 3060 gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 800 Euro "
	elif text=="14.png\n":
		ttt="i3 10100 \n gtx 1050 ti \n 16gb DDR4 Crucial Ballisitix 3200 mhz \n 550w Cooler master MWE \n 600 Euro "
	opis.config(text=ttt)



win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
	lbox.insert(END,element)

lbox.pack()
lbox.bind("«ListboxSelect»",list_to_txt)
txt=Text(win,height=4,width=20,wrap=WORD)
txt.pack()
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=200,bg="gold")
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
panel = Label(win, image = pc)
panel.pack(side = "bottom", fill = "both", expand = "yes")
foto=PhotoImage(file="4.png")
bt=Button(text='Info', command=opisanie).pack()#, command=op
opis=Label(win, text="", width=50, height=20)
opis.pack()
can.pack()
win.mainloop()
