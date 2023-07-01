<h1 align="center">CopyOptimize</h1>
<p align="center">(Previously known as CopyRaw)</p>



https://github.com/TheoIsDumb/CopyOptimize/assets/118801625/928c9865-571c-4f4f-9d8d-25a7e559cb7a



(dialog box looks like an error box due to inkex.utils.debug() being used)


An Inkscape Extension I made for myself.

Copies raw and optimized SVG directly instead of saving it as an optimized SVG, then opening it in a text editor, Ctrl-a + Ctrl-c, you know all of that stuff. 

Added Scour for optimization.

```
Scour flags:
- --strip-xml-prolog
- --enable-viewboxing
- --no-line-breaks
- --remove-descriptive-elements
- --enable-comment-stripping
- --enable-id-stripping
- --shorten-ids
```

## How to use

1. Select paths/strokes/whatever.
2. Go to `Extensions -> Custom -> CopyOptimize.`
3. Copy the SVG text from the box that pops up. (inkex.utils.debug())

## Installation

```
cd ~/.config/inkscape/extensions # or wherever you store extensions, dunno about windows/mac
git clone https://github.com/TheoIsDumb/CopyOptimize
```

Open Inkscape (re-launch if already open) and CopyOptimize will be available in the Extensions menu.

## ProTip 

![protip](protip.webp)

> Set a keyboard shortcut for CopyOptimize in Edit -> Preferences -> Interface -> Keyboard. 
> (I used Pause, cause I never use it.)
