import flet as ft

class ConfirmPassword(ft.UserControl):
    def __init__(self,switchContainer):
        super().__init__()
        self.switchContainer = switchContainer

        self.password_field = ft.TextField(
            border_width=2,
            border_color='blue',
            label='New Password',
            password=True,
            can_reveal_password=True,
            border_radius=10,
        )

        self.confirmPassword_field = ft.TextField(
            border_width=2,
            border_color='blue',
            border_radius=10,
            label='Confirm New Password',
            password=True,
            can_reveal_password=True,  
        )

        self.error_message = ft.Text(value="", color="red", size=12, text_align="center")

        self.submit_button = ft.Container(
            content=ft.Text("Submit", color="white", size=14),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE,
            height=40,
            border_radius=30,
            on_click=lambda _: self.switchContainer("/login"),
        )

        
        self.login_link = ft.TextButton(
            content=ft.Text("Back to Login", color=ft.colors.BLUE, size=12),
            on_click=lambda _: self.switchContainer("/login"),
        )
        
        
    def build(self):
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
                                value="Change Password",
                                size=35,
                                color=ft.colors.BLUE,
                                text_align="center"
                            ),
                        ),
                        ft.Column(
                            spacing=25,
                            controls=[
                                self.password_field,
                                self.confirmPassword_field,
                            ]
                        ),
                        self.error_message,
                        self.submit_button,
                        self.login_link,
                    ],
                ),
            ),
        )

