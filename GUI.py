# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_try.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(645, 692)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(644, 691))
        Dialog.setMaximumSize(QtCore.QSize(646, 693))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 211, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBox.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        self.comboBox.setPalette(palette)
        font = QtGui.QFont()
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setUpdatesEnabled(True)
        self.comboBox.setVisible(True)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setWindowTitle(_fromUtf8(""))
        self.comboBox.setWindowIconText(_fromUtf8(""))
        self.comboBox.setWindowOpacity(1.0)
        self.comboBox.setWindowModified(False)
        self.comboBox.setToolTip(_fromUtf8(""))
        self.comboBox.setStatusTip(_fromUtf8(""))
        self.comboBox.setWhatsThis(_fromUtf8(""))
        self.comboBox.setAccessibleName(_fromUtf8(""))
        self.comboBox.setAccessibleDescription(_fromUtf8(""))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(_fromUtf8(""))
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.RussianFederation))
        self.comboBox.setWindowFilePath(_fromUtf8(""))
        self.comboBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setMaxCount(2147483647)
        self.comboBox.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setIconSize(QtCore.QSize(16, 16))
        self.comboBox.setAutoCompletion(True)
        self.comboBox.setAutoCompletionCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(250, 10, 381, 671))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 610, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setUpdatesEnabled(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setWindowTitle(_fromUtf8(""))
        self.pushButton_2.setWindowIconText(_fromUtf8(""))
        self.pushButton_2.setWindowOpacity(1.0)
        self.pushButton_2.setWindowModified(False)
        self.pushButton_2.setToolTip(_fromUtf8(""))
        self.pushButton_2.setStatusTip(_fromUtf8(""))
        self.pushButton_2.setWhatsThis(_fromUtf8(""))
        self.pushButton_2.setAccessibleName(_fromUtf8(""))
        self.pushButton_2.setAccessibleDescription(_fromUtf8(""))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.RussianFederation))
        self.pushButton_2.setWindowFilePath(_fromUtf8(""))
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setShortcut(_fromUtf8(""))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setDown(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 610, 101, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setUpdatesEnabled(True)
        self.pushButton.setVisible(True)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setWindowTitle(_fromUtf8(""))
        self.pushButton.setWindowIconText(_fromUtf8(""))
        self.pushButton.setWindowOpacity(1.0)
        self.pushButton.setWindowModified(False)
        self.pushButton.setToolTip(_fromUtf8(""))
        self.pushButton.setStatusTip(_fromUtf8(""))
        self.pushButton.setWhatsThis(_fromUtf8(""))
        self.pushButton.setAccessibleName(_fromUtf8(""))
        self.pushButton.setAccessibleDescription(_fromUtf8(""))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.RussianFederation))
        self.pushButton.setWindowFilePath(_fromUtf8(""))
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setShortcut(_fromUtf8(""))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setDown(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 650, 101, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_3.setUpdatesEnabled(True)
        self.pushButton_3.setVisible(True)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setWindowTitle(_fromUtf8(""))
        self.pushButton_3.setWindowIconText(_fromUtf8(""))
        self.pushButton_3.setWindowOpacity(1.0)
        self.pushButton_3.setWindowModified(False)
        self.pushButton_3.setToolTip(_fromUtf8(""))
        self.pushButton_3.setStatusTip(_fromUtf8(""))
        self.pushButton_3.setWhatsThis(_fromUtf8(""))
        self.pushButton_3.setAccessibleName(_fromUtf8(""))
        self.pushButton_3.setAccessibleDescription(_fromUtf8(""))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(_fromUtf8(""))
        self.pushButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.RussianFederation))
        self.pushButton_3.setWindowFilePath(_fromUtf8(""))
        self.pushButton_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setShortcut(_fromUtf8(""))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoRepeatDelay(300)
        self.pushButton_3.setAutoRepeatInterval(100)
        self.pushButton_3.setDown(False)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 650, 111, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 40, 151, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))

        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(180, 40, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Программа учета деталей", None))
        self.comboBox.setItemText(0, _translate("Dialog", "50НР4", None))
        self.comboBox.setItemText(1, _translate("Dialog", "50НР6.3", None))
        self.comboBox.setItemText(2, _translate("Dialog", "50НР10", None))
        self.comboBox.setItemText(3, _translate("Dialog", "50НР14", None))
        self.comboBox.setItemText(4, _translate("Dialog", "50НР16", None))
        self.comboBox.setItemText(5, _translate("Dialog", "50НР32", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Детали", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Склад", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Требуется", None))
        self.pushButton_2.setText(_translate("Dialog", "Выход", None))
        self.pushButton.setText(_translate("Dialog", "Выполнить заказ", None))
        self.pushButton_3.setText(_translate("Dialog", "Пополнить склад", None))
        self.pushButton_4.setText(_translate("Dialog", "Посмотреть склад", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

