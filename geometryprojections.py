import ogr, osr, os
os.chdir('D:\Projects\GIS\Working directory')
driver = ogr.GetDriverByName('ESRI Shapefile')
dataset = driver.Open('TM_WORLD_BORDERS-0.3.shp')
layer = dataset.GetLayer()
feature = layer.GetNextFeature()
geom = feature.GetGeometryRef()
print geom.GetX(), geom.GetY()
geoSR = osr.SpatialReference()
geoSR.ImportFromEPSG(4326)
utmSR = osr.SpatialReference()
utmSR.ImportFromEPSG(32612)
coordTrans = osr.CoordinateTransformation(geoSR, utmSR)
geom.Transform(coordTrans)
print geom.GetX(), geom.GetY()