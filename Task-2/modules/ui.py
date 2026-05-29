import customtkinter as ctk
from modules.calculator_logic import calculate_expression


class CalculatorUI:

    def __init__(self, root):

        self.root = root
        self.expression = ""

        self.create_ui()

    def button_click(self, value):

        self.expression += str(value)

        self.display.delete(0, "end")
        self.display.insert(0, self.expression)

    def clear(self):

        self.expression = ""

        self.display.delete(0, "end")

    def calculate(self):

        result = calculate_expression(
            self.expression
        )

        self.expression = result

        self.display.delete(0, "end")
        self.display.insert(0, result)

    def create_ui(self):

        self.display = ctk.CTkEntry(
            self.root,
            width=380,
            height=90,
            font=("Segoe UI", 30, "bold"),
            justify="right"
        )

        self.display.pack(
            pady=20
        )

        frame = ctk.CTkFrame(
            self.root,
            fg_color="#0b1220"
        )

        frame.pack(
            pady=10
        )

        button_font = (
            "Segoe UI",
            20,
            "bold"
        )

        buttons = [
            ["C", "/", "*", "-"],
            ["7", "8", "9", "+"],
            ["4", "5", "6", "."],
            ["1", "2", "3", "0"]
        ]

        for row_num, row in enumerate(buttons):

            for col_num, value in enumerate(row):

                if value == "C":

                    btn = ctk.CTkButton(
                        frame,
                        text=value,
                        width=80,
                        height=70,
                        fg_color="#ef4444",
                        hover_color="#dc2626",
                        font=button_font,
                        command=self.clear
                    )

                elif value in [
                    "+",
                    "-",
                    "*",
                    "/"
                ]:

                    btn = ctk.CTkButton(
                        frame,
                        text=value,
                        width=80,
                        height=70,
                        fg_color="#2563eb",
                        hover_color="#1d4ed8",
                        font=button_font,
                        command=lambda v=value:
                        self.button_click(v)
                    )

                else:

                    btn = ctk.CTkButton(
                        frame,
                        text=value,
                        width=80,
                        height=70,
                        fg_color="#111827",
                        hover_color="#1f2937",
                        font=button_font,
                        command=lambda v=value:
                        self.button_click(v)
                    )

                btn.grid(
                    row=row_num,
                    column=col_num,
                    padx=6,
                    pady=6
                )

        equal_btn = ctk.CTkButton(
            frame,
            text="=",
            width=180,
            height=75,
            fg_color="#16a34a",
            hover_color="#22c55e",
            font=("Segoe UI", 26, "bold"),
            command=self.calculate
        )

        equal_btn.grid(
            row=4,
            column=1,
            columnspan=2,
            padx=6,
            pady=12
        )