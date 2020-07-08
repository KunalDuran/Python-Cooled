from tkinter import *
import webbrowser


Height = 370
Width = 150


def dothis():
    user_input = entry_field.get()
    path = "https://www.youtube.com/results?search_query="
    webbrowser.open(path+user_input)


root = Tk()
root.geometry('370x150')
root.title('No Distraction YouTube Search')


entry_field = Entry(root, font =5)
entry_field.pack()
entry_field.insert(0, "Enter here")


button1 = Button(root ,text='Search YouTube', command=dothis)
button1.pack(side=BOTTOM)


root.mainloop()



