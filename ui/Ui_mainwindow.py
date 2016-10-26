# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fsk/Entwicklung/pywawi/ui/mainwindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(637, 491)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tab1wid = QtGui.QGridLayout()
        self.tab1wid.setObjectName(_fromUtf8("tab1wid"))
        self.verticalLayout_2.addLayout(self.tab1wid)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tab2wid = QtGui.QGridLayout()
        self.tab2wid.setObjectName(_fromUtf8("tab2wid"))
        self.verticalLayout_3.addLayout(self.tab2wid)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 637, 30))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDatei = QtGui.QMenu(self.menuBar)
        self.menuDatei.setObjectName(_fromUtf8("menuDatei"))
        self.menuBearbeiten = QtGui.QMenu(self.menuBar)
        self.menuBearbeiten.setObjectName(_fromUtf8("menuBearbeiten"))
        self.menuAuswerten = QtGui.QMenu(self.menuBar)
        self.menuAuswerten.setObjectName(_fromUtf8("menuAuswerten"))
        self.menuHilfe = QtGui.QMenu(self.menuBar)
        self.menuHilfe.setObjectName(_fromUtf8("menuHilfe"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionProcess = QtGui.QAction(MainWindow)
        self.actionProcess.setObjectName(_fromUtf8("actionProcess"))
        self.actionSankey = QtGui.QAction(MainWindow)
        self.actionSankey.setObjectName(_fromUtf8("actionSankey"))
        self.actionColumns = QtGui.QAction(MainWindow)
        self.actionColumns.setObjectName(_fromUtf8("actionColumns"))
        self.actionSaveas = QtGui.QAction(MainWindow)
        self.actionSaveas.setObjectName(_fromUtf8("actionSaveas"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSensitivities = QtGui.QAction(MainWindow)
        self.actionSensitivities.setObjectName(_fromUtf8("actionSensitivities"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuDatei.addAction(self.actionNew)
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionSave)
        self.menuDatei.addAction(self.actionSaveas)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionClose)
        self.menuDatei.addAction(self.actionExit)
        self.menuBearbeiten.addAction(self.actionCut)
        self.menuBearbeiten.addAction(self.actionCopy)
        self.menuBearbeiten.addAction(self.actionPaste)
        self.menuAuswerten.addAction(self.actionProcess)
        self.menuAuswerten.addSeparator()
        self.menuAuswerten.addAction(self.actionSankey)
        self.menuAuswerten.addAction(self.actionColumns)
        self.menuAuswerten.addAction(self.actionSensitivities)
        self.menuHilfe.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuBearbeiten.menuAction())
        self.menuBar.addAction(self.menuAuswerten.menuAction())
        self.menuBar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyWaWi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Neu CtrlWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Neu FCWidget", None))
        self.menuDatei.setTitle(_translate("MainWindow", "Da&tei", None))
        self.menuBearbeiten.setTitle(_translate("MainWindow", "Bearbeite&n", None))
        self.menuAuswerten.setTitle(_translate("MainWindow", "A&uswerten", None))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hi&lfe", None))
        self.actionNew.setText(_translate("MainWindow", "&Neu", None))
        self.actionOpen.setText(_translate("MainWindow", "&Öffnen", None))
        self.actionSave.setText(_translate("MainWindow", "&Speichern", None))
        self.actionClose.setText(_translate("MainWindow", "S&chließen", None))
        self.actionCut.setText(_translate("MainWindow", "&Ausschneiden", None))
        self.actionCopy.setText(_translate("MainWindow", "&Kopieren", None))
        self.actionProcess.setText(_translate("MainWindow", "&Flüsse berechnen (process)", None))
        self.actionSankey.setText(_translate("MainWindow", "&Sankey-Diagramm", None))
        self.actionColumns.setText(_translate("MainWindow", "&Balkendiagramm", None))
        self.actionSaveas.setText(_translate("MainWindow", "Speichern &als...", None))
        self.actionExit.setText(_translate("MainWindow", "&Beenden", None))
        self.actionPaste.setText(_translate("MainWindow", "&Einfügen", None))
        self.actionSensitivities.setText(_translate("MainWindow", "S&ensitivitäten", None))
        self.actionAbout.setText(_translate("MainWindow", "&Über", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

