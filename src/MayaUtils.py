from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtCore import Qt
import maya.OpenMayaUI as omui
import shiboken2
import maya.cmds as mc

def IsMesh(obj):
    shapes = mc.listRelatives(obj, s=True)
    if not shapes:
        return False
    
    for s in shapes:
        if mc.objectType(s) == "mesh":
            return True

    return False

def IsController(obj):
    shapes = mc.listRelatives(obj, s=True)
    if not shapes:
        return False
    
    for s in shapes:
        if mc.objectType(s) == "nurbsCurve":
            return True

    return False

def IsGroup(obj):
    shapes = mc.listRelatives(obj, s=True)
    if not shapes:
        return False
    
    for s in shapes:
        if len(shapes) == 0:
            return True

    return False

def GetMayaMainWindow()->QMainWindow:
    mainWindow = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(mainWindow), QMainWindow)

def DeleteWidgetWithName(name):
    for widget in GetMayaMainWindow().findChildren(QWidget, name):
        widget.deleteLater()

class MayaWindow(QWidget):
    def __init__(self):
        super().__init__(parent = GetMayaMainWindow())
        DeleteWidgetWithName(self.GetWidgetUniqueName())
        self.setWindowFlags(Qt.WindowType.Window)
        self.setObjectName(self.GetWidgetUniqueName())

    def GetWidgetUniqueName(self):
        return "akjsboecnalcsvakajgvflawha"