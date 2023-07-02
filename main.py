#!/usr/bin/env python
# coding=utf-8

import inkex
import scour
from scour.scour import scourString, parse_args
import os
import warnings

warnings.filterwarnings("ignore", category=ImportWarning)

os.environ["LC_ALL"] = "C"

try:
    import gi
except ImportError:
    gui = False
finally:
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    gui = True

class COWindow(Gtk.Window):
    def __init__(self, text):
        Gtk.Window.__init__(self, title="CopyOptimize")
        self.set_default_size(800, 400)
        self.text = text

        self.textview = Gtk.TextView()
        self.textview.set_editable(False)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)  # Set wrap_mode property to WORD
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(text)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_border_width(10)
        scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        scrolledwindow.add(self.textview)

        self.add(scrolledwindow)

scour_options = parse_args(['--strip-xml-prolog', '--enable-viewboxing', '--no-line-breaks', '--remove-descriptive-elements', '--enable-comment-stripping', '--enable-id-stripping', '--shorten-ids'])

class CopyOptimize(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

    def template(self):
        width = self.document.getroot().get('width')
        height = self.document.getroot().get('height')
        viewbox = self.document.getroot().get('viewBox')
        defs = self.document.getroot().defs.tostring().decode()

        return f'<svg width="{width}" height="{height}" viewBox="{viewbox}" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">' + defs
                
    def effect(self):
        elements = []

        if len(self.svg.selection) == 0:
            raise inkex.AbortExtension("None selected.")
        else:
            for elem in self.svg.selection:
                elements.append(elem.tostring().decode())

        svg_string = self.template() + ' '.join(elements[::-1]) + "</svg>"

        if gui == True:
            win = COWindow(svg_string)
            win.connect("destroy", Gtk.main_quit)
            win.show_all()
            Gtk.main()
        else:
            inkex.utils.debug(scourString(svg_string, scour_options))

if __name__ == '__main__':
    CopyOptimize().run()
