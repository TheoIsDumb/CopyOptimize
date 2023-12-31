<h1 align="center">CopyOptimize</h1>
<p align="center">(Previously known as CopyRaw)</p>



https://github.com/TheoIsDumb/CopyOptimize/assets/118801625/928c9865-571c-4f4f-9d8d-25a7e559cb7a



<sup>(dialog box looks like an error box due to inkex.utils.debug() being used)</sup>


An Inkscape Extension I made for myself.

Copies raw and optimized SVG directly instead of saving it as an optimized SVG, then opening it in a text editor, Ctrl-a + Ctrl-c, you know all of that stuff. 

Added Scour for optimization.

```
Scour flags:
1 --strip-xml-prolog
2 --enable-viewboxing
3 --no-line-breaks
4 --remove-descriptive-elements
5 --enable-comment-stripping
6 --enable-id-stripping
7 --shorten-ids
```

NOTE: `gtk` branch has a version of CopyOptimize that displays the optimized SVG in a GTK3 window. (Requires `python-gobject` and `gtk3`)

## Why

Everytime I have to make an SVG to use on websites or something, I have to go through this tiring process of saving it as an optimized SVG, opening it in a text editor, copying it and pasting it. I make one change and I have to do it all over again.

This extension helps me do it all in one go.

## Installation

```
cd ~/.config/inkscape/extensions # or wherever you store extensions, dunno about windows/mac
git clone https://github.com/TheoIsDumb/CopyOptimize
```

Open Inkscape (re-launch if already open) and CopyOptimize will be available in the Extensions menu.

## How to use

1. Select paths/strokes/whatever.
2. Go to `Extensions -> Custom -> CopyOptimize.`
3. Copy the SVG text from the box that pops up. (inkex.utils.debug())

## ProTip 

![protip](protip.webp)

> Set a keyboard shortcut for CopyOptimize in Edit -> Preferences -> Interface -> Keyboard. 
> (I used Pause, cause I never use it.)
