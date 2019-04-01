
import sqlite3

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QPalette
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QMessageBox, \
    QDialogButtonBox, QGroupBox, QFormLayout, QLabel


class Window(QtWidgets.QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.l = QtWidgets.QLabel("Welcome to Steel Section's Database")
        self.m = QtWidgets.QPushButton("Display")
        self.b = QtWidgets.QPushButton("Search")
        self.e = QtWidgets.QPushButton("Append")
        self.edit = QtWidgets.QLineEdit(self)
        self.label = QtWidgets.QLabel("Designation")
        self.s = QtWidgets.QPushButton("Show")
        self.searchBeams = QtWidgets.QPushButton("Search in Beams")
        self.searchChannels = QtWidgets.QPushButton("Search in Channels")
        self.searchAngles = QtWidgets.QPushButton("Search in Angles")
        self.oka = QtWidgets.QPushButton("OK")
        self.oks = QtWidgets.QPushButton("OK")

        self.designation_a = QtWidgets.QLineEdit(self)
        self.mass_a = QtWidgets.QLineEdit(self)
        self.area_a = QtWidgets.QLineEdit(self)
        self.axb_a = QtWidgets.QLineEdit(self)
        self.t_a = QtWidgets.QLineEdit(self)
        self.r1_a = QtWidgets.QLineEdit(self)
        self.r2_a = QtWidgets.QLineEdit(self)
        self.cz_a = QtWidgets.QLineEdit(self)
        self.cy_a = QtWidgets.QLineEdit(self)
        self.tan_a = QtWidgets.QLineEdit(self)
        self.iz_a = QtWidgets.QLineEdit(self)
        self.iy_a = QtWidgets.QLineEdit(self)
        self.iu_a = QtWidgets.QLineEdit(self)
        self.iv_a = QtWidgets.QLineEdit(self)
        self.rz_a = QtWidgets.QLineEdit(self)
        self.ry_a = QtWidgets.QLineEdit(self)
        self.ru_a = QtWidgets.QLineEdit(self)
        self.rv_a = QtWidgets.QLineEdit(self)
        self.zz_a = QtWidgets.QLineEdit(self)
        self.zy_a = QtWidgets.QLineEdit(self)
        self.zpz_a = QtWidgets.QLineEdit(self)
        self.zpy_a = QtWidgets.QLineEdit(self)
        self.source_a = QtWidgets.QLineEdit(self)


        self.designation_c = QtWidgets.QLineEdit(self)
        self.mass_c = QtWidgets.QLineEdit(self)
        self.area_c = QtWidgets.QLineEdit(self)
        self.d_c = QtWidgets.QLineEdit(self)
        self.b_c = QtWidgets.QLineEdit(self)
        self.tw_c = QtWidgets.QLineEdit(self)
        self.t_c = QtWidgets.QLineEdit(self)
        self.flangeSlope_c = QtWidgets.QLineEdit(self)
        self.r1_c = QtWidgets.QLineEdit(self)
        self.r2_c = QtWidgets.QLineEdit(self)
        self.cy_c = QtWidgets.QLineEdit(self)
        self.iz_c = QtWidgets.QLineEdit(self)
        self.iy_c = QtWidgets.QLineEdit(self)
        self.rz_c= QtWidgets.QLineEdit(self)
        self.ry_c = QtWidgets.QLineEdit(self)
        self.zz_c = QtWidgets.QLineEdit(self)
        self.zy_c = QtWidgets.QLineEdit(self)
        self.zpz_c = QtWidgets.QLineEdit(self)
        self.zpy_c = QtWidgets.QLineEdit(self)
        self.source_c = QtWidgets.QLineEdit(self)


        self.designation_b = QtWidgets.QLineEdit(self)
        self.mass_b = QtWidgets.QLineEdit(self)
        self.area_b = QtWidgets.QLineEdit(self)
        self.d_b = QtWidgets.QLineEdit(self)
        self.b_b = QtWidgets.QLineEdit(self)
        self.tw_b = QtWidgets.QLineEdit(self)
        self.t_b = QtWidgets.QLineEdit(self)
        self.flangeSlope_b = QtWidgets.QLineEdit(self)
        self.r1_b = QtWidgets.QLineEdit(self)
        self.r2_b = QtWidgets.QLineEdit(self)
        self.iz_b = QtWidgets.QLineEdit(self)
        self.iy_b = QtWidgets.QLineEdit(self)
        self.rz_b = QtWidgets.QLineEdit(self)
        self.ry_b = QtWidgets.QLineEdit(self)
        self.zz_b = QtWidgets.QLineEdit(self)
        self.zy_b = QtWidgets.QLineEdit(self)
        self.zpz_b = QtWidgets.QLineEdit(self)
        self.zpy_b = QtWidgets.QLineEdit(self)
        self.source_b = QtWidgets.QLineEdit(self)

        self.init_ui()


    def init_ui(self):

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch(2)


        self.m.setStyleSheet("background-color: #708090;"
                               "border-style: outset;"
                                 "border-width: 1px;"
                                  "border-radius: 4px;"
                                   "border-color: beige;"
                                  
                                    "font: bold 12px ;"
                                     "min-width: 8em;"
                                      "padding: 5px;")
        self.b.setStyleSheet("background-color: #708090;"
                             "border-style: outset;"
                             "border-width: 1px;"
                             "border-radius: 4px;"
                             "border-color: beige;"
                             "font: bold 12px;"
                             "min-width: 8em;"
                             "padding: 5px;")
        self.e.setStyleSheet("background-color: #708090;"
                             "border-style: outset;"
                             "border-width: 1px;"
                             "border-radius: 4px;"
                             "border-color: beige;"
                             "font: bold 12px;"
                             "min-width: 8em;"
                             "padding: 5px;")
        h_box.addWidget(self.m)
        #h_box.addStretch(2)
        h_box.addWidget(self.b)
        #h_box.addStretch(2)
        h_box.addWidget(self.e)
        h_box.addStretch(2)
        s_box = QtWidgets.QVBoxLayout()
        #h_box.setAlignment(Qt.Align)
        image = QtGui.QImage("backimage.jpg")
        #sImage = image.scaled(QtCore.QSize(400, 400))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QtGui.QBrush(image))  # 10 = Windowrole
        self.setPalette(palette)
        s_box.addStretch(1)
        self.l.setStyleSheet("font: SansSerif 24px;"
                             "color:black;")
        self.l.setFont(QtGui.QFont('SansSerif', 30))
        s_box.addWidget(self.l, alignment=Qt.AlignHCenter)

        s_box.addLayout(h_box)
        s_box.addStretch(1)
        self.setLayout(s_box)
        self.setWindowTitle("Fossee - Python")

        self.setWindowIcon(QtGui.QIcon("icon.jpg"))
        self.showMaximized()

        #self.setAutoFillBackground(True)
        #self.setBackgroundRole(QtGui.QPalette.Highlight)
        self.oka.clicked.connect(self.okadd)
        #self.oks.clicked.connect()

        self.searchBeams.clicked.connect(self.search_beams)
        self.searchAngles.clicked.connect(self.search_angles)
        self.searchChannels.clicked.connect(self.search_channels)
        self.b.clicked.connect(self.search_click)
        self.e.clicked.connect(self.append_click)
        self.m.clicked.connect(self.display_click)
        self.s.clicked.connect(self.show_click)


        #self.show()

    def display_click(self):
        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle("Display")
        dialog_box1.resize(170, 170)
        h_box1 = QtWidgets.QHBoxLayout()
        # h_box1.addStretch()
        self.b1 = QtWidgets.QRadioButton("Beams")

        self.b2 = QtWidgets.QRadioButton("Channels")
        self.b3 = QtWidgets.QRadioButton("Angles")
        self.label1 = QtWidgets.QLabel("Select A Table")


        h_box1.addWidget(self.b1)

        h_box1.addWidget(self.b2)
        h_box1.addWidget(self.b3)
        # h_box1.addStretch()
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.label1, alignment=Qt.AlignHCenter)
        v_box1.addLayout(h_box1)

        self.b1.toggled.connect(lambda: self.btnstate1(self.b1))
        self.b2.toggled.connect(lambda: self.btnstate1(self.b2))
        self.b3.toggled.connect(lambda: self.btnstate1(self.b3))

        dialog_box1.setLayout(v_box1)
        dialog_box1.setStyleSheet("font-size:14px;"
                                  "color: black;"
                                  "background-color: #708090;"
                                  "font: SanSerif; "
                                  )
        dialog_box1.setWindowIcon(QtGui.QIcon("icon.jpg"))
        dialog_box1.exec_()



    def btnstate1(self,bd):
        if bd.text() == "Beams":
            if bd.isChecked() == True:
                conn = sqlite3.connect('steel_sections.sqlite')

                cursor = conn.cursor()
                rowcount2 = cursor.execute('''SELECT COUNT(*) FROM Beams''').fetchone()[0]
                tblTable = QTableWidget()

                tableItem = QTableWidgetItem()
                tblTable.setWindowTitle("Details")
                tblTable.setRowCount(rowcount2)
                tblTable.setColumnCount(20)
                tblTable.setHorizontalHeaderLabels(
                    ['Id', 'Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Iz', 'Iy',
                     'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source'])

                cursor.execute('''SELECT * FROM Beams''')

                for row, form in enumerate(cursor):
                    for column, item in enumerate(form):
                        tblTable.setItem(row, column, QTableWidgetItem(str(item)))
                tblTable.horizontalHeader().setStretchLastSection(True)
                tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                tblTable.show()
                dialog = QDialog()
                dialog.setWindowTitle("Details of Beams Section")
                dialog.resize(600, 400)
                dialog.setLayout(QVBoxLayout())
                dialog.layout().addWidget(tblTable)
                dialog.setStyleSheet("font-size:14px;"
                                          "color: black;"
                                          "background-color: #A9A9A9;"
                                          "font: SanSerif; "
                                          )
                dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                dialog.exec()

        if bd.text() == "Channels":
            if bd.isChecked() == True:
                conn = sqlite3.connect('steel_sections.sqlite')

                cursor = conn.cursor()
                rowcount1 = cursor.execute('''SELECT COUNT(*) FROM Channels''').fetchone()[0]
                tblTable = QTableWidget()

                tableItem = QTableWidgetItem()
                tblTable.setWindowTitle("Details")
                tblTable.setRowCount(rowcount1)
                tblTable.setColumnCount(21)
                tblTable.setHorizontalHeaderLabels(
                    ['Id', 'Designation', 'Mass', 'Area', 'D', 'B', 'tw', 'T', 'FlangeSlope', 'R1', 'R2', 'Cy', 'Iz',
                     'Iy', 'rz', 'ry', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source'])

                cursor.execute('''SELECT * FROM Channels''')

                for row, form in enumerate(cursor):
                    for column, item in enumerate(form):
                        tblTable.setItem(row, column, QTableWidgetItem(str(item)))
                tblTable.horizontalHeader().setStretchLastSection(True)
                tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                tblTable.show()
                dialog = QDialog()
                dialog.setWindowTitle("Details of Channels Section")
                dialog.resize(600, 400)
                dialog.setLayout(QVBoxLayout())
                dialog.layout().addWidget(tblTable)
                dialog.setStyleSheet("font-size:14px;"
                                     "color: black;"
                                     "background-color: #A9A9A9;"
                                     "font: SanSerif; "
                                     )
                dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                dialog.exec()

        if bd.text() == "Angles":
            if bd.isChecked() == True:
                conn = sqlite3.connect('steel_sections.sqlite')

                cursor = conn.cursor()
                rowcount3 = cursor.execute('''SELECT COUNT(*) FROM Angles ''').fetchone()[0]
                tblTable = QTableWidget()

                tableItem = QTableWidgetItem()
                tblTable.setWindowTitle("Details")
                tblTable.setRowCount(rowcount3)
                tblTable.setColumnCount(24)
                tblTable.setHorizontalHeaderLabels(
                    ['Id', 'Designation', 'Mass', 'Area', 'AXB', 't', 'R1', 'R2', 'Cz', 'Cy', 'Tan?', 'Iz', 'Iy',
                     'Iu(max)', 'Iv(min)', 'rz', 'ry', 'ru(max)', 'rv(min)', 'Zz', 'Zy', 'Zpz', 'Zpy', 'Source'])
                cursor.execute('''SELECT * FROM Angles ''')

                for row, form in enumerate(cursor):
                    for column, item in enumerate(form):
                        tblTable.setItem(row, column, QTableWidgetItem(str(item)))
                tblTable.horizontalHeader().setStretchLastSection(False)
                tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
                tblTable.show()

                dialog = QDialog()
                dialog.setWindowTitle("Details of Angles Section")
                dialog.resize(600, 400)
                dialog.setLayout(QVBoxLayout())
                dialog.layout().addWidget(tblTable)
                dialog.setStyleSheet("font-size:14px;"
                                     "color: black;"
                                     "background-color:#A9A9A9;"
                                     "font: SanSerif; "
                                     )
                dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
                dialog.exec()






    def search_click(self):

        dialog_box1 = QDialog()
        dialog_box1.setWindowTitle("Search")
        dialog_box1.resize(170, 170)
        h_box1 = QtWidgets.QHBoxLayout()
        # h_box1.addStretch()
        self.bs1 = QtWidgets.QRadioButton("Beams")

        self.bs2 = QtWidgets.QRadioButton("Channels")
        self.bs3 = QtWidgets.QRadioButton("Angles")
        self.label1 = QtWidgets.QLabel("Select A Table")

        h_box1.addWidget(self.bs1)

        h_box1.addWidget(self.bs2)
        h_box1.addWidget(self.bs3)
        # h_box1.addStretch()
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addWidget(self.label1, alignment=Qt.AlignHCenter)
        v_box1.addLayout(h_box1)

        self.bs1.toggled.connect(lambda: self.btnstate2(self.bs1))
        self.bs2.toggled.connect(lambda: self.btnstate2(self.bs2))
        self.bs3.toggled.connect(lambda: self.btnstate2(self.bs3))

        dialog_box1.setLayout(v_box1)
        dialog_box1.setStyleSheet("font-size:14px;"
                                  "color: black;"
                                  "background-color: #708090;"
                                  "font: SanSerif; "
                                  )
        dialog_box1.setWindowIcon(QtGui.QIcon("icon.jpg"))

        dialog_box1.exec_()

    ''' h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.label)
        self.edit.setMaximumHeight(30)
        self.edit.setMaximumWidth(200)
        h_box1.addWidget(self.edit)
        h_box1.addStretch()
        v_box1 = QtWidgets.QVBoxLayout()
        v_box1.addLayout(h_box1)
        v_box1.addWidget(self.s)

        dialog_box = QDialog()
        dialog_box.setWindowTitle("Fossee")

        dialog_box.setLayout(v_box1)


        dialog_box.exec_()'''


    def btnstate2(self,bs):
        if bs.text() == "Beams":
            if bs.isChecked() == True:
                h_box1 = QtWidgets.QHBoxLayout()
                h_box1.addStretch()
                h_box1.addWidget(self.label)
                self.edit.setMaximumHeight(30)
                self.edit.setMaximumWidth(200)
                h_box1.addWidget(self.edit)
                h_box1.addStretch()
                v_box1 = QtWidgets.QVBoxLayout()
                v_box1.addLayout(h_box1)
                #v_box1.addWidget(self.s)
                v_box1.addWidget(self.searchBeams)

                dialog_box = QDialog()
                dialog_box.setWindowTitle("Search")


                dialog_box.setLayout(v_box1)
                dialog_box.setStyleSheet("color: black;"
                    "background-color: #A9A9A9;"
                                     )
                dialog_box.setWindowIcon(QtGui.QIcon("icon.jpg"))

                dialog_box.exec_()
        if bs.text() == "Channels":
            if bs.isChecked() == True:
                h_box1 = QtWidgets.QHBoxLayout()
                h_box1.addStretch()
                h_box1.addWidget(self.label)
                self.edit.setMaximumHeight(30)
                self.edit.setMaximumWidth(200)
                h_box1.addWidget(self.edit)
                h_box1.addStretch()
                v_box1 = QtWidgets.QVBoxLayout()
                v_box1.addLayout(h_box1)
                # v_box1.addWidget(self.s)
                v_box1.addWidget(self.searchChannels)

                dialog_box = QDialog()
                dialog_box.setWindowTitle("Search")

                dialog_box.setLayout(v_box1)
                dialog_box.setStyleSheet(
                                         "color: black;"
                                         "background-color: #A9A9A9;"

                                         )
                dialog_box.setWindowIcon(QtGui.QIcon("icon.jpg"))

                dialog_box.exec_()
        if bs.text() == "Angles":
            if bs.isChecked() == True:
                h_box1 = QtWidgets.QHBoxLayout()
                h_box1.addStretch()
                h_box1.addWidget(self.label)
                self.edit.setMaximumHeight(30)
                self.edit.setMaximumWidth(200)
                h_box1.addWidget(self.edit)
                h_box1.addStretch()
                v_box1 = QtWidgets.QVBoxLayout()
                v_box1.addLayout(h_box1)
                # v_box1.addWidget(self.s)
                v_box1.addWidget(self.searchAngles)

                dialog_box = QDialog()
                dialog_box.setWindowTitle("Search")

                dialog_box.setLayout(v_box1)
                dialog_box.setLayout(v_box1)
                dialog_box.setStyleSheet(
                    "color: black;"
                    "background-color: #A9A9A9;"

                )
                dialog_box.setWindowIcon(QtGui.QIcon("icon.jpg"))

                dialog_box.exec_()


    def search_beams(self):
        designation = self.edit.text()


        conn = sqlite3.connect('steel_sections.sqlite')

        cursor = conn.cursor()

        if cursor.execute('''SELECT COUNT(*) FROM Beams where designation=?;''',(designation,)).fetchone()[0]!=0:
            rowcount2 = cursor.execute('''SELECT COUNT(*) FROM Beams where designation=?;''',(designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount2)
            tblTable.setColumnCount(20)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','D','B','tw','T','FlangeSlope','R1','R2','Iz','Iy','rz','ry','Zz','Zy','Zpz','Zpy','Source'])

            cursor.execute('''SELECT * FROM Beams where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(True)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 200)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.exec()

        else:
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 400)
            label = QtWidgets.QLabel("Nothing to Display")
            new_layout = QtWidgets.QVBoxLayout()
            new_layout.addWidget(label)
            dialog.setLayout(new_layout)
            dialog.setStyleSheet("font-size:20px;"
                                 "color: black;"
                                 "background-color: #A9A9A9;"
                                 "font: SanSerif; "
                                 )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()

    def search_channels(self):
        designation = self.edit.text()


        conn = sqlite3.connect('steel_sections.sqlite')

        cursor = conn.cursor()

        if cursor.execute('''SELECT COUNT(*) FROM Channels where designation=?;''',(designation,)).fetchone()[0]!=0:
            rowcount1 = cursor.execute('''SELECT COUNT(*) FROM Channels where designation=?;''',(designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount1)
            tblTable.setColumnCount(21)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','D','B','tw','T','FlangeSlope','R1','R2','Cy','Iz','Iy','rz','ry','Zz','Zy','Zpz','Zpy','Source'])

            cursor.execute('''SELECT * FROM Channels where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(True)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 200)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.setStyleSheet("font-size:14px;"
                                 "color: black;"
                                 "background-color: #A9A9A9;"
                                 "font: SanSerif; "
                                 )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()
        else:
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 400)
            label = QtWidgets.QLabel("Nothing to Display")
            label.setAlignment(Qt.AlignCenter)
            #label.setStyleSheet("font:SanSerif 20px;")
            new_layout = QtWidgets.QVBoxLayout()
            new_layout.addWidget(label)
            dialog.setLayout(new_layout)
            dialog.setStyleSheet("font-size:20px;"
                                 "color: black;"
                                 "background-color: #A9A9A9;"
                                 "font: SanSerif; "
                                 )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()


    def search_angles(self):
        designation = self.edit.text()


        conn = sqlite3.connect('steel_sections.sqlite')

        cursor = conn.cursor()

        if cursor.execute('''SELECT COUNT(*) FROM Angles where designation=?;''', (designation,)).fetchone()[0]!=0:
            rowcount3 = cursor.execute('''SELECT COUNT(*) FROM Angles where designation=?;''', (designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount3)
            tblTable.setColumnCount(24)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','AXB','t','R1','R2','Cz','Cy','Tan?','Iz','Iy','Iu(max)','Iv(min)','rz','ry','ru(max)','rv(min)','Zz','Zy','Zpz','Zpy','Source'])
            cursor.execute('''SELECT * FROM Angles where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(False)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()

            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 200)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.setStyleSheet("font-size:14px;"
                                 "color: black;"
                                 "background-color: #A9A9A9;"
                                 "font: SanSerif; "
                                 )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()
        else:
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(400, 400)
            label = QtWidgets.QLabel("Nothing to Display")
            new_layout = QtWidgets.QVBoxLayout()
            new_layout.addWidget(label)
            dialog.setLayout(new_layout)
            dialog.setStyleSheet("font-size:20px;"
                                 "color: black;"
                                 "background-color: #A9A9A9;"
                                 "font: SanSerif; "
                                 )
            dialog.setWindowIcon(QtGui.QIcon("icon.jpg"))
            dialog.exec()


    def show_click(self):
        designation = self.edit.text()

        conn = sqlite3.connect('steel_sections.sqlite')

        cursor = conn.cursor()

        if  cursor.execute('''SELECT COUNT(*) FROM Channels where designation=?;''',(designation,)).fetchone()[0]!=0:
            rowcount1 = cursor.execute('''SELECT COUNT(*) FROM Channels where designation=?;''',(designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount1)
            tblTable.setColumnCount(21)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','D','B','tw','T','FlangeSlope','R1','R2','Cy','Iz','Iy','rz','ry','Zz','Zy','Zpz','Zpy','Source'])

            cursor.execute('''SELECT * FROM Channels where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(True)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()
            dialog = QDialog()
            dialog.setWindowTitle("Student Details")
            dialog.resize(500, 300)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.exec()

        elif cursor.execute('''SELECT COUNT(*) FROM Beams where designation=?;''',(designation,)).fetchone()[0]!=0:
            rowcount2 = cursor.execute('''SELECT COUNT(*) FROM Beams where designation=?;''',(designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount2)
            tblTable.setColumnCount(20)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','D','B','tw','T','FlangeSlope','R1','R2','Iz','Iy','rz','ry','Zz','Zy','Zpz','Zpy','Source'])

            cursor.execute('''SELECT * FROM Beams where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(True)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()
            dialog = QDialog()
            dialog.setWindowTitle("Student Details")
            dialog.resize(500, 300)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.exec()
        elif cursor.execute('''SELECT COUNT(*) FROM Angles where designation=?;''', (designation,)).fetchone()[0]!=0:
            rowcount3 = cursor.execute('''SELECT COUNT(*) FROM Angles where designation=?;''', (designation,)).fetchone()[0]
            tblTable = QTableWidget()

            tableItem = QTableWidgetItem()
            tblTable.setWindowTitle("Details")
            tblTable.setRowCount(rowcount3)
            tblTable.setColumnCount(24)
            tblTable.setHorizontalHeaderLabels(['Id','Designation','Mass','Area','AXB','t','R1','R2','Cz','Cy','Tan?','Iz','Iy','Iu(max)','Iv(min)','rz','ry','ru(max)','rv(min)','Zz','Zy','Zpz','Zpy','Source'])
            cursor.execute('''SELECT * FROM Angles where designation=?''', (designation,))

            for row, form in enumerate(cursor):
                for column, item in enumerate(form):
                    tblTable.setItem(row, column, QTableWidgetItem(str(item)))
            tblTable.horizontalHeader().setStretchLastSection(False)
            tblTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            tblTable.show()

            dialog = QDialog()
            dialog.setWindowTitle("Student Details")
            dialog.resize(500, 300)
            dialog.setLayout(QVBoxLayout())
            dialog.layout().addWidget(tblTable)
            dialog.exec()
        else:
            dialog = QDialog()
            dialog.setWindowTitle("Details")
            dialog.resize(500, 300)
            label=QtWidgets.QLabel("Nothing to Display")
            new_layout=QtWidgets.QVBoxLayout()
            new_layout.addWidget(label)
            dialog.setLayout(new_layout)
            dialog.exec()


    def append_click(self):

         dialog_box1 = QDialog()
         dialog_box1.setWindowTitle("Append")
         dialog_box1.resize(170,170)
         h_box1 = QtWidgets.QHBoxLayout()
         #h_box1.addStretch()
         self.ba1 = QtWidgets.QRadioButton("Beams")

         self.ba2 = QtWidgets.QRadioButton("Channels")
         self.ba3 = QtWidgets.QRadioButton("Angles")
         self.label1 = QtWidgets.QLabel("Select A Table")

         h_box1.addWidget(self.ba1)

         h_box1.addWidget(self.ba2)
         h_box1.addWidget(self.ba3)
         #h_box1.addStretch()
         v_box1 = QtWidgets.QVBoxLayout()
         v_box1.addWidget(self.label1,alignment=Qt.AlignHCenter)
         v_box1.addLayout(h_box1)
         v_box1.addWidget(self.oka)


         dialog_box1.setLayout(v_box1)
         dialog_box1.setStyleSheet("font-size:14px;"
                                   "color: black;"
                                   "background-color: #708090;"
                                   "font: SanSerif; "
                                   )
         dialog_box1.setWindowIcon(QtGui.QIcon("icon.jpg"))
         dialog_box1.exec_()

    def okadd(self):
        if self.ba1.isChecked() == True:
            dialog = QDialog()

            formGroupBox = QGroupBox("Add Information")
            layout = QFormLayout()
            layout.addRow(QLabel("Designation"), self.designation_b)
            layout.addRow(QLabel("Mass"), self.mass_b)
            layout.addRow(QLabel("Area"), self.area_b)
            layout.addRow(QLabel("D"), self.d_b)
            layout.addRow(QLabel("B"), self.b_b)
            layout.addRow(QLabel("tw"), self.tw_b)
            layout.addRow(QLabel("T"), self.t_b)
            layout.addRow(QLabel("FlangeSlope"), self.flangeSlope_b)
            layout.addRow(QLabel("R1"), self.r1_b)
            layout.addRow(QLabel("R2"), self.r2_b)
            layout.addRow(QLabel("Iz"), self.iz_b)
            layout.addRow(QLabel("Iy"), self.iy_b)
            layout.addRow(QLabel("rz"), self.rz_b)
            layout.addRow(QLabel("ry"), self.ry_b)
            layout.addRow(QLabel("Zz"), self.zz_b)
            layout.addRow(QLabel("Zy"), self.zy_b)
            layout.addRow(QLabel("Zpz"), self.zpz_b)
            layout.addRow(QLabel("Zpy"), self.zpy_b)
            layout.addRow(QLabel("Source"), self.source_b)
            formGroupBox.setLayout(layout)

            buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttonBox.accepted.connect(self.add_beams)
            # buttonBox.rejected.connect(self.reject)

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(formGroupBox)
            mainLayout.addWidget(buttonBox)

            self.setWindowTitle("Fossee")

            dialog.setLayout(mainLayout)
            dialog.exec_()
        if self.ba2.isChecked() == True:
            dialog = QDialog()
            formGroupBox = QGroupBox("Add Information")
            layout = QFormLayout()
            layout.addRow(QLabel("Designation"), self.designation_c)
            layout.addRow(QLabel("Mass"), self.mass_c)
            layout.addRow(QLabel("Area"), self.area_c)
            layout.addRow(QLabel("D"), self.d_c)
            layout.addRow(QLabel("B"), self.b_c)
            layout.addRow(QLabel("tw"), self.tw_c)
            layout.addRow(QLabel("T"), self.t_c)
            layout.addRow(QLabel("FlangeSlope"), self.flangeSlope_c)
            layout.addRow(QLabel("R1"), self.r1_c)
            layout.addRow(QLabel("R2"), self.r2_c)
            layout.addRow(QLabel("Cy"), self.cy_c)
            layout.addRow(QLabel("Iz"), self.iz_c)
            layout.addRow(QLabel("Iy"), self.iy_c)
            layout.addRow(QLabel("rz"), self.rz_c)
            layout.addRow(QLabel("ry"), self.ry_c)
            layout.addRow(QLabel("Zz"), self.zz_c)
            layout.addRow(QLabel("Zy"), self.zy_c)
            layout.addRow(QLabel("Zpz"), self.zpz_c)
            layout.addRow(QLabel("Zpy"), self.zpy_c)
            layout.addRow(QLabel("Source"), self.source_c)

            formGroupBox.setLayout(layout)

            buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttonBox.accepted.connect(self.add_channels)
            # buttonBox.rejected.connect(self.reject)

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(formGroupBox)
            mainLayout.addWidget(buttonBox)

            self.setWindowTitle("Fossee")

            dialog.setLayout(mainLayout)
            dialog.exec_()
        if self.ba3.isChecked()==True:
            dialog = QDialog()
            # NumGridRows = 3
            # NumButtons =4
            formGroupBox = QGroupBox("Add Information")
            layout = QFormLayout()
            layout.addRow(QLabel("Designation"), self.designation_a)
            layout.addRow(QLabel("Mass"), self.mass_a)
            layout.addRow(QLabel("Area"), self.area_a)
            layout.addRow(QLabel("AxB"), self.axb_a)
            layout.addRow(QLabel("t"), self.t_b)
            layout.addRow(QLabel("R1"), self.r1_a)
            layout.addRow(QLabel("R2"), self.r2_a)
            layout.addRow(QLabel("Cz"), self.cz_a)
            layout.addRow(QLabel("Cy"), self.cy_a)
            layout.addRow(QLabel("Tan?"), self.tan_a)
            layout.addRow(QLabel("Iz"), self.iz_a)
            layout.addRow(QLabel("Iy"), self.iy_a)
            layout.addRow(QLabel("Iu(max)"), self.iu_a)
            layout.addRow(QLabel("Iv(min)"), self.iv_a)
            layout.addRow(QLabel("rz"), self.rz_a)
            layout.addRow(QLabel("ry"), self.ry_a)
            layout.addRow(QLabel("ru(max)"), self.ru_a)
            layout.addRow(QLabel("rv(min)"), self.rv_a)
            layout.addRow(QLabel("Zz"), self.zz_a)
            layout.addRow(QLabel("Zy"), self.zy_c)
            layout.addRow(QLabel("Zpz"), self.zpz_a)
            layout.addRow(QLabel("Zpy"), self.zpy_a)
            layout.addRow(QLabel("Source"), self.source_a)

            formGroupBox.setLayout(layout)

            buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttonBox.accepted.connect(self.add_angles)
            # buttonBox.rejected.connect(self.reject)

            mainLayout = QVBoxLayout()
            mainLayout.addWidget(formGroupBox)
            mainLayout.addWidget(buttonBox)

            self.setWindowTitle("Fossee")

            dialog.setLayout(mainLayout)
            dialog.exec_()

    def btnstate3(self, ba):

        if ba.text() == "Beams":
            if ba.isChecked() == True:
                dialog = QDialog()

                formGroupBox = QGroupBox("Add Information")
                layout = QFormLayout()
                layout.addRow(QLabel("Designation"), self.designation_b)
                layout.addRow(QLabel("Mass"), self.mass_b)
                layout.addRow(QLabel("Area"), self.area_b)
                layout.addRow(QLabel("D"), self.d_b)
                layout.addRow(QLabel("B"), self.b_b)
                layout.addRow(QLabel("tw"), self.tw_b)
                layout.addRow(QLabel("T"), self.t_b)
                layout.addRow(QLabel("FlangeSlope"), self.flangeSlope_b)
                layout.addRow(QLabel("R1"), self.r1_b)
                layout.addRow(QLabel("R2"), self.r2_b)
                layout.addRow(QLabel("Iz"), self.iz_b)
                layout.addRow(QLabel("Iy"), self.iy_b)
                layout.addRow(QLabel("rz"), self.rz_b)
                layout.addRow(QLabel("ry"), self.ry_b)
                layout.addRow(QLabel("Zz"), self.zz_b)
                layout.addRow(QLabel("Zy"), self.zy_b)
                layout.addRow(QLabel("Zpz"), self.zpz_b)
                layout.addRow(QLabel("Zpy"), self.zpy_b)
                layout.addRow(QLabel("Source"), self.source_b)
                formGroupBox.setLayout(layout)


                buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttonBox.accepted.connect(self.add_beams)
                #buttonBox.rejected.connect(self.reject)

                mainLayout = QVBoxLayout()
                mainLayout.addWidget(formGroupBox)
                mainLayout.addWidget(buttonBox)


                self.setWindowTitle("Fossee")

                dialog.setLayout(mainLayout)
                dialog.exec_()
        elif ba.text() == "Channels":
            if ba.isChecked() == True:
                dialog = QDialog()
                formGroupBox = QGroupBox("Add Information")
                layout = QFormLayout()
                layout.addRow(QLabel("Designation"),self.designation_c)
                layout.addRow(QLabel("Mass"), self.mass_c)
                layout.addRow(QLabel("Area"), self.area_c)
                layout.addRow(QLabel("D"), self.d_c)
                layout.addRow(QLabel("B"), self.b_c)
                layout.addRow(QLabel("tw"), self.tw_c)
                layout.addRow(QLabel("T"), self.t_c)
                layout.addRow(QLabel("FlangeSlope"), self.flangeSlope_c)
                layout.addRow(QLabel("R1"), self.r1_c)
                layout.addRow(QLabel("R2"), self.r2_c)
                layout.addRow(QLabel("Cy"), self.cy_c)
                layout.addRow(QLabel("Iz"), self.iz_c)
                layout.addRow(QLabel("Iy"), self.iy_c)
                layout.addRow(QLabel("rz"), self.rz_c)
                layout.addRow(QLabel("ry"), self.ry_c)
                layout.addRow(QLabel("Zz"), self.zz_c)
                layout.addRow(QLabel("Zy"), self.zy_c)
                layout.addRow(QLabel("Zpz"), self.zpz_c)
                layout.addRow(QLabel("Zpy"), self.zpy_c)
                layout.addRow(QLabel("Source"), self.source_c)

                formGroupBox.setLayout(layout)


                buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttonBox.accepted.connect(self.add_channels)
                #buttonBox.rejected.connect(self.reject)

                mainLayout = QVBoxLayout()
                mainLayout.addWidget(formGroupBox)
                mainLayout.addWidget(buttonBox)


                self.setWindowTitle("Fossee")

                dialog.setLayout(mainLayout)
                dialog.exec_()

        elif str(ba.text()) == "Angles":
            if ba.isChecked() == True:
                dialog = QDialog()
                #NumGridRows = 3
                #NumButtons =4
                formGroupBox = QGroupBox("Add Information")
                layout = QFormLayout()
                layout.addRow(QLabel("Designation"), self.designation_a)
                layout.addRow(QLabel("Mass"), self.mass_a)
                layout.addRow(QLabel("Area"), self.area_a)
                layout.addRow(QLabel("AxB"), self.axb_a)
                layout.addRow(QLabel("t"), self.t_b)
                layout.addRow(QLabel("R1"), self.r1_a)
                layout.addRow(QLabel("R2"), self.r2_a)
                layout.addRow(QLabel("Cz"), self.cz_a)
                layout.addRow(QLabel("Cy"), self.cy_a)
                layout.addRow(QLabel("Tan?"), self.tan_a)
                layout.addRow(QLabel("Iz"), self.iz_a)
                layout.addRow(QLabel("Iy"), self.iy_a)
                layout.addRow(QLabel("Iu(max)"), self.iu_a)
                layout.addRow(QLabel("Iv(min)"), self.iv_a)
                layout.addRow(QLabel("rz"), self.rz_a)
                layout.addRow(QLabel("ry"), self.ry_a)
                layout.addRow(QLabel("ru(max)"), self.ru_a)
                layout.addRow(QLabel("rv(min)"), self.rv_a)
                layout.addRow(QLabel("Zz"), self.zz_a)
                layout.addRow(QLabel("Zy"), self.zy_c)
                layout.addRow(QLabel("Zpz"), self.zpz_a)
                layout.addRow(QLabel("Zpy"), self.zpy_a)
                layout.addRow(QLabel("Source"), self.source_a)

                formGroupBox.setLayout(layout)


                buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
                buttonBox.accepted.connect(self.add_angles)
                #buttonBox.rejected.connect(self.reject)

                mainLayout = QVBoxLayout()
                mainLayout.addWidget(formGroupBox)
                mainLayout.addWidget(buttonBox)


                self.setWindowTitle("Fossee")

                dialog.setLayout(mainLayout)
                dialog.exec_()


    def add_beams(self):

        desg_b = self.designation_b.text()
        mass_b = self.mass_b.text()
        area_b = self.area_b.text()
        d_b = self.d_b.text()
        b_b = self.b_b.text()
        tw_b = self.tw_b.text()
        t_b = self.t_b.text()
        flangeSlope_b = self.flangeSlope_b.text()
        r1_b = self.r1_b.text()
        r2_b = self.r2_b.text()
        iz_b = self.iz_b.text()
        iy_b = self.iy_b.text()
        rz_b = self.rz_b.text()
        ry_b = self.ry_b.text()
        zz_b = self.zz_b.text()
        zy_b = self.zy_b.text()
        zpz_b = self.zpz_b.text()
        zpy_b = self.zpy_b.text()
        source_b = self.source_b.text()


        conn = sqlite3.connect('steel_sections.sqlite')

        c = conn.cursor()
        c.execute('''INSERT INTO Beams (Designation,Mass,Area,D,B,tw,T,FlangeSlope,R1,R2,Iz,Iy,rz,ry,
                            Zz,zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (desg_b, mass_b, area_b,
                                                                                                      d_b, b_b, tw_b, t_b,
                                                                                                      flangeSlope_b, r1_b,
                                                                                                      r2_b, iz_b, iy_b, rz_b,
                                                                                                      ry_b, zz_b, zy_b
                                                                                                                            ,
                                                                                                      zpz_b, zpy_b, source_b))
        conn.commit()
        c.close()
        conn.close()
        QMessageBox.information(QMessageBox(), 'Data', 'Student is added successfully to the database.')


    def add_channels(self):

        desg_c = self.designation_c.text()
        mass_c = self.mass_c.text()
        area_c = self.area_c.text()
        d_c = self.d_c.text()
        b_c = self.b_c.text()
        tw_c = self.tw_c.text()
        t_c = self.t_c.text()
        flangeSlope_c = self.flangeSlope_b.text()
        r1_c = self.r1_c.text()
        r2_c = self.r2_c.text()
        cy_c = self.cy_c.text()
        iz_c = self.iz_c.text()
        iy_c = self.iy_c.text()
        rz_c = self.rz_c.text()
        ry_c = self.ry_c.text()
        zz_c = self.zz_c.text()
        zy_c = self.zy_c.text()

        zpz_c = self.zpz_c.text()
        zpy_c = self.zpy_c.text()
        source_c = self.source_c.text()


        conn = sqlite3.connect('steel_sections.sqlite')

        c = conn.cursor()
        c.execute('''INSERT INTO channels (Designation,Mass,Area,D,B,tw,T,FlangeSlope,R1,R2,Cy,Iz,Iy
                                        ,rz,ry,Zz,Zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       (desg_c, mass_c, area_c, d_c, b_c, tw_c, t_c, flangeSlope_c, r1_c, r2_c, cy_c, iz_c, iy_c, rz_c, ry_c,
                        zz_c, zy_c, zpz_c, zpy_c, source_c))
        conn.commit()
        c.close()
        conn.close()
        QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')



    def add_angles(self):
        desg_a= self.designation_a.text()
        mass_a = self.mass_a.text()
        area_a = self.area_a.text()
        axb_a = self.axb_a.text()
        t_a = self.t_a.text()


        r1_a = self.r1_a.text()
        r2_a = self.r2_a.text()
        cz_a = self.cz_a.text()
        cy_a = self.cy_a.text()
        tan_a = self.tan_a.text()
        iz_a = self.iz_a.text()
        iy_a = self.iy_a.text()
        iu_a = self.iu_a.text()
        iv_a = self.iv_a.text()
        rz_a = self.rz_a.text()
        ry_a = self.ry_a.text()
        ru_a = self.ru_a.text()
        rv_a = self.rv_a.text()
        zz_a = self.zz_a.text()
        zy_a = self.zy_a.text()

        zpz_a = self.zpz_a.text()
        zpy_a = self.zpy_a.text()
        source_a = self.source_a.text()

        conn = sqlite3.connect('steel_sections.sqlite')

        c = conn.cursor()
        c.execute('''INSERT INTO Angles (Designation,Mass,Area,AXB,t,R1,R2,Cz,Cy,'Tan?',Iz,Iy,'Iu(max)'
                           ,'Iv(min)',rz,ry,'ru(max)','rv(min)',Zz,Zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
                           ,?,?,?)''', (desg_a, mass_a, area_a, axb_a, t_a, r1_a, r2_a, cz_a, cy_a, tan_a, iz_a, iy_a, iu_a, iv_a,
                                        rz_a, ry_a, ru_a, rv_a,
                                        zz_a, zy_a, zpz_a, zpy_a, source_a))

        conn.commit()
        c.close()
        conn.close()
        QMessageBox.information(QMessageBox(), 'Successful', 'Data is added successfully to the database.')



