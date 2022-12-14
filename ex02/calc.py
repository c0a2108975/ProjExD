import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    txt = entry.get()
    if len(txt) == 1:
        if txt == "+" or txt == "*" or txt == "/" or txt == "^" or txt == "=" or txt == "税込":
            return
    if num == "=":
        pass
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    
    elif num == "c":
        entry.delete(0,tk.END)

    elif num == "税込":
        siki = entry.get()
        res = eval(siki)
        res = res*1.1
        entry.insert(tk.END,int(res*1.1))

    elif num == "**":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res**2)

    else:
        entry.insert(tk.END,num)

root = tk.Tk()
root.geometry("400x1000")
entry = tk.Entry(root,justify="right",width = 10,font= ("",40))
entry.grid(row=0,column=0,columnspan=3)

r,c = 1,0

for num in range(9,-1,-1):
    button = tk.Button(root,text=f"{num}",width  = 4,height = 2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%3 == 0:
        r +=1
        c = 0
operators = ["+","=","**","-"]
r,c = 4,1
for ope in operators:
    button = tk.Button(root,text=f"{ope}",width = 4,height = 2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r +=1
        c = 1

operators2 = ["*","/","c","税込"]
r,c = 1,3
for ope2 in operators2:
    button = tk.Button(root,text=f"{ope2}",width = 4,height = 2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    r += 1
    if c%4 == 0:
        r +=1
        c = 0

root.mainloop()