from flet import * 
from Employer import Employer
from DataTransmiter import DataTransmiter

class EmployerCV(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.padding = 20
        self.expand = True
        self.alignment = alignment.top_center
        self.Width = self.page.window.width 
        self.Height = self.page.window.height 
        self.page.padding  = 20
        self.pick_files_dialog = FilePicker(on_result=self.on_file_picked)
        self.path = None

        self.emplower = Employer()

        apppbar_Title = Text("Jobs & Resume Ranker",weight=FontWeight.W_500) 
        self.appbar = AppBar(leading=Icon(Icons.DESCRIPTION,size=40,color=Colors.BLUE_500),title=apppbar_Title,bgcolor=Colors.WHITE)

        #! ======================================================= Headline ===================================================
        self.headline = Text(spans=[
            TextSpan(text="Screen & Rank Jobs ",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=40)),
            TextSpan(text="Instantly",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLUE,size=40))
            ],text_align=TextAlign.CENTER)       
        #! ======================================================= subtitle ===================================================
        self.subtitle = Text("Upload a resume and paste the job description to get an instant match score using our advanced AI engine.",width=self.Width / 2,max_lines=3,text_align=TextAlign.CENTER,
        style=TextStyle(color=Colors.GREY_700,size=20,weight=FontWeight.W_500))

        
        #! ======================================================= Description Feild ===================================================
        self.clear_btn = TextButton("Clear Text", on_click=lambda _: print("Clear"), style=ButtonStyle(color=Colors.BLUE_600))
        self.description_header_row = Row([
                    Container(content=Text("1", color=Colors.WHITE, size=12, weight="bold"),bgcolor=Colors.BLUE_400,border_radius=10,padding=5,width=25,height=25,alignment=alignment.center),
                    Text("Filtering Search", size=18, weight="bold", color="#1a202c"),
                ],alignment=MainAxisAlignment.CENTER)
        

        Qualifications_options = [dropdown.Option(text=job,key=job) for job in self.emplower.Get_Qualifications()]
        self.Qualifications_input = Dropdown(width=250,autofocus=False,label="Qualifications",label_style=TextStyle(color=Colors.BLUE,weight=FontWeight.W_600),border_radius=BorderRadius(10,10,10,10),border_width=1,max_menu_height=30,color ="#36618e",text_style=TextStyle(weight=FontWeight.W_500),options=Qualifications_options)
        
        Worktype_options = [dropdown.Option(text=job,key=job) for job in self.emplower.Get_WorkTypes()]
        self.Worktype_input = Dropdown(width=250,autofocus=False,label="Work Type",label_style=TextStyle(color=Colors.BLUE,weight=FontWeight.W_600),border_radius=BorderRadius(10,10,10,10),border_width=1,max_menu_height=30,color ="#36618e",text_style=TextStyle(weight=FontWeight.W_500),options=Worktype_options)
        
        Gender_options = [dropdown.Option(text=job,key=job) for job in ["Male","Female"]]
        self.Gender_input = Dropdown(width=250,autofocus=False,label="Gender",label_style=TextStyle(color=Colors.BLUE,weight=FontWeight.W_600),border_radius=BorderRadius(10,10,10,10),border_width=1,max_menu_height=30,color ="#36618e",text_style=TextStyle(weight=FontWeight.W_500),options=Gender_options)
        
        self.description_Column = Column(controls=[self.description_header_row,Row(controls=[self.Qualifications_input,self.Worktype_input,self.Gender_input],alignment=MainAxisAlignment.CENTER)],expand=True,spacing=20,horizontal_alignment=CrossAxisAlignment.CENTER)
        
        
        #! ======================================================= upload Resume ===================================================
        self.upload_header = Row([Container(content=Text("2", color=Colors.WHITE, size=12, weight="bold"),bgcolor=Colors.BLUE_400,border_radius=10,padding=5,width=25,height=25,alignment=alignment.center),Text("Upload Resume", size=18, weight="bold", color="#1a202c"),],alignment=MainAxisAlignment.CENTER)

        self.uploadContainer = Container(content=Column(expand=True,controls=[
            Icon(name=Icons.UPLOAD_FILE,color=Colors.BLUE_700,size=50),
            Text(value="Click to Upload your Resume",style=TextStyle(weight=FontWeight.W_700,color=Colors.BLACK,size=30)),
            Text(value="Supported formats: .pdf, .docx, .txt",style=TextStyle(weight=FontWeight.W_500,color=Colors.GREY_600,size=15)),
            
            ],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER),expand=True,ink=True,on_click= lambda x:self.pick_files_dialog.pick_files(dialog_title="Uploud Your Resume",allow_multiple=False),bgcolor=Colors.WHITE,width=self.Width - 300,height=self.Height * 0.3,alignment=alignment.center,border_radius=border_radius.all(25),border=border.all(width=2,color=Colors.BLUE))
        self.upload_column = Column(controls=[self.upload_header,self.uploadContainer],expand=True,horizontal_alignment=CrossAxisAlignment.CENTER)

        #! ======================================================= upload Resume ===================================================
        buttonColors = {ControlState.HOVERED: Colors.WHITE,ControlState.DEFAULT: Colors.WHITE,ControlState.DISABLED: Colors.WHITE}
        buttonbgcolors = {ControlState.HOVERED: Colors.BLUE,ControlState.DEFAULT: Colors.BLUE_900,ControlState.DISABLED: Colors.BLUE_900}

        self.findjobs_btn =  ElevatedButton(on_click=lambda e:self.add_cldld(),text="Find Jobs Based on your Resume",icon=Icons.SEARCH, width=self.Width / 4,height=self.Height / 10,style=ButtonStyle(icon_size=30,bgcolor=buttonbgcolors,color=buttonColors,shape=RoundedRectangleBorder(radius=border_radius.all(25))))
        #! ======================================================= Page Controls ===================================================
        self.controls = [
            Column([self.headline,self.subtitle],expand=True,alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,spacing=2),    
            self.description_Column,

            self.upload_column,
            self.findjobs_btn
        ]


        self.main_column = Column(
            controls=[Row(controls=[control],alignment=MainAxisAlignment.CENTER) for control in self.controls],
            expand=True,
            spacing=20,
            alignment=alignment.top_center,
            horizontal_alignment=alignment.top_center,
        )

        self.content = Row(expand=True,controls=[self.main_column], alignment=alignment.top_center)
        self.page.overlay.append(self.pick_files_dialog)





    
    def add_cldld(self):
        progress_ring_row = Row(controls=[ProgressRing(color=Colors.BLUE),Text(value="This may take several minutes. Please wait...",style=TextStyle(weight=FontWeight.W_600))], alignment=MainAxisAlignment.CENTER)
        self.main_column.controls.append(progress_ring_row)
        self.findjobs_btn.disabled = True
        self.page.update()

        description = self.emplower.Read_CV(path=self.path)
        DataTransmiter.set_Results(Results=self.emplower.GetTopJobs(Employer_Desc=description,Qualifications=self.Qualifications_input.value,Work_type=self.Worktype_input.value,Gender=self.Gender_input.value))
        DataTransmiter.set_CVText(cv=description)
        self.page.go("/EmployerRank")
        self.page.update()

    

    def on_file_picked(self,e: FilePickerResultEvent):
        self.path = e.files[0].path
        self.uploadContainer.content.controls[-1].value = f"The Resume Successfully uploaded from {self.path}"
        self.uploadContainer.content.controls[-1].color = Colors.GREEN
        self.page.update()
