import tkinter.font as tkFont
import tkinter
from tkinter import *

class VaultApp():
    def __init__(self):
        # Main Window layout
        self.MainWindow = tkinter.Tk()

    def LoginWindow(self):
        # Main Window layout
        self.MainWindow.title('THE VAULT')
        self.MainWindow.geometry("450x200+300+200")
        self.MainWindow.configure(bg="#FFB266")

        # Frames for the main login window
        mainFrame = Frame(self.MainWindow, bg="#FFB266")
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame, bg="#FFB266")
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame, bg="#FFB266")
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame, bg="#FFB266")
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame, bg="#FFB266")
        boxFrame.pack(side=RIGHT)

        # Labels for entries for main login window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Account Name:", bg="#FFB266", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Master Password:", bg="#FFB266", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes for main login window
        accountNameEntry = Entry(boxFrame, bd=5, bg="#FFB266")
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        accountNameEntry.configure(highlightbackground="#FFB266")
        masterPasswordEntry = Entry(boxFrame, bd=5, bg="#FFB266", show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)
        masterPasswordEntry.configure(highlightbackground= "#FFB266")


        def Reset(self):
            # Reset Window layout
            ResetWindow = tkinter.Tk()
            ResetWindow.title('Reset')
            ResetWindow.geometry("700x700")

            # Reset Window frames
            mainFrame = Frame(ResetWindow)
            mainFrame.pack(fill="none", expand=True)
            upperFrame = Frame(mainFrame)
            upperFrame.pack(side=TOP, fill="none", expand=False)
            lowerFrame = Frame(mainFrame)
            lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
            labelFrame = Frame(upperFrame)
            labelFrame.pack(side=LEFT)
            boxFrame = Frame(upperFrame)
            boxFrame.pack(side=RIGHT)

            # Labels for entries in reset window
            times = tkFont.Font(family="TimesNewRoman", size=14)
            accountNameLabel = Label(labelFrame, text="Account Name:", font=times)
            accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
            masterPasswordLabel = Label(labelFrame, text="Master Password:", font=times)
            masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

            # User and password entry boxes in reset window
            accountNameEntry = Entry(boxFrame, bd=5)
            accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
            masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
            masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

            # Login button in reset window
            EnterButton = tkinter.Button(lowerFrame, text="Login", command=self.welcome)
            EnterButton.pack(side=BOTTOM, expand=YES, pady=20)
            EnterButton.pack()

        # Login button in main login window
        loginButton = tkinter.Button(lowerFrame, text="Login", bg='#FFB266', height=1, width=6, command=self.welcome)
        loginButton.pack(side=TOP, expand=YES, pady=10)
        loginButton.configure(relief=RAISED)
        loginButton.pack()

        # Link to reset the user's Account Name and Password in main login window
        link = Label(lowerFrame, text="Forgot Master Password?", bg="#FFB266", fg="blue", cursor="arrow")
        link.pack(side=BOTTOM, expand=YES)
        link.bind("<Button-1>", Reset)

        self.MainWindow.mainloop()

    # Create a settings window
    def Settings(self):
        settingsWindow = tkinter.Tk()
        settingsWindow.title('Settings')
        settingsWindow.geometry("700x700")

        # Create a menu bar in settings window
        menu_bar = Menu(settingsWindow)
        settingsWindow.config(menu=menu_bar)

        # Create a File drop down menu in settings window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Close settings window
        filemenu.add_command(label="Log Out", command=settingsWindow.destroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=settingsWindow.quit)

        # Frames for the settings window
        mainFrame = Frame(settingsWindow)
        mainFrame.pack(fill="none", expand=True)
        upperFrame = Frame(mainFrame)
        upperFrame.pack(side=TOP, fill="none", expand=False)
        lowerFrame = Frame(mainFrame)
        lowerFrame.pack(side=BOTTOM, fill="none", expand=False)
        labelFrame = Frame(upperFrame)
        labelFrame.pack(side=LEFT)
        boxFrame = Frame(upperFrame)
        boxFrame.pack(side=RIGHT)

        # Labels for entries in settings window
        times = tkFont.Font(family="TimesNewRoman", size=14)
        accountNameLabel = Label(labelFrame, text="Enter new Account Name:", font=times)
        accountNameLabel.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordLabel = Label(labelFrame, text="Enter new Master Password:", font=times)
        masterPasswordLabel.pack(side=BOTTOM, fill=BOTH, pady=5)

        # User and password entry boxes in settings window
        accountNameEntry = Entry(boxFrame, bd=5)
        accountNameEntry.pack(side=TOP, fill=BOTH, pady=5)
        masterPasswordEntry = Entry(boxFrame, bd=5, show='*')
        masterPasswordEntry.pack(side=BOTTOM, fill=BOTH, pady=5)

        # Login button in settings window
        enterButton = tkinter.Button(lowerFrame, text="Enter")
        enterButton.pack(side=BOTTOM, expand=YES, pady=5)
        enterButton.pack()

        #settingsWindow.mainloop()


    def welcome(self):
        # Welcome window layout
        welcomeWindow = tkinter.Tk()
        welcomeWindow.title('WELCOME')
        welcomeWindow.geometry("700x700+300+150")

        # Create a menu bar in welcome window
        menu_bar = Menu(welcomeWindow)
        welcomeWindow.config(menu=menu_bar, bg="#856ff8")

        # Create a File drop down menu in welcome window
        filemenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=filemenu)
        # Settings should take you to another window
        filemenu.add_command(label="Settings", command=self.Settings)
        # Close welcome window
        filemenu.add_command(label="Log Out", command=welcomeWindow.destroy)
        # Exit out of whole app
        filemenu.add_command(label="Exit", command=welcomeWindow.quit)

        # Create an Action drop down menu in welcome window
        actionMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Action", menu=actionMenu)
        # Store should take you to a window to store passwords
        actionMenu.add_command(label="Store")
        # Retrieve should take you to window that retrieves password
        actionMenu.add_command(label="Retrieve")

        # Create frame for buttons in welcome window
        frame = Frame(welcomeWindow)
        frame.pack(fill="none", expand=True)
        frame.configure(bg="#856ff8")
        frame.pack()

        # Retrieve button in welcome window
        retrieveButton = Button(frame, text="Retrieve", height="2", width="10")
        retrieveButton.pack(side=LEFT, padx=10)
        retrieveButton.configure(bg="#856ff8", relief=RAISED, state=ACTIVE)
        retrieveButton.pack()

        # Store button in welcome window
        storeButton = Button(frame, text="Store", height="2", width="10")
        storeButton.pack(side=RIGHT, padx=10)
        storeButton.configure(bg="#856ff8", relief=RAISED, state=ACTIVE)
        storeButton.pack()

        # welcomeWindow.mainloop()


start = VaultApp()
start.LoginWindow()

