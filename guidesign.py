from tkinter import * 
from comdecom import compress,decompress
def compression(i,o):
    compress(i,o)
def decompression(i,o):
    decompress(i,o)
window = Tk()
window.title("Compression engine")
window.geometry("600x400")
input_entry = Entry(window)
input_entry.grid(row=0,column=1)
output_entry = Entry(window)
output_entry.grid(row=1,column=1)
label = Label(window,text="File to be compressed")
label.grid(row=0,column=0)
label = Label(window,text="Name of compressed file")
label.grid(row=1,column=0)
button = Button(window,text="Compress",command = lambda : compression(input_entry.get(),output_entry.get()))
button.grid(row=2,column=1)

window.mainloop()
#decompress ka bhi krna hai