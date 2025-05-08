from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtCore import Qt
import maya.OpenMayaUI as omui
import shiboken2
import maya.cmds as mc

def IsMesh(obj):
    shapes = mc.listRelatives(obj, s=True, fullPath=True)
    if not shapes:
        return False
    
    for s in shapes:
        if mc.objExists(s) and mc.objectType(s) == "mesh":
            return True

    return False

def IsController(obj):
    shapes = mc.listRelatives(obj, s=True, fullPath=True)
    if not shapes:
        return False
    
    for s in shapes:
        if mc.objExists(s) and mc.objectType(s) == "nurbsCurve":
            return True

    return False

def IsGroup(obj):
    if mc.objectType(obj) != "transform":
        return False
    
    shapes = mc.listRelatives(obj, s=True, fullPath=True) or []
    return len(shapes) == 0

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
        return "okvnsaponfosanjvp"