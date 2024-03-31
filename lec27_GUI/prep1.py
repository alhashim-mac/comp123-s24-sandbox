"""
Practicing with the code in the reading assignment

"""
import tkinter as tk


class BasicGUI:
    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.title("First Example")
        self.root_window.config(bg="blue")

        # greeting label
        self.label_greet = tk.Label(self.root_window)
        self.label_greet.config(text="Welcome to COMP123",
                                font="Arial 18 bold",
                                bg="#DD10C1",
                                relief=tk.RIDGE)
        self.label_greet.grid(row=0, column=0)

        # note label
        self.label_note = tk.Label(self.root_window)
        self.label_note.config(text="This is GUI Example",
                               font="Arial 10 italic",
                               bg="#ffffff",
                               relief=tk.RIDGE,
                               justify=tk.LEFT)
        self.label_note.grid(row=1, column=0)  # note label

        # counter label
        self.label_note = tk.Label(self.root_window)
        self.label_note.config(text="0",
                               font="Arial 20")
        self.label_note.grid(row=2, column=0)

        # counter button
        self.button_counter = tk.Button(self.root_window)
        self.button_counter.config(text="Increment",
                                   font="Arial 10",
                                   command=self.button_counter_action)
        self.button_counter.grid(row=3, column=0)

        # quite button
        self.button_quit = tk.Button(self.root_window)
        self.button_quit.config(text="Quit",
                                font="Arial 10",
                                command=self.button_quite_action)
        self.button_quit.grid(row=4, column=0)

        # label name
        self.label_name = tk.Label(self.root_window)
        self.label_name.config(text="name",
                               font="Arial 20")
        self.label_name.grid(row=5, column=0)

        # entry name
        self.entry_name = tk.Entry(self.root_window)
        self.entry_name.bind("<Return>", self.entry_name_response)
        self.entry_name.grid(row=6, column=0)

        # button name
        self.button_name = tk.Button(self.root_window)
        self.button_name.config(text="Add",
                                font="Arial 10",
                                command=self.button_name_action)
        self.button_name.grid(row=7, column=0)

    def run(self):
        self.root_window.mainloop()

    def button_counter_action(self):
        self.label_note["text"] = int(self.label_note["text"]) + 1

    def button_quite_action(self):
        self.root_window.destroy()

    def button_name_action(self):
        self.label_name["text"] = self.entry_name.get()
        self.entry_name.delete(0, tk.END)

    def entry_name_response(self, event: tk.Event):
        if event.keysym == "Return":
            self.button_name_action()


def main():
    basic_gui = BasicGUI()
    basic_gui.run()


if __name__ == '__main__':
    main()
