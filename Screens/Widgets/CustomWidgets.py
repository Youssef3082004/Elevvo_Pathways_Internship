from flet import *

class CustomTooltip(Tooltip):
    def __init__(self,text:str,color:Colors):
        super().__init__(message=text)
        self.message = text
        self.padding= padding.all(10)
        self.border_radius = 10
        self.exit_duration = Duration(microseconds=300)
        self.text_style=TextStyle(size=12, color=Colors.WHITE, weight=FontWeight.W_600)
        self.bgcolor = color


class button_functions():
    def __init__(self,page:Page):
        self.page = page

    def _close_window(self):
        self.page.window.close()
        self.page.update()
    
    def _minimize_window(self):
        self.page.window.minimized = True 
        self.page.update()
    
    def _maxmize_window(self):
        self.page.window.center()
        self.page.window.maximized = not self.page.window.maximized
        self.page.update()
    
    def Get_Buttons(self) -> list[IconButton]:
        self.close_button = IconButton(icon=Icons.CLOSE,icon_color=Colors.BLUE_500,icon_size=30,on_click=lambda e: self._close_window())
        self.maxmize_button = IconButton(icon=Icons.SQUARE_OUTLINED,icon_color=Colors.BLUE_500,on_click=lambda e: self._maxmize_window())
        self.minimize_button = IconButton(icon=Icons.MINIMIZE_ROUNDED,icon_color=Colors.BLUE_500,icon_size=30,on_click=lambda e: self._minimize_window())  
        return [self.minimize_button,self.maxmize_button,self.close_button]


class CustomSnackbar(SnackBar):
    def __init__(self,Message: str, is_error: bool,bgColor:Colors = Colors.GREY_900):
        icon = Icon(Icons.ERROR, color=Colors.RED_600) if is_error else Icon(Icons.CHECK_CIRCLE, color=Colors.GREEN_600)
        snackbar_text = Text(Message,rtl=False,style=TextStyle(size=15, weight=FontWeight.W_500, color=Colors.WHITE))
        content_row = Row(controls=[snackbar_text],rtl=False)
        super().__init__(content=Row(rtl=False,alignment=MainAxisAlignment.START,controls=[icon,content_row]))
        self.show_close_icon = True
        self.close_icon_color = Colors.WHITE
        self.rtl = False
        self.bgcolor = bgColor
        self.duration = 10000