import sys
import os

# Determine base path depending on frozen or non-frozen environment
base_path = os.path.join(sys._MEIPASS, 'mp_software_stylesheets') if getattr(sys, 'frozen',
                                                                             False) else 'mp_software_stylesheets'

# Load CSS files with error handling
try:
    with open(os.path.join(base_path, 'style.css'), 'r') as stylesheet_f:
        AppCSS = stylesheet_f.read()

except FileNotFoundError as e:
    print(f'Error: {e}. File not found.')
except IOError as e:
    print(f'Error: {e}. An I/O error occurred.')

