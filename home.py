from flet import *
import sqlite3
con = sqlite3.connect("workers.db",check_same_thread=False)
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS infworker(name TEXT, familyname TEXT, date TEXT, number TEXT, cart TEXT, live TEXT)
""")
con.commit()
def user_view(page:Page):
    page.window.resizable = True
    page.window.maximizable = False
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    return View(
        route="/home",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("الصفحة الرئيسية",color=Colors.AMBER,size=15),
                leading=Icon(Icons.HOME,color=Colors.DEEP_PURPLE),
                actions=[
                    PopupMenuButton(
                        items=[
                            PopupMenuItem("المساعدة",Icon(Icons.HELP),on_click=lambda e:page.go("/hellp")),
                            PopupMenuItem(),
                            PopupMenuItem("اتصل بنا",Icon(Icons.CALL),on_click=call),
                        ],
                    ),  
                ],
            ),
            Row(
                controls=[
                    IconButton(Image(src="asets/imo/count.png",width=120),icon_size=50,on_click=lambda e: page.go("/workadd")),IconButton(Image(src="asets/imo/remove-user.png",width=120),icon_size=50,on_click=lambda e: page.go("/moveworck")),
                ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
             Row([
                 Text("👨‍🌾➕👨‍🌾➕👨‍🌾"),Text("👨‍🌾🚷👨‍🌾🚷👨‍🌾")
             ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,),
            Row(
                controls=[
                    IconButton(Image(src="asets/imo/checkbox (1).png",width=120),icon_size=50,on_click=lambda e: page.go("/present")),IconButton(Image(src="asets/imo/delete-user.png",width=120),icon_size=50,on_click=lambda e: page.go("/absent")),
                ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Row([
                 Text("👨‍🌾✔👨‍🌾✔👨‍🌾"),Text("👨‍🌾❌👨‍🌾❌👨‍🌾")
             ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,),
            Row(
                controls=[
                    IconButton(Image(src="asets/imo/employee_1165769.png",width=120),icon_size=50,on_click=lambda e: page.go("/allworck")),IconButton(Image(src="asets/imo/shopping-cart_1050935.png",width=120),icon_size=50,on_click=lambda e: page.go("/chop")),
                ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Row([
                 Text("👨‍🌾👨‍🌾👨‍🌾👨‍🌾👨‍🌾"),Text("🥩🍅🧅🍇🍞")
             ],expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,),
            
        ],vertical_alignment="center",horizontal_alignment="center",scroll="auto",padding = 0,bgcolor=Colors.WHITE,spacing=15.80
        
    )
