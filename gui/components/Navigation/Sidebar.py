"""
modern_navbar.py

This module defines the ModernNavBar component for the application.

The ModernNavBar component provides a sidebar navigation system with animated collapsing behavior.
"""

import flet as ft

class Sidebar(ft.UserControl):
    """
    A ModernNavBar component that provides a collapsible sidebar navigation menu.
    
    Attributes:
    -----------
    switchContainer : callable
        A function to switch views when a navigation item is clicked.
    sidebar_width : int
        The width of the sidebar, toggles between expanded and collapsed states.
    
    Methods:
    --------
    AnimateSideBar(event):
        Animates the sidebar between expanded and collapsed states.
    highlight(event):
        Highlights a navigation item when hovered.
    UserData(initials: str, name: str, description: str) -> ft.Container:
        Creates a user profile container for the sidebar.
    ContainedIcon(icon_name: str, text: str, router: str) -> ft.Container:
        Creates a clickable navigation icon with a label.
    build() -> ft.Container:
        Constructs the sidebar navigation UI.
    """
    def __init__(self, switchContainer: callable):
        """
        Initializes the ModernNavBar component.

        Parameters:
        -----------
        switchContainer : callable
            Function to switch views when a navigation item is clicked.
        """
        super().__init__()
        self.switchContainer = switchContainer
        self.sidebar_width: int = 200

    def AnimateSideBar(self, event: ft.ControlEvent) -> None:
        """
        Toggles the sidebar width between expanded and collapsed states.

        Parameters:
        -----------
        event : ft.ControlEvent
            The event object triggered by the sidebar toggle button.
        """
        self.sidebar_width = 65 if self.sidebar_width == 200 else 200
        event.control.update()

    def highlight(self, event: ft.ControlEvent) -> None:
        """
        Highlights the navigation item when hovered.

        Parameters:
        -----------
        event : ft.ControlEvent
            The event object triggered when hovering over a navigation item.
        """
        if event.data == "true":
            event.control.bgcolor = 'white10'
            event.control.content.controls[0].icon_color = 'white'
            event.control.content.controls[1].color = 'white'
        else:
            event.control.bgcolor = None
            event.control.content.controls[0].icon_color = 'white54'
            event.control.content.controls[1].color = 'white54'
        event.control.update()

    def UserData(self, initials: str, name: str, description: str) -> ft.Container:
        """
        Creates a user profile container for the sidebar.
        
        Parameters:
        -----------
        initials : str
            The initials of the user.
        name : str
            The full name of the user.
        description : str
            A short description or role of the user.
        
        Returns:
        --------
        ft.Container
            A container displaying the user's profile information.
        """
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        margin=ft.margin.only(left=4),
                        width=40, height=40, bgcolor='white',
                        border_radius=5, alignment=ft.alignment.center,
                        content=ft.Text(value=initials, size=20, weight='bold', color=ft.colors.BLUE)
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=10),
                        content=ft.Column(
                            spacing=1,
                            controls=[
                                ft.Text(value=name, size=15, weight='bold', opacity=1, animate_opacity=200),
                                ft.Text(value=description, color='white54', size=11, weight='w400', opacity=1,
                                    animate_opacity=200)
                            ]
                        )
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str, router: str) -> ft.Container:
        """
        Creates a clickable navigation icon with a label.
        
        Parameters:
        -----------
        icon_name : str
            The name of the icon.
        text : str
            The label for the navigation item.
        router : str
            The path associated with the navigation item.
        
        Returns:
        --------
        ft.Container
            A container representing a clickable navigation item.
        """
        return ft.Container(
            width=190, height=45, border_radius=5,
            on_hover=self.highlight,
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name, icon_size=30, icon_color='white54',
                        on_click=lambda _: self.switchContainer(router),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    ),
                    ft.Text(value=text, color='white54', size=20, opacity=1, animate_opacity=200)
                ]
            )
        )

    def build(self) -> ft.Container:
        """
        Constructs the sidebar navigation UI.
        
        Returns:
        --------
        ft.Container
            The fully constructed sidebar navigation component.
        """
        return ft.Container(
            width=self.sidebar_width,
            bgcolor='blue',
            animate=ft.animation.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
            height=1080,
            padding=ft.padding.only(top=10, left=10),
            content=ft.Column(
                scroll='auto',
                width=300,
                alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
                controls=[
                    self.UserData("Y", 'Youssef', "Software"),
                    ft.Divider(height=5, color='transparent'),
                    ft.Container(
                        width=180, height=45,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon_size=30, icon_color='white54', icon=ft.icons.MENU,
                                    on_click=self.AnimateSideBar,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
                                ),
                                ft.Text(value='Menu', color='white54', size=20, opacity=1, animate_opacity=200),
                            ]
                        )
                    ),
                    self.ContainedIcon(ft.icons.HOME, "Home", "/home"),
                    self.ContainedIcon(ft.icons.DASHBOARD, "Dashboard", "/dashboard"),
                    self.ContainedIcon(ft.icons.LOCAL_HOSPITAL, "Doctors", "/doctors"),
                    self.ContainedIcon(ft.icons.HEALING, "Nurses", "/nurses"),
                    self.ContainedIcon(ft.icons.PEOPLE, "Patients", "/patients"),
                    self.ContainedIcon(ft.icons.LOCAL_PHARMACY, "Pharmacy", "/pharmacy"),
                    self.ContainedIcon(ft.icons.GROUP, "Staff", "/staff"),
                    self.ContainedIcon(ft.icons.PERSON, "Users", "/users"),
                    self.ContainedIcon(ft.icons.CALENDAR_TODAY, "Attendance", "/attendance"),
                    self.ContainedIcon(ft.icons.MONEY, "Expenses", "/expenses"),
                    self.ContainedIcon(ft.icons.EVENT, "Appointments", "/appointments"),
                    self.ContainedIcon(ft.icons.MEETING_ROOM, "Rooms", "/rooms"),
                    self.ContainedIcon(ft.icons.BUSINESS, "Department", "/department"),
                    self.ContainedIcon(ft.icons.RECEIPT, "Billing", "/billing"),
                ]
            )
        )