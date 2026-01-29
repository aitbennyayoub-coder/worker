from flet import *
import sqlite3

con = sqlite3.connect("workers.db",check_same_thread=False)
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS absent(name TEXT, familyname TEXT, date TEXT)
""")
con.commit()
def absent_view(page:Page):
    def on_click():
        if not name_wrk_remov.value or name_wrk_remov.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت سمية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not family_name_werk_remov.value or family_name_werk_remov.value.strip()=="":
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
    tabel = "absent"
    query = f'SELECT COUNT(*) FROM {tabel}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    def add_data():
        cor.execute("INSERT INTO absent(name, familyname, date) VALUES(?,?,?)", (name_wrk_remov.value, family_name_werk_remov.value,date.value))
        con.commit()
    ###########################################################################################################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM absent")
        data = c.fetchone()
        if data:
            print_data()
        else:
            alert=AlertDialog(title=Text("مكاينش لغياب",color="red",size=30))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ########? print all worekers in tireminal ###############################################################?
    def print_data():
        c = con.cursor()
        c.execute("SELECT * FROM absent")
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
                                    Text("تاريخ لي منك فيه: ",color=Colors.WHITE,size=18),
                                    Text(i["date"],color=Colors.GREEN,size=14),
                                ]),
                            ]),rtl=True
                        )
                    )
                )
        else:
            alert=AlertDialog(title=Text("لا يوجد غياب",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ####################################################################################################################################?
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    name_wrk_remov = TextField(label="سمية",width=200,)
    family_name_werk_remov =TextField(label="لكنية",width=200,)
    date = TextField(label="تاريخ",width=200,)
    return View(
        route="/absent",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("صفحة الغياب",color=Colors.AMBER,size=15),
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
            Text("لخدامة لي كيمنكو 👨‍🌾❌",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/user (2).png",width=200),
            name_wrk_remov,family_name_werk_remov,date,
                ElevatedButton("غائب",rtl=True,icon=Icons.DO_NOT_DISTURB,bgcolor=Colors.BLUE, on_click=on_click),
                ElevatedButton("شوف لائحة ديال لغياب",rtl=True,bgcolor=Colors.BLUE, icon=Icons.VISIBILITY, on_click=chow_data),
        ],horizontal_alignment="center",padding = 0,bgcolor=Colors.WHITE,scroll="auto"
    )
