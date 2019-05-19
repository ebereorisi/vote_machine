import tkinter as tk
from tkinter import ttk, Menu, filedialog
from tkinter import messagebox as mBox
from threading import Thread
import itertools, webbrowser, os, sys


win=tk.Tk()
win.title("vote machine ~ v1.0")
win.resizable(0, 0)

#quit command
def _quit():
	win.quit()
	win.destroy()
	exit()

#new window callback
def _newWindow():
    os.startfile(r"vote_machine_gui.py")
#vote_machine cli callback
def _vote_machinecli():
	os.startfile(r"vote_machine.py")
#about vote_machine callback
def _msgBox():
	mBox.showinfo("vote_machine v1.0", "vote_machine is a cummulative frequency voters app\ncreated by the legend: Ebere")
#website callback
def _website():
	webbrowser.open_new(r"http://ebereorisi.github.io")

#Menu
menuBar = Menu(win)
win.config(menu=menuBar)

#Project menu
projectMenu = Menu(menuBar, tearoff=0)
projectMenu.add_command(label="New project window", command=_newWindow)
projectMenu.add_separator()
projectMenu.add_command(label="vote_machine CLI", command=_vote_machinecli)
projectMenu.add_separator()
projectMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="Project", menu=projectMenu)

#Help menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Website", command=_website)
helpMenu.add_separator()
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)


#Overall app container
appContainer = ttk.LabelFrame(win)
appContainer.grid(column=0, row=0)

#vote Text
charLabel = ttk.Label(appContainer, text="Ebere's voters machine")
charLabel.grid(column=0, row=0)

#vote frame
voteFrame = ttk.LabelFrame(appContainer)
voteFrame.grid(column=0, row=2)

#first_vote label
first_voteLabel = ttk.Label(voteFrame, text="VOTE 1")
first_voteLabel.grid(column=0, row=0 )
#first_vote Box
first_voteBox = ttk.Entry(voteFrame, width=10)
first_voteBox.grid(column=0, row=1)

#second_vote label
second_voteLabel = ttk.Label(voteFrame, text="VOTE 2 ")
second_voteLabel.grid(column=1, row=0 )
#second_vote Box
second_voteBox = ttk.Entry(voteFrame, width=10)
second_voteBox.grid(column=1, row=1)

#third_vote label
third_voteLabel = ttk.Label(voteFrame, text="VOTE 3")
third_voteLabel.grid(column=2, row=0 )
#third_vote Box
third_voteBox = ttk.Entry(voteFrame, width=10)
third_voteBox.grid(column=2, row=1)

#vote again frame
vote_againLabel = ttk.LabelFrame(appContainer)
vote_againLabel.grid(column=0, row=3)

#finish vote frame
finish_voteLabel = ttk.LabelFrame(appContainer)
finish_voteLabel.grid(column=1, row=3)

#voted window
def _quitVoted():
	genWin.quit()
	genWin.destroy()

def _voted():
	genWin = tk.Toplevel()
	genWin.resizable(0, 0)
	votedLabel = ttk.Label(genWin, text="VOTE SUCESSFULL!!!")
	votedLabel.grid(column=0, row=0)

#result window
def _quitResult():
	genWin2.quit()
	genWin2.destroy()

def _result():
    genWin2 = tk.Toplevel()
    genWin2.resizable(0, 0)
    resultLabel = ttk.Label(genWin2, text="RESULT SAVED")
    resultLabel.grid(column=0, row=0)


vote_list= []
#vote again callback
def _vote():
    first_vote = first_voteBox.get()
    vote_list.append(first_vote)
    second_vote = second_voteBox.get()
    vote_list.append(second_vote)
    third_vote = third_voteBox.get()
    vote_list.append(third_vote)
    print("voted")
    genWinTD = Thread(target=_voted())

#finish action
def _finish():
    while True:
        _vote()
        print("")
        print("Vote list is: ", vote_list)
        print("")
        counts = {}
        for i in vote_list:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        print (counts)
        sys.exit("Thanks for voting")
        genWinTD2 = Thread(target=_result())

#vote again Button
vote_again = ttk.Button(vote_againLabel, text="VOTE", command=_vote)
vote_again.grid(column=1, row=0, padx=10)

#finish vote Button
finish_vote = ttk.Button(finish_voteLabel, text="FINISH", command=_finish)
finish_vote.grid(column=1, row=0, padx=10)

win.mainloop()
