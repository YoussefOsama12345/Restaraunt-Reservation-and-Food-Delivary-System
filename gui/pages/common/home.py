import flet as ft

class Home(ft.UserControl):
    """Represents the home screen of the Hospital Management System."""

    def __init__(self):
        """Initializes the Home class."""
        super().__init__()

    def build(self):
        """Builds the UI layout for the home screen."""
        return ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    width=1720,  # 1920 - 200 (navbar width)
                    height=1080,
                    bgcolor=ft.colors.WHITE,
                    padding=20,
                    content=ft.Text(
                        "Welcome to Hospital Management System", size=30, weight="bold"
                    ),
                )
            ],
        )



    
    
    # contentContainer = ft.Container(width=1920,height=1080,bgcolor=ft.colors.WHITE)
    
    
    # def switchPanel(panel_name):
        
    #     spinner = ft.Container(width=80,height=80,content=ft.ProgressRing(width=80, height=80, stroke_width=6, color="blue"),alignment=ft.alignment.center)
        
    #     match panel_name:
    #         case "Home":
    #             contentContainer.content = Home()
    #             page.update()
    #         case "Dashboard":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Dashboard()
    #             page.update()
    #         case "Doctors":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Doctors(menubar,datePicker,BirthDatePicker)
    #             page.update()
    #         case "Nurses":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Nurses(menubar,datePicker,BirthDatePicker)
    #             page.update()
    #         case "Patients":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Patients(menubar)
    #             page.update()
    #         case "Pharamacy":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Pharamacy(menubar)
    #             page.update()
    #         case "Staff":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Staff(menubar)
    #             page.update()
    #         case "Users":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Users(menubar)
    #             page.update()
    #         case "Attendance":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Attendance(menubar)
    #             page.update()
    #         case "Expenses":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Expenses(menubar)
    #             page.update()
    #         case "Appointments":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Appointments(menubar)
    #             page.update()
    #         case "Rooms":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Room(menubar)
    #             page.update()
    #         case "Department":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Department(menubar)
    #             page.update()
    #         case "Billing":
    #             contentContainer.content =   spinner
    #             page.update()
    #             time.sleep(0.5)
    #             contentContainer.content = Billing(menubar)
    #             page.update()



    # def AnimateSideBar(event):

    #     userTextContainer = page.controls[0].controls[0].controls[0].content.controls[0].content.controls[1].content
    #     userTextList = page.controls[0].controls[0].controls[0].content.controls[0].content.controls[1].content.controls[:]
    #     componentsList = page.controls[0].controls[0].controls[0].content.controls[2:13]


    #     if page.controls[0].controls[0].controls[0].width == 200:

    #         for item in userTextList:
    #             item.opacity = 0
    #             userTextContainer.update()

    #         for component in componentsList:
    #             component.content.controls[1].opacity = 0
    #             component.update()

    #         page.controls[0].controls[0].controls[0].width = 65
    #         page.controls[0].controls[0].controls[0].update()

    #     elif page.controls[0].controls[0].controls[0].width != 200:

    #         for item in userTextList:
    #             item.opacity = 1
    #             userTextContainer.update()

    #         for component in componentsList:
    #             component.content.controls[1].opacity = 1
    #             component.update()

    #         page.controls[0].controls[0].controls[0].width = 200
    #         page.controls[0].controls[0].controls[0].update()
    
    
    # page.add(ModernNavBar(AnimateSideBar))
