import tkinter as tk


window = tk.Tk()
window.title("Kilometer to Miles Converter")
window.minsize(600, 450)
window.config(padx=100, pady=100)


km_label = tk.Label(window, text="Enter kilometers:")
km_label.grid(row=0, column=0)
km_entry = tk.Entry(window, width=20)
km_entry.grid(row=0, column=1)


def convert_km_to_miles():
    km = float(km_entry.get())
    miles = km * 0.621371
    result_label.config(text=f"{km} kilometers is equal to {miles:.2f} miles")

click_button = tk.Button(window, text="Convert to Miles", command=convert_km_to_miles)
click_button.grid(row=1, column=0, columnspan=2,pady=20)


result_label = tk.Label(window, text="Result")
result_label.grid(row=2, column=0, columnspan=2)

window.mainloop()