from flet import * 
import pandas as pd
import webbrowser
from Employer import Employer
import re

class EmployerRank(Container):
    def __init__(self, page: Page, Results: pd.DataFrame = None,CVText:str = None):
        super().__init__()
        self.page = page
        self.Results = Results
        self.CVText = CVText
        self.padding = 20
        self.expand = True
        self.alignment = alignment.top_center
        self.Width = self.page.window.width 
        self.Height = self.page.window.height 
        self.page.padding  = 20

        exit_button = IconButton(icon=Icons.ARROW_BACK_IOS_ROUNDED,icon_color=Colors.BLUE_500,on_click=lambda e:self.page.go(f"{self.page.views[-2].route}"))
        apppbar_Title = Text("Jobs & Resume Ranker", weight=FontWeight.W_500) 
        self.appbar = AppBar(leading=exit_button, title=apppbar_Title, bgcolor=Colors.WHITE)

        #! ======================================================= Headline ===================================================
        self.headline = Text(spans=[
            TextSpan(text="Ranked Jobs Based on your ", style=TextStyle(weight=FontWeight.BOLD, color=Colors.BLACK, size=40)),
            TextSpan(text="Resume", style=TextStyle(weight=FontWeight.BOLD, color=Colors.BLUE, size=40))
            ], text_align=TextAlign.CENTER)      
        
        #! ======================================================= Results Data Logic ===================================================
        top_match = self.Results.iloc[0]
        other_matches = self.Results.iloc[1:]

        #! ======================================================= Top Match UI ===================================================
        self.top_match_card = Container(
            width=self.Width * 0.6, # Keeps it nicely centered and responsive
            content=Column([
                Row([
                    Icon(Icons.STAR, color=Colors.AMBER_400, size=30),
                    Text("Top Match", size=20, weight=FontWeight.BOLD, color=Colors.WHITE),
                ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                
                Text(spans=[
                TextSpan(text=f"{top_match['Job Title']} in ",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=24)),
                TextSpan(text=f"{top_match['Company']}",style=TextStyle(weight=FontWeight.BOLD,color=Colors.WHITE,size=24))
                ],text_align=TextAlign.LEFT),
                Row([
                   IconButton(icon=Icons.LOCATION_ON,icon_color=Colors.WHITE,on_click= lambda e:webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={top_match["latitude"]},{top_match["longitude"]}")), 
                   Text(f"{top_match['location']}, {top_match['Country']}", size=14, color=Colors.WHITE70),
                ],spacing=2),
                

                
                Divider(color=Colors.WHITE24),
                
                Row([
                    Icon(Icons.WORK_OUTLINE, color=Colors.WHITE70, size=16),
                    Text(f"Salary: {top_match['Salary Range']}", color=Colors.WHITE),
                ]),
                Row([
                    Icon(Icons.LOCATION_CITY, color=Colors.WHITE70, size=16),
                    Text(f"Company Size: {top_match['Company Size']}", color=Colors.WHITE),
                ]),
                Row(controls = [
                Icon(Icons.CALL, color=Colors.WHITE70, size=16),
                Text(f"{top_match['Contact Person']}:{top_match['Contact']}", size=14, color=Colors.WHITE70),
                ]),
                
                Text(top_match['Job Description'], size=14, color=Colors.WHITE, max_lines=3, overflow=TextOverflow.ELLIPSIS),
                
                Row([ 
                Container(content=Text(f"{skill}", weight=FontWeight.BOLD, color=Colors.BLUE_700),
                            bgcolor=Colors.BLUE_100,
                            padding=padding.symmetric(horizontal=10, vertical=5),
                            border_radius=10
                            ) for skill in Employer.extract_skills(text=self.CVText,knowsSkills=re.findall(pattern=r"\b[A-Z]+[a-z]*(?:\s+[a-z]+)*",string=top_match["skills"]))]),
                            

                
                # Match Score Badge
                Container(
                    content=Text(f"{top_match['Match_Score']:.1f}% Match", weight=FontWeight.BOLD, color=Colors.BLUE_900),
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
        
        for index, row in other_matches.iterrows():
            self.other_choices_list.controls.append(
                Card(
                    elevation=2,
                    content=Container(
                        width=self.Width * 0.6, 
                        padding=15,
                        content=ListTile(
                            leading=IconButton(icon=Icons.LOCATION_ON,icon_color=Colors.BLUE_GREY_800,icon_size=30 ,on_click= lambda e:webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={row["latitude"]},{row["longitude"]}")),
                            title= Text(spans=[
                                    TextSpan(text=f"{row['Job Title']} in ",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLACK,size=24)),
                                    TextSpan(text=f"{row['Company']}",style=TextStyle(weight=FontWeight.BOLD,color=Colors.BLUE,size=24))
                                    ],text_align=TextAlign.LEFT),
                            subtitle=Column(controls=[
                                Text(f"{row['location']}, {row['Country']} • {row['Salary Range']}", weight=FontWeight.W_600,size=12, color=Colors.BLACK45),
                                Text(f"{row['Contact Person']}: {row['Contact']}", size=14, color=Colors.GREY_600),
                                Text(row['Job Description'], size=12, max_lines=1, overflow=TextOverflow.ELLIPSIS, color=Colors.GREY_500),
                                 Row([ 
                                    Container(content=Text(f"{skill}", weight=FontWeight.BOLD, color=Colors.BLUE_700),
                                                bgcolor=Colors.BLUE_100,
                                                padding=padding.symmetric(horizontal=10, vertical=5),
                                                border_radius=10
                                                ) for skill in Employer.extract_skills(text=self.CVText,knowsSkills=re.findall(pattern=r"\b[A-Z]+[a-z]*(?:\s+[a-z]+)*",string=row["skills"]))]),
                                    
                            ], spacing=5),
                            trailing=Container(
                                content=Text(f"{row['Match_Score']:.1f}%", weight=FontWeight.BOLD, color=Colors.BLUE_700),
                                bgcolor=Colors.BLUE_50,
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
            self.top_match_card,
            Container(height=10), # Spacer
            Text(f"Other {len(other_matches)} Matches", size=18, weight=FontWeight.BOLD, color=Colors.BLUE_GREY_800),
            self.other_choices_list
        ]

        # Your original layout wrappers
        self.main_column = Column(
            controls=[Row(controls=[control], alignment=MainAxisAlignment.CENTER) for control in self.controls],
            expand=True,
            spacing=20,
            alignment=MainAxisAlignment.START, # Changed to START so it scrolls naturally
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll=ScrollMode.AUTO # Added scroll so the list doesn't get cut off
        )

        self.content = Row(expand=True, controls=[self.main_column], alignment=MainAxisAlignment.CENTER)

