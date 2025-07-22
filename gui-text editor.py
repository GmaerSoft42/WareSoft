try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog
    from tkinter import *
    import os
    global file_path
    global encoder
    global parameter
    file_path = ""
    encoder = "utf-8"
    parameter = 0
    def new_file():
        text.delete("1.0", tk.END)

    def open_file():
            global file_path
            global encoder
            file_path = filedialog.askopenfilename(title="Select file to open",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r", encoding=encoder) as file:
                    content = file.read()
                text.delete("1.0", tk.END)
                text.insert("1.0", content)

    def set_encoder():
        global encoder
        encoder = simpledialog.askinteger("GUI Text Editor", "Please select an encoder:\n[1] UTF-8 (most recommended for modern systems)\n[2] ANSI (Windows XP and older encoder, recommended as opening a file with the wrong encoder can break it)\n[3] Custom encoder")
        if encoder == 1:
            encoder = "utf-8"
        elif encoder == 2:
            encoder = "ansi"
        else:
            encoder = simpledialog.askstring("GUI Text Editor", "Enter an encoder name: ")

    def save_file():
        global encoder
        global file_path
        file_path = filedialog.asksaveasfilename(title="Select file to save",defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text.get("1.0", tk.END))
            messagebox.showinfo("Info", "File saved successfully!")
        
    def about():
        messagebox.showinfo("About", "Python Text Editor\nCreated by GamerSoft24.\n© GamerSoftware Corporation™. All rights reserved.\n\nEdits made by Okmeque1 Software. ")

    def set_parameter():
        global parameter
        parameter = 1 
    def freplace():
        global encoder
        global file_path
        global parameter
        counter = 0
        counter1 = 0
        match = False
        passon = {}
        tofind = simpledialog.askstring("GUI Text Editor","Enter thing to find in file: ")
        if parameter == 1:
            toreplace = simpledialog.askstring("GUI Text Editor","Enter thing to replace: ")
        with open(file_path,"r",encoding=encoder) as read1:
            dalines = read1.readlines()
            for x in range(len(dalines)):
                while counter < len(dalines[x]):
                    counter1 = 0
                    while counter1 <= len(tofind)-1 and dalines[x][counter] == tofind[counter1]:
                        counter += 1
                        counter1 += 1
                    if counter1 == len(tofind):
                        match == True
                        a = counter - len(tofind)
                        b = x
                        found = messagebox.showinfo("GUI Text Editor","Line where found : " + str(b+1) + "\nPosition in line : " + str(a+1))
                        parameter = 2
                        if b not in passon:
                            passon[b] = [a]
                        else:
                            passon[b].append(a)
                    if counter1 == 0:
                        counter += 1
            if parameter != 2:
                x = messagebox.showerror("GUI Text Editor",f"No matches found for {tofind}. Aborting replace operation...")
                parameter = 0
            if parameter == 2:
                parameter = 0
            counter = 0
            if parameter == 1:
                with open(file_path,"r",encoding=encoder) as replaceit:
                    lines = replaceit.readlines()
                    for x in passon:
                        for y in passon[x]:
                            lines[x] = lines[x][:y] + toreplace + lines[x][y + len(tofind):]
                with open(file_path,"w", encoding=encoder) as actuallyreplace:
                    for x in range(len(lines)):
                        actuallyreplace.writelines(lines[x])
                x = messagebox.showinfo("GUI Text Editor","Replacement Successful! The file will be re-loaded for the changes to take effect.")
                with open(file_path, "r", encoding=encoder) as file:
                    content = file.read()
                    text.delete("1.0", tk.END)
                    text.insert("1.0", content)
                    parameter = 0
    root = tk.Tk()
    root.title("Python Text Editor")

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Configure encoder", command=set_encoder)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Find & Replace ", command=set_parameter)
    edit_menu.add_command(label="Find", command=freplace)

    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    text = tk.Text(root)
    text.pack(fill=tk.BOTH, expand=True)

    root.geometry("800x600")
    root.mainloop()

except FileExistsError as e:
    x = messagebox.showerror("GUI Text Editor",f"There is a file conflicting with the file path that you specified. Change the name of any files that may be interfering, then try again.\nError code: 6510A\nDetails: {e}")
except FileNotFoundError as e:
    x = messagebox.showerror("GUI Text Editor",f"The specified file was not found. Make sure you entered the right file name and that the file is valid, then try again.\nError code: 6510B\nDetails: {e}")
except OSError as e:
    x = messagebox.showerror("GUI Text Editor",f"A system error has occured. To continue working, save your work in all programs, close any programs then restart your computer. \nError Code: 0271\nDetails: {e}")
except ValueError as e:
    x = messagebox.showerror("GUI Text Editor",f"You have entered a wrong value or this program has been tampered with. \nError Code: 0211\nDetails: {e}")
except LookupError as e:
    x = messagebox.showerror("GUI Text Editor",f"The specified incoder is invalid. Make sure that the encoder is installed and that you typed it correctly.\nError code: 1E/18\nDetails: {e}")
except UnicodeDecodeError as e:
    x = messagebox.showerror("GUI Text Editor",f"The specified encoder failed to parse the file. Try using a different encoder (so if you used UTF-8, try ANSI)\nError code: 1E/10\nDetails: {e}")
except UnicodeEncodeError as e:
    x = messagebox.showerror("GUI Text Editor",f"The specified encoder could parse and encode the data in the editor to a file.  Try using a different encoder (so if you used UTF-8, try ANSI)\nError code: 1E/10B\nDetails: {e}")
except KeyboardInterrupt:
    print("LOG: User has chosen to exit. Exiting...")
    exit()
except EOFError:
    print("LOG: User has chosen to exit. Exiting...")
    exit()
except IOError as e:
    x = messagebox.showerror("GUI Text Editor",f"I/O error. You have unplugged a device or a device on the host is malfunctioning.\nError Code: 0272\nDetails: {e}")
except Exception as e:
    x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception has occured in this program. To continue working, save your work in all programs, close any programs then restart your computer.\n\nRefer to the GitHub GamerSoft24/Software PySoft Error chart and the Python manual for more information.\nError code: 770A\nDetails: {e}")
except BaseException as e:
    x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception has occured in this program. To continue working, save your work in all programs, close any programs then restart your computer.\n\nRefer to the GitHub GamerSoft24/Software PySoft Error chart and the Python manual for more information.\nError code: 770A\nDetails: {e}")
except:
    x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception has occured in this program. To continue working, save your work in all programs, close any programs then restart your computer.\n\nRefer to the GitHub GamerSoft24/Software PySoft Error chart and the Python manual for more information.\nError code: 770A")
