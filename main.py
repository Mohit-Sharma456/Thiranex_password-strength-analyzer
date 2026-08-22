import tkinter as tk
from tkinter import messagebox
import secrets

from analyzer import analyze_password
from database import (
    initialize_database,
    is_password_reused,
    save_password,
    get_password_count,
    clear_password_history,
)
from password_generator import generate_strong_password


# ============================================================
# APPLICATION
# ============================================================

class PasswordStrengthAnalyzer:

    # ========================================================
    # SHOW / HIDE PASSWORD
    # ========================================================

    def toggle_password(self):

        if self.show_password:
            # Hide password
            self.password_entry.config(show="•")
            self.show_password = False
        else:
            # Show password
            self.password_entry.config(show="")
            self.show_password = True

        # Update the eye icon. When password is visible,
        # a diagonal cross/slash is drawn over the eye.
        self.draw_eye_icon()

    def draw_eye_icon(self):
        """Draw the eye icon and add a slash when password is visible."""

        self.eye_canvas.delete("all")

        # Eye outline
        self.eye_canvas.create_oval(
            7, 11, 33, 29,
            outline="#94A3B8",
            width=2
        )

        # Eye pupil
        self.eye_canvas.create_oval(
            16, 15, 24, 23,
            fill="#94A3B8",
            outline=""
        )

        # Cross/slash appears ONLY when password is visible
        if self.show_password:
            self.eye_canvas.create_line(
                5, 32, 35, 7,
                fill="#EF4444",
                width=2
            )

    def __init__(self, root):

        self.root = root

        self.root.title("Password Strength Analyzer")
        self.root.geometry("1000x720")
        self.root.minsize(900, 650)

        self.root.configure(bg="#0F172A")

        initialize_database()

        self.create_variables()
        self.create_ui()

    # ========================================================
    # VARIABLES
    # ========================================================

    def create_variables(self):

        self.password_var = tk.StringVar()

        self.score_var = tk.StringVar(
            value="Score: -- / 100"
        )

        self.strength_var = tk.StringVar(
            value="Strength: Not Analyzed"
        )

        self.entropy_var = tk.StringVar(
            value="Entropy: -- bits"
        )

        self.status_var = tk.StringVar(
            value="Enter a password and click Analyze Password."
        )

        self.show_password = False

    # ========================================================
    # UI
    # ========================================================

    def create_ui(self):

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        header = tk.Frame(
            self.root,
            bg="#111827",
            height=100
        )

        header.pack(
            fill="x"
        )

        title = tk.Label(
            header,
            text="PASSWORD STRENGTH ANALYZER",
            font=("Segoe UI", 25, "bold"),
            bg="#111827",
            fg="#38BDF8"
        )

        title.pack(
            pady=(20, 2)
        )

        subtitle = tk.Label(
            header,
            text="Cybersecurity Password Assessment Tool",
            font=("Segoe UI", 11),
            bg="#111827",
            fg="#94A3B8"
        )

        subtitle.pack()

        # ----------------------------------------------------
        # Main container
        # ----------------------------------------------------

        main = tk.Frame(
            self.root,
            bg="#0F172A"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # ----------------------------------------------------
        # Password Section
        # ----------------------------------------------------

        # password_card = tk.Frame(
        #     main,
        #     bg="#1E293B",
        #     bd=0
        # )

        # password_card.pack(
        #     fill="x",
        #     pady=(0, 15)
        # )

        # password_label = tk.Label(
        #     password_card,
        #     text="Enter Password",
        #     font=("Segoe UI", 13, "bold"),
        #     bg="#1E293B",
        #     fg="white"
        # )

        # password_label.pack(
        #     anchor="w",
        #     padx=20,
        #     pady=(15, 8)
        # )

        # input_frame = tk.Frame(
        #     password_card,
        #     bg="#1E293B"
        # )

        # input_frame.pack(
        #     fill="x",
        #     padx=20
        # )

        # self.password_entry = tk.Entry(
        #     input_frame,
        #     textvariable=self.password_var,
        #     font=("Segoe UI", 15),
        #     show="•",
        #     bg="#0F172A",
        #     fg="white",
        #     insertbackground="white",
        #     relief="flat"
        # )

        # self.password_entry.pack(
        #     side="left",
        #     fill="x",
        #     expand=True,
        #     ipady=12
        # )

        # show_button = tk.Button(
        #     input_frame,
        #     text="SHOW",
        #     font=("Segoe UI", 10, "bold"),
        #     bg="#334155",
        #     fg="white",
        #     activebackground="#475569",
        #     activeforeground="white",
        #     relief="flat",
        #     cursor="hand2",
        #     command=self.toggle_password
        # )

        # show_button.pack(
        #     side="right",
        #     padx=(8, 0),
        #     ipadx=12,
        #     ipady=8
        # )

        # ============================================================
        # PASSWORD INPUT
        # ============================================================

        password_card = tk.Frame(
            main,
            bg="#1E293B"
        )

        password_card.pack(
            fill="x",
            pady=(0, 15)
        )

        password_label = tk.Label(
            password_card,
            text="ENTER PASSWORD",
            font=("Segoe UI", 11, "bold"),
            bg="#1E293B",
            fg="#CBD5E1"
        )

        password_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 8)
        )

        # Input container
        password_input_frame = tk.Frame(
            password_card,
            bg="#0F172A",
            highlightthickness=1,
            highlightbackground="#334155",
            highlightcolor="#38BDF8"
        )

        password_input_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 15),
            ipady=2
        )

        # Password entry
        self.password_entry = tk.Entry(
            password_input_frame,
            textvariable=self.password_var,
            font=("Segoe UI", 15),
            show="•",
            bg="#0F172A",
            fg="#F8FAFC",
            insertbackground="#38BDF8",
            relief="flat",
            bd=0
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(14, 0),
            ipady=11
        )

        # Eye icon INSIDE the password input.
        # Hidden  -> normal eye
        # Visible -> same eye with a diagonal cross/slash
        self.eye_canvas = tk.Canvas(
            password_input_frame,
            width=40,
            height=40,
            bg="#0F172A",
            highlightthickness=0,
            cursor="hand2"
        )

        self.eye_canvas.pack(
            side="right",
            padx=(4, 8),
            pady=4
        )

        self.eye_canvas.bind(
            "<Button-1>",
            lambda event: self.toggle_password()
        )

        self.draw_eye_icon()

        # ----------------------------------------------------
        # Buttons
        # ----------------------------------------------------

        button_frame = tk.Frame(
            password_card,
            bg="#1E293B"
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        analyze_button = tk.Button(
            button_frame,
            text="ANALYZE PASSWORD",
            font=("Segoe UI", 12, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.analyze
        )

        analyze_button.pack(
            side="left",
            ipadx=25,
            ipady=10
        )

        generate_button = tk.Button(
            button_frame,
            text="GENERATE STRONG PASSWORD",
            font=("Segoe UI", 12, "bold"),
            bg="#059669",
            fg="white",
            activebackground="#047857",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.generate_password
        )

        generate_button.pack(
            side="left",
            padx=10,
            ipadx=15,
            ipady=10
        )

        clear_button = tk.Button(
            button_frame,
            text="CLEAR",
            font=("Segoe UI", 12, "bold"),
            bg="#475569",
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.clear
        )

        clear_button.pack(
            side="left",
            ipadx=20,
            ipady=10
        )

        # ----------------------------------------------------
        # Result Cards
        # ----------------------------------------------------

        result_frame = tk.Frame(
            main,
            bg="#0F172A"
        )

        result_frame.pack(
            fill="x",
            pady=(0, 15)
        )

        # Score

        score_card = tk.Frame(
            result_frame,
            bg="#1E293B"
        )

        score_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        tk.Label(
            score_card,
            text="SECURITY SCORE",
            font=("Segoe UI", 10, "bold"),
            bg="#1E293B",
            fg="#94A3B8"
        ).pack(
            pady=(15, 5)
        )

        tk.Label(
            score_card,
            textvariable=self.score_var,
            font=("Segoe UI", 18, "bold"),
            bg="#1E293B",
            fg="#38BDF8"
        ).pack(
            pady=(0, 15)
        )

        # Strength

        strength_card = tk.Frame(
            result_frame,
            bg="#1E293B"
        )

        strength_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            strength_card,
            text="PASSWORD STRENGTH",
            font=("Segoe UI", 10, "bold"),
            bg="#1E293B",
            fg="#94A3B8"
        ).pack(
            pady=(15, 5)
        )

        self.strength_label = tk.Label(
            strength_card,
            textvariable=self.strength_var,
            font=("Segoe UI", 18, "bold"),
            bg="#1E293B",
            fg="#F59E0B"
        )

        self.strength_label.pack(
            pady=(0, 15)
        )

        # Entropy

        entropy_card = tk.Frame(
            result_frame,
            bg="#1E293B"
        )

        entropy_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            entropy_card,
            text="ESTIMATED ENTROPY",
            font=("Segoe UI", 10, "bold"),
            bg="#1E293B",
            fg="#94A3B8"
        ).pack(
            pady=(15, 5)
        )

        tk.Label(
            entropy_card,
            textvariable=self.entropy_var,
            font=("Segoe UI", 18, "bold"),
            bg="#1E293B",
            fg="#A78BFA"
        ).pack(
            pady=(0, 15)
        )

        # ----------------------------------------------------
        # Analysis area
        # ----------------------------------------------------

        analysis_frame = tk.Frame(
            main,
            bg="#1E293B"
        )

        analysis_frame.pack(
            fill="both",
            expand=True
        )

        # LEFT

        left_frame = tk.Frame(
            analysis_frame,
            bg="#1E293B"
        )

        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(15, 8),
            pady=15
        )

        tk.Label(
            left_frame,
            text="SECURITY CHECKS",
            font=("Segoe UI", 12, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        self.checks_text = tk.Text(
            left_frame,
            height=10,
            bg="#0F172A",
            fg="#E2E8F0",
            insertbackground="white",
            font=("Consolas", 10),
            relief="flat",
            wrap="word"
        )

        self.checks_text.pack(
            fill="both",
            expand=True
        )

        self.checks_text.config(
            state="disabled"
        )

        # RIGHT

        right_frame = tk.Frame(
            analysis_frame,
            bg="#1E293B"
        )

        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(8, 15),
            pady=15
        )

        tk.Label(
            right_frame,
            text="SECURITY SUGGESTIONS",
            font=("Segoe UI", 12, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        self.suggestions_text = tk.Text(
            right_frame,
            height=10,
            bg="#0F172A",
            fg="#E2E8F0",
            insertbackground="white",
            font=("Segoe UI", 10),
            relief="flat",
            wrap="word"
        )

        self.suggestions_text.pack(
            fill="both",
            expand=True
        )

        self.suggestions_text.config(
            state="disabled"
        )

        # ----------------------------------------------------
        # Footer
        # ----------------------------------------------------

        footer = tk.Frame(
            self.root,
            bg="#111827",
            height=45
        )

        footer.pack(
            fill="x"
        )

        tk.Label(
            footer,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            bg="#111827",
            fg="#94A3B8"
        ).pack(
            side="left",
            padx=20,
            pady=12
        )

        self.database_label = tk.Label(
            footer,
            text=f"Password history records: {get_password_count()}",
            font=("Segoe UI", 10),
            bg="#111827",
            fg="#64748B"
        )

        self.database_label.pack(
            side="right",
            padx=20
        )

    # ========================================================
    # TOGGLE PASSWORD
    # ========================================================

    # def toggle_password(self):

    #     self.show_password = not self.show_password

    #     if self.show_password:
    #         self.password_entry.config(show="")
    #     else:
    #         self.password_entry.config(show="•")

        def toggle_password(self):

            if self.show_password:

                # Hide password
                self.password_entry.config(
                    show="•"
                )

                self.show_hide_button.config(
                    text="👁"
                )

                self.show_password = False

            else:

                # Show password
                self.password_entry.config(
                    show=""
                )

                self.show_hide_button.config(
                    text="🙈"
                )

                self.show_password = True

    # ========================================================
    # ANALYZE PASSWORD
    # ========================================================

    def analyze(self):

        password = self.password_var.get()

        if not password:

            messagebox.showwarning(
                "Password Required",
                "Please enter a password first."
            )

            return

        # ----------------------------------------------------
        # Run analyzer ONLY when button is clicked
        # ----------------------------------------------------

        result = analyze_password(password)

        score = result["score"]
        strength = result["strength"]
        entropy = result["entropy"]

        # ----------------------------------------------------
        # Database reuse check
        # ----------------------------------------------------

        reused = is_password_reused(password)

        if reused:

            self.status_var.set(
                "WARNING: This password was previously used."
            )

            result["suggestions"].insert(
                0,
                "Do not reuse this password. It exists in your local password history."
            )

            messagebox.showwarning(
                "Password Reuse Detected",
                "This password has already been used before.\n\n"
                "Choose a different password."
            )

        else:

            self.status_var.set(
                "Analysis completed successfully."
            )

        # ----------------------------------------------------
        # Update result
        # ----------------------------------------------------

        self.score_var.set(
            f"Score: {score} / 100"
        )

        self.strength_var.set(
            f"Strength: {strength}"
        )

        self.entropy_var.set(
            f"Entropy: {entropy} bits"
        )

        # ----------------------------------------------------
        # Strength label color
        # ----------------------------------------------------

        strength_colors = {
            "Very Weak": "#EF4444",
            "Weak": "#F97316",
            "Medium": "#F59E0B",
            "Strong": "#22C55E",
            "Very Strong": "#10B981",
        }

        self.strength_label.config(
            fg=strength_colors.get(
                strength,
                "#F59E0B"
            )
        )

        # ----------------------------------------------------
        # Display checks
        # ----------------------------------------------------

        self.checks_text.config(
            state="normal"
        )

        self.checks_text.delete(
            "1.0",
            tk.END
        )

        for name, passed, description in result["checks"]:

            if passed:
                symbol = "PASS"
            else:
                symbol = "FAIL"

            self.checks_text.insert(
                tk.END,
                f"[{symbol}] {name}\n"
                f"       {description}\n\n"
            )

        self.checks_text.config(
            state="disabled"
        )

        # ----------------------------------------------------
        # Display suggestions
        # ----------------------------------------------------

        self.suggestions_text.config(
            state="normal"
        )

        self.suggestions_text.delete(
            "1.0",
            tk.END
        )

        for index, suggestion in enumerate(
            result["suggestions"],
            start=1
        ):

            self.suggestions_text.insert(
                tk.END,
                f"{index}. {suggestion}\n\n"
            )

        self.suggestions_text.config(
            state="disabled"
        )

        # ----------------------------------------------------
        # Save only if it is a new password
        # ----------------------------------------------------

        if not reused:

            save_password(password)

            self.database_label.config(
                text=f"Password history records: {get_password_count()}"
            )

    # ========================================================
    # GENERATE PASSWORD
    # ========================================================

    def generate_password(self):

        password = generate_strong_password(18)

        self.password_var.set(
            password
        )

        self.status_var.set(
            "Strong password generated. Click Analyze Password to evaluate it."
        )

        # Clear previous analysis
        self.score_var.set(
            "Score: -- / 100"
        )

        self.strength_var.set(
            "Strength: Not Analyzed"
        )

        self.entropy_var.set(
            "Entropy: -- bits"
        )

        self.strength_label.config(
            fg="#F59E0B"
        )

        self.clear_text_widgets()

    # ========================================================
    # CLEAR
    # ========================================================

    def clear(self):

        self.password_var.set("")

        self.score_var.set(
            "Score: -- / 100"
        )

        self.strength_var.set(
            "Strength: Not Analyzed"
        )

        self.entropy_var.set(
            "Entropy: -- bits"
        )

        self.strength_label.config(
            fg="#F59E0B"
        )

        self.status_var.set(
            "Enter a password and click Analyze Password."
        )

        self.clear_text_widgets()

    # ========================================================
    # CLEAR TEXT WIDGETS
    # ========================================================

    def clear_text_widgets(self):

        self.checks_text.config(
            state="normal"
        )

        self.checks_text.delete(
            "1.0",
            tk.END
        )

        self.checks_text.config(
            state="disabled"
        )

        self.suggestions_text.config(
            state="normal"
        )

        self.suggestions_text.delete(
            "1.0",
            tk.END
        )

        self.suggestions_text.config(
            state="disabled"
        )

    # ========================================================
    # RUN
    # ========================================================


def main():

    root = tk.Tk()

    app = PasswordStrengthAnalyzer(root)

    root.mainloop()


if __name__ == "__main__":
    main()