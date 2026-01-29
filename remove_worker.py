from flet import *
import sqlite3
####################### data worecers ##########################################
con = sqlite3.connect("workers.db",check_same_thread=False)
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS tablestop(name TEXT, familyname TEXT,  date TEXT)
""")
con.commit()
###############################################################################
def removeworker_view(page:Page):
    def on_click():
        if not name_wrk_stop.value or name_wrk_stop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت سمية خاوي",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not family_name_werk_stop.value or family_name_werk_stop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت لكنية خاوي",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not date_stop.value or date_stop.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تاريخ خاوي",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        page.update()
        add_info_worker()
     ################ info_worck #########################
    tabel_name = "tablestop"
    query = f'SELECT COUNT(*) FROM {tabel_name}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    def add_info_worker():
        cor.execute("INSERT INTO tablestop(name, familyname, date) VALUES(?,?,?)", (name_wrk_stop.value, family_name_werk_stop.value,date_stop.value))
        con.commit()
    
    ####################################################
    def chow_data():
        c = con.cursor()
        c.execute("SELECT * FROM tablestop")
        data = c.fetchone()
        if data:
            print_chop()
        else:
            alert=AlertDialog(title=Text("مكاينش توقيف",color="red",size=30))
            page.overlay.append(alert)
            alert.open=True
            page.update()
    ########? print all worekers in tireminal ###############################################################?
    def print_chop():
        c = con.cursor()
        c.execute("SELECT * FROM tablestop")
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
                                    Text("سمية ديال لخدام: " ,color=Colors.WHITE,size=18),
                                    Text(i["name"],color=Colors.GREEN,size=14),
                                ]
                                ),
                                Row([
                                    Text("لكنية ديال لخدام: ",color=Colors.WHITE,size=18),
                                    Text(i["familyname"],color=Colors.GREEN,size=14),
                                ]),
                                Row([
                                    Text("تاريخ لي وقف فيه لخدمة: ",color=Colors.WHITE,size=18),
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
    name_wrk_stop = TextField(label="سمية",width=200,)
    family_name_werk_stop =TextField(label="لكنية",width=200,)
    date_stop = TextField(label="تاريخ",width=200,)
    return View(
        route="/moveworck",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("صفحة التوقيف عن العمل",color=Colors.AMBER,size=15),
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
            Text("لخدامة لي مبقوش فلخدمة 🚷",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/user (2).png",width=200),
            Row([
                Text("عدد لخدامة لي مبقاوش فلخدمة: ",rtl=True,size=18,color=Colors.AMBER,font_family="Light"),
                Text(row_count,rtl=True,size=14,color=Colors.BLACK),
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
            name_wrk_stop,family_name_werk_stop,date_stop,
            ElevatedButton("حبسو من لخدمة",rtl=True,bgcolor=Colors.AMBER, on_click=on_click),
            ElevatedButton("شوف لائحة",color=Colors.BLACK,rtl=True,bgcolor=Colors.DEEP_PURPLE,icon=Icons.VISIBILITY, on_click=chow_data),
        ],horizontal_alignment="center",padding = 0,bgcolor=Colors.WHITE,scroll="auto"
    )
