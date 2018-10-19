from osgeo import ogr
shapefile = ogr.Open("TM_WORLD_BORDERS-0.3.shp") # here put the full path
layer = shapefile.GetLayer(0)
countries = []
for i in range(layer.GetFeatureCount()):
	feature = layer.GetFeature(i)
	countryCode = feature.GetField("ISO3")
	countryName = feature.GetField("NAME")
	geometry = feature.GetGeometryRef()
	minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
	countries.append((countryName, countryCode,minLat, maxLat,
	minLong, maxLong))
countries.sort()
for name,code,minLat,maxLat,minLong,maxLong in countries:
	print "%s (%s) lat=%0.4f..%0.4f, long=%0.4f..%0.4f" \
	% (name, code,minLat, maxLat,minLong, maxLong)
	#print "%s (%s) lat=%0.4f..%0.4f, long=%0.4f..%0.4f" \% (name, code,minLat, maxLat,minLong, maxLong)