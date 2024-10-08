import sys, os

# Determine base path depending on frozen or non-frozen environment
base_path = os.path.join(sys._MEIPASS, 'mp_software_stylesheets') if getattr(sys, 'frozen',
                                                                             False) else 'mp_software_stylesheets'

# Load CSS files with error handling
try:
    with open(os.path.join(base_path, 'mac_style.css'), 'r') as mac_file:
        macCSS = mac_file.read()

    with open(os.path.join(base_path, 'windows_style.css'), 'r') as windows_file:
        windowsCSS = windows_file.read()

    with open(os.path.join(base_path, 'unified.css'), 'r') as unified_file:
        unifiedCSS = unified_file.read()

    with open(os.path.join(base_path, 'blender.css'), 'r') as blender_file:
        blenderCSS = blender_file.read()

except FileNotFoundError as e:
    print(f"Error: {e}. File not found.")
except IOError as e:
    print(f"Error: {e}. An I/O error occurred.")

