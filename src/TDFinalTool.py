import maya.cmds as mc

class ControllerAnimFinder:
    def GetAllTransfors():
        return mc.ls(type='transform', long=True) or []