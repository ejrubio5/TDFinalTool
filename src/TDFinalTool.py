import importlib
import MayaUtils
importlib.reload(MayaUtils)

from MayaUtils import MayaWindow
from PySide2.QtWidgets import QLabel, QMessageBox, QPushButton, QVBoxLayout
import maya.cmds as mc

class AnimationKeyFinder:
    def __init__(self, parent=None):
        self.parent = parent

    def FindKeysBasedOnSelection(self, filterFunc):
        allTransforms = mc.ls(type='transform') or []
        matches = []
        for obj in allTransforms:
            if filterFunc(obj) and mc.keyframe(obj, query=True, name=True):
                matches.append(obj)
        return matches
    
    def ShowErrorMessage(self, category):
        QMessageBox.warning(self.parent, "No keys Found!", f"No keyed {category} found in this scene!")

    def SelectControllers(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        if controllers:
            mc.select(controllers, replace=True)
        else:
            self.ShowErrorMessage("controllers")
    
    def SelectMeshes(self):
        meshes = self.FindKeysBasedOnSelection(MayaUtils.IsMesh)
        if meshes:
            mc.select(meshes, replace=True)
        else:
            self.ShowErrorMessage("meshes")
    
    def SelectGroups(self):
        groups = self.FindKeysBasedOnSelection(MayaUtils.IsGroup)
        if groups:
            mc.select(groups, replace=True)
        else:
            self.ShowErrorMessage("groups")
    
    def SelectAll(self):
        controllers = self.FindKeysBasedOnSelection(MayaUtils.IsController)
        meshes = self.FindKeysBasedOnSelection(MayaUtils.IsMesh)
        groups = self.FindKeysBasedOnSelection(MayaUtils.IsGroup)
        allItems = controllers + meshes + groups

        if allItems:
            mc.select(allItems, replace=True)
        else:
            self.ShowErrorMessage("controllers, meshes, or groups")


class KeyFinderWidget(MayaWindow):
    def __init__(self):
        super().__init__()
        self.keyFinder = AnimationKeyFinder(parent=self)
        self.setWindowTitle("Animation Key Finder")

        self.masterLayout = QVBoxLayout()
        self.setLayout(self.masterLayout)

        toolTipLabel = QLabel("Press the button for which objects you want to select!")
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
            self.keyFinder.SelectControllers()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectMeshesBtnClicked(self):
        try:
            self.keyFinder.SelectMeshes()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectGrpsBtnClicked(self):
        try:
            self.keyFinder.SelectGroups()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

    def SelectAllBtnClicked(self):
        try:
            self.keyFinder.SelectAll()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

keyFinderWidget = KeyFinderWidget()
keyFinderWidget.show()