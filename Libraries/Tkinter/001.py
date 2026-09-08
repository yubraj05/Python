import tkinter as tk


root = tk.Tk()

root.title("New")

width = int(root.winfo_screenwidth()*0.5)
height = int(root.winfo_screenheight()*0.5)
print(width,height)
root.geometry(f"{width}x{height}")

r1 = tk.Label(root,text= "Its a flexible label",bg = "grey",padx=5,pady=5)
r1.pack()

image = tk.PhotoImage(file = "logo.png")

photo_label = tk.Label(root,image = image)
photo_label.place(x=100,y=200)





root.mainloop()

