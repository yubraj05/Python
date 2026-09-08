import tkinter as tk
import Flames as fl 




    
import tkinter as tk

def calculate_flames(event=None):   # event=None → Enter key binding support
    name1 = entry_name1.get().strip()
    name2 = entry_name2.get().strip()

    if name1 == "" or name2 == "":
        result_label.config(text="⚠️ Please enter both names!", fg="red")
        return

    valc = fl.calculate(name1,name2)
    valy = fl.calculate(name2,name1)
    prompt = f"You love {name2} by {valc} \n{name2} loves you by {valy}"


    result_label.config(text=prompt, fg="white")


# ------------------------------
# ROOT WINDOW
# ------------------------------
root = tk.Tk()
root.title("FLAMES Calculator")
width = int(root.winfo_screenwidth()*0.75)
height = int(root.winfo_screenheight()*0.75)
root.geometry(f"{width}x{height}")
root.config(bg="#222831")  # dark theme

# Centering window (optional but looks good)
root.eval('tk::PlaceWindow . center')


# ------------------------------
# MAIN FRAME
# ------------------------------
frame = tk.Frame(root, bg="#393E46", padx=20, pady=20)
frame.pack(pady=20)


# Title
title = tk.Label(frame, text="🔥 FLAMES Calculator 🔥",
                 font=("Arial", 17, "bold"), bg="#393E46", fg="#00ADB5")
title.pack(pady=10)


# Name 1
label1 = tk.Label(frame, text="Enter Name 1:", bg="#393E46", fg="white")
label1.pack(anchor="w")
entry_name1 = tk.Entry(frame, width=28, font=("Arial", 12))
entry_name1.pack(pady=5)


# Name 2
label2 = tk.Label(frame, text="Enter Name 2:", bg="#393E46", fg="white")
label2.pack(anchor="w")
entry_name2 = tk.Entry(frame, width=28, font=("Arial", 12))
entry_name2.pack(pady=5)


# Calculate Button
calc_btn = tk.Button(frame,
                     text="Calculate",
                     font=("Arial", 12, "bold"),
                     bg="#00ADB5", fg="white",
                     activebackground="#007B7F",
                     command=calculate_flames)
calc_btn.pack(pady=15)


# Result Label
result_label = tk.Label(frame, font=("Arial", 14),
                        bg="#393E46", fg="white")
result_label.pack()


# ------------------------------
# ENTER KEY BINDING
# ------------------------------
root.bind("<Return>", calculate_flames)


# Focus on first entry
entry_name1.focus()

root.mainloop()
