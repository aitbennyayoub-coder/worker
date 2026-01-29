from flet import *
import sqlite3
con = sqlite3.connect("workers.db",check_same_thread=False)
cor=con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS prisent(name TEXT, familyname TEXT, date TEXT)
""")
con.commit()

def present_view(page:Page):
    def on_click():
        if not name_wrk.value or name_wrk.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت سمية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not family_name_werk.value or family_name_werk.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت لكنية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not date.value or date.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تاريخ خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        page.update()

        add_data()
    #################### add data in tabel ################################################################################################
    tabel = "prisent"
    query = f'SELECT COUNT(*) FROM {tabel}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    def add_data():
        cor.execute("INSERT INTO prisent(name, familyname, date) VALUES(?,?,?)", (name_wrk.value, family_name_werk.value,date.value))
        con.commit()
    ###########################################################################################################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM prisent")
        data = c.fetchone()
        if data:
            print_chop()
        else:
            alert=AlertDialog(title=Text("مكاين تا واحد",color="red",size=30))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ########? print all worekers in tireminal ###############################################################?
    def print_chop():
        c = con.cursor()
        c.execute("SELECT * FROM prisent")
        chop = c.fetchall()
        print(chop)

        if not chop == "":
            keys = ['name','familyname','date']
            shops = [dict(zip(keys,values)) for values in chop]
            for i in shops:
                page.add(
                    Card(
                        bgcolor=Colors.BLACK,
                        content=Container(
                            content=Column([
                                Row([
                                    Text("سمية: " ,color=Colors.WHITE,size=18),
                                    Text(i["name"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                Row([
                                    Text("لكنية: ",color=Colors.WHITE,size=18),
                                    Text(i["familyname"],color=Colors.GREEN,size=14),
                                ]),
                                Row([
                                    Text("تاريخ الحضور: ",color=Colors.WHITE,size=18),
                                    Text(i["date"],color=Colors.GREEN,size=14),
                                ]),
                            ]),rtl=True
                        )
                    )
                )
    ####################################################################################################################################?
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    name_wrk = TextField(label="سمية",width=200,)
    family_name_werk =TextField(label="لكنية",width=200,)
    date = TextField(label="تاريخ",width=200,)
    return View(
        route="/present",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("صفحة الحضور",color=Colors.AMBER,size=15),
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
            Text("حضور العمال ✔",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/images (2).png",width=200),
            name_wrk,family_name_werk,date,
            ElevatedButton("حاضر",rtl=True,icon=Icons.CO_PRESENT,bgcolor=Colors.BLUE, on_click=on_click),
            ElevatedButton("شوف لائحة",rtl=True,bgcolor=Colors.BLUE, icon=Icons.VISIBILITY, on_click=chow_data),
        ],horizontal_alignment="center",padding = 0,bgcolor=Colors.WHITE,scroll="auto"
    )
