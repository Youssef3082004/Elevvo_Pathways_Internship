from flet import * 
from Screens.Intro import Intro

 
class Main_application(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.title = "Jobs & Resume Ranker"
        self.page.window.frameless = False
        self.page.window.resizable = False
        self.page.window.maximized = True
        self.page.scroll = ScrollMode.AUTO
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER

        self.page.fonts = {"plus":r"font/PlusJakartaSans.ttf"}
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.page_go
        self.page.go(route="/Intro")
        self.page.update()


    def route_change(self,e):
        self.Intro_Screen = Intro(page=self.page)

        if self.page.route == "/Intro":
            self.page.views.append(View("/Intro",[self.Intro_Screen],padding=0,appbar=self.Intro_Screen.appbar))
        
        # elif self.page.route == "/employer":
        #     # adminScreen_class = EmployerScreen(page=self.page)
        #     self.page.views.append(View("/employer",[adminScreen_class],padding=0,appbar=adminScreen_class.appbar,bgcolor="#f6f8f6"))
        
        # elif self.page.route == "/supervisor":
        #     # adminScreen_class = SupervisorScreen(page=self.page)
        #     self.page.views.append(View("/supervisor",[adminScreen_class],padding=0,appbar=adminScreen_class.appbar,bgcolor="#f6f8f6"))

        # elif self.page.route == "/newclient":
        #     # adminScreen_class = NewClientScreen(page=self.page)            
        #     self.page.views.append(View("/newclient",[adminScreen_class],padding=0,appbar=adminScreen_class.appbar,bgcolor="#f6f8f6"))
        
        # elif self.page.route == "/client":
        #     Client_class = ClientScreen(page=self.page,Client_data=self.login_Screen.Client_Data)            
        #     self.page.views.append(View("/client",[Client_class],padding=0,appbar=Client_class.appbar,bgcolor="#f6f8f6"))
        
        # elif self.page.route == "/update":
        #     Client_class = UpdateScreen(page=self.page)            
        #     self.page.views.append(View("/client",[Client_class],appbar=Client_class.appbar,padding=0,bgcolor="#f6f8f6"))

        self.page.update()
        
    def page_go(self,e):
        self.page.views.pop()
        back_page = self.page.views[-1]
        self.page.go(back_page.route)
        self.page.update()

    


def main(page:Page):
   page.window.icon = r"images/logo.ico"
   page.add(Main_application(page=page))
   page.update()
   

app(target=main, assets_dir="assets")