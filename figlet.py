from typing import Any

from pyfiglet import Figlet


def figs_cli() -> Any:
    """
    Pyfiglet is a python module for converting strings into ASCII Text with arts fonts.
    """
    msg = Figlet(font="slant")
    return msg.renderText("Lyrics Finder")
