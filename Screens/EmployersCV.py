from flet import * 
import winsound
from DataTransmiter import EmployersDataTransmiter
from Employers import Employers
from .Widgets.CustomWidgets import *


class EmployersCV(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.page.padding = 40
        self.padding = 40
        self.expand = True
        self.alignment = alignment.top_center
        
        #! ======================================================= Variables and objects ===================================================
        self.Header = button_functions(self.page)
        self.pick_files_dialog = FilePicker(on_result=self.on_file_picked)
        self.path = None
        self.Width = self.page.window.width 
        self.Height = self.page.window.height

        #! ======================================================= Appbar ===================================================
        exit_button = IconButton(icon=Icons.ARROW_BACK_IOS_ROUNDED,icon_color=Colors.BLUE_500,on_click=lambda e:self.page.go("/Intro"))
        apppbar_Title = Text("Jobs & Resume Ranker",weight=FontWeight.W_500) 
        self.appbar = AppBar(leading=exit_button,title=apppbar_Title,bgcolor=Colors.WHITE,elevation_on_scroll=0,elevation=0,actions=self.Header.Get_Buttons())

        #! ======================================================= Headline ===================================================
        self.headline = Text(spans=[
            TextSpan(text="Screen & Rank Jobs ",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=40)),
            TextSpan(text="Instantly",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLUE,size=40))
            ],text_align=TextAlign.CENTER) 
              
        #! ======================================================= subtitle ===================================================
        self.subtitle = Text("Upload a Resume and Paste the Job Description to Get an Instant Match Score Using our Advanced AI Engine",width=self.Width / 2,max_lines=3,text_align=TextAlign.CENTER,
        style=TextStyle(color=Colors.GREY_700,size=20,weight=FontWeight.W_500))
        
        #! ======================================================= Description Feild ===================================================
        self.clear_btn = TextButton("Clear Text", on_click=lambda _: self.ClearDescription(), style=ButtonStyle(color=Colors.BLUE_600))
        self.description_header_row = Row(
            controls=[
                Row([
                    Container(content=Text("2", color=Colors.WHITE, size=12, weight="bold"),bgcolor=Colors.BLUE_400,border_radius=10,padding=5,width=25,height=25,alignment=alignment.center),
                    Text("Job Description", size=18, weight="bold", color="#1a202c"),
                ]),
                self.clear_btn
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN, 
            width=self.Width - 500 
        )
        
        self.job_description = TextField(height=self.Height * 0.4,counter=Text("0 char",color=Colors.RED,weight=FontWeight.W_600),
            hint_text="Paste the full Job Sescription Here. We'll Analyze Keywords, Skills, and Eequirements to Match Against the Resume...",
            multiline=True,min_lines=15,max_lines=15,border_radius=border_radius.all(25),bgcolor=Colors.WHITE,border_color=Colors.BLUE,border_width=2,
            autocorrect=True,hint_style=TextStyle(weight=FontWeight.W_500,color=Colors.GREY_600,size=15),cursor_color=Colors.BLUE
        )
        self.job_description.on_change = lambda x: self.job_decription_onchange(x)
        
        self.description_Column = Column(controls=[self.description_header_row,self.job_description],expand=True)
        
        #! ======================================================= upload Resume ===================================================
        self.upload_header = Row([Container(content=Text("1", color=Colors.WHITE, size=12, weight="bold"),bgcolor=Colors.BLUE_400,border_radius=10,padding=5,width=25,height=25,alignment=alignment.center),Text("Select Folder Path", size=18, weight="bold", color="#1a202c"),])

        self.uploadContainer = Container(content=Column(controls=[
            Icon(name=Icons.UPLOAD_FILE,color=Colors.BLUE_700,size=50),
            Text(value="Select Folder that have CVs",style=TextStyle(weight=FontWeight.W_700,color=Colors.BLACK,size=30)),
            Text(value="Make Sure the Chosen Folder Contains the Correct Resumes for this Job Description",text_align=TextAlign.CENTER,style=TextStyle(weight=FontWeight.W_500,color=Colors.GREY_600,size=15)),
            
            ],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER),ink=True,on_click= lambda e: self.pick_files_dialog.get_directory_path(dialog_title="Select Folders with CVs"),bgcolor=Colors.WHITE,height=self.Height * 0.4,alignment=alignment.center,border_radius=border_radius.all(25),border=border.all(width=2,color=Colors.BLUE))

        self.upload_column = Column(controls=[self.upload_header,self.uploadContainer],expand=True)

        #! ======================================================= upload Resume ===================================================
        buttonColors = {ControlState.HOVERED: Colors.WHITE,ControlState.DEFAULT: Colors.WHITE,ControlState.DISABLED: Colors.WHITE}
        buttonbgcolors = {ControlState.HOVERED: Colors.BLUE,ControlState.DEFAULT: Colors.BLUE_900,ControlState.DISABLED: Colors.BLUE_900}

        self.findjobs_btn =  ElevatedButton(text="Find Best Match for Job Description",on_click=lambda x:self.SearchEmployers(),icon=Icons.SEARCH, width=self.Width / 4,height=self.Height / 10,style=ButtonStyle(icon_size=30,bgcolor=buttonbgcolors,color=buttonColors,shape=RoundedRectangleBorder(radius=border_radius.all(25))))
        
        #! ======================================================= Page Controls ===================================================
        self.controls = [
            Column([self.headline,self.subtitle],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,spacing=2,expand=True),
            Row([self.upload_column,self.description_Column],alignment=MainAxisAlignment.CENTER,spacing=20,expand=True),
            self.findjobs_btn
        ]
        
        self.main_column = Column(
            controls=[Row(controls=[control],alignment=MainAxisAlignment.CENTER) for control in self.controls],
            expand=True,
            spacing=20,
            alignment=alignment.top_center,
            horizontal_alignment=alignment.top_center,
        )

        self.content = Row(expand=True,controls=[self.main_column],alignment=alignment.top_center)
        self.page.overlay.append(self.pick_files_dialog)


    def SearchEmployers(self):
        if len(self.job_description.value) <= 100:
            self.page.open(CustomSnackbar(Message="Job description is Required! Please Provide a Detailed Job Description before Proceeding",is_error=True))
        elif self.path == None:
            self.page.open(CustomSnackbar(Message="No Folder Selected! Please Choose a Folder that Contains the Resumes to Continue",is_error=True))
        else:
            progress_ring_row = Row(controls=[ProgressRing(color=Colors.BLUE),Text(value="This May Take Several Minutes. Please Wait...",style=TextStyle(weight=FontWeight.W_600))], alignment=MainAxisAlignment.CENTER)
            self.main_column.controls.append(progress_ring_row)
            self.findjobs_btn.disabled = True            
            self.page.update()
            EmployersDataTransmiter.set_Results(Results=Employers.GetTopCVs(job_description=self.job_description.value,path=self.path))
            EmployersDataTransmiter.set_Path(path=self.path)
            self.page.go("/EmployersRank")
    

    def job_decription_onchange(self,e:ControlEvent):
        text = e.control.value
        self.job_description.counter = Text(f"{len(text)}")
        length = len(text)

        if length < 100:
            self.job_description.counter = Text(f"{length} char",color=Colors.RED,weight=FontWeight.W_600)
        elif 100 <= length < 300:
            self.job_description.counter = Text(f"{length} char",color=Colors.AMBER,weight=FontWeight.W_600)
        elif 300 <= length <= 500:
            self.job_description.counter = Text(f"{length} char",color=Colors.BLUE,weight=FontWeight.W_600)
        else:  
            self.job_description.counter = Text(f"{length} char",color=Colors.GREEN,weight=FontWeight.W_600)

        self.job_description.update()
        self.page.update()

    def on_file_picked(self,e: FilePickerResultEvent):
        self.path = e.path
        self.uploadContainer.content.controls[-1].value = f"The Folder Successfully Selected from {self.path}"
        self.uploadContainer.content.controls[-1].color = Colors.GREEN
        self.page.update()
    

    def ClearDescription(self):
        self.job_description.value = ""
        self.job_description.counter = Text(f"{0} char",color=Colors.RED,weight=FontWeight.W_600)
        winsound.MessageBeep()
        self.page.update()