# Glacier complex product

**New in RGI 7.0**

The glacier complex product is the result of a spatial merge operation of the glacier product ([dissolve](http://wiki.gis.com/wiki/index.php/Dissolve) in the GIS jargon). The operation is realized on geometries only, which means that any cluster of connected glaciers (however small the connection) will be merged into one entity in the glacier complex product. The resulting inventory has the same area but a smaller or equal number of entities as the glacier product. Only a few attributes from the original glacier product remain after the merge.

The glacier complex product may be preferred over the glacier product for certain applications, for example for distributed glacier flow modeling or for ice thickness inversions.

:::{figure-md} complex-fig
<img src="../img/example_complex.png" alt="complex map" class="bg-primary mb-1">

Example of the glacier complex product (light blue), with outlines in black. In comparison with [the glacier product](glacier-fig), the divides between individual glaciers have disappeared and the entire ice mass constitutes one single entity.
:::

## Product files

In the following, file contents are explained using RGI region 01 (Alaska) as example:

`RGI2000-v7.0-C-01_alaska.shp`
: The RGI glacier complex outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-C-01_alaska-attributes.csv`
: Glacier complex attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows users to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-C-01_alaska-attributes_metadata.json`
: Information about the attributes: full name, description, units, etc.

`RGI2000-v7.0-C-01_alaska-CtoG_links.json`
: Links between the glacier complex to the glacier products, in a JSON dictionary. The keys are the glacier complex ids (same length as the glacier complex file) and the values are the corresponding glacier product ids (one or more depending on the cluster).

## Full list of attributes

The following attributes are available in the RGI 7.0 shapefiles.

`rgi_id`
: `long_name`: RGI identifier <br/> `description`: Unique identifier assigned to a single glacier complex. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`o1region`
: `long_name`: First order region <br/> `description`: The code of the first-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`o2region`
: `long_name`: Second order region <br/> `description`: The code of the second-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`cenlon`
: `long_name`: Center longitude <br/> `description`: Longitude of an approximately central point within the glacier outlines (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI

`cenlat`
: `long_name`: Center latitude <br/> `description`: Latitude of an approximately central point within the glacier outlines (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI

`utm_zone`
: `long_name`: UTM zone <br/> `description`: Number of the UTM zone for this glacier complex, based on its representative point. Note that this attribute is for information only, the geometries are all in WGS84. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI

`area_km2`
: `long_name`: Glacier complex area <br/> `description`: Area of the glacier complex. <br/> `datatype`: float <br/> `units`: km2 <br/> `source`: RGI

`geometry`
: `long_name`: Geometry <br/> `description`: Glacier complex geometry (Polygon). <br/> `datatype`:  <br/> `units`: deg <br/> `source`: RGI
