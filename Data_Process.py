# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys

import csv
import numpy as np
import pandas as pd
from scipy.stats import norm
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDoubleSpinBox,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel
)

"""This example implements the interaction between Qt Widgets and a 2D
matplotlib plot showing a gaussian curve with scipy"""


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #  create widgets
        # self.view_single = FigureCanvas(Figure(figsize=(8, 6)))
        self.view_double = FigureCanvas(Figure(figsize=(8, 6)))
        # self.axes_single = self.view_single.figure.subplots()
        self.axes_double = self.view_double.figure.subplots()
        # self.toolbar_single = NavigationToolbar2QT(self.view_single, self)
        self.toolbar_double = NavigationToolbar2QT(self.view_double, self)
        self.qspinbox_num = QSpinBox()
        self.pushButton_single = QPushButton()
        self.pushButton_double = QPushButton()
        self.pushButton_single.setText("单组数据")
        self.pushButton_double.setText("绘制有效值折线图")
        self.lineEdit_frequency = QLineEdit()
        self.label_frequency = QLabel()
        self.label_num = QLabel()
        self.label_num.setText('Num of Groups')
        self.label_frequency.setText('Sample frequency')

        #  Create layout
        input_layout = QHBoxLayout()
        # input_layout.addWidget(self.pushButton_single)
        input_layout.addWidget(self.pushButton_double)
        input_layout.addWidget(self.label_num)
        input_layout.addWidget(self.qspinbox_num)
        input_layout.addWidget(self.label_frequency)
        input_layout.addWidget(self.lineEdit_frequency)
        vlayout = QVBoxLayout()
        # vlayout.addWidget(self.toolbar_single)
        # vlayout.addWidget(self.view_single)
        vlayout.addWidget(self.toolbar_double)
        vlayout.addWidget(self.view_double)
        vlayout.addLayout(input_layout)
        self.setLayout(vlayout)

        # connect inputs with on_change method
        # self.pushButton_single.clicked.connect(self.pushButton_single_clicked)
        self.pushButton_double.clicked.connect(self.pushButton_double_clicked)
        self.qspinbox_num.valueChanged.connect(self.qspinbox_num_clicked)
        self.lineEdit_frequency.textChanged.connect(self.lineEdit_frequency_changed)

    @Slot()
    def on_change(self):
        """ Update the plot with the current input values """
        effective = []
        for i in range(6):
            file_name = str(1) + '-' + str((i + 1) * 500) + '.csv'
            data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
            data_ = data_.to_numpy()
            data = np.asarray(data_[:, 0], dtype=float)
            effective_value = np.sqrt(np.mean(data ** 2))
            print(effective_value)
            effective.append(effective_value)
        x = [500, 1000, 1500, 2000, 2500, 3000]
        print(x)
        y = effective
        self.axes_single.clear()
        self.axes_single.plot(x, y)
        self.view_single.draw()

    @Slot()
    def pushButton_single_clicked(self):
        """ Update the plot with the current input values """
        effective = []
        num = int(self.num)
        for i in range(6):
            file_name = str(1) + '-' + str((i + 1) * 500) + '.csv'
            data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
            data_ = data_.to_numpy()
            data = np.asarray(data_[:, 0], dtype=float)
            effective_value = np.sqrt(np.mean(data ** 2))
            print(effective_value)
            effective.append(effective_value)
        x = [500, 1000, 1500, 2000, 2500, 3000]
        y = effective
        self.axes_single.clear()
        self.axes_single.plot(x, y)
        self.axes_single.set_title('Acceleration a --- Rotate speed n')
        self.axes_single.set_ylabel('Acceleration a\g')
        self.axes_single.set_xlabel('Rotate speed n\(r/min)')
        self.view_single.draw()

    @Slot()
    def pushButton_double_clicked(self):
        effective = [[], [], [], [], []]
        x = [500, 1000, 1500, 2000, 2500, 3000]
        num = int(self.num)
        self.axes_double.clear()

        # with open('results.csv', 'w', newline='') as csvfile:
        csvfile = open('results.csv', 'w', newline='')
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['测试有效值分析结果'])
        spamwriter.writerow(['加速度(g)/转速(r/min)', 500, 1000, 1500, 2000, 2500, 3000])
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        for j in range(num):
            for i in range(6):
                file_name = str(j + 1) + '-' + str((i + 1) * 500) + '.csv'
                data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
                data_ = data_.to_numpy()
                frequency = self.frequency
                data = np.asarray(data_[0:int(60 * frequency), 0], dtype=float)
                effective_value = np.sqrt(np.mean(data ** 2))
                effective[j].append(effective_value)
            print(effective[j])
            spamwriter.writerow(
                ['第' + str(j + 1) + '组', effective[j][0], effective[j][1], effective[j][2], effective[j][3],
                 effective[j][4], effective[j][5]])
            self.axes_double.plot(x, effective[j], label=str(j + 1))
        # self.axes_double.plot(x, effective[0], label='1')
        # self.axes_double.plot(x, effective[1], label='2')
        self.axes_double.set_title('Acceleration a --- Rotate speed n')
        self.axes_double.set_ylabel('Acceleration a\g')
        self.axes_double.set_xlabel('Rotate speed n\(r/min)')
        self.axes_double.legend()
        self.view_double.draw()

    @Slot()
    def lineEdit_frequency_changed(self):
        self.frequency = self.lineEdit_frequency.text()

    @Slot()
    def qspinbox_num_clicked(self):
        self.num = self.qspinbox_num.value()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PlotWidget()
    w.show()
    sys.exit(app.exec())
