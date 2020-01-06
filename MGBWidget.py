# -*- coding: utf-8 -*-
"""
 ***************************************************************************
    MBG

    Processing
                             -------------------
        begin                : 2017-07-01
        updated              : 2019-10-28 by Leonardo Laipelt
        copyright            : (C) 2017 by HGE-IPH
        email                : martinbiancho@hotmail.com
 ***************************************************************************

 ***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************
"""

import os

from PyQt5 import QtGui, uic
from PyQt5.QtCore import pyqtSignal


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'MGBWidget.ui'))

FORM_CLASS2, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'MGBWidget2.ui'))

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from qgis.core import QgsProject

class Widget(QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

class Widget2(QDialog, FORM_CLASS2):
    def __init__(self, parent=None):
        """Constructor."""
        super(Widget2, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
