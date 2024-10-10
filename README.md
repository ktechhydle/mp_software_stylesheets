# MP Software Stylesheets
***The official Qt CSS (QSS) stylesheets of MP Software***

We offer four stylesheets, `macCSS`, `windowsCSS`, `unifiedCSS`, and `blenderCSS` all working for the desired platform.
Each one includes fonts and styles supported on the respective platform, and all logos/assets
are interchangeable.

## Supported Widgets
- **QMainWindow** and **QWidget**
- **QMenu**
- **QMenuBar**
- All **QDialogs** (e.g., QColorPicker, QMessageBox, etc.)
- **QTabWidget**
- **QDockWidget**
- **QToolbar**
- **QToolButton**
- **QToolBox**
- **QToolTip**
- **QGraphicsView**
- **QScrollbar**
- **QScrollWidget**
- **QListWidget**
- **QListWidgetItem**
- **QSpinBox**
- **QDoubleSpinBox** (QAbstractSpinBox)
- **QComboBox**
- **QLineEdit**
- **QPushButton**
- **QCheckBox**
- **QSlider**
- **QGroupBox**

## Install
To start, simply clone the repository (`https://github.com/ktechhydle/mp_software_stylesheets.git`) to your 
project and add an import statement to your Python file(s): 
##### `from styles import macCSS`
Then, just pass the `macCSS` object into your `QApplication.setStyleSheet()` function and you are good to go.
You can also set the stylesheet to any supported widgets, for example:
##### `myWidget.setStyleSheet(macCSS)`

## Full demo
```
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mp_software_stylesheets.styles import macCSS, windowsCSS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Demo')
        
        # Main widget
        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)
        
        # Basic widgets
        layout.addWidget(QLabel("Label"))
        layout.addWidget(QPushButton("Button"))
        layout.addWidget(QCheckBox("CheckBox"))
        layout.addWidget(QRadioButton("RadioButton"))
        layout.addWidget(QLineEdit("LineEdit"))
        layout.addWidget(QComboBox())
        layout.addWidget(QSpinBox())
        layout.addWidget(QSlider(Qt.Horizontal))
        layout.addWidget(QProgressBar())
        layout.addWidget(QTextEdit())
        layout.addWidget(QListView())
        layout.addWidget(QTableView())
        layout.addWidget(QTreeView())
        layout.addWidget(QTabWidget())
        layout.addWidget(QToolBar("ToolBar"))
        layout.addWidget(QStatusBar())
        layout.addWidget(QMenuBar())
        
        self.setCentralWidget(main_widget)
        self.setGeometry(300, 100, 800, 600)

app = QApplication([])

if sys.platform == 'darwin':
    app.setStyleSheet(macCSS)
else:
    app.setStyleSheet(windowsCSS)

window = MainWindow()
window.show()
app.exec()
```

## Project Info
We will update these stylesheets based on our software's requirements and updates, so please read release info
before updating this repository. Thank you for your support!

P.S. Nobody said you can't use these stylesheets for C++, feel free to!