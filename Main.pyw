import sqlite3
from PyQt4 import QtCore, QtGui
import GUI
import sys
from openpyxl import load_workbook   # Importing SQLite3, PyQt4, Gui - file made with QtDesigner, sys, openpyxl to work with Excel table.
from datetime import datetime

con = sqlite3.connect("Pumps.db")
cur = con.cursor()      # Connecting with database and make a cursor
cur_load = con.cursor()

wb = load_workbook('Orders.xlsx')
ws = wb.get_sheet_by_name('Main')

app = QtGui.QApplication(sys.argv)
Dialog = QtGui.QWidget()
ui = GUI.Ui_Dialog()
ui.setupUi(Dialog)
Dialog.setFixedSize(645, 692)
Dialog.setWindowIcon(QtGui.QIcon('5571.ico'))   # Making application and setting it right

count_press = 2

QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL("clicked()"), lambda: count())
QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL("clicked()"), Dialog, QtCore.SLOT('close()'))
QtCore.QObject.connect(ui.pushButton_3, QtCore.SIGNAL("clicked()"), lambda: full(ui))
QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL("clicked()"), lambda: stock(ui))
QtCore.QObject.connect(ui.comboBox, QtCore.SIGNAL("activated(const QString&)"), lambda: load(ui))   # Connecting functions with widgets


def count():      # Making function to count SQLite3 data
    global wb, ws
    if ui.comboBox.currentText() == '50НР4':
        condition = "Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР6.3':
        condition = "Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР10':
        condition = "Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР14':
        condition = "Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР16':
        condition = "Pumps = '50НР16' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1'"
    elif ui.comboBox.currentText() == '50НР32':
        condition = "Pumps = '50НР32' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1'"
    cur.execute("""UPDATE Details SET Stock = Stock - Needed WHERE %s""" % condition)
    cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
    con.commit()

    customer = QtGui.QInputDialog()
    a = customer.getText(customer, 'Введите ФИО/Компанию заказчика', 'ФИО/Компания')
    data_add = (ui.comboBox.currentText(), datetime.today().date())
    final_data = a[:1] + data_add
    ws.append(final_data)
    wb.save('Orders.xlsx')


def full(ui):       # Making function to increase amount of parts
    global count_press
    if ui.comboBox.currentText() == '50НР4':
        condition = "(Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    elif ui.comboBox.currentText() == '50НР6.3':
        condition = "(Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    elif ui.comboBox.currentText() == '50НР10':
        condition = "(Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    elif ui.comboBox.currentText() == '50НР14':
        condition = "(Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    elif ui.comboBox.currentText() == '50НР16':
        condition = "(Pumps = '50НР16' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    elif ui.comboBox.currentText() == '50НР32':
        condition = "(Pumps = '50НР32' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1')"
        cur.execute("""SELECT Part FROM Details WHERE %s ORDER BY Part""" % condition)
    if count_press % 2 == 0:
        ui.comboBox_2.setEnabled(True)
        ui.spinBox.setEnabled(True)

        for row in cur.fetchall():
            ui.comboBox_2.addItem(row[0])

    elif count_press % 2 != 0:
        ui.comboBox_2.setDisabled(True)
        ui.spinBox.setDisabled(True)
        spin_value = ui.spinBox.value()
        if ui.comboBox_2.currentText() == 'Корпус':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Корпус' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Крышка передняя':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Крышка передняя' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Крышка задняя':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Крышка задняя' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Шайбы гров М8':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Шайбы гров М8' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Шарик 11,112':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Шарик 11,112' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Подшипник 310':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Подшипник 310' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Манжета 38х58':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Манжета 38х58' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Винты М8х25':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Винты М8х25' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Кольцо передней крышки':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Кольцо передней крышки' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Кольцо ст. 3':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Кольцо ст. 3' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Корпус клапана':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Корпус клапана' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Седло клапана':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Седло клапана' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Колпачок':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Колпачок' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Прокладка паронит':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Прокладка паронит' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Кольцо замковое':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Кольцо замковое' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Противовес':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Противовес' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Вал':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Вал' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Пружина':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Пружина' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Подпятник':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Подпятник' AND %s""" % condition, (spin_value,))
        elif ui.comboBox_2.currentText() == 'Поршень':
            cur.execute("""UPDATE Details SET Stock = Stock + ? WHERE Part = 'Поршень' AND %s""" % condition, (spin_value,))
        ui.spinBox.setValue(0)
        ui.comboBox_2.clear()
    count_press += 1


def stock(ui):      # Making function to show full stock
    cur.execute("""SELECT Part, Stock, Pumps FROM Details""")
    ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Насос'))
    for row,form in enumerate(cur):
        ui.tableWidget.removeRow(row)
        ui.tableWidget.insertRow(row)
        for column, item in enumerate(form):
            ui.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(str(item)))


def load(ui):       # Making function to insert data into QTableWidget
    ui.tableWidget.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem('Требуется'))
    if ui.comboBox.currentText() == '50НР4':
        cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР4' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
    elif ui.comboBox.currentText() == '50НР6.3':
        cur.execute("""UPDATE Details SET Needed = 5 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР6' OR Pumps = '50НР4/6' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
    elif ui.comboBox.currentText() == '50НР10':
        cur.execute("""UPDATE Details SET Needed = 3 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР10' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
    elif ui.comboBox.currentText() == '50НР14':
        cur.execute("""UPDATE Details SET Needed = 10 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР14' OR Pumps = '50НР4/6/14' OR Pumps = 'All' OR Pumps = 'All1' GROUP BY Part""")
    elif ui.comboBox.currentText() == '50НР16':
        cur.execute("""UPDATE Details SET Needed = 5 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР16' OR Pumps = '50НР10/16' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1' ORDER BY Part""")
    elif ui.comboBox.currentText() == '50НР32':
        cur.execute("""UPDATE Details SET Needed = 10 WHERE Pumps = 'All'""")
        cur_load.execute("""SELECT Part, Stock, Needed FROM Details WHERE Pumps = '50НР32' OR Pumps = '50НР10/16/32' OR Pumps = 'All' OR Pumps = 'All1' ORDER BY Part""")
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
