from flet import *
import sqlite3
con = sqlite3.connect("workers.db",check_same_thread=False)
cor = con.cursor()
cor.execute("""
CREATE TABLE IF NOT EXISTS infworker(name TEXT, familyname TEXT,  date TEXT, number TEXT, cart TEXT, live TEXT)
""")
con.commit()
card_nationl = TextField(label="لكارط ناسيونال",width=200,bgcolor=Colors.WHITE_10)
live = TextField(label="لبلاد فين كيعيش",width=200,bgcolor=Colors.WHITE_10)
def addwoker_view(page:Page):
    def know_plus():
        page.add(
                    Card(
                        bgcolor=Colors.WHITE,
                        content=Container(
                            content=Column([
                                number_fon,
                                card_nationl,
                                live,
                            ]),rtl=True
                        )
                    )
                )
        
    ################ info_worck #########################
    tabel_name = "infworker"
    query = f'SELECT COUNT(*) FROM {tabel_name}'
    cor.execute(query)
    result = cor.fetchone()
    row_count = result[0]
    def add_info_worker():
    
        cor.execute("INSERT INTO infworker(name, familyname, date, number, cart, live) VALUES(?,?,?,?,?,?)", (name_worker.value,familyname_worker.value,date_add.value,number_fon.value,card_nationl.value,live.value))
        con.commit()
        ####################################################
    def on_click():
        if not name_worker.value or name_worker.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت سمية خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not familyname_worker.value or familyname_worker.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت لكنية خاوية",color="red",size=16),)
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        if not date_add.value or date_add.value.strip()=="":
            alert=AlertDialog(title=Text("راه خليتي بلاصت تاريخ خاوية",color="red",size=16))
            page.overlay.append(alert)
            alert.open=True
            page.update()
            return
        page.update()

        add_info_worker()
    
    ##################### call me #########################################
    def call():
        alert= AlertDialog(title=Text("الى طرا ليك شي موشكيل فهاد التطبيق تواصل مع هاد راقم:\n0717207647\nاولا هاد لانستكرام:\nAyoub Ben",color="black",selectable=True,rtl=True,size=18))
        page.overlay.append(alert)
        alert.open=True
    ######################################################################
    name_worker = TextField(label="سمية",width=200,bgcolor=Colors.WHITE_70)
    familyname_worker = TextField(label="لكنية",width=200,bgcolor=Colors.WHITE_70)
    date_add = TextField(label="تاريخ لي بدا فيه",width=200,bgcolor=Colors.WHITE_70)
    number_fon = TextField(label="نمرا ديال تيليفون",width=200,bgcolor=Colors.WHITE_70)
    return View(
        route="/workadd",
        controls=[
            AppBar(
                bgcolor=Colors.WHITE,
                title=Text("صفحة اضافة العمال",color=Colors.AMBER,size=15),
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
            
            Text(" زيد خدام جديد ➕",rtl=True,size=18,color=Colors.CYAN,font_family="Elephant"),
            Image(src="asets/imo/count.png",width=100),
            Row(
                [
                Text("عدد لخدامة لي كاينين: ",size=18,color=Colors.BROWN),
                Text(row_count,size=15)
                ],alignment=MainAxisAlignment.CENTER,rtl=True
            ),
            name_worker,
            familyname_worker,
            date_add,
            TextButton(" !? نعرف شي حاجة أخر على الخدام",on_click=know_plus),
            ElevatedButton("زيدو فلائحة",rtl=True,icon=Icons.ADD,bgcolor=Colors.BLUE, on_click=on_click),
            
        ],horizontal_alignment="center",padding = 0,bgcolor=Colors.WHITE,scroll="auto"
    )
