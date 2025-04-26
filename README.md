# MP Software Stylesheets
The official Qt CSS (QSS) stylesheets used by MP Software

## Overview
Stylesheets are app-specific for our software, but these can be used for reference in your own stylesheets.

## Install
To start, clone the repository (`https://github.com/ktechhydle/mp_software_stylesheets.git`) to your 
project and add an import statement to your Python file(s): 

`from mp_software_stylesheets.styles import MPRUNCSS, DOT39CSS, SWEEPPCCSS, IBROWSECSS`

You can then pass the `MPRUNCSS` object (string) into your widget.

`myWidget.setStyleSheet(macCSS)`

## Project Info
We will update these stylesheets based on our software's requirements and updates, so please read release info
before updating this repository. Thank you for your support!