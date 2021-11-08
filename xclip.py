#!/usr/bin/env python3
"""this script is used to remove prefix from nautilus-clipboard."""

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

def callBack(*args):
    """callBack"""
    text: str = clip.wait_for_text()
    if text.startswith("x-special/nautilus-clipboard"):
        COPY_FILE_HEAD = "file://"
        len_head = len(COPY_FILE_HEAD)
        lines = text.split("\n")[2:]
        lines = [line[len_head:] for line in lines if line.startswith(COPY_FILE_HEAD)]
        clip.set_text("\n".join(lines), -1)


clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect("owner-change", callBack)

Gtk.main()
