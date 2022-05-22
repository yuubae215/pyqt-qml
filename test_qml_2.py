from PyQt5.QtGui import QGuiApplication, QColor, QPen, QPainter
from PyQt5.QtQuick import QQuickView, QQuickPaintedItem
from PyQt5.QtCore import QUrl, QObject, pyqtSignal
from PyQt5.QtQml import qmlRegisterType

import os
import sys

class PieChart (QQuickPaintedItem):
    def __init__(self, parent = None):
        QQuickPaintedItem.__init__(self, parent)
        self.color = QColor()
    def paint(self, painter):
        pen = QPen(self.color, 2)
        painter.setPen(pen)
        painter.setRenderHints(QPainter.Antialiasing, True)
        # From drawPie(const QRect &rect, int startAngle, int spanAngle)
        painter.drawPie(self.boundingRect().adjusted(1,1,-1,-1), 90 * 16, 290 * 16)

    def getColor(self):
        return self.color

    def setColor(self, value):
        if value != self.color:
            self.color = value
            self.update()
            self.colorChanged.emit()

    colorChanged = pyqtSignal()
    color = QObject.property(QColor, getColor, setColor, notify=colorChanged)

app = QGuiApplication(sys.argv)

qmlRegisterType(PieChart, 'Charts', 1, 0, 'PieChart')

view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)

current_path = os.path.abspath(os.path.dirname(__file__))
qml_file = os.path.join(current_path, 'app_2.qml')
view.setSource(QUrl.fromLocalFile(qml_file))

if view.status() == QQuickView.Error:
    sys.exit(-1)

view.show()
res = app.exec_()
del view
sys.exit(res)
