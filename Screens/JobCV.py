from flet import * 



class JobCV(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.padding = 40
        self.expand = True
        self.alignment = alignment.top_center
        self.Width = self.page.window.width 
        self.Height = self.page.window.height 
        self.page.padding = 40

        
        self.pick_files_dialog = FilePicker(on_result=self.on_file_picked)


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
        
        self.job_description = TextField(height=self.Height * 0.4,
            hint_text="Paste the full job description here. We'll analyze keywords, skills, and requirements to match against the resume...",
            multiline=True,min_lines=15,max_lines=15,border_radius=border_radius.all(25),bgcolor=Colors.WHITE,border_color=Colors.BLUE,border_width=2,
            autocorrect=True,hint_style=TextStyle(weight=FontWeight.W_500,color=Colors.GREY_600,size=15),cursor_color=Colors.BLUE
                                        )
        
        self.description_Column = Column(controls=[self.description_header_row,self.job_description],expand=True)
        
        #! ======================================================= upload Resume ===================================================
        self.upload_header = Row([Container(content=Text("1", color=Colors.WHITE, size=12, weight="bold"),bgcolor=Colors.BLUE_400,border_radius=10,padding=5,width=25,height=25,alignment=alignment.center),Text("Select Folder Path", size=18, weight="bold", color="#1a202c"),])

        uploadContainer = Container(content=Column(controls=[
            Icon(name=Icons.UPLOAD_FILE,color=Colors.BLUE_700,size=50),
            Text(value="Select Folder that have CVs",style=TextStyle(weight=FontWeight.W_700,color=Colors.BLACK,size=30)),
            Text(value="Make sure the folder is the desired for this job description",style=TextStyle(weight=FontWeight.W_500,color=Colors.GREY_600,size=15)),
            
            ],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER),ink=True,on_click= lambda e: self.pick_files_dialog.get_directory_path(dialog_title="Select Folders with CVs"),bgcolor=Colors.WHITE,height=self.Height * 0.4,alignment=alignment.center,border_radius=border_radius.all(25),border=border.all(width=2,color=Colors.BLUE))

        self.upload_column = Column(controls=[self.upload_header,uploadContainer],expand=True)
        #! ======================================================= upload Resume ===================================================
        buttonColors = {ControlState.HOVERED: Colors.WHITE,ControlState.DEFAULT: Colors.WHITE}
        buttonbgcolors = {ControlState.HOVERED: Colors.BLUE,ControlState.DEFAULT: Colors.BLUE_900}

        self.findjobs_btn =  ElevatedButton(text="Find Best Match for Job Description",on_click=lambda x:self.add_cldld(),icon=Icons.SEARCH, width=self.Width / 4,height=self.Height / 10,style=ButtonStyle(icon_size=30,bgcolor=buttonbgcolors,color=buttonColors,shape=RoundedRectangleBorder(radius=border_radius.all(25))))
        
        #! ======================================================= Page Controls ===================================================
        self.controls = [
            Column([self.headline,self.subtitle],alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,spacing=2,expand=True),
            Row([self.upload_column,self.description_Column],alignment=MainAxisAlignment.CENTER,spacing=20,expand=True),
            self.findjobs_btn
        ]
        
        self.main_column = Column(
            controls=[Row(controls=[control],alignment=MainAxisAlignment.CENTER) for control in self.controls],
            expand=True,
            spacing=30,
            alignment=alignment.top_center,
            horizontal_alignment=alignment.top_center,
        )

        self.content = Row(expand=True,controls=[self.main_column],alignment=alignment.top_center)
        self.page.overlay.append(self.pick_files_dialog)

    


    def add_cldld(self):
        progress_ring_row = Row(controls=[ProgressRing(color=Colors.BLUE),Text(value="Plesae Wait ...",style=TextStyle(weight=FontWeight.W_600))], alignment=MainAxisAlignment.CENTER)
        self.main_column.controls.append(progress_ring_row)            
        self.page.update()
        self.update()
    

    def on_file_picked(self,e: FilePickerResultEvent):
        print(e.path)

