import sqlite3
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QMessageBox

import view


class Model:

    def search_table(self):
        designation = view.Window.edit.text()

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

    def add_data_beams(self):

        desg_b = view.Window.designation_b.text()
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
                                    Zz,zy,Zpz,Zpy,Source) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                  (desg_b, mass_b, area_b,
                   d_b, b_b, tw_b, t_b,
                   flangeSlope_b, r1_b,
                   r2_b, iz_b, iy_b, rz_b,
                   ry_b, zz_b, zy_b
                   ,
                   zpz_b, zpy_b, source_b))
        conn.commit()
        c.close()
        conn.close()
        #QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')




    def add_data_channels(self):

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
        #QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')


    def add_data_angles(self):
        desg_a = self.designation_a.text()
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
                                  ,?,?,?)''',
                  (desg_a, mass_a, area_a, axb_a, t_a, r1_a, r2_a, cz_a, cy_a, tan_a, iz_a, iy_a, iu_a, iv_a,
                   rz_a, ry_a, ru_a, rv_a,
                   zz_a, zy_a, zpz_a, zpy_a, source_a))

        conn.commit()
        c.close()
        conn.close()
        #QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')


