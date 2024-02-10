from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    yourscore=0
    # ASK A QUESTION AND CHECK THE ANSWER
    name = simpledialog.askstring(title="question", prompt="how many continents are there?")
    if name=="7" or name=="seven" or name=="Seven":
        messagebox.showinfo(message="good job")
        yourscore+=1
    else:
        messagebox.showinfo(message="wrong answer")
    #      // 2.  Ask the user a question are you
    name = simpledialog.askstring(title="question", prompt="2x-10=?")
    #      // 3.  Use an if statement to check if their answer is correct
    if name =="5" or name =="x=5":
        messagebox.showinfo(message="good job")
        yourscore+=1
    else:
        messagebox.showinfo(message="wrong")
    #      // 4.  if the user's answer was correct, add one to their score 

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    name = simpledialog.askstring(title="question", prompt="how many bones are in the human body")
    if name =="206":
        messagebox.showinfo(message="goodjob")
        yourscore+=1
    else:
        messagebox.showinfo(message="wrong")

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message="your score is "+str(yourscore))
    # Run the window's .mainloop() method
    window.mainloop()