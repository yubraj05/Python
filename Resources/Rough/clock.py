import tkinter as tk
from math import cos, sin, radians
from time import localtime, strftime

# Create the main window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("400x400")
root.config(bg="white")

# Create a Canvas widget to draw the clock
canvas = tk.Canvas(root, width=400, height=400, bg="white", bd=0, highlightthickness=0)
canvas.pack()

def draw_clock_face():
    # Draw the clock background (circle)
    canvas.create_oval(20, 20, 380, 380, fill="white", outline="black", width=5)

    # Draw hour ticks and minute ticks
    for i in range(60):
        angle = 6 * i
        radius = 120 if i % 5 else 140
        draw_tick(angle, radius)

    for i in range(12):
        angle = 30 * i
        draw_tick(angle, 150, is_hour_tick=True)

def draw_tick(angle, radius, is_hour_tick=False):
    # Calculate the position of the tick mark
    rad = radians(angle - 90)  # -90 for adjusting 0 degree to top
    print(angle,rad)
    x1 = 200 + radius * cos(rad)
    y1 = 200 + radius * sin(rad)
    x2 = 200 + (radius + 10) * cos(rad)
    y2 = 200 + (radius + 10) * sin(rad)

    # Draw the tick line
    color = "blue" if not is_hour_tick else "black"
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)

def draw_hand(angle, length, width, color):
    # Calculate the end point of the hand
    rad = radians(angle - 90)
    x = 200 + length * cos(rad)
    y = 200 + length * sin(rad)

    # Draw the hand line
    canvas.create_line(200, 200, x, y, width=width, fill=color)

def draw_numbers():
    # Numbers (12, 3, 6, 9) around the clock face, correctly placed
    font = ("Helvetica", 20)
    
    # Correct positions for 12, 3, 6, 9
    canvas.create_text(200, 90, text="12", font=font)   # 12 at the top
    canvas.create_text(295, 200, text="3", font=font)   # 3 on the right
    canvas.create_text(200, 355, text="6", font=font)   # 6 at the bottom
    canvas.create_text(105, 200, text="9", font=font)   # 9 on the left

def update_clock():
    # Get current time
    time = strftime("%H:%M:%S", localtime())
    hour, minute, second = map(int, time.split(":"))

    # Clear the canvas and redraw the clock face, hands, and numbers
    canvas.delete("all")
    draw_clock_face()
    draw_hands(hour, minute, second)
    draw_numbers()

    # Call the update_clock function again after 1000ms (1 second)
    root.after(1000, update_clock)

def draw_hands(hour, minute, second):
    # Calculate the angles of the hands
    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = (minute + second / 60) * 6
    second_angle = second * 6

    # Draw hour hand (in red)
    draw_hand(hour_angle, 50, 6, "red")
    # Draw minute hand (in blue)
    draw_hand(minute_angle, 70, 4, "blue")
    # Draw second hand (in red)
    draw_hand(second_angle, 90, 2, "red")

# Start the clock update
update_clock()

# Run the main loop
root.mainloop()
