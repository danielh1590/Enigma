from tkinter import messagebox

import customtkinter
import re
from collections import Counter


def show_error(message):
    messagebox.showerror("Fehler", message)


class SettingsWindow:
    def __init__(self):
        self.selected_reversing_rotor = None
        self.entered_rotor_values = None
        self.selected_rotors = None
        self.entered_plugboard_configuration = None

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        self.root = customtkinter.CTk()

        window_width = 720
        window_height = 480

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2)
        center_y = int(screen_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
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

        self.entry_plugboard = customtkinter.CTkEntry(self.root, placeholder_text="Plugboard Example: AB CD EF",
                                                      width=250)
        self.entry_plugboard.pack(pady=10)

        self.button = customtkinter.CTkButton(self.root, text="Save values", command=self.save_values)
        self.button.pack(pady=20)

    def setup_rotor_combobox_and_entry(self, frame):
        dropdown_rotor = customtkinter.CTkComboBox(frame,
                                                   values=["Rotor I", "Rotor II", "Rotor III", "Rotor IV", "Rotor V"])
        dropdown_rotor.pack(side="left", padx=10)
        self.dropdown_rotors.append(dropdown_rotor)

        entry_rotor = customtkinter.CTkEntry(frame, placeholder_text="Starting Pos: 1 to 26", )
        entry_rotor.pack(side="left", padx=10)
        self.entry_rotors.append(entry_rotor)

    def save_values(self):
        if self.check_values():
            show_error("You need to set the starting positions.")
            return
        elif self.check_values_number():
            show_error("Starting Position 1 to 26")
            return
        elif not self.check_plugboard_length():
            show_error("Plugboard length is max 10")
            return
        elif not self.check_plugboard_configuration():
            show_error("Plugboard configuration is invalid. Should be AB CD EF")
            return
        elif self.check_plugboard_duplicate():
            show_error("Plugboard has duplicate entries")
            return
        self.selected_rotors = [dropdown.get() for dropdown in self.dropdown_rotors]
        self.entered_rotor_values = [entry.get() for entry in self.entry_rotors]
        self.selected_reversing_rotor = self.dropdown_reversing_rotor.get()
        self.entered_plugboard_configuration = self.entry_plugboard.get()
        self.root.destroy()

    def get_values(self):
        return [self.selected_rotors, self.entered_rotor_values, self.selected_reversing_rotor,
                self.entered_plugboard_configuration]

    def check_values(self):
        values = [entry.get() for entry in self.entry_rotors]
        for value in values:
            if value == "":
                return True
        return False

    def check_values_number(self):
        values = [entry.get() for entry in self.entry_rotors]
        values = list(map(int, values))
        for value in values:
            if value <= 0 or value > 26:
                return True
        return False

    def check_plugboard_configuration(self):
        plugboard_configuration = self.entry_plugboard.get()
        if plugboard_configuration == "":
            return True
        pattern = r"^([A-Z]{2})(?:\s[A-Z]{2}){0,9}$"
        return re.fullmatch(pattern, plugboard_configuration) is not None

    def check_plugboard_duplicate(self):
        plugboard_configuration = self.entry_plugboard.get()
        letters = plugboard_configuration.replace(" ", "")
        letter_counts = Counter(letters)
        return any(count > 1 for count in letter_counts.values())

    def check_plugboard_length(self):
        plugboard_configuration = self.entry_plugboard.get()
        if not plugboard_configuration:
            return True
        matches = re.findall(r"[A-Z]{2}", plugboard_configuration)
        return len(matches) <= 10

    def show(self):
        self.root.mainloop()

