"""The Little Angels Public Higher Secondary School management software."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import ttk

from core.data_store import DataStore
from modules.backup_tab import BackupTab
from modules.dashboard_tab import DashboardTab
from modules.donations_tab import DonationsTab
from modules.expenses_tab import ExpensesTab
from modules.fees_tab import FeesTab
from modules.info_tab import InfoTab
from modules.reports_tab import ReportsTab
from modules.staff_tab import StaffTab
from modules.students_tab import StudentsTab


class SchoolSoftwareApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("The Little Angels Public Higher Secondary School - Management System")
        self.geometry("1320x780")
        self.minsize(1100, 680)

        base_dir = Path(__file__).resolve().parent
        self.store = DataStore(base_dir)
        self._setup_style()
        self._build_ui()
        self.refresh_all_tabs()

    def _setup_style(self) -> None:
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("TNotebook.Tab", padding=(12, 7))
        style.configure("TLabelframe", padding=6)

    def _build_ui(self) -> None:
        wrapper = ttk.Frame(self)
        wrapper.pack(fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(wrapper)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.tabs: dict[str, ttk.Frame] = {}
        self.tabs["Dashboard"] = DashboardTab(self.notebook, self.store, self.select_tab)
        self.tabs["Students"] = StudentsTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Fees"] = FeesTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Staff"] = StaffTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Expenses"] = ExpensesTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Donations"] = DonationsTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Reports"] = ReportsTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Info"] = InfoTab(self.notebook, self.store, self.refresh_all_tabs)
        self.tabs["Backup"] = BackupTab(self.notebook, self.store, self.refresh_all_tabs)

        for name, tab in self.tabs.items():
            self.notebook.add(tab, text=name)

    def select_tab(self, tab_name: str) -> None:
        tab = self.tabs.get(tab_name)
        if not tab:
            return
        self.notebook.select(tab)

    def refresh_all_tabs(self) -> None:
        for tab_name in [
            "Students",
            "Fees",
            "Staff",
            "Expenses",
            "Donations",
            "Info",
            "Backup",
            "Reports",
            "Dashboard",
        ]:
            tab = self.tabs.get(tab_name)
            if tab and hasattr(tab, "refresh"):
                tab.refresh()


def main() -> None:
    app = SchoolSoftwareApp()
    app.mainloop()


if __name__ == "__main__":
    main()
