# Vehicle Force Calculator Application
# Description
This Force Calculator is a desktop application developed with Python and Tkinter.

It's designed to calculate and display the Drag Force, Gradient Force, Rolling Resistance, and Total Tractive Force affecting a vehicle based on user-provided input parameters. The application also showcases relevant images next to each force calculation to provide a visual understanding of how these forces impact a vehicle.

# Features
Calculate Drag Force using the coefficient of drag, frontal area, air density, and velocity.

Calculate Gradient Force considering the mass of the vehicle, gravity, and gradient angle.

Calculate Rolling Resistance based on the rolling resistance coefficient, mass of the vehicle, and gravity.

Display the Total Tractive Force as the sum of the above forces.

Display images next to each force calculation for a better visual understanding.

# Installation
# Prerequisites
Python 3.x installed on your system.

PIL (Python Imaging Library), also known as Pillow, for handling image files.

# Steps
Ensure Python 3.x is installed on your system. You can download it from python.org.

Install Pillow using pip (Python's package installer). Open your terminal or command prompt and run: pip install Pillow

Download the application files to a directory on your computer.

Ensure the images (Drag.jpg, Gradient.jpg, Rolling.jpg, TTF.jpg) are located in the specified directory within the code, or update the paths in the code to match their locations on your system.

# Usage
Navigate to the directory containing the application files in your terminal or command prompt.

Run the application with the command: python Forces_Calculator.py

Enter the required parameters for each force calculation in the provided input fields.


Click the "Calculate Forces" button to display the calculation results and corresponding images.

# Customization
You can replace the images with your preferred visual representations by updating the image paths in the code.

Adjust the size of the images displayed in the application by modifying the size parameter in the create_image_label function call.

# Support
For support, please ensure you've followed all installation steps correctly. If issues persist, verify your Python and Pillow installations.

For further assistance, consider reaching out on platforms like Stack Overflow or Python forums.
