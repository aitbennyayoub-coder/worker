from flet import *
import sqlite3

################! data chop ################################################!
con = sqlite3.connect("chop.db")
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS chopwork(name TEXT,familyname TEXT,purchases TEXT, price TEXT, date TEXT)
""")
con.commit()
#############################################################################!
def chopwork_view(page:Page):
    ################* add data in tabel ##############################################################################################################*
    tabel_name = "chopwork"
    query = f'SELECT COUNT(*) FROM {tabel_name}'
    cor.execute(query)
    def add_chop():
        cor.execute("INSERT INTO chopwork(name,familyname,purchases, price, date) VALUES(?,?,?,?,?)", (name_work.value,family_name_work.value,chpoing.value,much_chop.value,date_chop.value))
        con.commit()
    #################################################################################################################################################*
    ############################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM chopwork")
        data = c.fetchone()
        if data:
            print_chop()
        else:
            alert=AlertDialog(title=Text("ماكين تا تقضيا",color="red",size=30))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ############################################################
    ########? print all worekers in tireminal ###############################################################?
    def print_chop():
        c = con.cursor()
        c.execute("SELECT * FROM chopwork")
        chop = c.fetchall()
        print(chop)
    
        if not chop == "":
            keys = ['name','familyname','purchases','price','date']
            shops = [dict(zip(keys,values)) for values in chop]
            for i in shops:
                page.add(
                    Card(
                        bgcolor=Colors.BLACK,
                        content=Container(
                            content=Column([
                                Row([
                                    Text("سمية: ",color=Colors.WHITE,size=18),
                                    Text(i["name"],color=Colors.GREEN,size=14),
                                    Text("لكنية: ",color=Colors.WHITE,size=18),
                                    Text(i["familyname"],color=Colors.GREEN,size=14),
                                ]
                                ),
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
    def on_click():
        if not name_work.value or name_work.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت سمية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not family_name_work.value or family_name_work.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت لكنية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not chpoing.value or chpoing.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تقضيا خاوية",color="red",size=16))
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
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    page.window.resizable=True
    page.window.maximizable=False
    name_work = TextField(label="سمية ديال لخدام")
    family_name_work = TextField(label="لكنية ديال لخدام")
    chpoing = TextField(label="داكشي لي شريتي ليه")
    much_chop = TextField(label="ثامان باش شريتيه")
    date_chop = TextField(label="تاريخ فاش شريتيه")
    return View(
        route="/chopwork",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("تقضيا ديال كل واحد",color=Colors.AMBER,size=18),
                leading=IconButton(Image(src="asets/imo/undo.png",width=20),width=20,on_click=lambda e: page.go("/chop")),
                actions=[
                    PopupMenuButton(
                        items=[
                            PopupMenuItem("المساعدة",Icon(Icons.HELP),on_click=lambda e:page.go("/hellp")),
                            PopupMenuItem(),
                            PopupMenuItem("اتصل بنا",Icon(Icons.CALL),on_click=call),
                        ]
                    )
                ]
            ),
                name_work,family_name_work,chpoing,much_chop,date_chop,
                Row([
                    ElevatedButton("زيدو فلائحة",rtl=True,icon=Icons.ADD,bgcolor=Colors.BLUE, on_click=on_click),
                    ElevatedButton("شوف لائحة",rtl=True,icon=Icons.LIST_ALT,bgcolor=Colors.BLUE, on_click=chow_data),
                ])
        ],vertical_alignment="center",horizontal_alignment="center",scroll="auto",padding = 0,bgcolor=Colors.WHITE,spacing=35
    )
    
