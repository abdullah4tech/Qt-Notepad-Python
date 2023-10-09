from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 821, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 821, 581))
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuZoom = QtWidgets.QMenu(self.menuView)
        self.menuZoom.setObjectName("menuZoom")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut(QtGui.QKeySequence.New)
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionNew_Window.setShortcut(QtGui.QKeySequence.New)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut(QtGui.QKeySequence.Open)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut(QtGui.QKeySequence.Save)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave_as.setShortcut(QtGui.QKeySequence.SaveAs)
        self.actionPage_Setup = QtWidgets.QAction(MainWindow)
        self.actionPage_Setup.setObjectName("actionPage_Setup")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint.setShortcut(QtGui.QKeySequence.Print)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut(QtGui.QKeySequence.Undo)
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.setShortcut(QtGui.QKeySequence.Cut)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.setShortcut(QtGui.QKeySequence.Copy)
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.setShortcut(QtGui.QKeySequence.Paste)
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setShortcut(QtGui.QKeySequence.Delete)
        self.actionSearch_with_Bing = QtWidgets.QAction(MainWindow)
        self.actionSearch_with_Bing.setObjectName("actionSearch_with_Bing")
        self.actionSearch_with_Bing.setShortcut(QtGui.QKeySequence.Find)
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionFind.setShortcut(QtGui.QKeySequence.Find)
        self.actionFind_Previous = QtWidgets.QAction(MainWindow)
        self.actionFind_Previous.setObjectName("actionFind_Previous")
        self.actionFind_Previous.setShortcut(QtGui.QKeySequence.FindNext)
        self.actionFind_Previous_2 = QtWidgets.QAction(MainWindow)
        self.actionFind_Previous_2.setObjectName("actionFind_Previous_2")
        self.actionFind_Previous_2.setShortcut(QtGui.QKeySequence.FindPrevious)
        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.actionReplace.setShortcut(QtGui.QKeySequence.Replace)
        self.actionGo_To = QtWidgets.QAction(MainWindow)
        self.actionGo_To.setObjectName("actionGo_To")
        self.actionGo_To.setShortcut(QKeySequence.fromString("Ctrl+G"))
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSelect_All.setShortcut(QtGui.QKeySequence.SelectAll)
        self.actionTime_Date = QtWidgets.QAction(MainWindow)
        self.actionTime_Date.setObjectName("actionTime_Date")
        self.actionTime_Date.setShortcut(QtGui.QKeySequence.Refresh)
        self.actionWord_Wrap = QtWidgets.QAction(MainWindow)
        self.actionWord_Wrap.setObjectName("actionWord_Wrap")
        self.actionFonts = QtWidgets.QAction(MainWindow)
        self.actionFonts.setObjectName("actionFonts")
        self.actionStatus_Bar = QtWidgets.QAction(MainWindow)
        self.actionStatus_Bar.setCheckable(True)
        self.actionStatus_Bar.setObjectName("actionStatus_Bar")
        self.actionView_Help = QtWidgets.QAction(MainWindow)
        self.actionView_Help.setObjectName("actionView_Help")
        self.actionSend_Feedback = QtWidgets.QAction(MainWindow)
        self.actionSend_Feedback.setObjectName("actionSend_Feedback")
        self.actionAbout_Notepad = QtWidgets.QAction(MainWindow)
        self.actionAbout_Notepad.setObjectName("actionAbout_Notepad")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_In.setShortcut(QtGui.QKeySequence.ZoomIn)
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_Out.setShortcut(QtGui.QKeySequence.ZoomOut)
        self.actionRestore_Default_Zoom = QtWidgets.QAction(MainWindow)
        self.actionRestore_Default_Zoom.setObjectName("actionRestore_Default_Zoom")
        self.actionRestore_Default_Zoom.setShortcut(QtGui.QKeySequence(0))  # No default shortcut
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPage_Setup)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSearch_with_Bing)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Previous)
        self.menuEdit.addAction(self.actionFind_Previous_2)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGo_To)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionTime_Date)
        self.menuFormat.addAction(self.actionWord_Wrap)
        self.menuFormat.addAction(self.actionFonts)
        self.menuZoom.addAction(self.actionZoom_In)
        self.menuZoom.addAction(self.actionZoom_Out)
        self.menuZoom.addAction(self.actionRestore_Default_Zoom)
        self.menuView.addAction(self.menuZoom.menuAction())
        self.menuView.addAction(self.actionStatus_Bar)
        self.menu.addAction(self.actionView_Help)
        self.menu.addAction(self.actionSend_Feedback)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout_Notepad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notepad"))
        self.textEdit.setHtml(_translate("MainWindow", "<html><head/><body/></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuZoom.setTitle(_translate("MainWindow", "Zoom"))
        self.menu.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionPage_Setup.setText(_translate("MainWindow", "Page Setup..."))
        self.actionPrint.setText(_translate("MainWindow", "Print..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSearch_with_Bing.setText(_translate("MainWindow", "Search with Bing"))
        self.actionFind.setText(_translate("MainWindow", "Find..."))
        self.actionFind_Previous.setText(_translate("MainWindow", "Find Next"))
        self.actionFind_Previous_2.setText(_translate("MainWindow", "Find Previous"))
        self.actionReplace.setText(_translate("MainWindow", "Replace..."))
        self.actionGo_To.setText(_translate("MainWindow", "Go To..."))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionTime_Date.setText(_translate("MainWindow", "Time/Date"))
        self.actionWord_Wrap.setText(_translate("MainWindow", "Word Wrap"))
        self.actionFonts.setText(_translate("MainWindow", "Fonts..."))
        self.actionStatus_Bar.setText(_translate("MainWindow", "Status Bar"))
        self.actionView_Help.setText(_translate("MainWindow", "View Help"))
        self.actionSend_Feedback.setText(_translate("MainWindow", "Send Feedback"))
        self.actionAbout_Notepad.setText(_translate("MainWindow", "About Notepad"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionRestore_Default_Zoom.setText(_translate("MainWindow", "Restore Default Zoom"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect actions to functions
        self.ui.actionNew.triggered.connect(self.new_document)
        self.ui.actionOpen.triggered.connect(self.open_document)
        self.ui.actionSave.triggered.connect(self.save_document)
        self.ui.actionSave_as.triggered.connect(self.save_document_as)
        self.ui.actionUndo.triggered.connect(self.undo)  # Connect undo to the undo method
        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionFind.triggered.connect(self.find)
        self.ui.actionReplace.triggered.connect(self.replace)
        self.ui.actionSelect_All.triggered.connect(self.select_all)
        self.ui.actionWord_Wrap.toggled.connect(self.toggle_word_wrap)
        self.ui.actionGo_To.triggered.connect(self.go_to_line)

    def new_document(self):
        self.ui.textEdit.clear()

    def go_to_line(self):
        text, ok = QtWidgets.QInputDialog.getText(
            self, "Go To Line", "Go to line:")
        if ok and text:
            try:
                line_number = int(text)
                cursor = self.ui.textEdit.textCursor()
                cursor.setPosition(0)  # Move to the beginning
                cursor.movePosition(QtGui.QTextCursor.Down, QtGui.QTextCursor.MoveAnchor, line_number - 1)  # Go to the specified line
                self.ui.textEdit.setTextCursor(cursor)
            except ValueError:
                QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid line number.")

    def copy(self):
        self.ui.textEdit.copy()

    def paste(self):
        self.ui.textEdit.paste()

    def select_all(self):
        self.ui.textEdit.selectAll()

    def open_document(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                self.ui.textEdit.setPlainText(file.read())

    def save_document(self):
        if hasattr(self, "current_file"):
            with open(self.current_file, "w") as file:
                file.write(self.ui.textEdit.toPlainText())
        else:
            self.save_document_as()

    def save_document_as(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File As", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            self.current_file = file_name
            self.save_document()

    def find(self):
        text, ok = QtWidgets.QInputDialog.getText(
            self, "Find", "Find:")
        if ok and text:
            cursor = self.ui.textEdit.textCursor()
            cursor.movePosition(QtGui.QTextCursor.Start)
            while cursor.movePosition(QtGui.QTextCursor.NextWord, QtGui.QTextCursor.KeepAnchor):
                if text == cursor.selectedText():
                    self.ui.textEdit.setTextCursor(cursor)
                    break

    def replace(self):
        find_text, ok = QtWidgets.QInputDialog.getText(
            self, "Find", "Find:")
        if not ok or not find_text:
            return

        replace_text, ok = QtWidgets.QInputDialog.getText(
            self, "Replace", "Replace with:")
        if not ok:
            return

        cursor = self.ui.textEdit.textCursor()
        cursor.beginEditBlock()

        while cursor.movePosition(QtGui.QTextCursor.Start):
            if cursor.selectedText() == find_text:
                cursor.removeSelectedText()
                cursor.insertText(replace_text)

        cursor.endEditBlock()

    def undo(self):
        self.ui.textEdit.undo()

    def cut(self):
        self.ui.textEdit.cut()

    def toggle_word_wrap(self):
        self.ui.textEdit.setLineWrapMode(
            QtWidgets.QTextEdit.WidgetWidth if self.ui.actionWord_Wrap.isChecked() else QtWidgets.QTextEdit.NoWrap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
