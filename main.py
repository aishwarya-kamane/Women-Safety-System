# modules/gui_main.py
import tkinter as tk
from tkinter import ttk
from modules import gui_theme
from modules.gui_dashboard import DashboardFrame
from modules.gui_settings import SettingsFrame
from modules.gui_logs import LogsFrame

class WomenSafetyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Women Safety Dashboard")
        self.geometry("900x600")
        self.configure(bg=gui_theme.BG_COLOR)

        # State Variables
        self.panic_mode = False
        self.active_frame = None

        # Build UI
        self._build_header()
        self._build_content()
        self._build_footer()

        # Show Dashboard by default
        self.show_dashboard()

    def _build_header(self):
        """Creates top header bar with app title + voice status in blue theme"""
        self.header_frame = tk.Frame(self, bg="#1E3A8A", height=70)  # Dark blue header
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        # App Title - centered, large, bold
        title_label = tk.Label(
            self.header_frame,
            text="WOMEN SAFETY SYSTEM",
            font=("Helvetica", 24, "bold"),  # Big and bold
            fg="#FFFFFF",                     # White text
            bg="#1E3A8A"
        )
        title_label.pack(side=tk.TOP, pady=10)  # Centered vertically with padding

        # Optional: add subtle underline for professional look
        underline = tk.Frame(self.header_frame, bg="#60A5FA", height=3)  # Light blue line
        underline.pack(side=tk.TOP, fill=tk.X)

        # Voice Status Indicator - right aligned
        self.voice_status = tk.Label(
            self.header_frame,
            text="🎤 Listening...",
            font=("Helvetica", 12, "italic"),
            fg="#A3E635",  # Greenish for active status
            bg="#1E3A8A"
        )
        self.voice_status.pack(side=tk.RIGHT, padx=20, pady=5)

    def _build_content(self):
        """Main content area (changes based on active view)"""
        self.content_frame = tk.Frame(self, bg=gui_theme.BG_COLOR)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def _build_footer(self):
        """Footer with navigation buttons"""
        self.footer_frame = tk.Frame(self, bg=gui_theme.FOOTER_BG, height=50)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Navigation Buttons
        ttk.Button(self.footer_frame, text="Dashboard", command=self.show_dashboard).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(self.footer_frame, text="Settings", command=self.show_settings).pack(side=tk.LEFT, padx=10, pady=5)
        ttk.Button(self.footer_frame, text="Logs", command=self.show_logs).pack(side=tk.LEFT, padx=10, pady=5)

    def _clear_content(self):
        """Destroys current frame before loading new one"""
        if self.active_frame:
            self.active_frame.destroy()
            self.active_frame = None

  # ---------------- Frame Switch Methods ----------------
    def _clear_content(self):
        if self.active_frame:
            self.active_frame.destroy()
            self.active_frame = None

    def show_dashboard(self):
        self._clear_content()
        self.active_frame = DashboardFrame(self.content_frame, app=self)
        self.active_frame.pack(fill=tk.BOTH, expand=True)

    def show_settings(self):
        self._clear_content()
        self.active_frame = SettingsFrame(self.content_frame)
        self.active_frame.pack(fill=tk.BOTH, expand=True)

    def show_logs(self):
        self._clear_content()
        self.active_frame = LogsFrame(self.content_frame)
        self.active_frame.pack(fill=tk.BOTH, expand=True)
        
    def toggle_panic_mode(self, state: bool):
        """Activates/Deactivates panic overlay"""
        self.panic_mode = state
        if state:
            self._start_panic_overlay()
        else:
            self._stop_panic_overlay()

    def _start_panic_overlay(self):
        """Flash background red to indicate panic"""
        def flash():
            if not self.panic_mode:
                self.configure(bg=gui_theme.BG_COLOR)
                return
            current_color = self.cget("bg")
            next_color = gui_theme.PANIC_COLOR if current_color != gui_theme.PANIC_COLOR else gui_theme.BG_COLOR
            self.configure(bg=next_color)
            self.after(400, flash)  # repeat every 400ms

        flash()

    def _stop_panic_overlay(self):
        self.configure(bg=gui_theme.BG_COLOR)


if __name__ == "__main__":
    app = WomenSafetyApp()
    app.mainloop()
