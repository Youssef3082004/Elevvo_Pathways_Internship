from flet import * 



class Intro(Container):
    def __init__(self,page:Page):
        super().__init__()
        self.page = page
        self.padding = 40
        self.expand = True
        # self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        # self.page.vertical_alignment = CrossAxisAlignment.CENTER
        self.alignment = alignment.center
        self.Width = self.page.window.width 
        self.Height = self.page.window.height 



        apppbar_Title = Text("Jobs & Resume Ranker",weight=FontWeight.W_500) 
        self.appbar = AppBar(leading=Icon(Icons.DESCRIPTION,size=40,color=Colors.BLUE_500),title=apppbar_Title,bgcolor=Colors.WHITE)

        #! ======================================================= Headline ===================================================
        self.headline = Text(spans=[
            TextSpan(text="Find Your Perfect\n",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=40)),
            TextSpan(text="Match in ",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=40)),
            TextSpan(text="Seconds",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLUE,size=40))
            ])
        self.headlineRow = Row(controls=[Icon(Icons.DESCRIPTION,size=80,color=Colors.BLUE_500),self.headline],alignment=MainAxisAlignment.CENTER)
       
        #! ======================================================= subtitle ===================================================
        self.subtitle = Text("Revolutionize your hiring with our AI driven screeningprocess, Analyze resumes against job descriptions instantly with state of the art AI.",width=self.Width / 2,max_lines=3,text_align=TextAlign.CENTER,
        style=TextStyle(color=Colors.GREY_700,size=20,weight=FontWeight.W_500))
        
        self.subtitleRow = Row(controls=[self.subtitle],alignment=MainAxisAlignment.CENTER)
        #! ======================================================= Badge ===================================================
        self.badge = Container(content=Row(spacing=3,alignment=MainAxisAlignment.CENTER,controls=[
            Icon(Icons.BOLT,color=Colors.BLUE_900),
            Text("POWERED BY ADVANCED AI",style=TextStyle(color=Colors.BLUE_900,size=15,weight=FontWeight.W_500))]
            ),
        padding=5,bgcolor=Colors.with_opacity(color=Colors.BLUE_200,opacity=0.5),border_radius=border_radius.all(25),width=self.page.width / 4.5)
        
        self.badgeRow = Row(controls=[self.badge],alignment=MainAxisAlignment.CENTER)

        #! ======================================================= Buttons ===================================================
        buttonColors = {ControlState.HOVERED: Colors.WHITE,ControlState.DEFAULT: Colors.WHITE}
        buttonbgcolors = {ControlState.HOVERED: Colors.BLUE,ControlState.DEFAULT: Colors.BLUE_900}

        self.matchcv_btn =  ElevatedButton(text="Find Jobs by Uploading Resume",on_click=lambda e:self.add_cldld(),icon=Icons.DOCUMENT_SCANNER, width=self.Width / 4,height=self.Height / 8,style=ButtonStyle(icon_size=30,bgcolor=buttonbgcolors,color=buttonColors,shape=RoundedRectangleBorder(radius=border_radius.all(25))))
        self.matchjobdescription_btn =  ElevatedButton(text="Find Employers by Job Description",on_click=lambda e:self.page.go("/JobCV"),icon=Icons.SEARCH, width=self.Width / 4,height=self.Height / 8,style=ButtonStyle(icon_size=30,bgcolor=buttonbgcolors,color=buttonColors,shape=RoundedRectangleBorder(radius=border_radius.all(25))))

        self.buttonsRow = Row(controls=[self.matchcv_btn,self.matchjobdescription_btn],alignment=MainAxisAlignment.CENTER)
        
        #! ======================================================= Page Controls ===================================================
        self.content = Row(controls=[
            Column(controls=[self.badgeRow,self.headlineRow,self.subtitleRow,self.buttonsRow],expand=True,spacing=30,alignment=MainAxisAlignment.CENTER,horizontal_alignment=alignment.center),
            Image(src=r"assets/image.png",width=500,height=500,border_radius=border_radius.all(25))


        ],alignment=MainAxisAlignment.CENTER)
    


        
    def add_cldld(self):
        self.page.go("/EmployerCV")
        progress_ring_row = Row(controls=[ProgressRing(color=Colors.BLUE),Text(value="Plesae Wait ...",style=TextStyle(weight=FontWeight.W_600))], alignment=MainAxisAlignment.CENTER)
        self.content.controls[0].controls.append(progress_ring_row)            
        self.page.update()
        self.update()