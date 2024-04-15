import customtkinter


class SettingsWindow:
    def __init__(self):
        self.selected_reversing_rotor = None
        self.entered_rotor_values = None
        self.selected_rotors = None
        self.entered_plugboard_configuration = None
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.root = customtkinter.CTk()
        self.root.geometry("720x480")
        self.root.title("Enigma Settings")

        self.rotor_frames = [customtkinter.CTkFrame(self.root) for _ in range(3)]
        for frame in self.rotor_frames:
            frame.pack(pady=(20, 10))

        self.dropdown_rotors = []
        self.entry_rotors = []
        for frame in self.rotor_frames:
            self.setup_rotor_combobox_and_entry(frame)

        self.dropdown_reversing_rotor = customtkinter.CTkComboBox(self.root,
                                                                  values=["Reversing Rotor A", "Reversing Rotor B",
                                                                          "Reversing Rotor C"], width=250)
        self.dropdown_reversing_rotor.pack(pady=10)

        self.entry_plugboard = customtkinter.CTkEntry(self.root, placeholder_text="Plugboard Example: (\"C\", \"R\"), "
                                                                                  "(\"P\", \"V\")",
                                                      width=250)
        self.entry_plugboard.pack(pady=10)

        self.button = customtkinter.CTkButton(self.root, text="Werte speichern", command=self.save_values)
        self.button.pack(pady=20)

    def setup_rotor_combobox_and_entry(self, frame):
        dropdown_rotor = customtkinter.CTkComboBox(frame,
                                                   values=["Rotor I", "Rotor II", "Rotor III", "Rotor IV", "Rotor V"])
        dropdown_rotor.pack(side="left", padx=10)
        self.dropdown_rotors.append(dropdown_rotor)

        entry_rotor = customtkinter.CTkEntry(frame, placeholder_text="1 to 26",)
        entry_rotor.pack(side="left", padx=10)
        self.entry_rotors.append(entry_rotor)

    def save_values(self):
        self.selected_rotors = [dropdown.get() for dropdown in self.dropdown_rotors]
        self.entered_rotor_values = [entry.get() for entry in self.entry_rotors]
        self.selected_reversing_rotor = self.dropdown_reversing_rotor.get()
        self.entered_plugboard_configuration = self.entry_plugboard.get()
        self.root.destroy()

    def get_values(self):
        return [self.selected_rotors, self.entered_rotor_values, self.selected_reversing_rotor,
                self.entered_plugboard_configuration]

    def show(self):
        self.root.mainloop()
