#from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import QApplication
from pyqtgraph.Qt import QtGui 
# from pyqtgraph.flowchart import Flowchart ,  FlowchartCtrlWidget ,  FlowchartWidget
from ui.mainwindow import MainWindow
#from ui.dialog import Dialog
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


    
    
