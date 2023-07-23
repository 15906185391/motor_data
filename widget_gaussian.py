# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys

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
        self.view_single = FigureCanvas(Figure(figsize=(8, 6)))
        self.view_double = FigureCanvas(Figure(figsize=(8, 6)))
        self.axes_single = self.view_single.figure.subplots()
        self.axes_double = self.view_double.figure.subplots()
        self.toolbar_single = NavigationToolbar2QT(self.view_single, self)
        self.toolbar_double = NavigationToolbar2QT(self.view_double, self)
        self.pushButton_single = QPushButton()
        self.pushButton_double = QPushButton()
        self.pushButton_single.setText("单组数据")
        self.pushButton_double.setText("双组数据")
        self.lineEdit_frequency = QLineEdit()
        self.label_frequency = QLabel()
        self.label_frequency.setText('Sample frequency')

        #  Create layout
        input_layout = QHBoxLayout()
        # input_layout.addWidget(self.mu_input)
        # input_layout.addWidget(self.std_input)
        input_layout.addWidget(self.pushButton_single)
        input_layout.addWidget(self.pushButton_double)
        input_layout.addWidget(self.label_frequency)
        input_layout.addWidget(self.lineEdit_frequency)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar_single)
        vlayout.addWidget(self.view_single)
        vlayout.addWidget(self.toolbar_double)
        vlayout.addWidget(self.view_double)
        vlayout.addLayout(input_layout)
        self.setLayout(vlayout)

        # connect inputs with on_change method
        # self.mu_input.valueChanged.connect(self.on_change)
        # self.std_input.valueChanged.connect(self.on_change)
        self.pushButton_single.clicked.connect(self.pushButton_single_clicked)
        self.pushButton_double.clicked.connect(self.pushButton_double_clicked)
        self.lineEdit_frequency.textChanged.connect(self.lineEdit_frequency_changed)

        # self.on_change()

    @Slot()
    def on_change(self):
        """ Update the plot with the current input values """
        effective = []
        for i in range(6):
            print(i + 1)
            file_name = str(1) + '-' + str((i + 1) * 500) + '.csv'
            # data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
            data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
            print(data_)
            data_ = data_.to_numpy()
            data = np.asarray(data_[:, 0], dtype=float)
            effective_value = np.sqrt(np.mean(data ** 2))
            print(effective_value)
            effective.append(effective_value)
        # mu = self.mu_input.value()
        # std = self.std_input.value()
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
        for i in range(6):
            print(i + 1)
            file_name = str(1) + '-' + str((i + 1) * 500) + '.csv'
            # data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
            data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
            print(data_)
            data_ = data_.to_numpy()
            data = np.asarray(data_[:, 0], dtype=float)
            effective_value = np.sqrt(np.mean(data ** 2))
            print(effective_value)
            effective.append(effective_value)
        # mu = self.mu_input.value()
        # std = self.std_input.value()
        x = [500, 1000, 1500, 2000, 2500, 3000]
        print(x)
        y = effective
        self.axes_single.clear()
        self.axes_single.plot(x, y)
        self.axes_single.set_title('Acceleration a --- Rotate speed n')
        self.axes_single.set_ylabel('Acceleration a\g')
        self.axes_single.set_xlabel('Rotate speed n\(r/min)')
        self.view_single.draw()

    @Slot()
    def pushButton_double_clicked(self):
        effective = [[], []]
        for j in range(2):
            # print(j)
            for i in range(6):
                # print(i+1)
                file_name = str(j + 1) + '-' + str((i + 1) * 500) + '.csv'
                # data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
                data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
                # print(data_)
                data_ = data_.to_numpy()
                frequency = self.frequency
                data = np.asarray(data_[0:int(20 * frequency), 0], dtype=float)
                effective_value = np.sqrt(np.mean(data ** 2))
                # print(effective_value)
                effective[j].append(effective_value)

            print(effective[j])
        x = [500, 1000, 1500, 2000, 2500, 3000]
        self.axes_double.clear()
        self.axes_double.plot(x, effective[0], label='1')
        self.axes_double.plot(x, effective[1], label='2')
        self.axes_double.set_title('Acceleration a --- Rotate speed n')
        self.axes_double.set_ylabel('Acceleration a\g')
        self.axes_double.set_xlabel('Rotate speed n\(r/min)')
        self.axes_double.legend()
        self.view_double.draw()

    @Slot()
    def lineEdit_frequency_changed(self):
        # print(self.lineEdit_frequency.text())
        self.frequency = self.lineEdit_frequency.text()
        print(self.frequency)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PlotWidget()
    w.show()
    sys.exit(app.exec())
