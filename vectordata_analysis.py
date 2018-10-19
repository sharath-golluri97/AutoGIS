import ogr,  os, sys
os.chdir('D:\Projects\GIS\Geopython')
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open('TM_WORLD_BORDERS-0.3.shp', 1)


featAreas = Area.GetNextFeature()
poly = featAreas.GetGeometryRef()
Sites.GetFeatureCount()
Sites.SetSpatialFilter(poly)
Sites.GetFeatureCount()
Sites.SetSpatialFilterRect(460000,4590000,
490000, 4600000)
Sites.GetFeatureCount()
Sites.SetSpatialFilter(None)
Sites.GetFeatureCount()