# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication
from ui.home_page import HomePage


def main():
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()




 
