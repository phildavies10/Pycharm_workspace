from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes=[])
buildOptions = dict(include_files = ['mainWindow.qss', 'dfConfig.cfg'])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('c:\\PyCharm workspace\\DayfactoPyCharm\\dayfactoApp.py', base=base)
]
excludes = [
    '_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
    'Tkconstants', 'Tkinter']

includes = ['mainWindow.qss', 'dfConfig.cfg']


build_exe_options = {
    "excludes": excludes,
    "includes": includes}

setup(name='Dayfacto_0.1',
      version = '0.1',
      description = 'Journal diary',
      options = dict(build_exe = buildOptions),
      executables = executables)
