
#Imagine you have a satellite image and you want to view it with a custom color palette. You can create a custom colors palette using the Custom_colors_palette script.

#-----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import custom_color_palette as ccpl

#-----------------------------------------------------------------------------------------------------------------------------------

SatImg = np.fromfile('SatImage.bin', dtype='float32').reshape((800,1000))

#-----------------------------------------------------------------------------------------------------------------------------------

mypalette, colorslabels = ccpl.creates_palette([['white','black']], [180.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example00', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example00.png')

#-----------------------------------------------------------------------------------------------------------------------------------

mypalette, colorslabels = ccpl.creates_palette([['gold','orange','red','blue','cyan','#5A6673',(0/255, 0/255, 0/255)]], [180.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example01', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example01.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([plt.cm.jet], [180.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example02', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example02.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([['yellow','gold','red','darkred'], plt.cm.ocean_r], [180.0,250.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example03', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example03.png')

#-----------------------------------------------------------------------------------------------------------------------------------

mypalette, colorslabels = ccpl.creates_palette([['yellow','gold','red','darkred'], ['lime'], ['hotpink'], plt.cm.ocean_r], [180.0,250.0,255.0,260.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example04', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example04.png')

#-----------------------------------------------------------------------------------------------------------------------------------

mypalette, colorslabels = ccpl.creates_palette([['yellow','gold','red','darkred'], ['lime'], ['hotpink'], plt.cm.ocean_r], [180.0,250.0,255.0,260.0,330.0], Increase=[1.0,1.0,5.0,5.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example05', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example05.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([plt.cm.Greys], [180.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example06', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example06.png')

#-----------------------------------------------------------------------------------------------------------------------------------



mypalette, colorslabels = ccpl.creates_palette([['maroon', 'red', 'darkorange', '#ffff00', 'forestgreen', 'cyan', 'royalblue', (148/255, 0/255, 211/255)], plt.cm.Greys], [180.0,240.0,330.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example07', figsize=(6,4), dpi=100)
img = plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example07.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([['maroon', 'red', 'darkorange', '#ffff00', 'forestgreen', 'cyan', 'royalblue', (148/255, 0/255, 211/255)], plt.cm.Greys], [180.0,240.0,330.0], EditPalette=[None,[180.0,330.0,240.0,330.0]])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example08', figsize=(6,4), dpi=100)
img=plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example08.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([['maroon', 'red', 'darkorange', '#ffff00', 'forestgreen', 'cyan', 'royalblue', (148/255, 0/255, 211/255)], plt.cm.Greys], [180.0,240.0,330.0], EditPalette=[None,[180.0,330.0,240.0,330.0]], Increase=[1.0,5.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example09', figsize=(6,4), dpi=100)
img=plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example09.png')

#-----------------------------------------------------------------------------------------------------------------------------------


mypalette, colorslabels = ccpl.creates_palette([['maroon', 'red', 'darkorange', '#ffff00', 'forestgreen', 'cyan', 'royalblue', (148/255, 0/255, 211/255)], plt.cm.Greys], [180.0,240.0,330.0], EditPalette=[None,[180.0,330.0,240.0,330.0]], Increase=[5.0,1.0])

norm = colors.BoundaryNorm(colorslabels, ncolors=mypalette.N)
tickslabels = np.arange(180,340,10)

fig = plt.figure('example10', figsize=(6,4), dpi=100)
img=plt.imshow(SatImg, cmap=mypalette, norm=norm)
cbar = plt.colorbar(img, spacing='proportional', ticks=tickslabels)
cbar.ax.set_yticklabels(tickslabels)
plt.savefig('example10.png')

#-----------------------------------------------------------------------------------------------------------------------------------

plt.show()

