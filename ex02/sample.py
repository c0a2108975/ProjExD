import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()
root.geometry("500x200")
label = tk.Label(root,text="ラベルを書いてみた件",font=("",20))
label.pack()
button = tk.Button(root,text="押すな")
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
button.bind("<1>",button_click)
button.pack()
entry = tk.Entry(root,width = 30)
entry.insert(tk.END,"fugapiyo")
entry.pack()

root.mainloop()
