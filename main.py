import tkinter as tk


def main():
    root = tk.Tk()
    root.geometry("700x500")
    root.resizable(False, False)
    root.title("Генератор расписаний")
    root["bg"] = "white"

    title = tk.Label(text="Генератор расписаний", bg="#fff", fg="#000", font=(None, 30))

    title.place(x=195, y=30)

    root.mainloop()


if __name__ == "__main__":
    main()

