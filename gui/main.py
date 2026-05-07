import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x400")

    entry = tk.Entry(root, width=20, font=('Arial', 24), justify="right")
    entry.grid(row=0, column=0, columnspan=4, padx=5, pady=25, sticky="ew")

    number = 1
    for i in range(1,4):
        for j in range(1,4):
            create_button(root, entry, number, i, j)
            number += 1

    create_button(root, entry, "0", 4, 2)
    create_button(root, entry, "C", 4, 1)
    create_button(root, entry, "=", 4, 3)

    create_button(root, entry, "+", 1, 0)
    create_button(root, entry, "-", 2, 0)
    create_button(root, entry, "*", 3, 0)
    create_button(root, entry, "/", 4, 0)

    root.mainloop()

def create_button(root, entry, content, row, column):
    if content == "=":
        button = tk.Button(root, text=content, font=('Arial', 15), command=lambda: calculate(entry))

    elif content == "C":
        button = tk.Button(root, text=content, font=('Arial', 15), command=lambda: clear_entry(entry))

    else:
        button = tk.Button(root, text=content, font=('Arial', 15), command=lambda: update_entry(entry, content))

    button.grid(row=row, column=column, ipadx=10, ipady=10, pady=10)

def update_entry(entry, content):
    entry.insert(tk.END, content)

def calculate(entry):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(e))

def clear_entry(entry):
    entry.delete(0, tk.END)
    entry.insert(tk.END, "")

if __name__ == "__main__":
    main()