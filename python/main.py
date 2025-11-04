import tkinter as tk

window = tk.Tk()
window.title("Discount Calculator")
window.geometry("350x200")

def discount():
    original_price = int(original_price_entry.get())
    discount_percentage = int(discount_percentage_entry.get())
    fixed_price = round(original_price - (original_price * (discount_percentage/100)))
    fixed_price_label.configure(text=f"Final Price: Rp {fixed_price}")

original_price_label = tk.Label(window, text="Original Price: ")
original_price_entry = tk.Entry(window, width=50)

discount_percentage_label = tk.Label(window, text="Discount (%): ")
discount_percentage_entry = tk.Entry(window, width=50)

calculate_button = tk.Button(window, text="Calculate", command=discount)

fixed_price_label = tk.Label(window)

original_price_label.pack()
original_price_entry.pack()
discount_percentage_label.pack()
discount_percentage_entry.pack()
calculate_button.pack(pady=10)
fixed_price_label.pack()

window.mainloop()