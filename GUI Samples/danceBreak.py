#################### Select box - given choices and can select one

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()

root.title('Listbox')

# create a list box
songs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tk.Variable(value=songs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)


def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_songs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_songs}'
    messagebox.askokcancel(f'You selected: {selected_songs},
                           Is this your final choice')

    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()