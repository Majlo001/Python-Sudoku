# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Majlo\Gitbin\Python-Games\ui_files\sudoku_game.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sudoku(object):
    def setupUi(self, Sudoku):
        Sudoku.setObjectName("Sudoku")
        Sudoku.resize(792, 778)
        Sudoku.setStyleSheet("")
        self.SudokuTable = QtWidgets.QTableWidget(Sudoku)
        self.SudokuTable.setGeometry(QtCore.QRect(120, 90, 541, 541))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SudokuTable.setFont(font)
        self.SudokuTable.setMouseTracking(False)
        self.SudokuTable.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.SudokuTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SudokuTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SudokuTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SudokuTable.setAlternatingRowColors(False)
        self.SudokuTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.SudokuTable.setTextElideMode(QtCore.Qt.ElideLeft)
        self.SudokuTable.setShowGrid(True)
        self.SudokuTable.setGridStyle(QtCore.Qt.DashLine)
        self.SudokuTable.setWordWrap(False)
        self.SudokuTable.setCornerButtonEnabled(True)
        self.SudokuTable.setRowCount(9)
        self.SudokuTable.setColumnCount(9)
        self.SudokuTable.setObjectName("SudokuTable")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.SudokuTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        brush = QtGui.QBrush(QtGui.QColor(222, 222, 222))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 238, 100))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.SudokuTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(57, 208, 22))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.SudokuTable.setItem(1, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(2, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(4, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(5, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(6, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.SudokuTable.setItem(6, 7, item)
        self.SudokuTable.horizontalHeader().setVisible(False)
        self.SudokuTable.horizontalHeader().setDefaultSectionSize(60)
        self.SudokuTable.horizontalHeader().setHighlightSections(False)
        self.SudokuTable.horizontalHeader().setMinimumSectionSize(10)
        self.SudokuTable.verticalHeader().setVisible(False)
        self.SudokuTable.verticalHeader().setDefaultSectionSize(60)
        self.SudokuTable.verticalHeader().setHighlightSections(False)
        self.SudokuTable.verticalHeader().setMinimumSectionSize(10)
        self.vline1 = QtWidgets.QFrame(Sudoku)
        self.vline1.setGeometry(QtCore.QRect(280, 90, 41, 541))
        self.vline1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline1.setLineWidth(3)
        self.vline1.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline1.setObjectName("vline1")
        self.vline2 = QtWidgets.QFrame(Sudoku)
        self.vline2.setGeometry(QtCore.QRect(460, 90, 41, 541))
        self.vline2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.vline2.setLineWidth(3)
        self.vline2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline2.setObjectName("vline2")
        self.hline1 = QtWidgets.QFrame(Sudoku)
        self.hline1.setGeometry(QtCore.QRect(120, 260, 541, 16))
        self.hline1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline1.setLineWidth(3)
        self.hline1.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline1.setObjectName("hline1")
        self.hline2 = QtWidgets.QFrame(Sudoku)
        self.hline2.setGeometry(QtCore.QRect(120, 440, 541, 16))
        self.hline2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hline2.setLineWidth(3)
        self.hline2.setMidLineWidth(0)
        self.hline2.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline2.setObjectName("hline2")
        self.timerLabel = QtWidgets.QLabel(Sudoku)
        self.timerLabel.setGeometry(QtCore.QRect(510, 20, 151, 51))
        self.timerLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        self.difficultyLabel = QtWidgets.QLabel(Sudoku)
        self.difficultyLabel.setGeometry(QtCore.QRect(130, 20, 151, 51))
        self.difficultyLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.difficultyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.clearButton = QtWidgets.QPushButton(Sudoku)
        self.clearButton.setGeometry(QtCore.QRect(120, 640, 121, 51))
        self.clearButton.setObjectName("clearButton")
        self.checkButton = QtWidgets.QPushButton(Sudoku)
        self.checkButton.setGeometry(QtCore.QRect(540, 640, 121, 51))
        self.checkButton.setObjectName("checkButton")
        self.pauseButton = QtWidgets.QPushButton(Sudoku)
        self.pauseButton.setGeometry(QtCore.QRect(360, 640, 61, 51))
        self.pauseButton.setObjectName("pauseButton")

        self.retranslateUi(Sudoku)
        QtCore.QMetaObject.connectSlotsByName(Sudoku)

    def retranslateUi(self, Sudoku):
        _translate = QtCore.QCoreApplication.translate
        Sudoku.setWindowTitle(_translate("Sudoku", "Form"))
        self.SudokuTable.setSortingEnabled(False)
        __sortingEnabled = self.SudokuTable.isSortingEnabled()
        self.SudokuTable.setSortingEnabled(False)
        self.SudokuTable.setSortingEnabled(__sortingEnabled)
        self.timerLabel.setText(_translate("Sudoku", "TIMER"))
        self.difficultyLabel.setText(_translate("Sudoku", "EASY"))
        self.clearButton.setText(_translate("Sudoku", "Clear"))
        self.checkButton.setText(_translate("Sudoku", "Check"))
        self.pauseButton.setText(_translate("Sudoku", "Pause"))