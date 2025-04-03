import flet as ft

from .Signup import Signup
from .ForgetPassword import FirstForgotPassword
from .ConfirmPassword import ConfirmPassword
from ..rms import Landing

class Login(ft.UserControl):
    def __init__(self,switchContainer):
        super().__init__()
        self.switchContainer = switchContainer

        # Input Fields
        self.name_field = ft.TextField(
            border_width=2,
            border_color='blue',
            label='Full Name',
            border_radius=10,
        )

        self.password_field = ft.TextField(
            label="Password",
            border_width=2,
            border_color='blue',
            border_radius=10,
            color="black",
            cursor_color="black",
            password=True,
            can_reveal_password=True,
        )

        self.error_message = ft.Text(value="", color="red", size=12, text_align="center")

        
        self.login_button = ft.Container(
            content=ft.Text("Log In", color="white", size=14),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE,
            height=40,
            border_radius=30,
            on_click=lambda _: self.switchContainer("/rms"),
        )

        
        self.forgot_password_link = ft.TextButton(
            content=ft.Text("Forgot Password?", color=ft.colors.BLUE, size=12),
            on_click=lambda _: self.switchContainer("/firstforgotpassword"),
        )

        self.signup_link = ft.TextButton(
            content=ft.Text("Do not have an account? Sign up!", color=ft.colors.BLUE, size=12),
            on_click=lambda _: self.switchContainer("/signup"),
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
                    border=ft.border.all(width=3,color='blue'),
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
                                    value="Login",
                                    size=35,
                                    color=ft.colors.BLUE,
                                    text_align="center"),
                            ),
                            ft.Column(
                                spacing=25,
                                controls=[
                                    self.name_field,
                                    self.password_field,
                                ]
                            ),
                            self.error_message,
                            self.login_button,
                            self.forgot_password_link,
                            self.signup_link,
                        ],
                    ),
                ),
        )
    

def main(page: ft.Page):
    page.title = "Login"
    page.padding = 0
    page.window_width = 1920
    page.window_height = 1080
    page.window_full_screen = True
    
    
    def switchContainer(router):
        if router == "/signup":
            mainContainer.content = Signup(switchContainer)
            mainContainer.update()
            
        elif router == "/login":
            mainContainer.content = Login(switchContainer)
            mainContainer.update()
            
        elif router == "/firstforgotpassword":
            mainContainer.content = FirstForgotPassword(switchContainer)
            mainContainer.update()
            
        elif router == "/secondforgotpassword":
            mainContainer.content = ConfirmPassword(switchContainer)
            mainContainer.update()
            
        elif router == "/rms":
            mainContainer.content = Landing(switchContainer)
            mainContainer.update()
            
        
            
            
    mainContainer = ft.Container(
        width=1920,
        height=1080,
        bgcolor='white',
        content=Login(switchContainer),
    )
    
    page.add(mainContainer)
    
