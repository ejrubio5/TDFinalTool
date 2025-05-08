import importlib
import MayaUtils
importlib.reload(MayaUtils)

from MayaUtils import MayaWindow
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QColorDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QSlider, QVBoxLayout, QWidget
from PySide2.QtCore import Qt, Signal
from maya.OpenMaya import MVector
import maya.mel as mel
import maya.cmds as mc

class AnimationKeyFinder:
    def __init__(self):
        return

    def FindKeysBasedOnSelection(self, filterFunc):
        allTransforms = mc.ls(type='transform') or []
        matches = []
        for obj in allTransforms:
            if filterFunc(obj) and mc.keyframe(obj, query=True, name=True):
                matches.append(obj)
        return matches
    
    def ShowErrorMessage(self, category):
        QMessageBox.warning(self, "No keys Found!", f"No keyed {category} found in this scene!")

    def SelectControllers(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        mc.select(controllers, replace=True)
    
    def SelectMeshes(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        mc.select(controllers, replace=True)
    
    def SelectControllers(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        mc.select(controllers, replace=True)
    
    def SelectControllers(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        mc.select(controllers, replace=True)
    


class KeyFinderWidget(MayaWindow):
    def __init__(self):
        super().__init__()
        self.keyFinder = AnimationKeyFinder()
        self.setWindowTitle("Animation Key Finder")

        self.masterLayout = QVBoxLayout()
        self.setLayout(self.masterLayout)

        toolTipLabel = QLabel("Press the button for which objects you want to selct!")
        self.masterLayout.addWidget(toolTipLabel)

        selectCtrlsBtn = QPushButton("Select Controllers with Keys")
        selectCtrlsBtn.clicked.connect(self.SelectCtrlsBtnClicked)
        self.masterLayout.addWidget(selectCtrlsBtn)

        selectMeshesBtn = QPushButton("Select Meshes with Keys")
        selectMeshesBtn.clicked.connect(self.SelectMeshesBtnClicked)
        self.masterLayout.addWidget(selectMeshesBtn)

        selectGrpsBtn = QPushButton("Select Groups with Keys")
        selectGrpsBtn.clicked.connect(self.SelectGrpsBtnClicked)
        self.masterLayout.addWidget(selectGrpsBtn)

        selectAllBtn = QPushButton("Select All with Keys")
        selectAllBtn.clicked.connect(self.SelectAllBtnClicked)
        self.masterLayout.addWidget(selectAllBtn)

    def SelectCtrlsBtnClicked(self):
        try:
            self.keyFinder.FindKeysBasedOnSelection()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectMeshesBtnClicked(self):
        try:
            self.keyFinder.FindKeysBasedOnSelection()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectGrpsBtnClicked(self):
        try:
            self.keyFinder.FindKeysBasedOnSelection()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectAllBtnClicked(self):
        try:
            self.keyFinder.FindKeysBasedOnSelection()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")