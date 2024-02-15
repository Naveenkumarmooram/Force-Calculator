import tkinter as tk
from PIL import Image, ImageTk
import math

# Function to calculate Drag Force
def calculate_drag_force():
    try:
        CD = float(cd_entry.get())
        A = float(a_entry.get())
        p = float(density_entry.get())
        v = float(velocity_entry.get())
        FD = 0.5 * CD * A * p * v ** 2
        drag_force_label.config(text=f"Drag Force: {FD:.2f} N")
        return FD
    except ValueError:
        drag_force_label.config(text="Please enter valid numbers.")
        return 0

# Function to calculate Gradient Force
def calculate_gradient_force():
    try:
        M = float(mass_entry.get())
        g = float(gravity_entry.get())
        α = math.radians(float(gradient_angle_entry.get()))  # Convert angle from degrees to radians
        Fg = M * g * math.sin(α)
        gradient_force_label.config(text=f"Gradient Force: {Fg:.2f} N")
        return Fg
    except ValueError:
        gradient_force_label.config(text="Please enter valid numbers.")
        return 0

# Function to calculate Rolling Resistance
def calculate_rolling_resistance():
    try:
        Fr = float(rr_coefficient_entry.get())
        M = float(mass_entry.get())
        g = float(gravity_entry.get())
        RR = Fr * M * g
        rolling_resistance_label.config(text=f"Rolling Resistance: {RR:.2f} N")
        return RR
    except ValueError:
        rolling_resistance_label.config(text="Please enter valid numbers.")
        return 0

# Function to calculate and display all forces and the total tractive force
def calculate_all_forces():
    FD = calculate_drag_force()
    Fg = calculate_gradient_force()
    RR = calculate_rolling_resistance()
    TTF = FD + Fg + RR  # Sum of forces
    total_tractive_force_label.config(text=f"Total Tractive Force: {TTF:.2f} N")

# Function to create and return an image label
def create_image_label(image_path, master=None, size =(500,500)):
    img = Image.open(image_path)
    img_resized = img.resize(size, Image.ANTIALIAS)  # Resize the image using Pillow
    img_tk = ImageTk.PhotoImage(img_resized)
    label = tk.Label(master=master, image=img_tk)
    label.image = img_tk  # Keep a reference!
    return label

# Main window setup
window = tk.Tk()
window.title("Force Calculator")

# Input fields and labels setup
cd_label = tk.Label(window, text="Coefficient of Drag (CD):")
cd_label.grid(row=0, column=2)
cd_entry = tk.Entry(window)
cd_entry.grid(row=0, column=3)

a_label = tk.Label(window, text="Frontal Area (A) [sq.m]:")
a_label.grid(row=1, column=2)
a_entry = tk.Entry(window)
a_entry.grid(row=1, column=3)

density_label = tk.Label(window, text="Air Density (ρ) [kg/m^3]:")
density_label.grid(row=2, column=2)
density_entry = tk.Entry(window)
density_entry.grid(row=2, column=3)

velocity_label = tk.Label(window, text="Velocity (v) [m/s]:")
velocity_label.grid(row=3, column=2)
velocity_entry = tk.Entry(window)
velocity_entry.grid(row=3, column=3)

mass_label = tk.Label(window, text="Mass of Vehicle (kg):")
mass_label.grid(row=4, column=2)
mass_entry = tk.Entry(window)
mass_entry.grid(row=4, column=3)

gravity_label = tk.Label(window, text="Gravity (m/s^2):")
gravity_label.grid(row=5, column=2)
gravity_entry = tk.Entry(window)
gravity_entry.grid(row=5, column=3)

gradient_angle_label = tk.Label(window, text="Gradient Angle (degrees):")
gradient_angle_label.grid(row=6, column=2)
gradient_angle_entry = tk.Entry(window)
gradient_angle_entry.grid(row=6, column=3)

rr_coefficient_label = tk.Label(window, text="Rolling Resistance Coefficient:")
rr_coefficient_label.grid(row=7, column=2)
rr_coefficient_entry = tk.Entry(window)
rr_coefficient_entry.grid(row=7, column=3)

# Calculate Forces Button
calculate_button = tk.Button(window, text="Calculate Forces", command=calculate_all_forces)
calculate_button.grid(row=8, column=2, columnspan=2)

# Result Labels
drag_force_label = tk.Label(window, text="Drag Force: N/A")
drag_force_label.grid(row=9, column=0)

gradient_force_label = tk.Label(window, text="Gradient Force: N/A")
gradient_force_label.grid(row=9, column=4)

rolling_resistance_label = tk.Label(window, text="Rolling Resistance: N/A")
rolling_resistance_label.grid(row=10, column=0)

total_tractive_force_label = tk.Label(window, text="Total Tractive Force: N/A")
total_tractive_force_label.grid(row=10, column=4)

# Image Labels
drag_force_image_label = create_image_label("D:/Projects&publications/Software/Tractive Force Calculator/Drag.jpg", window, size =(250,250))
drag_force_image_label.grid(row=9, column=1)

gradient_force_image_label = create_image_label("D:/Projects&publications/Software/Tractive Force Calculator/Gradient.jpg", window, size=(250,250))
gradient_force_image_label.grid(row=9, column=5)

rolling_resistance_image_label = create_image_label("D:/Projects&publications/Software/Tractive Force Calculator/Rolling.jpg", window,size=(250,250))
rolling_resistance_image_label.grid(row=10, column=1)

total_tractive_force_image_label = create_image_label("D:/Projects&publications/Software/Tractive Force Calculator/TTF.jpg", window,size=(250,250))
total_tractive_force_image_label.grid(row=10, column=5)

window.mainloop()
