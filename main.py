import tkinter as tk
import random

def generate_password():
    # Lists of possible characters
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    spec = ['.',',','-','!','%','/','$','>','<','}','#']
    num = ['0','1','2','3','4','5','6','7','8','9']

    random.shuffle(abc)
    random.shuffle(spec)
    random.shuffle(num)

    passwrd = []
    length = int(entry_length.get())  # Retrieving password length from the user

    # Adding letters to the password
    for i in range(0,len(abc)):
        if abc[i] == abc[10]:
            break
        else:
            if i %2 == 0:
                passwrd.append(abc[i].lower())
            else:
                passwrd.append(abc[i].upper())

    # Adding special characters to the password
    for i in range(0,len(spec)):
        if spec[i] == spec[5]:
            break
        else:
            passwrd.append(spec[i])

    # Adding numbers to the password
    for i in range(0,len(num)):
        if num[i] == num[5]:
            break
        else:
            passwrd.append(num[i])

    # Randomly shuffling the elements of the password and generating the password
    random.shuffle(passwrd)
    generated_password = ''.join(passwrd[:length])

    # Displaying the generated password in the Text widget
    text_widget.config(state='normal')  # Allowing text input
    text_widget.delete('1.0', tk.END)   # Deleting text
    text_widget.insert(tk.END, generated_password)  # Inserting generated password
    text_widget.config(state='disabled')  # Disabling text input

def copy_password():
    # Copying selected text to clipboard
    text_widget.clipboard_clear()  # Clearing clipboard content
    text_widget.clipboard_append(text_widget.get("1.0", tk.END))  # Appending selected text to clipboard

root = tk.Tk()
root.title("Password Generator")
root.configure(bg='black')  # Setting window background color
root.geometry("400x200")   # Setting window size

background_color = "black"   # Background color
foreground_color = "white"   # Text color

label_length = tk.Label(root, text="Password length:", bg=background_color, fg=foreground_color)  # Label for password length
label_length.pack()

entry_length = tk.Entry(root)  # Entry field to set password length
entry_length.pack()

button_generate = tk.Button(root, text="Generate Password", command=generate_password, bg=background_color, fg=foreground_color)  # Button to generate password
button_generate.pack()

text_widget = tk.Text(root, height=1, width=20, bg=background_color, fg=foreground_color)  # Text widget to display the generated password
text_widget.pack()

copy_button = tk.Button(root, text="Copy", command=copy_password, bg=background_color, fg=foreground_color)  # Button to copy password
copy_button.pack()

root.mainloop()
