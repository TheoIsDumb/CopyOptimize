#!/usr/bin/env python
# coding=utf-8

import inkex
import scour
from scour.scour import scourString, parse_args

options = parse_args(['--strip-xml-prolog', '--enable-viewboxing', '--no-line-breaks', '--remove-descriptive-elements', '--enable-comment-stripping', '--enable-id-stripping', '--shorten-ids'])

class CopyRaw(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

    def template(self):
        width = self.document.getroot().get('width')
        height = self.document.getroot().get('height')
        viewbox = self.document.getroot().get('viewBox')
        defs = self.document.getroot().defs.tostring().decode()

        return f'<svg width="{width}" height="{height}" viewBox="{viewbox}" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">' + defs
                
    def effect(self):
        stuff = []

        if len(self.svg.selection) == 0:
            raise inkex.AbortExtension("None selected.")
        else:
            for elem in self.svg.selection:
                stuff.append(elem.tostring().decode())

        svg_string = self.template() + ' '.join(stuff[::-1]) + "</svg>"
        inkex.utils.debug(scourString(svg_string, options))

if __name__ == '__main__':
    CopyRaw().run()