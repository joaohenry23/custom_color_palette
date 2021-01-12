# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------
'''
Description: Creates python custom colors palette
Author: Joao Henry Huaman Chinchay
E-mail: joaohenry23@gmail.com
Created date: Sep 07, 2019
Modification date: Jan 12, 2021
'''
#-----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import BoundaryNorm
import sys
#-----------------------------------------------------------------------------------------------------------------------------------

def range(vmin,vmax,step):

    """
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

    """

    ndec = 0

    for item in [vmin,vmax,step]:
        if isinstance(item,float):
            dec = len(str(item).split('.')[1])
            if dec > ndec:
                ndec = dec

    values = np.arange(vmin*(10**ndec),vmax*(10**ndec)+step*(10**ndec),step*(10**ndec))/(10**ndec)
    return np.trunc(values*10**ndec)/(10**ndec)

#-----------------------------------------------------------------------------------------------------------------------------------

def creates_palette(Palette_Attr, extend='neither', lower_color=None, upper_color=None, nan_color=None):

    """
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

    """

    idxfin = len(Palette_Attr)-1
    lowercolor = None
    uppercolor = None

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    for idx, subpalette in enumerate(Palette_Attr):
        cols = subpalette[0]
        levs = subpalette[1]

        if isinstance(levs,np.ndarray)==False:
            levs = np.array(levs)

        addlowercol = 0
        adduppercol = 0

        if idx == 0 and ( extend == 'min' or extend == 'both'):
            addlowercol = 1

        if idx == idxfin and ( extend == 'max' or extend == 'both'):
            adduppercol = 1

        #  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .

        if len(subpalette) == 3:
            extlevs = subpalette[2][0]
            vmin = subpalette[2][1]
            vmax = subpalette[2][2]

            if isinstance(extlevs,np.ndarray)==False:
                extlevs = np.array(extlevs)

            if [vmin] in list(extlevs):
                argvmin = np.argwhere(vmin==extlevs)[0][0]
            else:
                print('\n\t{} was not found in {}\n'.format(vmin,extlevs))
                sys.exit()

            if [vmax] in list(extlevs):
                argvmax = np.argwhere(vmax==extlevs)[0][0]
            else:
                print('\n\t{} was not found in {}\n'.format(vmax,extlevs))
                sys.exit()

            levs2 = extlevs[argvmin:argvmax+1]

            if levs.shape[0] != levs2.shape[0]:
                print('\n\t{}  and  {} have not the same size\n'.format(levs,levs2))
                sys.exit()

        #  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
            ncolors = extlevs.shape[0]-1+addlowercol+adduppercol

        else:
            argvmin = 0
            argvmax = levs.shape[0]-1
            ncolors = levs.shape[0]-1+addlowercol+adduppercol

        #  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .

        if isinstance(cols,list):
            if len(cols)==1:
                cols = cols + cols
            subccp = LinearSegmentedColormap.from_list(name='CCP', colors=cols, N=ncolors)(np.linspace(0.0,1.0,ncolors))
        else:
            subccp = cols(np.linspace(0.0,1.0,ncolors))

        if addlowercol>0:
            lowercolor = subccp[0]

        if adduppercol>0:
            uppercolor = subccp[-1]


        subccp = subccp[addlowercol:ncolors-adduppercol]
        subccp = subccp[argvmin:argvmax]


        if idx == 0:
            ccp = subccp
            labs = levs
        else:
            ccp = np.vstack((ccp,subccp))
            labs = np.concatenate((labs,levs[1:]))

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    Palette = LinearSegmentedColormap.from_list('ccp', ccp, N=ccp.shape[0])
    Norm = BoundaryNorm(labs, ncolors=Palette.N)
    Ticks = list(labs)
    Bounds = [Ticks[0]-1.0] + Ticks + [Ticks[-1]+1.0]


    if isinstance(lowercolor,np.ndarray):
        Palette.set_under(lowercolor)

    if isinstance(uppercolor,np.ndarray):
        Palette.set_over(uppercolor)

    if lower_color != None:
        Palette.set_under(lower_color)

    if upper_color != None:
        Palette.set_over(upper_color)

    if nan_color != None:
        Palette.set_bad(nan_color)

    return Palette, Ticks, Norm, Bounds;

#-----------------------------------------------------------------------------------------------------------------------------------


