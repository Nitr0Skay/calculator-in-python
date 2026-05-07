from calculator import Calculator
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
            create_button(root, number, i, j)
            number += 1

    create_button(root, "0", 4, 2)
    create_button(root, "C", 4, 1)
    create_button(root, "=", 4, 3)

    create_button(root, "+", 1, 0)
    create_button(root, "-", 2, 0)
    create_button(root, "*", 3, 0)
    create_button(root, "/", 4, 0)

    root.mainloop()

def create_button(root, content, row, column):
    button = tk.Button(root, text=content, font=('Arial', 15))
    button.grid(row=row, column=column, ipadx=10, ipady=10, pady=10)

if __name__ == "__main__":
    main()