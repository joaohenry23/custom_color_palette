# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------------------
'''
Description: Creates python custom colors palette
Author: Joao Henry Huaman Chinchay
E-mail: joaohenry23@gmail.com
Created date: Sat, Sep 07, 2019
'''
#-----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import BoundaryNorm
#-----------------------------------------------------------------------------------------------------------------------------------
#Creates custom colors palette

def creates_palette(ColorList, Intervals, Increase=[1.0], EditPalette=False):
   """

   Parameters
   ----------
   ColorList:   List with color palette name (Matplotlib's color palettes) and/or sub-lists with colors names.
                Color palette name must be written without brackets.

   Intervals:   Values range of each color palette of ColorList.

   Increase:    Values between colors of palette. This parameter is optional and its default value is 1.0. 

   EditPalette: Gives information to edit the colors palettes of ColorList. This parameter is optional and can be False or be a list,
                its default value is False. When is False this parameter is ignored. When is a list this parameter must have
                information (inside list) to edit each colors palette of ColorList. This information can be None (if do not want to
                edit the color palette) or can be a sub-list is want to edit the colors palettes. This sub-list must have 4 item,
                the first item and the second item indicate the values range of colors palette, the third and the fourth item indicate
                the colors that will be extracted from color palette (created from first and second item of sub-list). The number of
                colors extracted must match with the number of colors of palette defined in Intervals.


   Returns
   -------
   FullCustomPalette: Custom color palette output
   FullColorsLabels:  Values of each colors from FullCustomPalette

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
            print('Increase must have one item or have the same dimensions of ColorList')
            exit()

         for idx in range(len(Intervals)-1):
            NColorList[idx] = int((Intervals[idx+1]-Intervals[idx])/Increase[idx])
            EndColorSplit[idx] = int((Intervals[idx+1]-Intervals[idx])/Increase[idx])

            if idx==0:
               FullColorsLabels = np.arange(Intervals[idx],Intervals[idx+1]+Increase[idx],Increase[idx])
            elif idx>0 and idx<len(Intervals)-2:
               ColorsLabels = np.arange(Intervals[idx],Intervals[idx+1]+Increase[idx],Increase[idx])
               FullColorsLabels = np.concatenate((FullColorsLabels[0:-1],ColorsLabels))
            elif idx==len(Intervals)-2:
               ColorsLabels = np.arange(Intervals[idx],Intervals[idx+1]+Increase[idx],Increase[idx])
               FullColorsLabels = np.concatenate((FullColorsLabels[0:-1],ColorsLabels))



         if EditPalette==False :
            pass
         else:
            if len(EditPalette)!=len(ColorList):
               print('ColorList and EditPalette must have the same number of items')
               exit()
            else:
               for idx in range(len(EditPalette)):

                  if EditPalette[idx]==None:
                     pass
                  else:
                     if len(EditPalette[idx])!=4:
                        print('Items in brackets of EditPalette must have 4 sub-items')
                        exit()
                     else:
                        NColorList[idx] = int((EditPalette[idx][1]-EditPalette[idx][0])/Increase[idx])
                        IniColorSplit[idx] = int((EditPalette[idx][2]-EditPalette[idx][0])/Increase[idx])
                        EndColorSplit[idx] = int((EditPalette[idx][3]-EditPalette[idx][0])/Increase[idx])

         for idx in range(len(ColorList)):

            if type(ColorList[idx]) == list:

               if len(ColorList[idx]) == 1:
                  MyColorsList = [ColorList[idx][0], ColorList[idx][0]]
               if len(ColorList[idx]) > 1:
                  MyColorsList = ColorList[idx]

               CustomPalette = LinearSegmentedColormap.from_list(name = 'ColorGradient', colors = MyColorsList, N = NColorList[idx])
               CustomPalette = CustomPalette(np.linspace(0.0, 1.0, NColorList[idx]))
               CustomPalette = CustomPalette[IniColorSplit[idx]:EndColorSplit[idx]]

            else: #if type(ColorList[idx]) == LinearSegmentedColormap:
               CustomPalette = ColorList[idx](np.linspace(0.0, 1.0, NColorList[idx]))
               CustomPalette = CustomPalette[IniColorSplit[idx]:EndColorSplit[idx]]

            if idx==0:
               FullCustomPalette = CustomPalette
            elif idx>0:
               FullCustomPalette = np.vstack((FullCustomPalette, CustomPalette))

         ncolors = FullCustomPalette.shape[0]

         if ncolors == 1:
            FullCustomPalette = np.concatenate((FullCustomPalette,FullCustomPalette))

         FullCustomPalette = LinearSegmentedColormap.from_list('ColorGradient', FullCustomPalette, ncolors)
         norm = BoundaryNorm(FullColorsLabels, ncolors=FullCustomPalette.N)

      else:
         print('ColorList and Increase must have the same number of items')
         exit()

   else:
      print('Intervals must have one item more than ColorList')
      exit()

   return FullCustomPalette, FullColorsLabels, norm;

#-----------------------------------------------------------------------------------------------------------------------------------


