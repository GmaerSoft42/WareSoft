import time
import random
import os
from cryptography.fernet import Fernet
import hashlib
if os.name != 'nt':
    input("Sorry, this program is not compatible with the operating system that you are using. For best results, please use Windows 10 or later")
    exit()
global prodkey
global preinstalled
global installed
global order
prodkey = ""
preinstalled = False
installed = False
order = ["REM","HDD"]
def clear():
    if os.name == 'nt':
        os.system('cls')
        return
    else:
        os.system('clear')
        return
def setup():
    clear()
    global prodkey
    global preinstalled
    global installed
    global order
    print('========================================')
    print('                   GKC Setup            ')
    print('========================================')
    print('A : Install GKC from Removable Device')
    print('B : Start computer with plain iCMD Shell   ')
    print('C : Boot from system disk  ')
    setup_input = input('Pick a choice : A (A) , B (B) , C (C) ')
    if setup_input == 'A':
        print('XMA ScanDisk')
        scandisk = input ('ScanDisk is checking for errors in drive C. Press ENTER to continue')
        progressbar = []
        for x in range(101):
            progressbar.append("░")
        if scandisk == '':
            for x in range(101):
                print(f'{x}% ', "".join(progressbar),end='\r')
                progressbar[x] = "▓"
                time.sleep(random.randint(1,2))

        copy = input('No Errors were found. Setup will now copy all of the required files. Press ENTER to continue...                             ')
        if copy == '':
            print('Setup will now continue')
        for y in range(698):
            print(f'Setup is copying file {y}...please wait', end='\r')
            time.sleep(random.choice([0,0,0,0,0,0,0.1,0.45,0.7,1]))
            print(f'Setup is copying file {y}...Done!',end='\r')
        print('Setup needs to restart your computer to continue.')
        file = input('Your computer will restart when you press ENTER')
        if file == '':
            print('Your computer should restart...')
            clear()
            time.sleep(5)
        preinstalled = True
        kickstart()
    if setup_input == 'B':
        print('Computer is loading iCMD, please wait...')
        time.sleep(5)
        icmdlite()
    if setup_input == 'C':
        order[0] = "HDD"
        kickstart()
def oobe():
        global prodkey
        global preinstalled
        global installed
        global order
        clear()
        global installed
        if preinstalled != True:
            print("GKC Not installed properly! - Please run the GKC Setup program.")
            input("Press ENTER to BOOT...")
            preinstalled = False
            kickstart()
        product_key = ''
        if prodkey !=  'ZF3R0-FHED2-M80TY-8QYGC-NPKYF':
            while product_key != 'ZF3R0-FHED2-M80TY-8QYGC-NPKYF':
                clear()
                print('Please enter your product key(e.g : XXXXX-XXXXX-XXXXX-XXXXX-XXXXX) - Type ` to abort setup')
                product_key = input('Product Key: ')
                if product_key == 'ZF3R0-FHED2-M80TY-8QYGC-NPKYF':
                    print('Setup will now continue...')
                    break
                if product_key == '`':
                    clear()
                    setup()
                else:
                    print('Invalid product key! Please try again or press CTRL-C to END setup.')
        print('Setup is now scanning for plug and play hardware...')
        time.sleep(2)
        print('If your computer is not responding, restart your computer')
        time.sleep(7)
        print("Updating system settings...")
        progressbar = []
        for x in range(100):
            progressbar.append("░")
        for x in range(100):
                print(f'{x}% ', "".join(progressbar),end='\r')
                progressbar[x] = "▓"
                time.sleep(random.randint(0,1))
        print('Setup has finished configuring your system. Press ENTER to reboot the system: ')
        installed = True
def fm(sdir):
    global prodkey
    global preinstalled
    global installed
    global order
    flag = True
    try:
        try:
            while flag == True:
                clear()
                dshow = "dir " + sdir + " /p"
                os.system(dshow)
                valid = [1,2,3,4,5,6,7,8,9,10,11]
                print("Operations :")
                print("[1] Change DIR")
                print("[2] Run file ")
                print("[3] Make FOLDER")
                print("[4] Make FILE")
                print("[5] Move FILES")
                print("[6] Copy FILES")
                print("[7] None")
                print("[8] Enter CMD.EXE")
                print("[9] Delete DIR")
                print("[10] Delete FILE")
                print("[11] Exit")
                print("Current DIR : " + sdir)
                userchoice = int(input("Choose : "))
                print("Loading specified utility,please wait...")
                time.sleep(1)
                badchoice = True
                for x in range(len(valid)):
                    if valid[x] == userchoice:
                        badchoice = False
                        break
                if badchoice == True:
                    input("Invalid choice. Press ENTER to continue")
                if userchoice == 1:
                    chdir = input("Enter a VALID directory to change to : ")
                    os.chdir(chdir)
                    sdir = chdir
                    input("DIR changed. Press ENTER to continue...")
                elif userchoice == 2:
                    runfl = input("Enter a VALID file to run :")
                    os.system(runfl)
                    input("No Errors were logged. Press ENTER to continue...")
                elif userchoice == 3:
                    mkdir = input("Enter DIR file path/name(Example : C:\ST\TEST) : ")
                    mkdir0 = "mkdir " + mkdir
                    os.system(mkdir0)
                    input("DIR made with no errors. Press ENTER to continue...")
                elif userchoice == 4:
                    make = input("Enter a VALID file name to create(Example : C:\ST\TEST\TEST.TXT) : ")
                    with open(make,"x"):
                        input("File made with no errors. Press ENTER to continue...")
                elif userchoice == 5:
                    move = input("From : ")
                    to = input("To : ")
                    moveto = "move " + move + " " + to
                    os.system(moveto)
                    input("Moved " + move + " to " + to + " with no errors. Press ENTER to continue...")
                elif userchoice == 6:
                    copy = input("From : ")
                    dest = input("To : ")
                    copyto = "copy " + copy + " " + dest
                    os.system(copyto)
                    input("Copied " + copy + " to " + dest + " with no errors. Press ENTER to continue...")
                elif userchoice == 7:
                    time.sleep(3)
                    print("FAILED : Exiting to GKC...")
                    time.sleep(1)
                    flag = False
                elif userchoice == 8:
                    os.system("C:\Windows\System32\CMD.EXE")
                elif userchoice == 9:
                    rmdir = input("Enter DIR to remove : ")
                    os.rmdir(rmdir)
                    input("Removed DIR with no errors. Press ENTER to continue...")
                elif userchoice == 10:
                    rmf = input("Enter FILE to remove : ")
                    os.remove(rmf)
                    input("Removed File with no errors. Press ENTER to continue...")
                elif userchoice == 11:
                    flag = False
            icmd()
        except PermissionError:
            input("STOP : 0210\nYou do not have the permissions to edit this file. Press ENTER to exit...")
            flag = False
        except FileNotFoundError:
            input("STOP : 6510B\nFile or folder specified is not valid. Please specify a valid file or folder\nPress ENTER to exit...")
            flag = False
        except EOFError:
            print("STOP : 0250\nYou have raised EOFError and will now exit to GKC.\nDetails : User raised EOFError unexpectedly which was caught by an except block.")
            flag = False
        except ValueError:
            input("STOP : 0211\nInvalid parameter.Acceptable values are from 1-9. Press ENTER to exit...")
            flag = False
        except KeyboardInterrupt:
            print("STOP : 0270\nKeyboardInterrupt called. Now exiting to GKC...")
            flag = False
        except IOError:
            input("STOP : 6510C\nAn I/O error has occured. Exiting to GKC...")
            flag = False
        except:
            input("STOP : 770A\nAn unexpected error occured. Press ENTER to exit...")
            flag = False
    except:
        flag = False
def icmd():
    global prodkey
    global preinstalled
    global installed
    global order
    try:
        clear()
        iprompt = 'GKC>'
        ver = 'iCMD Full 1.05A - Okmeque1 Corporation - (c) Okmeque1 Corporation 2023-2097 All Rights Reserved.'
        print(ver)
        print("GKC Version 1.0")
        print("GKC Command Line Version 1.0 with all utilities available. Type 'dsc' for more informatoin")
        try:
            flag = True
            import os
            while flag == True:
                prompt = input(iprompt)
                if 'prompt:' in prompt:
                    iprompt = prompt[7:] + ">"
                prompt = prompt.lower()
                if prompt == 'files':
                    fm("%USERPROFILE%")
                if prompt == 'pwd':
                    pwd()
                if prompt == 'exit' or prompt == 'return':
                    flag = False
                elif prompt == 'ver':
                    print(ver)
                elif 'cd' in prompt[0:3]:
                    os.chdir(prompt[3:])
                elif prompt == 'dsc':
                    print("iCMD - Custom Command Line interface")
                    print("Okmeque1 Corporation is not liable for any damages done to any computers or people using this program.")
                    print("This is the GKC Operating System shell. If the product has been installed correctly, GKC has been optimised carefully for your choice of hardware")
                    print("GKC comamnds:")
                    print("files : file manager")
                    print("pwd : password manager")
                    print("exit or return : reboot computer to startup menu")
                elif 'prompt' in prompt and 'prompt:' not in prompt:
                    print("Usage : PROMPT:[STRING]")
                else:
                    os.system(prompt)
            win()
        except:
            print("STOP : 0281\nThe program has forcibly exited with code 1")
            input("Press ENTER to exit...")
            return None
    except:
            print("STOP : 0281\nThe program has forcibly exited with code 1")
            input("Press ENTER to exit...")
            return None
def keygen():
    print("Program made by Okmeque1")
    keygen1 = input("Please enter a valid file name to generate the key(Please make sure that the file is empty before use.) → ")
    key = Fernet.generate_key()
    with open(keygen1,"wb") as openfl:
        openfl.write(key)
    cont = input("Generate other key?[Y,any invalid option to abort]")
    if cont == "Y":
        keygen()
    else:
        return
def enc(key):
    try:
        file_enc = input("Please enter a valid file name to encrypt → ")
        with open(file_enc,"rb") as lwe:
            towr = lwe.read()
        key1 = Fernet(key)
        encrypted = key1.encrypt(towr)
        with open(file_enc,"wb") as twrite:
            twrite.write(encrypted)
        print("Encrypted with no errors")
    except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to exit.")
        win()
    except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit. Exiting...")
        win()
def dec(key):
    try:
        file_dec = input("Please enter a valid file name to decrypt → ")
        with open(file_dec,"rb") as lwd:
            tore = lwd.read()
        key2 = Fernet(key)
        decrypted = key2.decrypt(tore)
        with open(file_dec,"wb") as td:
            td.write(decrypted)
        print("Decrypted with no errors.")
    except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to exit.")
        win()
    except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        win()
def pwd():
    try:
            flag = True
            print("****THE OPEN SOURCE PASSWORD SECURITY SYSTEM - HASH EDITION****")
            print("Program version 1.2.0")
            print("DISCLAIMER : THIS PROGRAM NOR OKMEQUE1 CARES ABOUT YOUR PASSWORD FILE.IF YOU LOSE INFORMATION DUE TO THIS PROGRAM,YOU ARE THE ONE RESPONSIBLE FOR THE DAMAGES!")
            a = input("Do you have an encryption key? [Y/N]: ")
            if a != 'Y':
                keygen()
            keychose = input("For this program to function properly, you must provide the file path for the key to encrypt and decrypt(none to a default of G:\Python\Demo\key.txt.).If you do not have a key, please quit and re-run this program, saying 'N' at the prompt where you are asked if you have encryption key : ")
            if keychose == "":
                keychose = "G:\python\demo\key.txt"
            while flag == True:
                with open(keychose,"rb") as load:
                    key = load.read()
                print("Affiliate company © TCG - Technology, Coding and Gaming Inc ™")
                print("1 -> Add or generate password to save file.")
                print("2 -> Retrieve password from save file.")
                print("3 -> Format save file")
                print("4 -> More info.")
                print("5 -> Encrypt files(this option is required as part of security.)")
                print("6 -> Decrypt files(this option is REQUIRED to run this program with no errors.)")
                print("7 -> Advanced Password Generator")
                print("8 -> Change a password")
                print("9 -> Save and quit")
                print("When you are asked a valid file name,please make sure that the directory is valid and for best compatability,please make sure that the file already exists.")
                print("If you are a non-technical user,please choose option 4 before proceeding as it tells you about filepaths,OS compatability and more.")
                print("This is an open-source program so you can share it anywhere on the internet,USB/CD/DVD or other media.Please mention in your copy Okmeque1 so that the original code is not lost to time.")
                option = int(input("Select option : "))
                if option == 1:
        
        
                    print('Welcome to your password generator')
        
                    chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
        
                    number = 1
        
                    length = input('Password length ')
                    length = int(length)
                    if length <= 10:
                        print("Password not long enough.Please choose a longer character(a minimum of 15 is recommended)")
                    
                    
        
        
                    for pwd in range(number):
                        passwords = ''
                        for c in range(length):
                            passwords += random.choice(chars)
                            
                            print("You are at " + str(c) + " of " + str(length) + " complete.")
                        print("")
                        print(passwords)
                        print("")
                        print('Passwords Generated.Saving...')
                        filename = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
                        if filename == "":
                            filename = "G:\python\demo\demo.pc"
                            set0 = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                            passave = open(filename,"a")
                            passave.write(set0 + " -> " + passwords + "\n")
                            passave.close()
                        else:
                            set0 = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                            passave = open(filename,"a")
                            passave.write(set0 + " -> " + passwords + "\n")
                            passave.close()
                        print("Save has completed with no disk errors.")
                        print("Now returning to the main menu")
                elif option == 2:
                    fileopen = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
                    if fileopen == "":
                        fileopen = "G:\python\demo\demo.pc"
                        passopen  = open(fileopen,"r")
                        set1 = input("Please enter the set name for the desired password. : ")
                        for line in passopen:
                            if line.split(" -> ")[0] == set1:
                                print(line.split(" -> ")[1])
                    else:
                        passopen  = open(fileopen,"r")
                        set1 = input("Please enter the set name for the desired password. : ")
                        for line in passopen:
                            if line.split(" -> ")[0] == set1:
                                print(line.split(" -> ")[1])
                elif option == 3:
                    password = input("This is an IRREVERSIBLE decision as you may corrupt files if used incorrectly.You may now enter your password → ")
                    with open("g:\python\demo\okmeque1.txt","r") as passchk:
                        passchk0 = passchk.readlines()
                
                    if passchk0[0] == hashlib.sha256(password.encode('utf-8')).hexdigest():
                        del1 = input("Press enter to continue...")
                        filedel = input("Please enter a valid file name.The format for the file must be a:\directory\pwdfile.extention : ")
                        if del1 == "":
                            with open(filedel,"r") as read0:
                                read = read0.readlines()
                            with open(filedel,"w") as passdelete:
                                del2 = input("Enter set name : ")
                                for line in read:
                                    if line.split(" -> ")[0] != del2:
                                        passdelete.write(line)
                                        print("Set overwritten with value of none.")
        
                    else:
                        print("Bad Value for memory address 70 72 69 6E 74 28 22 42 61 64 20 56 61 6C 75 65 20 66 6F 72 20 6D 65 6D 6F 72 79 20 61 64 64 72 65 73 73 20 20 5C 6E 22 29 \n The following operation has been terminated.")
                elif option == 4:
                    print("\n")
                    print("This program is open source and made by Okmeque1.If you desire to copy this program,please keep a mention of Okmeque1 in the code as so the original code is not lost to time.")
                    print("This program can create a secure password of your length,8 to 19 characters is recommended for a secure password(DO NOT MAKE YOUR PASSWORD TOO LONG AS IT CAN OVERLOAD THE BUFFER ON THE COMPUTER AND CRASH IT.),can retrieve the password(this function is only useful if the file extention is foreign) and can erase the password file in case of hacking")
                    print("You may change the program defaults on line 37,39,53 and 55.(If you want to do this,you must change the defaults on ALL of the lines to ensure maximum compatability and change the input str to the default set in the none → default variable)")
                    print("For maximum compatability,run this program in Python 3+ and Windows 7 or higher(Please note that you can run it lower than those versions but the program might throw errors in lower version of windows(XP,Vista,etc) and some python functions might not exist in lower versions of python)")
                    print("The program will run on macOS and Linux but the filepath format will vary as neither of those use drive letters (eg A:\directory\file.ext).The structure for those OS's will either be : ")
                    print("1 : macOS : The file structure may be /path/path1/pwdfile.extention")
                    print("2 : Linux : The file structure is unclear as there are so many Linux distros out there but the structure may be /dev/sda/mountpoint1/folder/pwdfile.extention.")
                    print("Please note that in both cases,DO NOT USE FOREIGN FILE EXTENTIONS(.dell,pc or any non-standard file format that can't be read by a text editor.) as the disk check utility might assume that the file is corrupt and delete it.")
                    print("Please do NOT modify this program as the file may become unoriginal and might cause program breakage.This program took HOURS to complete and be at its current state.\n")
                    input("Press enter to continue")
                elif option == 5:
                    enc(key)
                elif option == 6:
                    dec(key)
                elif option == 7:
                    end = ""
                    passwd = ""
                    spc = '¦¬`!£$€%^&*()-_=+;:@~#\|,<.>/?'
                    num = "1234657890"
                    ch = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmMm"
                    spcs = ""
                    nums = ""
                    chs = ""
                    spcn = int(input("Enter special character count : "))
                    numn = int(input("Enter number count : "))
                    chn = int(input("Enter standard character count : "))
                    for p in range(spcn):
                        spcs += random.choice(spc)
                    for s in range(numn):
                        nums += random.choice(num)
                    for ad in range(chn):
                        chs += random.choice(ch)
                    end += spcs + nums + chs
                    for x in range(len(end)):
                        passwd += random.choice(end)
                    print(passwd)
                    filenam = input("Please enter a valid file name (none to default of G:\python\demo\demo.pc). The format must be a:\directory\pwdfile.extention. : ")
                    if filenam == "":
                        filenam = "G:\python\demo\demo.pc"
                        sets = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                        passavee = open(filenam,"a")
                        passavee.write(sets + " -> " + passwd + "\n")
                        passavee.close()
                    else:
                        sets = input("Enter a set name for your password to continue this program.This will be used later to retrieve back the password.This program does NOT support having 2 sets of the same name.Entering a name that already exists will cause a conflict. : ")
                        passavee = open(filenam,"a")
                        passavee.write(sets + " -> " + passwd + "\n")
                        passavee.close()
                    print("Save has completed with no disk errors.")
                    print("Now returning to the main menu")
                elif option == 8:
                        filedels = input("Please enter a valid file name. The format for the file must be a:\directory\pwdfile.extention : ")
                        sets1 = input("Enter SET name to change : ")
        
                        with open(filedels,"r") as readpwd:
                            r1 = readpwd.readlines()
                            for b in range(len(r1)):
                                if r1[b].strip("\n").split(" -> ")[0] == sets1:
                                    setnarme = r1[b].strip("\n").split(" -> ")[0] + " -> "
                                    newpwd = input("Enter new password : ")
                                    newsetpwd = setnarme + newpwd + "\n"
                                    r1[b] = newsetpwd
                        with open(filedels,"w") as changepwd:
                            for a in range(len(r1)):
                                changepwd.writelines(r1[a])
                        print("Save completed with no disk errors. Returning to main menu...")
                elif option == 9:
                    print("Returning to GKC, please wait...")
                    flag = False 
                    return
    except FileNotFoundError:
            print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
            input("Press ENTER to exit.")
            win()
    except KeyboardInterrupt or EOFError:
            print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
            win()
def icmdlite():
        global prodkey
        global preinstalled
        global installed
        global order
        try:
                clear()
                print("GKC 1.0 - No GKC utilities available - Type 'exit' or 'return' to reboot")
                flag = True
                while flag == True:
                        prompt = input("GKC>")
                        if prompt == 'exit' or prompt == 'return':
                                flag = False
                                kickstart()
                        elif 'cd' in prompt[0:3]:
                                os.chdir(prompt[3:])
                        elif 'prompt' in prompt:
                                print("PROMPT disabled in iCMD-Lite")
                        os.system(prompt)
        except BaseException:
                print("STOP : 770A\n General Exception.Retry the operation")
                input("Press ENTER to exit...")
                return None
def winkey():
    global prodkey
    global preinstalled
    global installed
    global order
    clear()
    global prodkey
    prodkey = 'ZF3R0-FHED2-M80TY-8QYGC-NPKYF'
    return prodkey
def win():
    clear()
    global prodkey
    global preinstalled
    global installed
    global order
    clear()
    print('==============================================')
    print('             GKC startup menu          ')
    print('==============================================')
    print('A : Standard GKC with all utilities available')
    print('B : iCMD GKC Command Line with no utilities (Safe Mode)')
    print('C : Shut Down computer')
    win_opt = input('Pick a choice : A (A), B (B),C (C)')
    if win_opt == 'A':
        icmd()
    if win_opt == 'B':
        icmdlite()
    if win_opt == 'C':
        os.system('shutdown /s /t 0')
def sysconfig():
    global prodkey
    global preinstalled
    global installed
    global order
    global order
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("SYSTEM CONFIGURATION TOOL - (C) Okmeque1 Systems")
    print("[1] DISPLAY CURRENT CONFIGURATION")
    print("[2] CHANGE SYSTEM SETTINGS")
    print("[3] QUIT TO BOOT")
    sconfig = input("Please select the options marked in []. : ")
    config = f"****CURRENT SYSTEM CONFIGURATION****\n[1]DATE/TIME = {time.asctime()}\n[2]FLOPPY A = NONE - NONE\nFLOPPY B = NONE - NONE\n[3]FIXED DISK 0 = Integral Corp V Series PLUS 512GB SSD \n[4]CDROM = NONE - NONE\n[5]BOOT = {order}"
    if sconfig == "1":
        print(config)
        input("Press ENTER |-> to continue.")
        sysconfig()
    elif sconfig == "2":
            print(config)
            cconfig = input("Please enter the setting number to change : ")
            if cconfig == "1":
                os.system("date")
                os.system("time")
                sysconfig()
            elif cconfig == "5":
                print("Only 2 Boot Devices Available - Other boot device will be the remaining one")
                order[0] = input("Enter BOOT device (options are REM and HDD): ")
                if order[0] == "REM":
                    order[1] == "HDD"
                else:
                    order[1] = "REM"
                sysconfig()
    elif sconfig == "3":
        print("Saving data to the system, please wait...",end='\r')
        time.sleep(0.3)
        print("Saving data to the system, please wait...Done!")
        print("Rebooting NOW...")
        time.sleep(3)
        kickstart()
    else:
        sysconfig()
def removable_device():
    global prodkey
    global preinstalled
    global installed
    global order
    if preinstalled == False:
        print("Starting the GKC Setup...")
        time.sleep(5)
        setup()
    if installed == False:
        clear()
        a = input("GKC Software key detected - Do you want to pre-load it onto the system? [Y/N]: ")
        if a == "Y":
            prodkey = winkey()
        oobe()
    else:
        win()
        

 

def kickstart():
    global prodkey
    global preinstalled
    global installed
    global order
    global order
    try:
        clear() 
        print('===============================================')
        print('Intel ARC B580 BIOS N34.EP.08')
        print('Version 4.34.20.87.0P')
        print('Copyright (C) 1996-2003 Intel Corp')
        print('12880MB RAM')
        print('')
        print('Intel Xeon E5-1620: 3.80Ghz  (AMIBIOS VERSION 8.1)   ')
        print('16384MB OK')
        print('Hit CTRL-C to enter SYSTEM CONFIGURATION')
        print('')
        print('Detected on S-III : 0 is Integral Corp V Series PLUS 512GB SATA SSD')
        print('Detected on S-III: 1 None')
        print('Detected on S-III: 2 None')
        print('Detected on S-III: 3 None')
        countdown = ["5",'4','3','2','1']
        for x in countdown:
            print(f"Booting in {x} seconds...",end='\r')
            time.sleep(1)
        if order[0] != "REM" and order[0] != 'HDD' and order[1] != "REM" and order[1] != "HDD":
            input(f"Invalid boot device - {order[0]}\nCheck system settings. Press ENTER to REBOOT")
            time.sleep(1)
            kickstart()
        if order[0] == "REM":
            removable_device()
        elif order[0] == "HDD":
            if preinstalled == False:
                input("No operating system installed - Press ENTER to REBOOT")
                time.sleep(2)
                kickstart()
            else:
                if installed == True:
                    win()
                else:
                    oobe()
    except KeyboardInterrupt:
        sysconfig()
kickstart()
    
