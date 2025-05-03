import sys
import os

base_path = os.path.join(sys._MEIPASS, 'mp_software_stylesheets') if getattr(sys, 'frozen',
                                                                             False) else 'mp_software_stylesheets'

try:
    with open(os.path.join(base_path, 'dot39_style.css'), 'r') as stylesheet_f:
        DOT39CSS = stylesheet_f.read()
    with open(os.path.join(base_path, 'mprun_style.css'), 'r') as stylesheet_f:
        MPRUNCSS = stylesheet_f.read()
    with open(os.path.join(base_path, 'sweep_pc_style.css'), 'r') as stylesheet_f:
        SWEEPPCCSS = stylesheet_f.read()
    with open(os.path.join(base_path, 'ibrowse_style.css'), 'r') as stylesheet_f:
        IBROWSECSS = stylesheet_f.read()
    with open(os.path.join(base_path, 'slik_style.css'), 'r') as stylesheet_f:
        SLIKCSS = stylesheet_f.read()

except FileNotFoundError as e:
    print(f'Error: {e}. File not found.')
except IOError as e:
    print(f'Error: {e}. An I/O error occurred.')

