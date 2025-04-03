"""
Dashboard module for the Restaurant Management System (RMS).

This module defines the `Dashboard` class, which represents the main dashboard interface for the application.
It provides a structured layout with a title and a white background.
"""

from flet import Row, Container, Text, colors, UserControl

class Dashboard(UserControl):
    """
    Represents the main dashboard interface of the RMS.
    
    This class extends `UserControl` and constructs a simple dashboard layout.
    """
    
    def __init__(self) -> None:
        """Initializes the Dashboard class."""
        super().__init__()
    
    def build(self) -> Row:
        """
        Builds and returns the dashboard layout.

        Returns:
            Row: A row containing a container with the dashboard title.
        """
        return Row(
            controls=[
                Container(
                    expand=True,
                    width=1720,
                    height=1080,
                    bgcolor=colors.WHITE,
                    content=Text("Dashboard", size=30, weight="bold")
                )
            ]
        )
