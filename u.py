from tkinter import * 
from comdecom import compress,decompress
from tkinter import filedialog #we have filedialog which is used to take input from the desktop
def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)
def open_file():
    file = filedialog.askopenfile(initialdir='/',title="Select a file to compress",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    return file
window = Tk()
window.title("Compression engine")
window.geometry("600x400")
# input_entry = Entry(window)
# input_entry.grid(row=0,column=1)
# output_entry = Entry(window)
# output_entry.grid(row=1,column=1)
# label = Label(window,text="File to be compressed")
# label.grid(row=0,column=0)
# label = Label(window,text="Name of compressed file")
# label.grid(row=1,column=0)
# k = compress(open_file(),"new.txt")
button = Button(window,text="Compress",command = lambda  : compression(open_file(),"new.txt"))
button.grid(row=2,column=1)

window.mainloop()