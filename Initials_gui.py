import customtkinter as ctk

class InitialsDialog(ctk.CTkToplevel):
    def __init__(self, parent, player, callback, score):
        super().__init__(parent)
        self.title(f"{player} WON!")
        self.geometry("300x160")
        self.resizable(False, False)
        self.callback = callback
        self.score = score

        self.inish_var = ctk.StringVar()

        # Configure 3 rows, 1 column
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.label = ctk.CTkLabel(self, text="Enter your Initials! (AAA)")
        self.label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="n")

        self.entry = ctk.CTkEntry(self, textvariable=self.inish_var, justify="center")
        self.entry.grid(row=1, column=0, padx=40, pady=5, sticky="ew")
        self.entry.focus()

        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=2, column=0, pady=(0, 5), sticky="n")

        self.ok_button = ctk.CTkButton(self, text="OK", command=self.validate)
        self.ok_button.grid(row=3, column=0, pady=(5, 15), sticky="s")

        self.protocol("WM_DELETE_WINDOW", lambda: None)  # disable X button

    def validate(self):
        text = self.inish_var.get().strip()
        if len(text) == 3 and text.isalpha():
            self.callback(text.upper())
            self.destroy()
        else:
            self.error_label.configure(text="Enter exactly 3 letters.")
            self.inish_var.set("")