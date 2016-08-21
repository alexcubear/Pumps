import sqlite3
from PyQt4 import QtCore, QtGui
import GUI
import sys      ## Importing SQLite3, PyQt4, Gui - file made with QtDesigner, sys.


con = sqlite3.connect("Pumps.db")
cur = con.cursor()      ## Connecting with database and make a cursor
cur_load = con.cursor()

app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QWidget()
ui = GUI.Ui_Dialog()
ui.setupUi(Dialog)
Dialog.setFixedSize(645, 692)
Dialog.setWindowIcon(QtGui.QIcon('5571.ico')) ## Making application and setting it right
count_press = 2
arow = 0



QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), lambda: count())
QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL("clicked()"), Dialog, QtCore.SLOT('close()'))
QtCore.QObject.connect(ui.pushButton_3, QtCore.SIGNAL("clicked()"), lambda: full(ui))
QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL("clicked()"), lambda: stock(ui))
QtCore.QObject.connect(ui.comboBox, QtCore.SIGNAL("activated(const QString&)"), lambda: load(ui)) ## Connecting functions with widgets


def count():      ## Making function to count SQLite3 data
    global condition
    if ui.comboBox.currentText() == '50НР4':
        condition = "Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР6.3':
        condition = "Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР10':
        condition = "Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР14':
        condition = "Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    print(condition)
    cur.execute("""UPDATE Details SET Stock = Stock - Needed WHERE %s""" % condition)
    cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
    con.commit()

    msg = QtGui.QInputDialog()
    a = msg.getText(msg, 'Введите', 'Введите')
    print(a)


def full(ui):       ## Making function to increase amount of parts
    global count_press
    arow = 0
    i = []
    if ui.comboBox.currentText() == '50НР4':
        condition = "Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР6.3':
        condition = "Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР10':
        condition = "Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР14':
        condition = "Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    if count_press % 2 == 0:
        ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Изменить на:"))
        for table_row in range(0, 20):
            ui.tableWidget.setCellWidget(table_row, 2, QtGui.QSpinBox())
    elif count_press % 2 != 0:
        ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Требуется"))
        for table_row in range(0, 20):
            spin_value = ui.tableWidget.cellWidget(arow, 2).value()
            i.append(spin_value)
            ui.tableWidget.removeCellWidget(table_row, 2)
            arow += 1
        i = i
        print(i)
        print(len(i))
        print(tuple(i))
        print(len((i,)))
        a = 0
        cur.execute("""SELECT ROWID FROM Details WHERE %s""" % condition)
        r = cur.fetchall()
        r = [(w,) for w in r]
        i = [(u,) for u in i]
        for row in r:
            for h in i:
                cur.executemany("""UPDATE Details SET Stock = Stock - ? WHERE ROWID = ?""", [r, i])
                a += 1
        con.commit()

    count_press += 1


def stock(ui):      ## Making function to show full stock
    cur.execute("""SELECT Part, Stock, Pumps FROM Details""")
    ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Насос'))
    for row,form in enumerate(cur):
        ui.tableWidget.removeRow(row)
        ui.tableWidget.insertRow(row)
        for column, item in enumerate(form):
            ui.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(str(item)))


def load(ui):       ## Making function to insert data into QTableWidget
    ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Требуется'))
    if ui.comboBox.currentText() == '50НР4':
        cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
        # cur.execute("""UPDATE Details SET Needed = 3 WHERE Needed = 3""")
    elif ui.comboBox.currentText() == '50НР6.3':
        cur.execute("""UPDATE Details SET Needed = 5 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
        # cur.execute("""UPDATE Details SET Needed = 3 WHERE Needed = 5""")
    elif ui.comboBox.currentText() == '50НР10':
        cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
        # cur.execute("""UPDATE Details SET Needed = 3 WHERE Needed = 3""")
    elif ui.comboBox.currentText() == '50НР14':
        cur.execute("""UPDATE Details SET Needed = 10 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
        # cur.execute("""UPDATE Details SET Needed = 3 WHERE Needed = 10 AND Pumps = 'All'""")
    ui.tableWidget.setRowCount(0)
    for row, form in enumerate(cur_load):
        ui.tableWidget.insertRow(row)
        for column, item in enumerate(form):
            ui.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(str(item)))
    con.commit()

Dialog.show()
ret = app.exec_()
cur.execute("""UPDATE Details SET Needed = 3 WHERE Needed = 10""")
cur.close()
con.close()
sys.exit(ret)
