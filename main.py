from flet import *
from views.home import user_view
from views.add_worker import addwoker_view
from views.remove_worker import removeworker_view
from views.absent_workers import absent_view
from views.present_workers import present_view
from views.all_workers import allworker_view
from views.chopeng import chopeng_view
from views.hellp import hellp_view
from views.chopworker import chopwork_view
def main(page:Page):
    page.title = "عامل"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 340
    page.window.height = 660
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window.left = 860
    page.window.top = 1 
    page.window.resizable = True
    page.window.maximizable = False
    page.window.maximizable
    ################################ home page ################################################
    page.add(
        Text("أهلا وسهلا 👋🤝",rtl=True,size=30,color=Colors.GREEN,),
        Image(src="asets/imo/تنزيل (2).jfif",width=500),
        ElevatedButton("دخل مرحبا بيك",icon=Icons.INPUT, rtl=True,on_click=lambda e: page.go("/home"),bgcolor=Colors.RED),
        )
    ###########################################################################################
    ##################### ather page ###########################################################
    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.views.append(user_view(page))
        elif page.route == "/workadd":
            page.views.append(addwoker_view(page))
        elif page.route == "/moveworck":
            page.views.append(removeworker_view(page))
        elif page.route == "/absent":
            page.views.append(absent_view(page))
        elif page.route == "/present":
            page.views.append(present_view(page))
        elif page.route == "/allworck":
            page.views.append(allworker_view(page))
        elif page.route == "/chop":
            page.views.append(chopeng_view(page))
        elif page.route == "/hellp":
            page.views.append(hellp_view(page))
        elif page.route == "/chopwork":
            page.views.append(chopwork_view(page))
        page.update()
    ############################################################################################
    page.on_route_change = route_change
    page.go("/")
    page.update()
app(main)
