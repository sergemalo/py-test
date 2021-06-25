#!/usr/bin/python3.9
import platform
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QPushButton                                                                 

print("HELLO WORLD!");
print("Python version: ", platform.python_version())

                                                                                                    
def say_hello():
  print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)

# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()

# Run the main Qt loop
app.exec_()

