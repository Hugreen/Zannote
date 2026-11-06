from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtSvg import QSvgRenderer

from utils.paths import resource_path


def svg_to_icon(path, size=QSize(1024, 1024)):
    renderer = QSvgRenderer(
        str(resource_path(path))
    )

    pixmap = QPixmap(size)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    return QIcon(pixmap)