"""
FirstForgotPassword Module for Restaurant Management System (RMS)

This module implements the first step of the password recovery process, allowing users to verify their identity via a PIN and secret answer.

Key Features:
-------------
- Secure PIN input for user verification.
- Secret answer input for identity validation.
- Submit button to proceed to the next recovery step.
- Back to Login button for returning to the login page.

Attributes:
-----------
- switchContainer (Callable[[str], None]): Switches between UI screens based on the route.
- pin_input (ft.TextField): User PIN input field.
- secret_answer_input (ft.TextField): User secret answer input field.
- error_message (ft.Text): Displays validation errors.
- submit_button (ft.Container): Button to submit the form.
- login_link (ft.TextButton): Button to return to the login page.

Methods:
--------
1. __init__(self, switchContainer: callable) -> None:
    - Initializes UI components for the first step of password recovery.
    
2. validate_form(self) -> bool:
    - Validates the PIN (at least 4 characters) and non-empty secret answer. Returns True if valid, False otherwise.
    
3. submit_form(self, e: ft.ControlEvent) -> None:
    - Validates inputs and proceeds to the next screen if valid, or shows an error message.
    
4. build(self) -> ft.Container:
    - Constructs and returns the layout for the forgot password page, including input fields and action buttons.
"""

import flet as ft


class FirstForgotPassword(ft.UserControl):
    """
    Represents the first step of the forgot password process in the RMS.

    Attributes:
        switchContainer (Callable[[str], None]): A function to switch between different UI screens.
        pin_input (ft.TextField): Input field for entering the PIN.
        secret_answer_input (ft.TextField): Input field for entering the security question answer.
        error_message (ft.Text): Displays error messages if input validation fails.
        submit_button (ft.Container): Button to submit the form and navigate to the next step.
        login_link (ft.TextButton): Button to navigate back to the login page.
    """

    def __init__(self, switchContainer: callable) -> None:
        """Initializes the FirstForgotPassword class with UI components."""
        super().__init__()
        self.switchContainer = switchContainer

        self.pin_input = ft.TextField(
            label="Enter your PIN",
            border_width=2,
            border_color='blue',
            border_radius=10,
            password=True,
        )

        self.secret_answer_input = ft.TextField(
            label="Enter your secret answer",
            border_width=2,
            border_color='blue',
            border_radius=10,
            color="black",
            cursor_color="black",
        )

        self.error_message = ft.Text(value="", color="red", size=12, text_align="center")

        self.submit_button = ft.Container(
            content=ft.Text("Submit", color="white", size=14),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE,
            height=40,
            border_radius=30,
            on_click=self.submit_form,
        )

        self.login_link = ft.TextButton(
            content=ft.Text("Back to Login", color=ft.colors.BLUE, size=12),
            on_click=lambda _: self.switchContainer("/login"),
        )

    def validate_form(self) -> bool:
        """
        Validates the input fields (PIN and secret answer).

        Returns:
            bool: True if inputs are valid, False otherwise.
        """
        pin = self.pin_input.value
        secret_answer = self.secret_answer_input.value

        if not pin or len(pin) < 4:
            self.error_message.value = "PIN must be at least 4 digits."
            return False
        if not secret_answer:
            self.error_message.value = "Secret answer cannot be empty."
            return False

        self.error_message.value = ""
        return True

    def submit_form(self, e: ft.ControlEvent) -> None:
        """
        Handles form submission, validates input, and proceeds to the next screen if valid.

        Args:
            e (ft.ControlEvent): The event object triggered by clicking submit.
        """
        if self.validate_form():
            pin = self.pin_input.value
            secret_answer = self.secret_answer_input.value
            self.switchContainer("/secondforgotpassword")
        else:
            self.page.update()

    def build(self) -> ft.Container:
        """
        Builds and returns the UI layout for the forgot password page.

        Returns:
            ft.Container: A container with input fields, buttons, and error messages.
        """
        return ft.Container(
            padding=0,
            bgcolor='white',
            width=1920,
            height=1080,
            alignment=ft.alignment.center,
            content=ft.Container(
                width=500,
                height=500,
                border=ft.border.all(width=3, color='blue'),
                padding=40,
                bgcolor="white",
                border_radius=12,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(bottom=25),
                            content=ft.Text(
                                value="Forgot Password",
                                size=35,
                                color=ft.colors.BLUE,
                                text_align="center"
                            ),
                        ),
                        ft.Column(
                            spacing=25,
                            controls=[
                                self.pin_input,
                                self.secret_answer_input,
                            ]
                        ),
                        self.error_message,
                        self.submit_button,
                        self.login_link,
                    ],
                ),
            ),
        )
