# reading anf writing vector data
import ogr, os, sys
os.chdir('D:\Projects\GIS\Geopython')
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open('TM_WORLD_BORDERS-0.3.shp', 1)
if dataSource is None:
	print 'Could not open file'
	sys.exit(1)
layer = dataSource.GetLayer()

#getting shapefile info
numFeatures = layer.GetFeatureCount()
print 'Feature count:', numFeatures
extent = layer.GetExtent()
print 'Extent:', extent
#print 'Feature count:' + str(numFeatures)

#getting  shapefile features
#cnt = 0
feature = layer.GetFeature(0)
feature =layer.GetNextFeature()
#while feature:
	#cnt = cnt +1 
	#feature = layer.GetNextFeature()
	#layer.ResetReading()
	#feature.Destroy()
#print 'There are ' + str(cnt) + 'features'

#getting Feature's attributes
#id = feature.GetField('id')
#id = feature.GetFieldAsString('id')

#getting feature's geometry
#geometry = feature.GetGeometryRef()
#x = geometry.GetX()
#y = geometry.GetY()

#feature destroy
feature.Destroy()

#close the data source
dataSource.Destroy()