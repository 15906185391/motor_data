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
)

"""This example implements the interaction between Qt Widgets and a 2D
matplotlib plot showing a gaussian curve with scipy"""


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #  create widgets
        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        self.mu_input = QDoubleSpinBox()
        self.std_input = QDoubleSpinBox()
        self.mu_input.setPrefix("μ: ")
        self.std_input.setPrefix("σ: ")
        self.std_input.setValue(10)

        #  Create layout
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.mu_input)
        input_layout.addWidget(self.std_input)
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        vlayout.addLayout(input_layout)
        self.setLayout(vlayout)

        # connect inputs with on_change method
        self.mu_input.valueChanged.connect(self.on_change)
        self.std_input.valueChanged.connect(self.on_change)

        self.on_change()

    @Slot()
    def on_change(self):
        """ Update the plot with the current input values """
        effective = []
        for i in range(6):
            print(i + 1)
            file_name = str(i + 1) + '.csv'
            # data_ = np.loadtxt(file_name, dtype=str, delimiter=',')
            data_ = pd.read_csv(file_name, encoding='gb2312', skiprows=4, low_memory=False)
            print(data_)
            data_ = data_.to_numpy()
            data = np.asarray(data_[:, 0], dtype=float)
            effective_value = np.sqrt(np.mean(data ** 2))
            print(effective_value)
            effective.append(effective_value)
        mu = self.mu_input.value()
        std = self.std_input.value()

        x = [500,1000,1500,2000,2500,3000]
        print(x)
        y = effective

        self.axes.clear()
        self.axes.plot(x, y)
        self.view.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PlotWidget()
    w.show()
    sys.exit(app.exec())
