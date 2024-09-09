import sys, os

if getattr(sys, 'frozen', False):
    macCSS = open(os.path.join(sys._MEIPASS, 'mp_software_stylesheets/mac_style.css'), 'r').read()
    windowsCSS = open(os.path.join(sys._MEIPASS, 'mp_software_stylesheets/windows_style.css'), 'r').read()
else:
    macCSS = open('mp_software_stylesheets/mac_style.css', 'r').read()
    windowsCSS = open('mp_software_stylesheets/windows_style.css', 'r').read()
