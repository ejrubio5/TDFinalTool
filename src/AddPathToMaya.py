import sys

prjPath = "D:/profile redirect/ejrubio/Documents/TDFinalTool/src"
moduleDir = "D:/profile redirect/ejrubio/Documents"

if prjPath not in sys.path:
    sys.path.append(prjPath)

if moduleDir not in sys.path:
    sys.path.append(moduleDir)