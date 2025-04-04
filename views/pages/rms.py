import flet as ft

from .common.home import Home
from .admin.dashboard import Dashboard
from ..pages import Sidebar

class Landing(ft.UserControl):
    def __init__(self, switchContainer):
        super().__init__()
        self.switchContainer = switchContainer
        self.maincontainer = ft.Container(
            width=1720,
            height=1080,
            bgcolor=ft.colors.WHITE,
            content=Home()
        )
        
    
    def switchPanel(self, router):
        if router == "/home":
            self.maincontainer.content = Home()
            self.maincontainer.update()
            
        elif router == "/dashboard":
            self.maincontainer.content = Dashboard()
            self.maincontainer.update()
        
    
    def build(self):
        return ft.Container(
            width=1920,
            height=1080,
            bgcolor=ft.colors.WHITE,
            content=ft.Row(
                controls=[
                    Sidebar(self.switchPanel),
                    self.maincontainer
                ]
            )
        )
