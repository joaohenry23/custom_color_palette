# custom_colors_palette
Python package to create a custom color palette.
<br><br>

# Version
3.0
<br><br>

# Requirements
- Numpy
- Matplotlib
<br><br>

# Usage
See the jupyter notebooks examples for the last version:
- [v3.0](https://github.com/joaohenry23/custom_color_palette/blob/master/examples/tutorial_v3.0.ipynb)

Examples for older version can be found [here](https://github.com/joaohenry23/custom_color_palette/blob/master/examples/)
<br><br>

# Reference Guide
Click on the item to see the function and their description.
<details><summary>range</summary>
<br>

**range**(vmin, vmax, step)
```
    Creates a range of numbers that include the extreme values.

    Parameters
    ----------
    vmin: int or float
        First value of sequence of numbers.

    vmax: int or float
        Last value of sequence of numbers.

    step: int or float
        Step used to create sequence of numbers between vmin and vmax.



    Returns
    -------
    Return a numpy.ndarray with range of number between vmin and vmax.
```
<br>
</details>

<details><summary>creates_palette</summary>
<br>

**creates_palette**(Palette_Attr, extend='neither', lower_color=None, upper_color=None, nan_color=None)
```
    Creates a custom color palette from color list.

    Parameters
    ----------
    Palette_Attr : list
        List that contains sublists with the characteristics of the
        colors that will be used to create a custom color palette.
        Each sublist must has three elements: [Colors, Limits, Stretch]

        Colors : list or Matplotlib's Colormap
            Defines the colors that will be used to create the
            palette. Colors must be a Matplotlib's Colormap,
            a list with Matplotlib's colors name,
            a list with Hex color code or
            a list with RGB color code.

        Limits : list or numpy.ndarray
            Defines the limits of each color of palette.

        Stretch : list, optional
            Optional list used to stretch the color palette
            in order to obtain colors from a specific region.
            Stretch must have 3 elements: [Values, Vini, Vfin]

            Values : list or numpy.ndarray
                Sequence of numbers that will be cut.

            Vini : int or float
                First value used to cut Values.

            Vfin : int or float
                Last value used to cut Values.

            If Stretch is defined, the number of colors between
            Vini and Vfin must be equal to Colors.


    extend : str, default 'neither'
        It is an optional parameter that is used to sets the extreme color of
        palette. The valid options are 'neither', 'min', 'max', and
        'both'.


    lower_color : str, tuple, or None, default None
        It defines lower color of palette.


    upper_color : str, tuple, or None, default None
        It defines upper color of palette.


    nan_color : str, tuple, or None, default None
        It defines color of nan values.



    Returns
    -------
    Palette: object
        Custom color palette

    Ticks: list
        Limits of each color in the palette.

    Norm: class matplotlib.colors.BoundaryNorm
        Norm of limits of each color.

    Bounds: list
        List with limits of each colors of Palette, including the extend values.
```
<br>
</details>
<br><br>

# Installation
You can install **custom_color_palette** on Python 2 or 3 on Linux, Windows or other, using the following commands.
<br><br>
**Using PIP**:
```
pip install custom-color-palette

```

Check if package was installed with:

```
pip show custom-color-palette
```
<br>

If you already have the package installed, update it to the latest version with:

```
pip install --upgrade custom-color-palette
```
<br>

**Using clone**:
```
clone https://github.com/joaohenry23/custom_color_palette.git
cd custom_color_palette
python setup.py install

```
<br>

**Using python**:\
Download **custom_color_palette-master.zip** from github and following the next commands:
```
unzip custom_color_palette-master.zip
cd custom_color_palette-master
python setup.py install

```
<br><br>

# Support
If you have any questions, do not hesitate to write to:
```
joaohenry23@gmail.com

```

