import ogr, os, sys
os.chdir('D:\Projects\GIS\Geopython')

#reading and writing by block
xBlockSize = 64
yBlockSize = 64
for i in range(0, rows, yBlockSize): if
i + yBlockSize < rows:
numRows = yBlockSize else:
numRows = rows – i
for j in range(0, cols, xBlockSize): if
j + xBlockSize < cols:
numCols = xBlockSize
else:
numCols = cols – j
data = band.ReadAsArray(j, i, numCols, numRows)
# do calculations here to create outData array
outBand.WriteArray(outData, j, i)

#Set noData value
# SetNoDataValue(<value>)
#GetNoDataValue()

#calculate statistics
#Flushcache()
#GetStatistics(<approx_ok>,<force>)
#outBand.FlushCache()
#outBand.GetStatistics(0, 1)

#Georefernce the image
#If it is same as the  input image
geoTransform = inDataset.GetGeoTransform()
outDataset.SetGeoTransform(geoTransform) 
#with projection information
proj = inDataset.GetProjection()
outDataset.SetProjection(proj)

#build pyramids
gdal.SetConfigOption('HFA_USE_RRD', 'YES')

outDataset.BuildOverviews(overviewlist=[2,4,8,16,32,64,128])











