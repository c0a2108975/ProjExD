import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

#maze_maker.make_maze(15, 9)

root = tk.Tk()

"""def keikoku():
    tkm.showwarning("警告","やり直してください")

def celebrate():
    tkm.showinfo("ゴール","おめでとう")


def first():
    canvas.create_rectangle(100,200,200,100, fill="black")

def end():
    canvas.create_rectangle(1300,700,1400,800, fill="red")

def count_up():
    global tmr
    tmr = tmr-1
    if tmr == 0:
        keikoku()
        
    label["text"] = tmr
    root.after(1000,count_up)
    root.after(11000,lambda:root.destroy())
    """
def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global key ,mx ,my,cx,cy
    x = mx
    y = my
    if key == "Up":
        my -=1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1

    if  meiro[mx][my] == 0:
        cx = 100*mx+50
        cy = 100*my+50
    
    else:
        mx = x
        my = y
    
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)
    """if mx == 13 and my == 7:
        celebrate()

    else:
        root.after(100,main_proc)"""
    
   

if __name__ =="__main__":
    meiro = maze_maker.make_maze(15, 9)
    mx,my = 1,1
    label = tk.Label(root,font=("Times New Roman",80))
    label.pack()
    tmr = 20
    #root.after(1000,count_up)
    canvas = tk.Canvas(root,width = 1500,height= 900,bg = "black")
    maze_maker.show_maze(canvas,meiro)
    #first()
    #end()
    tori = tk.PhotoImage(file = "ex03/fig/fig/0.png")
    cx,cy = 150,150
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    canvas.pack()

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()

   
root.mainloop()