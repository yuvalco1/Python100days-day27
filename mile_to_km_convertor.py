from tkinter import *
from tkinter import font

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300, height=200)
window.config(padx=40, pady=40)

# label 1 - Miles
label1 = Label(text="Miles", font=("Arial", 24, "bold"), anchor="w", justify="left")
label1.grid(column=2, row=0)
# label 2 - is equal to
label2 = Label(text="is equal to", font=("Arial", 24, "bold"), anchor="e", justify="right")
label2.grid(column=0, row=1)
# label 3  - Km
label3 = Label(text=" Km", font=("Arial", 24, "bold"), anchor="w", justify="left")
label3.grid(column=2, row=1)
# label 4 - result
label4 = Label(text="0", font=("Arial", 24, "bold"), anchor="center", justify="center")
label4.grid(column=1, row=1)

# Entry
custom_font = font.Font(size=24, family="Arial", weight="bold")

entry = Entry(width=10, justify="center", font=custom_font)

# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)


def button_clicked():
    print("Calculate")
    new_text = entry.get()
    label4.config(text=str(round(float(new_text) * 1.609, 2)))


button = Button(text="Calculate", command=button_clicked, font=custom_font)
button.grid(column=1, row=2)

window.mainloop()
