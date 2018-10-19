#histogram calculation
# histogram.py
import sys, struct
from osgeo import gdal
from osgeo import gdalconst

# here we read only part of the image. Change it according to your DEM file
minLat = -60
maxLat = -30
minLong = 140
maxLong = 120
dataset = gdal.Open("DEM.tif")
band = dataset.GetRasterBand(1)
t = dataset.GetGeoTransform()
success,tInverse = gdal.InvGeoTransform(t)
x1,y1 = gdal.ApplyGeoTransform(tInverse, minLong, minLat)
x2,y2 = gdal.ApplyGeoTransform(tInverse, maxLong, maxLat)
minX = int(min(x1, x2))
maxX = int(max(x1, x2))
minY = int(min(y1, y2))
maxY = int(max(y1, y2))
width = (maxX - minX) + 1
fmt = "<" + ("h" * width)
for y in range(minY, maxY+1):
	scanline = band.ReadRaster(minX, y,width, 1,width, 1,gdalconst.GDT_Int16)
	values = struct.unpack(fmt, scanline)
	for value in values
		if value != band.GetNoDataValue():# exclude no data values
			try:
				histogram[value] += 1
			except KeyError:
				histogram[value] = 1
for height in sorted(histogram.keys()):
	print height,histogram[height]