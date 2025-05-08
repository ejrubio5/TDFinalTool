import sys

# Switch these depending on what computer using...

prjPath = "C:/Users/EJ/Documents/TDFinalTool/src"
moduleDir = "C:/Users/EJ/Documents"

if prjPath not in sys.path:
    sys.path.append(prjPath)

if moduleDir not in sys.path:
    sys.path.append(moduleDir)