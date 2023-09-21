#########################################
#                                       #
#              IMPRORTS                 #
#                                       #
#########################################

import tkinter as tk
from tkinter import filedialog

#########################################
#                                       #
#             FUNCTIONS                 #
#                                       #
#########################################


def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def submit_choices():
    file_path = file_entry.get()
    use_random_data = random_choice.get()

    # lets create a check => user cannot use random data and select a file


    # Process user's choices here
    print(f"File Path: {file_path}")
    print(f"Use Random Data: {use_random_data}")

#########################################
#                                       #
#                 MAIN                  #
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
algorithm_choice = tk.StringVar(root, "Algorithm 1")
algorithm1 = tk.Radiobutton(algorithm_frame, text="Algorithm 1", variable=algorithm_choice, value="Algorithm 1")
algorithm2 = tk.Radiobutton(algorithm_frame, text="Algorithm 2", variable=algorithm_choice, value="Algorithm 2")

algorithm_label.pack(side="top")
algorithm1.pack(side="top")
algorithm2.pack(side="top")

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_choices)

# Pack widgets
file_frame.pack(pady=10)
random_frame.pack(pady=10)
algorithm_frame.pack(pady=10)
submit_button.pack(pady=10)

root.mainloop()

