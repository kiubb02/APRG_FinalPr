#########################################
#                                       #
#               IMPORTS                 #
#                                       #
#########################################

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# random is needed for randomly generating n amounts of (x,y) Coordinates
import random
# our imports for the algorithms used
import algorithms.giftwrapping as jm
import algorithms.andrews as qh


#########################################
#                                       #
#             FUNCTIONS                 #
#                                       #
#########################################

def generate_data_rand():
    coordinates = []
    for _ in range(20): # TODO: Set another number => are 20 points enough ?
        # generate them in floats
        x = random.uniform(0.0, 100.0)  # Generate a random x coordinate between 0 and 100
        y = random.uniform(0.0, 100.0)  # Generate a random y coordinate between 0 and 100
        coordinates.append((x, y))
    return coordinates


def generate_file():
    n = 200
    file_name = "files/input_points.txt"

    with open(file_name, 'w') as file:
        file.write(f"Number of points: {n}\n")
        for i in range(1, n + 1):
            x = random.uniform(0, 100)  # Adjust the range as needed
            y = random.uniform(0, 100)  # Adjust the range as needed
            file.write(f"{i}: {x},{y}\n")


def generate_data_file(file):
    # assuming we get a simple txt file
    # firstly open the file in mode "r" ... r = read
    with open(file, 'r') as file:
        lines = file.readlines()

    # get the number of points => split the first line and get the last element which would be the number of points
    # idk if we will need it for now I commented it out
    # num_points = int(lines[0].split()[-1])
    coordinates = []
    for line in lines[1:]:
        parts = line.strip().split(':')
        index = int(parts[0])
        x, y = map(float, parts[1].strip().split(','))
        coordinates.append((x, y))

    return coordinates


def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def submit_choices():
    file_path = file_entry.get()
    use_random_data = random_choice.get()
    selected_algorithm = algorithm_choice.get()
    selected_mode = mode_choice.get()

    # Process user's choices here
    # check the users choices
    # selected mode will not be checked it will just be given to the main function of the chosen algorithm class
    if file_path and use_random_data == "Yes":
        messagebox.showerror("Error", "Please only select one Data Source.")
        return

    # firstly we generate the data
    if file_path:
        data = generate_data_file(file_path)
    else:
        data = generate_data_rand()
    # data is always an array of tuples meaning it looks the following: [(2.2, 3.3), (4.5,2.3), ...]

    # then we check which algorithm was chosen and call this function
    if selected_algorithm == "Gift Wrapping":
        print("Gift Wrapping was chosen") # here will be a function call
        jm_ = jm.GiftWrapping(data, selected_mode)
        jm_.convex_hull()
    else:
        print("Andrews was chosen") # here will be a function call
        qh_ = qh.AndrewsAlgorithm(data, selected_mode)
        qh_.convex_hull_andrew()


#########################################
#                                       #
#                  UI                   #
#                                       #
#########################################

root = tk.Tk()
root.title("Solve Convex Hull")

# Menu for browsing files
file_frame = tk.Frame(root)
file_label = tk.Label(file_frame, text="File Path:")
file_entry = tk.Entry(file_frame, width=30)
browse_button = tk.Button(file_frame, text="Browse", command=browse_file)

file_label.pack(side="left")
file_entry.pack(side="left")
browse_button.pack(side="left")

# Radio buttons for random data
random_frame = tk.Frame(root)
random_label = tk.Label(random_frame, text="Use Random Data:")
random_choice = tk.StringVar(root, "Yes")
random_yes = tk.Radiobutton(random_frame, text="Yes", variable=random_choice, value="Yes")
random_no = tk.Radiobutton(random_frame, text="No", variable=random_choice, value="No")

random_label.pack(side="left")
random_yes.pack(side="left")
random_no.pack(side="left")

# Radio buttons for algorithm selection
algorithm_frame = tk.Frame(root)
algorithm_label = tk.Label(algorithm_frame, text="Select Algorithm:")
algorithm_choice = tk.StringVar(root, "Gift Wrapping")
algorithm1 = tk.Radiobutton(algorithm_frame, text="Gift Wrapping", variable=algorithm_choice, value="Gift Wrapping")
algorithm2 = tk.Radiobutton(algorithm_frame, text="Andrews Algorithm", variable=algorithm_choice, value="Andrews")

algorithm_label.pack(side="top")
algorithm1.pack(side="top")
algorithm2.pack(side="top")

# Radio buttons for Mode selection
mode_frame = tk.Frame(root)
mode_label = tk.Label(mode_frame, text="Select Mode:")
mode_choice = tk.StringVar(root, "Performance Optimized")
mode1 = tk.Radiobutton(mode_frame, text="Performance Optimized", variable=mode_choice, value="optimized")
mode2 = tk.Radiobutton(mode_frame, text="Visual Mode", variable=mode_choice, value="visual")

mode_label.pack(side="top")
mode1.pack(side="top")
mode2.pack(side="top")

# generate data points file button
file_button = tk.Button(root, text="Generate Data File", command=generate_file)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_choices)

# Pack widgets
file_frame.pack(pady=10)
random_frame.pack(pady=10)
algorithm_frame.pack(pady=10)
mode_frame.pack(pady=10)
submit_button.pack(pady=10)
file_button.pack(pady=10)

root.mainloop()
