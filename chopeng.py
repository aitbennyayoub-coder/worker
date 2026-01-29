from flet import *
import sqlite3

################! data chop ################################################!
con = sqlite3.connect("chop.db")
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS l3chra(purchases TEXT, price TEXT, date TEXT)
""")
con.commit()
#############################################################################!
def chopeng_view(page:Page):
    ################* add data in tabel ##############################################################################################################*
    tabel_name = "l3chra"
    query = f'SELECT COUNT(*) FROM {tabel_name}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    def add_chop():
        cor.execute("INSERT INTO l3chra(purchases, price, date) VALUES(?,?,?)", (object_chop.value,much_chop.value,date_chop.value))
        con.commit()
    #################################################################################################################################################*
    def on_click():
        if not object_chop.value or object_chop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تقديا خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not much_chop.value or much_chop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تامان خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not date_chop.value or date_chop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تاريخ خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        page.update()

        add_chop()
    ############################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM l3chra")
        data = c.fetchone()
        if data:
            print_chop()
        else:
            alert=AlertDialog(title=Text("مكاين تا تقضيا",color="red",size=30))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ############################################################
    ########? print all worekers in tireminal ###############################################################?
    def print_chop():
        c = con.cursor()
        c.execute("SELECT * FROM l3chra")
        chop = c.fetchall()
        print(chop)
    
        if not chop == "":
            keys = ['purchases','price','date']
            shops = [dict(zip(keys,values)) for values in chop]
            for i in shops:
                page.add(
                    Card(
                        bgcolor=Colors.BLACK,
                        content=Container(
                            content=Column([
                                Row([
                                    Text("تقضيا: ",color=Colors.WHITE,size=18),
                                    Text(i["purchases"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                Row([
                                    Text("ثمنها: ",color=Colors.WHITE,size=18),
                                    Text(i["price"],color=Colors.GREEN,size=14),
                                ]),
                                Row([
                                    Text("تاريخ لي تشرات فيه: ",color=Colors.WHITE,size=18),
                                    Text(i["date"],color=Colors.GREEN,size=14),
                                ]),
                            ]),rtl=True
                        )
                    )
                )
    ####################################################################################################################################?
    object_chop = TextField(label="لحوايج لي شريتي",width=200,)
    much_chop =TextField(label="ثمن ديالها",width=200,prefix="درهم ")
    date_chop = TextField(label="تاريخ لي تشرات فيه",width=200,)
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    ################################# page view #####################################################################################################
    return View(
        route="/chop",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("صفحة المشتريات",color=Colors.AMBER,size=15),
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
            Text("العشرة 🍅🥔🍏🧅",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/chop.jfif",width=200),
            ElevatedButton("تقديا ديال كل واحد بوحدو",color=Colors.BLACK,bgcolor=Colors.AMBER_100,on_click=lambda e: page.go("/chopwork")),
            Row([
            Text("عدد لحوايج لي شريتي: ",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Text(row_count,rtl=True,size=14,color=Colors.BLACK,)
            ],alignment=MainAxisAlignment.CENTER,rtl=True,),
            object_chop,much_chop,date_chop,
                Row([
                    ElevatedButton("اضافة الى القائمة",rtl=True,icon=Icons.ADD,bgcolor=Colors.BLUE, on_click=on_click),
                    ElevatedButton("عرض القئمة",rtl=True,icon=Icons.LIST_ALT,bgcolor=Colors.BLUE, on_click=chow_data),
                ])
        ],horizontal_alignment="center",padding = 0,bgcolor=Colors.WHITE,rtl=True,scroll="auto"
    )
    ######################################################################################################################################
