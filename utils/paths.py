from pathlib import Path
import sys


def app_root():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parents[1]


def resource_path(relative_path):
    return app_root() / relative_path