from flet import * 
from DataTransmiter import JobsDataTransmiter ,EmployersDataTransmiter
from Screens.Intro import Intro
from Screens.JobsCV import JobsCV
from Screens.EmployersCV import EmployersCV
from Screens.JobsRank import JobsRank
from Screens.EmployersRank import EmployersRank


class Main_application(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.window.frameless = True
        self.page.window.resizable = False
        self.page.window.maximized = True
        self.page.scroll = ScrollMode.AUTO
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.page_go
        self.page.go(route="/Intro")
        self.page.update()


    def route_change(self,e):
        self.Intro_Screen = Intro(page=self.page)

        if self.page.route == "/Intro":
            self.page.views.append(View("/Intro",[self.Intro_Screen],padding=0,appbar=self.Intro_Screen.appbar))
        
        elif self.page.route == "/JobsCV":
            EmployerCVScreen_class = JobsCV(page=self.page)
            self.page.views.append(View("/JobsCV",[EmployerCVScreen_class],padding=0,appbar=EmployerCVScreen_class.appbar,bgcolor="#f6f8f6"))

        elif self.page.route == "/JobsRank":
            adminScreen_class = JobsRank(page=self.page,Results=JobsDataTransmiter.Get_Results(),CVText=JobsDataTransmiter.Get_CVText())
            self.page.views.append(View("/JobsRank",[adminScreen_class],padding=0,appbar=adminScreen_class.appbar,bgcolor="#f6f8f6"))
        
        elif self.page.route == "/EmployersCV":
            JobCVScreen_class = EmployersCV(page=self.page)
            self.page.views.append(View("/EmployersCV",[JobCVScreen_class],padding=0,appbar=JobCVScreen_class.appbar,bgcolor="#f6f8f6"))

        elif self.page.route == "/EmployersRank":
            Client_class = EmployersRank(page=self.page,Results=EmployersDataTransmiter.Get_Results(),path=EmployersDataTransmiter.Get_Path())            
            self.page.views.append(View("/EmployersRank",[Client_class],appbar=Client_class.appbar,padding=0,bgcolor="#f6f8f6"))
        
        self.page.update()
        
    def page_go(self,e):
        self.page.views.pop()
        back_page = self.page.views[-1]
        self.page.go(back_page.route)
        self.page.update()

def main(page:Page):
   page.window.icon = r"icons\cv.ico"
   page.add(Main_application(page=page))
   page.update()
   
app(target=main, assets_dir="assets")