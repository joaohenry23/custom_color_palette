# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------
'''
Description: Creates python custom colors palette
Author: Joao Henry Huaman Chinchay
E-mail: joaohenry23@gmail.com
Created date: Sat, Sep 07, 2019
Modification date: Mon, Jun 15, 2020
'''
#-----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import BoundaryNorm
#-----------------------------------------------------------------------------------------------------------------------------------

def creates_palette(ColorList, Intervals, Increase=[1.0], EditPalette=False, Extend='neither'):
   """

   Parameters
   ----------
   ColorList: list
              List with color palette name (Matplotlib's color palettes) and/or sub-lists with colors names.
              Color palette name must be written without brackets.

   Intervals: list
              Values range of each color palette of ColorList.

   Increase: list
             Values between colors of palette. This parameter is optional and its default value is 1.0. 

   EditPalette: bool or list
                Gives information to edit the colors palettes of ColorList. This parameter is optional and can be False or be a list,
                its default value is False. When is False this parameter is ignored. When is a list this parameter must have
                information (inside list) to edit each colors palette of ColorList. This information can be None (if do not want to
                edit the color palette) or can be a sub-list is want to edit the colors palettes. This sub-list must have 4 item,
                the first item and the second item indicate the values range of colors palette, the third and the fourth item indicate
                the colors that will be extracted from color palette (created from first and second item of sub-list). The number of
                colors extracted must match with the number of colors of palette defined in Intervals.

   Extend: str
           Set extreme colors as a extend colors. The options are 'min', 'max' and 'both'. Default is 'neither'.


   Returns
   -------
   FinalPalette: class matplotlib.colors.LinearSegmentedColormap
                 Custom color palette output

   ColorLabels: list
                Values of each colors from FullCustomPalette

   Norm: class matplotlib.colors.BoundaryNorm
         Norm of intervals.

   Bounds: list
           List with intervals, including Extend values.

   """

   if len(ColorList)+1==len(Intervals): 

      if len(Increase)==1 or len(Increase)==len(ColorList):

         NColorList = np.full([len(ColorList)],0)
         IniColorSplit = np.full([len(ColorList)],0)
         EndColorSplit = np.full([len(ColorList)],0)


         if len(Increase)==1:
            Increase = np.ones([len(ColorList)])*Increase
         elif len(ColorList)==len(Increase):
            pass
         else:
            print('\nIncrease must have one item or have the same dimensions of ColorList\n')
            exit()


         for idx in range(len(Intervals)-1):
            NColorList[idx] = round((Intervals[idx+1]-Intervals[idx])/Increase[idx])
            EndColorSplit[idx] = round((Intervals[idx+1]-Intervals[idx])/Increase[idx])

            if idx==0:
               ColorLabels = np.linspace(Intervals[idx],Intervals[idx+1],NColorList[idx]+1,endpoint=True)
            else:
               ColorLabels = np.concatenate((ColorLabels, np.linspace(Intervals[idx],Intervals[idx+1],NColorList[idx]+1,endpoint=True)[1:]))


         if EditPalette==False :
            pass
         else:
            if len(EditPalette)!=len(ColorList):
               print('\nColorList and EditPalette must have the same number of items\n')
               exit()
            else:
               for idx in range(len(EditPalette)):

                  if EditPalette[idx]==None:
                     pass
                  else:
                     if len(EditPalette[idx])!=4:
                        print('\nItems in brackets of EditPalette must have 4 sub-items\n')
                        exit()
                     else:
                        NColorList[idx] = round((EditPalette[idx][1]-EditPalette[idx][0])/Increase[idx])
                        IniColorSplit[idx] = round((EditPalette[idx][2]-EditPalette[idx][0])/Increase[idx])
                        EndColorSplit[idx] = round((EditPalette[idx][3]-EditPalette[idx][0])/Increase[idx])



         for idx in range(len(ColorList)):

            if type(ColorList[idx]) == list:

               if len(ColorList[idx]) == 1:
                  MyColorsList = [ColorList[idx][0], ColorList[idx][0]]
               if len(ColorList[idx]) > 1:
                  MyColorsList = ColorList[idx]

               CustomPalette = LinearSegmentedColormap.from_list(name = 'ColorGradient', colors = MyColorsList, N = NColorList[idx])
               CustomPalette = CustomPalette(np.linspace(0.0, 1.0, NColorList[idx]))
               CustomPalette = CustomPalette[IniColorSplit[idx]:EndColorSplit[idx]]

            else:
               CustomPalette = ColorList[idx](np.linspace(0.0, 1.0, NColorList[idx]))
               CustomPalette = CustomPalette[IniColorSplit[idx]:EndColorSplit[idx]]

            if idx==0:
               FullCustomPalette = CustomPalette
            elif idx>0:
               FullCustomPalette = np.vstack((FullCustomPalette, CustomPalette))

         ncolors = FullCustomPalette.shape[0]

         if ncolors == 1:
            FullCustomPalette = np.concatenate((FullCustomPalette,FullCustomPalette))


         if Extend=='neither':
            FinalPalette = LinearSegmentedColormap.from_list('ColorGradient', FullCustomPalette, ncolors)
            Norm = BoundaryNorm(ColorLabels, ncolors=FinalPalette.N)
            Bounds = list(ColorLabels)
            ColorLabels = list(ColorLabels)
         elif Extend=='min':
            if ncolors>1:
               FinalPalette = LinearSegmentedColormap.from_list('ColorGradient', FullCustomPalette[1:], ncolors-1)
               FinalPalette.set_under(FullCustomPalette[0])
               Bounds = list(ColorLabels)
               ColorLabels = list(ColorLabels[1:])
               Norm = BoundaryNorm(ColorLabels, ncolors=FinalPalette.N)
            else:
               print('\nYou have to define more than one colors\n')
               exit()
         elif Extend=='max':
            if ncolors>1:
               FinalPalette = LinearSegmentedColormap.from_list('ColorGradient', FullCustomPalette[:-1], ncolors-1)
               FinalPalette.set_over(FullCustomPalette[-1])
               Bounds = list(ColorLabels)
               ColorLabels = list(ColorLabels[:-1])
               Norm = BoundaryNorm(ColorLabels, ncolors=FinalPalette.N)
            else:
               print('\nYou have to define more than one colors\n')
               exit()
         elif Extend=='both':
            if ncolors>2:
               FinalPalette = LinearSegmentedColormap.from_list('ColorGradient', FullCustomPalette[1:-1], N=ncolors-2)
               FinalPalette.set_under(FullCustomPalette[0])
               FinalPalette.set_over(FullCustomPalette[-1])
               Bounds = list(ColorLabels)
               ColorLabels = list(ColorLabels[1:-1])
               Norm = BoundaryNorm(ColorLabels, ncolors=FinalPalette.N)
            else:
               print('\nYou have to define more than two colors\n')
               exit()


      else:
         print('\nColorList and Increase must have the same number of items\n')
         exit()

   else:
      print('\nIntervals must have one item more than ColorList\n')
      exit()

   return FinalPalette, ColorLabels, Norm, Bounds;

#-----------------------------------------------------------------------------------------------------------------------------------

