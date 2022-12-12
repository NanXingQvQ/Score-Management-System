
from PyQt6.QtGui import QStandardItem, QColor, QBrush, QPalette, QPainter
from PyQt6.QtSql import QSqlTableModel
from PyQt6.QtWidgets import QApplication, QAbstractItemDelegate, QStyledItemDelegate, QStyleOptionViewItem
from PyQt6.uic.properties import QtGui, QtCore


class my_item_delegate(QStyledItemDelegate):
    def __init__(self):
        super(my_item_delegate, self).__init__()

    def paint(self, painter, option, index):
        if(index.row()%2==0):
            painter.setPen(QColor(255,255,255))
            painter.setBrush(QBrush(QColor(239,244,249)))
        else:
            painter.setPen(QColor(255, 255, 255))
            painter.setBrush(QBrush(QColor(154, 215, 255)))
        painter.drawRect(option.rect.x(), option.rect.y(), option.rect.width(), option.rect.height())
        super().paint(painter,option,index)