import os, sys, ogr, gdal, utils, numpy
from gdalconst import *
os.chdir('D:\Projects\GIS\Geopython')
# register all of the GDAL drivers
gdal.AllRegister()
# open the image
ds = gdal.Open('ts.tif', GA_ReadOnly)
if ds is None:
	print 'Could not open aster.img'
sys.exit(1)
# get image size
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount
# get the band and block sizes
band = ds.GetRasterBand(1)
blockSizes = utils.GetBlockSize(band)
xBlockSize = blockSizes[0]
yBlockSize = blockSizes[1]
# initialize variable
count = 0
# loop through the rows
for i in range(0, rows, yBlockSize):
	if i + yBlockSize < rows:
		numRows = yBlockSize
	else:
		numRows = rows – I 
# loop through the columns
for j in range(0, cols, xBlockSize):
	if j + xBlockSize < cols:
		numCols = xBlockSize
	else:
		numCols = cols – j
# read the data and do the calculations
data = band.ReadAsArray(j, i, numCols, numRows).astype(Numeric.Float)
mask = Numeric.greater(data, 0)
count = count + Numeric.sum(Numeric.sum(mask))
# print results
print 'Number of non-zero pixels:', count