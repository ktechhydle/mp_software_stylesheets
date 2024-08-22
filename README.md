# MP Software Stylesheets
***The official Qt CSS (QSS) stylesheets of MP Software***

We offer two stylesheets, `macCSS` and `windowsCSS`, both working for the desired platform.
Each one includes fonts and styles supported on the respective platform. All logos and assets
are interchangeable, meaning they work for both platforms. 

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

## Custom Widgets
If you call `myWidget.setObjectName()`, you can specify that object in the stylesheet via `#myWidget` and
create custom attributes JUST for that widget. If you set any widgets object names to the ones below you get 
custom widgets not supported by normal Qt.

- `modernLineEdit`: a modern style for QLineEdits
- `dockWidgetTitleBar`: a title bar for QDockWidgets with custom title bars enabled
- `strokeLabel`: a label with an underline attribute for QLabels

## Install
To start, simply clone the repository (`https://github.com/ktechhydle/mp_software_stylesheets.git`) to your 
project and add an import statement to your Python file(s): 
##### `from styles import macCSS`
Then, just pass the `macCSS` object into your `QApplication.setStyleSheet()` function and you are good to go.
You can also set the stylesheet to any supported widgets, for example:
##### `myWidget.setStyleSheet(macCSS)`

## Project Info
We will update these stylesheets based on our software's requirements and updates, so please read release info
before updating this repository. Thank you for your support!