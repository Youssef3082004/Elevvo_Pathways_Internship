from flet import *
import winsound
import os
from .Widgets.CustomWidgets import *


class EmployersRank(Container):
    def __init__(self, page: Page, Results: list[tuple[str,float]],path:str):
        super().__init__()
        self.page = page
        self.Results = Results
        self.path = path 
        self.page.padding = 20
        self.padding = 20
        self.expand = True
        self.alignment = alignment.top_center

        #! ======================================================= Variables and objects ===================================================
        self.Header = button_functions(self.page)
        self.Width = self.page.window.width 
        self.Height = self.page.window.height

        #! ======================================================= Appbar ===================================================
        exit_button = IconButton(icon=Icons.ARROW_BACK_IOS_ROUNDED, icon_color=Colors.BLUE_500, on_click=lambda e: self.page.go(self.page.views[-2].route))
        apppbar_Title = Text("Jobs & Resume Ranker", weight=FontWeight.W_500) 
        self.appbar = AppBar(leading=exit_button, title=apppbar_Title, bgcolor=Colors.WHITE,elevation_on_scroll=0,actions=self.Header.Get_Buttons())

        #! ======================================================= Helper Function ===================================================
        def get_score_color(score):
            """Returns a color based on the match percentage for consistency."""
            if score >= 75.0:
                return Colors.GREEN_600
            elif score >= 60.0:
                return Colors.ORANGE_500
            else:
                return Colors.RED_500

        #! ======================================================= Headline & Header ===================================================
        self.headline = Text(spans=[
            TextSpan(text="Ranked Resumes Based on ", style=TextStyle(weight=FontWeight.BOLD, color=Colors.BLACK, size=40)),
            TextSpan(text="Job Description", style=TextStyle(weight=FontWeight.BOLD, color=Colors.BLUE, size=40))
            ], text_align=TextAlign.CENTER)      
        
        self.section_header = Row([
            Container(content=Text("1", color=Colors.WHITE, size=12, weight="bold"), bgcolor=Colors.BLUE_400, border_radius=10, padding=5, width=25, height=25, alignment=alignment.center),
            Text("Top Resume Match", size=18, weight="bold", color="#1a202c"),
        ], alignment=MainAxisAlignment.CENTER)

        #! ======================================================= Results Data Logic ===================================================
        top_match_filename, top_match_score = self.Results[0]
        other_matches = self.Results[1:]

        #! ======================================================= Top Match UI ===================================================
        self.top_match_card = Container(
            width=self.Width * 0.6, 
            content=Column([
                Row([
                    Text("Top Match", size=20, weight=FontWeight.BOLD, color=Colors.WHITE),
                    Icon(Icons.STAR, color=Colors.AMBER_400, size=30),
                ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                
                Row([
                    IconButton(tooltip=CustomTooltip(text=f"Click to view full {top_match_filename} resume",color=Colors.AMBER_400),icon=Icons.PICTURE_AS_PDF,icon_color=Colors.WHITE,icon_size=50,on_click=lambda x: os.startfile(f"{path}/{top_match_filename}")),
                    Text(f"{top_match_filename}", style=TextStyle(weight=FontWeight.BOLD, color=Colors.WHITE, size=28))
                ], alignment=MainAxisAlignment.START, spacing=15),
                
                Divider(color=Colors.WHITE24),
                
                Row([
                    Icon(Icons.CHECK_CIRCLE_OUTLINE, color=Colors.WHITE70, size=16),
                    Text("Highly recommended for review", color=Colors.WHITE),
                ]),
                
                # Match Score Badge
                Container(
                    content=Text(f"{top_match_score:.1f}% Match", weight=FontWeight.BOLD, color=Colors.BLUE_900),
                    bgcolor=Colors.AMBER_400,
                    padding=padding.symmetric(horizontal=12, vertical=6),
                    border_radius=20,
                    margin=margin.only(top=10)
                )
            ]),
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=[Colors.BLUE_700, Colors.BLUE_900],
            ),
            padding=20,
            border_radius=15,
            shadow=BoxShadow(blur_radius=10, color=Colors.BLACK26, offset=Offset(0, 5))
        )

        #! ======================================================= Other Choices UI ===================================================
        self.other_choices_list = Column(spacing=10)
        
        for index, (filename, score) in enumerate(other_matches):
            self.other_choices_list.controls.append(
                Card(
                    elevation=2,
                    content=Container(
                        width=self.Width * 0.6, 
                        padding=15,
                        content=ListTile(
                            leading = IconButton(tooltip=CustomTooltip(text=f"Click to view full {filename} resume",color=get_score_color(score=score)),icon=Icons.PICTURE_AS_PDF,icon_color=get_score_color(score=score),icon_size=35,on_click=lambda e, f=filename: os.startfile(f"{path}/{f}")),
                            title=Text(filename, style=TextStyle(weight=FontWeight.BOLD, color=Colors.BLACK87, size=18)),
                            subtitle=Text(f"Rank #{index + 2}", size=12, color=Colors.GREY_500,weight=FontWeight.W_500),
                            
                            trailing=Container(
                                content=Text(f"{score:.1f}%", weight=FontWeight.BOLD, color=Colors.WHITE),
                                bgcolor=get_score_color(score),
                                padding=padding.symmetric(horizontal=10, vertical=5),
                                border_radius=10
                            )
                        )
                    )
                )
            )

        #! ======================================================= Page Controls ===================================================
        self.controls = [
            self.headline,
            self.section_header,
            self.top_match_card,
            Container(height=10),
            Text(f"Other {len(other_matches)} Candidates", size=18, weight=FontWeight.BOLD, color=Colors.BLUE_GREY_800),
            self.other_choices_list
        ]

        self.main_column = Column(
            controls=[Row(controls=[control], alignment=MainAxisAlignment.CENTER) for control in self.controls],
            expand=True,
            spacing=20,
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll=ScrollMode.AUTO 
        )

        self.content = Row(expand=True, controls=[self.main_column], alignment=MainAxisAlignment.CENTER)
        winsound.MessageBeep()