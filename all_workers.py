from flet import *
import sqlite3
####################### data worecers ##########################################
con = sqlite3.connect("workers.db",check_same_thread=False)
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS infworker(name TEXT, familyname TEXT, date TEXT, number TEXT, cart TEXT, live TEXT)
""")
con.commit()
###############################################################################
def allworker_view(page:Page):
    tabel_name = "infworker"
    query = f'SELECT COUNT(*) FROM {tabel_name}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    ############################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM infworker")
        data = c.fetchone()
        if data:
            show()
        else:
            alert=AlertDialog(title=Text("مكاينينش لخدامة",color="red",size=26))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ############################################################
    ######## print all worekers in tireminal ############################
    def show():
        c = con.cursor()
        c.execute("SELECT * FROM infworker")
        worekers = c.fetchall()
        print(worekers)

        if not worekers == "":
            keys = ['name','familyname','date','number','cart','live']
            worekers = [dict(zip(keys,values)) for values in worekers]
            for i in worekers:
                page.add(
                    Card(
                        bgcolor=Colors.BLACK,
                        content=Container(
                            content=Column([
                                Row([
                                    Icon(Icons.PERSON,color=Colors.WHITE),
                                    Text("سمية: ",color=Colors.WHITE,size=18),
                                    Text(i["name"],color=Colors.GREEN,size=14),
                                    Text("لكنية: ",color=Colors.WHITE,size=18),
                                    Text(i["familyname"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                
                                Row([
                                    Icon(Icons.DATE_RANGE,color=Colors.WHITE),
                                    Text("تاريخ لي بدا فيه لخدمة: ",color=Colors.WHITE,size=18),
                                    Text(i["date"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                Row([
                                    Icon(Icons.PHONE,color=Colors.WHITE),
                                    Text("نمرا ديال تيليفون: ",color=Colors.WHITE,size=18),
                                    Text(i["number"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                Row([
                                    Icon(Icons.CARD_TRAVEL,color=Colors.WHITE),
                                    Text("نمرا ديال لكارط ناسيونال: ",color=Colors.WHITE,size=18,selectable=True),
                                    Text(i["cart"],color=Colors.GREEN,size=14,selectable=True),
                                ]
                                ),
                                Row([
                                    Icon(Icons.CARD_TRAVEL,color=Colors.WHITE,),
                                    Text("لبلاصة فين كيعيش: ",color=Colors.WHITE,size=18,),
                                    Text(i["live"],color=Colors.GREEN,size=14,),
                                ]
                                ),
                            ]),rtl=True,
                        )
                    ),
                )
                page.update()
        ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    #####################################################################
    return View(
        route="/allworck",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("لائحة العمال",color=Colors.AMBER,size=15),
                leading=IconButton(Image(src="asets/imo/undo.png",width=20),width=20,on_click=lambda e: page.go("/home")),
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
            Text("كاع لخدامة 👨‍🌾👩‍🌾👩‍🌾👩‍🌾",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/تنزيل (4).png",width=200),
             Row(
                [
                Text("عدد لخدامة: ",size=18,color=Colors.AMBER),
                Text(row_count,size=15,)
                ],alignment=MainAxisAlignment.CENTER,rtl=True,
            ),
            ElevatedButton("شوف كاع لخدامة",rtl=True,bgcolor=Colors.BLUE, icon=Icons.VISIBILITY, on_click=chow_data),
        ],horizontal_alignment="center",scroll="auto",padding = 0,bgcolor=Colors.WHITE,
    )
