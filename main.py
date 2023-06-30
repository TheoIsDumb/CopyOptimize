#!/usr/bin/env python
# coding=utf-8

import inkex

class CopyRaw(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

    def template(self):
        width = self.document.getroot().get('width')
        height = self.document.getroot().get('height')
        viewbox = self.document.getroot().get('viewBox')

        return f'<svg width="{width}" height="{height}" version="1.1" viewBox="{viewbox}" xmlns="http://www.w3.org/2000/svg">'

    def effect(self):
        stuff = []

        if len(self.svg.selection) == 0:
            inkex.errormsg(_("None selected."))
        else:
            for elem in self.svg.selection:
                stuff.append(elem.tostring().decode())

            inkex.utils.debug(self.template() + ' '.join(stuff[::-1]) + "</svg>")

if __name__ == '__main__':
    CopyRaw().run()