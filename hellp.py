from flet import *
def hellp_view(page:Page):
    page.window.resizable=True
    page.window.maximizable=False
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    return View(
        route="/hellp",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("المساعدة",color=Colors.AMBER),
                leading=IconButton(Image(src="asets/imo/undo.png",width=20),width=20,on_click=lambda e: page.go("/home")),
                actions=[
                    PopupMenuButton(
                        items=[
                            PopupMenuItem("اتصل بنا",Icon(Icons.CALL),on_click=call),
                        ]
                    )
                ]
            ),
            Row([
                Image(src="asets/imo/count.png",width=40),Text("هذي غتعاونك الى بغيتي تزيد لخدامة برك عليه\n أودخل لمعلومات ديالهم",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
            Row([
                Image(src="asets/imo/remove-user.png",width=40),Text("هذي غتعاونك الى بغيتي تحبس شي خدام من \nلخدمة",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
            Row([
                Image(src="asets/imo/checkbox (1).png",width=40),Text("هذي غتعاونك باش تسجل لخدامة لي حاضرين",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
            Row([
                Image(src="asets/imo/delete-user.png",width=40),Text("هذي غتعاونك باش تسجل لخدامة لي غيبين",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
            Row([
                Image(src="asets/imo/employee_1165769.png",width=40),Text("هذي غتعاونك باش تعرف لمجموع ديال لخدامة \nلي كاينين",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
            Row([
                Image(src="asets/imo/shopping-cart_1050935.png",width=40),Text("هذي غتعاونك الى بغيتي تسجل تقضيا لي \nشريتي",color=Colors.BLACK,size=14)
            ],rtl=True,scroll="auto"),
        ],vertical_alignment="center",horizontal_alignment="center",scroll="auto",padding = 0,bgcolor=Colors.WHITE,spacing=35
    )
    
