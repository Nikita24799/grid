from tkinter import *
foto_list=["pilt1.png","pilt2.png","pilt3.png","pilt4.png","pilt5.png"]
ttt="ttt"
list_ = ["Чехов","Лермонтов","Достоевский","Есенин","Пушкин"]
def list_to_txt(event):
    global can,foto
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)
    foto=PhotoImage(file=foto_list[valik[0]])
    can.create_image(0,0,image=foto,anchor=NW)

def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)
def opisanie():
    global ttt
    text = txt.get(0.0, END)
    print(list(text))
    if text=="Чехов\n":
        ttt="Антон Павлович Чехов (1860–1904 гг.) – великий русский писатель, талантливый драматург, академик, врач по профессии. Самое главное в его творчестве – это то, что многие произведения стали классикой мировой литературы, а его пьесы ставятся в театрах по всему миру"
    elif text=="Лермонтов\n":
        ttt="Михаил Лермонтов — один из самых известных русских поэтов, и признание к нему пришло еще при жизни. Его творчество, в котором сочетались острые социальные темы с философскими мотивами и личными переживаниями, оказало огромное влияние на поэтов и писателей XIX–XX веков. «Культура.РФ» рассказывает о личности, жизни и творчестве Михаила Лермонтова."
    elif text=="Достоевский\n":
        ttt="Федор Достоевский с детства мечтал стать писателем. Первый же его роман «Бедные люди» высоко оценили Николай Некрасов и Виссарион Белинский, а четыре поздних произведения вошли в список «100 лучших книг всех времен»."
    elif text=="Есенин\n":
        ttt="Сергей Есенин не сразу нашел свое литературное кредо: он бросался из одного направления в другое. Сначала выступал в лаптях и рубахе с новокрестьянскими поэтами, затем, облачившись в пиджак и галстук, создавал с имажинистами новую литературу. В конце концов он отказался от всех школ и стал свободным художником, заявив: «Я не крестьянский поэт и не имажинист, я просто поэт»."
    elif text=="Пушкин\n":
        ttt="Александр Пушкин начал писать свои первые произведения уже в семь лет. В годы учебы в Лицее он прославился, когда прочитал свое стихотворение Гавриилу Державину. Пушкин первым из русских писателей начал зарабатывать литературным трудом. Он создавал не только лирические стихи, но и сказки, историческую прозу и произведения в поддержку революционеров — за вольнодумство поэта даже отправляли в ссылки."
    else:
        ttt="ппппппппппппппппппппп"
    opis.config(text=ttt)



win=Tk()
win.geometry("600x600")
win.title("Проверочная работа")
lbox=Listbox(win,width=20,height=5,selectmode=SINGLE)
lbox.insert(1, "Чехов")
lbox.insert(2, "Лермонтов")
lbox.insert(3, "Достоевский")
lbox.insert(4, "Есенин")
lbox.insert(5, "Пушкин")
for element in foto_list:
    lbox.insert(END,element)

lbox.pack()
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=4,width=20,wrap=WORD)
txt.pack()
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=200,bg="gold")
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
panel = Label(win, image = pc)
panel.pack(side = "bottom", fill = "both", expand = "yes")
foto=PhotoImage(file="pilt1.png")
btn=Button(text='Справка', command=opisanie).pack()#, command=op
opis=Label(win, text="", width=50, height=20)
opis.pack()
can.pack()
win.mainloop()

