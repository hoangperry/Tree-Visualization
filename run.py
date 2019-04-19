from tkinter import *
from Student import Student
from BST_AVL import BST, AVL
import argparse
import re

parser = argparse.ArgumentParser("""
    *** BST_AVL tree                                ***
    *** 502043 (Data Structures and Algorithms)     ***
    *** Spring 2018-2019 assignment.                ***
""")

parser.add_argument('-t','--tree',
                    help="[BST] or [AVL], Example: -t bst", default="bst")

args = parser.parse_args()
type_of_tree = args.tree
if(type_of_tree.lower() == "avl"):
    tree = AVL()
else:
    tree = BST()

fields = ('ID', 'Name', 'Birthday', 'Credit', 'Score')

def drawNode(canvas, node, x=250, y=50, pre=None):
    if node == None:
        return
    canvas.create_circle(x, y, 20, fill="white")
    canvas.create_text(x, y, text=str(node.key.id), anchor='center')
    hash = int(canvas['width'])/(2**(tree.heightNode(node)+1))
    print(hash)
    drawNode(canvas, node.left, x=(x-hash), y=y+50)
    drawNode(canvas, node.right, x=(x+hash), y=y+50)
def draw(canvas):
    pre = None

    canvas.delete("all")
    list_node = tree.nlrNoPrint()
    drawNode(canvas, tree.root)
        # draw()
        #
        #     drawNode(canvas, node)
        #
        # if node.key.id < pre.key.id:
        #     x = int(canvas['width'])/(2**tree.heightNode(node))
        # else:
        #     x = int(canvas['width']) - int(canvas['width'])/(2**tree.heightNode(node))
        #
        # y = 60 * tree.heightNode(node)
        # canvas.create_circle(x, y, 20, fill="white")
        # canvas.create_text(x, y, text=str(node.key.id), anchor='center')

def addTree(entries, cmd, y_pos, canvas):
    id = int(entries['ID'].get())
    name = str(entries['Name'].get())
    birthday = str(entries['Birthday'].get())
    credit = int(entries['Credit'].get())
    score = float(entries['Score'].get())

    if(id > 999):
        cmd.create_text(5, y_pos, text="[ERROR]: ID must be less than 3 digits", anchor='nw', fill="red")
        return

    if(score > 10):
        cmd.create_text(5, y_pos, text="[ERROR]: Score must be less than 10", anchor='nw', fill="red")
        return

    if tree.containsID(id):
        tree.updateName(id, name)
        tree.updateScore(id, score)
        tree.updateCredit(id, credit)
        tree.updateBirthday(id, birthday)
    st = Student(id, name, birthday, score, credit)
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text="Added student: " + str(st), anchor='nw', fill="white")
    tree.put(st)
    draw(canvas)

def delTree(entries, cmd, y_pos, canvas):
    id = int(entries['ID'].get())
    name = str(entries['Name'].get())
    birthday = str(entries['Birthday'].get())
    credit = int(entries['Credit'].get())
    score = float(entries['Score'].get())

    if(id > 999):
        cmd.create_text(5, y_pos, text="[ERROR]: ID must be less than 3 digits", anchor='nw', fill="red")
        return

    if(score > 10):
        cmd.create_text(5, y_pos, text="[ERROR]: Score must be less than 10", anchor='nw', fill="red")
        return

    st = Student(id, name, birthday, score, credit)
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text="Deleted student: " + str(st), anchor='nw', fill="white")
    tree.delete(st)
    draw(canvas)

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=7, text=field+": ", anchor='w')
        ent = Entry(row)

        if field == "ID":
            ent.insert(0, "111")
        if field == "Name":
            ent.insert(0, "Nguyen Van A")
        if field == "Score":
            ent.insert(0, "10.0")
        if field == "Birthday":
            ent.insert(0, "19/4/2019")
        if field == "Credit":
            ent.insert(0, "5")

        row.pack(side = TOP, fill = X, padx = 15 , pady = 6)
        lab.pack(side = LEFT)
        ent.pack(side = LEFT)
        entries[field] = ent
    return entries

def clearCmd(cmd, y_pos):
    y_pos = 0
    cmd.delete("all")

def rln(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.rln(), anchor='nw', fill="white")
    y_pos += 15

def rnl(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.rnl(), anchor='nw', fill="white")
    y_pos += 15

def nrl(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.nrl(), anchor='nw', fill="white")
    y_pos += 15

def nlr(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.nlr(), anchor='nw', fill="white")
    y_pos += 15

def lnr(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.lnr(), anchor='nw', fill="white")
    y_pos += 15

def lrn(cmd, y_pos):
    clearCmd(cmd, y_pos)
    cmd.create_text(5, y_pos, text=tree.lrn(), anchor='nw', fill="white")
    y_pos += 15

def successor(entries, cmd, y_pos):
    id = int(entries['ID'].get())
    name = str(entries['Name'].get())
    birthday = str(entries['Birthday'].get())
    credit = int(entries['Credit'].get())
    score = float(entries['Score'].get())

    if(id > 999):
        cmd.create_text(5, y_pos, text="[ERROR]: ID must be less than 3 digits", anchor='nw', fill="red")
        return

    if(score > 10):
        cmd.create_text(5, y_pos, text="[ERROR]: Score must be less than 10", anchor='nw', fill="red")
        return

    st = Student(id, name, birthday, score, credit)

    clearCmd(cmd, y_pos)
    suc = tree.getSuccessor(st)
    if suc != None:
        cmd.create_text(5, y_pos, text="Successor is " + str(suc.key), anchor='nw', fill="white")
    else:
        cmd.create_text(5, y_pos, text="This Student doesn't have Successor", anchor='nw', fill="white")

def predecessor(entries, cmd, y_pos):
    id = int(entries['ID'].get())
    name = str(entries['Name'].get())
    birthday = str(entries['Birthday'].get())
    credit = int(entries['Credit'].get())
    score = float(entries['Score'].get())

    if(id > 999):
        cmd.create_text(5, y_pos, text="[ERROR]: ID must be less than 3 digits", anchor='nw', fill="red")
        return

    if(score > 10):
        cmd.create_text(5, y_pos, text="[ERROR]: Score must be less than 10", anchor='nw', fill="red")
        return

    st = Student(id, name, birthday, score, credit)

    clearCmd(cmd, y_pos)
    suc = tree.getPredecessor(st)
    if suc != None:
        cmd.create_text(5, y_pos, text="Successor is " + str(suc.key), anchor='nw', fill="white")
    else:
        cmd.create_text(5, y_pos, text="This Student doesn't have Predecessor", anchor='nw', fill="white")

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

if __name__ == '__main__':
    root = Tk()
    root.title("Demo Binary Search Tree")
    root.bind('<Escape>', lambda e: root.destroy())
    menubar = Menu(root)
    menubar.add_command(label="QUIT", command=root.destroy)
    root.config(menu=menubar)

    frame = Frame(root)
    frame.pack(side=LEFT, anchor=N)
    ents = makeform(frame, fields)

    cmd = Canvas(root, width=550, bg="black")
    cmd.pack(side=RIGHT, anchor=N, fill=Y)
    y_pos = 0

    addButton = Button(frame, text='ADD', command=(lambda e=ents:addTree(e, cmd, y_pos, canvas)), bg="green", foreground="white")
    addButton.pack(side=TOP, ipadx=80, ipady=10, anchor=N, fill=X)

    delButton = Button(frame, text='DELETE', command=(lambda e=ents:delTree(e, cmd, y_pos, canvas)), bg="red", foreground="black")
    delButton.pack(side=TOP, ipadx=80, ipady=10, anchor=N, fill=X)
    subFrame = Frame(frame)
    subFrame.pack(side=TOP)
    predecessorButton = Button(subFrame, text = 'Predecessor', command = (lambda e=ents:predecessor(e, cmd, y_pos)))
    predecessorButton.grid(column=0, row=0, ipadx=18, ipady=10, sticky=E)

    successorButton = Button(subFrame, text='Successor', command=(lambda e=ents:successor(e, cmd, y_pos)))
    successorButton.grid(column=1, row=0, ipadx=18, ipady=10, sticky=W)

    lnrButton = Button(frame, text = 'lnr', command = (lambda e = ents:lnr(cmd, y_pos)), bg="purple")
    lnrButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW)
    lrnButton = Button(frame, text = 'lrn', command = (lambda e = ents:lrn(cmd, y_pos)), bg="purple")
    lrnButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW, after=lnrButton)
    nlrButton = Button(frame, text = 'nlr', command = (lambda e = ents:nlr(cmd, y_pos)), bg="purple")
    nlrButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW)
    nrlButton = Button(frame, text = 'nrl', command = (lambda e = ents:nrl(cmd, y_pos)), bg="purple")
    nrlButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW)
    rnlButton = Button(frame, text = 'rnl', command = (lambda e = ents:rnl(cmd, y_pos)), bg="purple")
    rnlButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW)
    rlnButton = Button(frame, text = 'rln', command = (lambda e = ents:rln(cmd, y_pos)), bg="purple")
    rlnButton.pack(side=RIGHT, ipadx=5, ipady=10, anchor=NW)



    canvas = Canvas(root, width=500, height=600, bg='blue')
    canvas.pack(side=LEFT, anchor=W, fill=Y)


    # canvas.create_line(250, 40, 125, 150)
    # canvas.create_line(250, 40, 375, 150)
    # canvas.create_circle(250, 40, 30, fill="white")
    # canvas.create_circle(125, 150, 30, fill="white")
    # canvas.create_circle(375, 150, 30, fill="white")
    root.mainloop()