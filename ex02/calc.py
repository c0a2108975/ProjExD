import tkinter as tk
root = tk.Tk()
root.geometry("300x500")
r,c = 0,0
for num in range(9,-1,-1):
    button = tk.Button(root,text=f"{num}",width  = 4,height = 2,font=("",30))
    button.grid(row=r,column=c)
    c+=1
    if c%3 == 0:
        r +=1
        c = 0
root.mainloop()