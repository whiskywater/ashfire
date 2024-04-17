import tkinter as tk
import os
import shutil
import random
import string

def fill_disk_with_random_data():
    # Ask user to select the drive
    drive = drive_var.get()

    # Check if user canceled the selection
    if not drive:
        result_label.config(text="Please select a drive.")
        return

    # Get the total size and free space of the drive
    total, used, free = shutil.disk_usage(drive)

    # Calculate the available space
    available_space = free

    # Generate random data
    random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))

    # Write random data to drive until it's full
    try:
        with open(os.path.join(drive, "random_data.bin"), 'wb') as f:
            while available_space > 0:
                chunk_size = min(available_space, len(random_data))
                f.write(random_data[:chunk_size].encode())
                available_space -= chunk_size

        # Inform user that operation is completed
        result_label.config(text="Disk filled with random data and cleared.")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

    # Delete the file after writing
    os.remove(os.path.join(drive, "random_data.bin"))

# Create the main window
root = tk.Tk()
root.title("Disk Filler")

# Get list of available drives
drives = [drive + ":/" for drive in string.ascii_uppercase if os.path.exists(drive + ":/")]

# Create label
label = tk.Label(root, text="Select a drive to fill with random data:")
label.pack(pady=10)

# Create drive selection dropdown
drive_var = tk.StringVar(root)
drive_var.set(drives[0])  # Set default value
drive_dropdown = tk.OptionMenu(root, drive_var, *drives)
drive_dropdown.pack()

# Create fill button
fill_button = tk.Button(root, text="Fill Disk", command=fill_disk_with_random_data)
fill_button.pack(pady=5)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
