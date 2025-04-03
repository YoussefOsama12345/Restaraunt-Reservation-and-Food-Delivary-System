import flet as ft


class Signup(ft.UserControl):
    def __init__(self, switchContainer): 
        super().__init__()
        self.switchContainer = switchContainer

        self.name_field = ft.TextField(
            border_width=2,
            border_color='blue',
            label='Full Name',
            border_radius=10,
        )

        self.password_field = ft.TextField(
            border_width=2,
            border_color='blue',
            label='Password',
            password=True,
            can_reveal_password=True,
            border_radius=10,
        )

        self.confirmPassword_field = ft.TextField(
            border_width=2,
            border_color='blue',
            border_radius=10,
            label='Confirm Password',
            password=True,
            can_reveal_password=True,  
        )

        
        self.error_message = ft.Text(value="", color="red", size=12, text_align="center")

        self.signup_button = ft.Container(
            content=ft.Text("Create Account", color="white", size=14),
            alignment=ft.alignment.center,
            bgcolor="blue",
            height=40,
            border_radius=30,
            on_click=lambda _: self.switchContainer("/login"),
        )


        self.login_link = ft.TextButton(
            content=ft.Text("Already have an account? Login!", color="blue", size=12),
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
                padding=40,
                border=ft.border.all(width=3,color='blue'),
                bgcolor="white",
                border_radius=12,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(top=-30,bottom=20),
                            content=ft.Text(
                                value="Create Account",
                                size=35,
                                color=ft.colors.BLUE,
                                text_align="center"),
                        ),
                        ft.Column(
                            spacing=25,
                            controls=[
                                self.name_field,
                                self.password_field,
                                self.confirmPassword_field,
                            ]

                        ),


                        self.error_message,
                        self.signup_button,
                        self.login_link,
                    ],
                ),
            ),
        )
        

