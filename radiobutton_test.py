import tkinter as tk

root = tk.Tk()

# Create a variable to store the selected value
selected_option = tk.StringVar()

# Define radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="3")

# Arrange radio buttons
radio1.pack(anchor='w')
radio2.pack(anchor='w')
radio3.pack(anchor='w')

# Set a default selection
selected_option.set("1")

root.mainloop()
