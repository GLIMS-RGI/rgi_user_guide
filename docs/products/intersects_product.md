# Glacier intersects product

**New in RGI 7.0**

The glacier intersects products includes only the "divides" or "borders" between adjacent glaciers rather than the complete outlines. The resulting geometries are single lines (each with their own id), with attributes `rgi_g_id_1` and `rgi_g_id_2` indicating which glacier entities are adjacent. This product is useful for describing the connection between two glaciers (for example by the length of a common boundary) or for glacier models able to use this kind of information.

:::{figure-md} intersects-fig
<img src="../img/example_intersects.png" alt="intersects map" class="bg-primary mb-1">

Example of the glacier intersects product (red) drawn over the glacier product (light blue).
:::

## Product files

In the following, file contents are explained using RGI region 01 (Alaska) as example:

`RGI2000-v7.0-I-01_alaska.shp`
: RGI **glacier intersects** as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-I-01_alaska-attributes.csv`
: Glacier intersects **attributes** in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows users to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-I-01_alaska-attributes_metadata.json`
: **Description of the attributes** in the intersect product shapefile: full name, description, units, etc. The content of this file is displayed in [](intersects-attrs) below.

(intersects-attrs)=
## Full list of attributes

The following attributes are available in the RGI 7.0 shapefiles.

`rgi_id`
: `long_name`: RGI identifier <br/> `description`: Unique identifier assigned to a single intersect line. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`rgi_g_id_1`
: `long_name`: RGI glacier identifier of glacier 1 <br/> `description`: Glacier identifier of the intersected glacier number 1. An intersect line is always connecting two glaciers, but the choice of which glacier is listed as 1 is arbitrary. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`rgi_g_id_2`
: `long_name`: RGI glacier identifier of glacier 2 <br/> `description`: Glacier identifier of the intersected glacier number 2. An intersect line is always connecting two glaciers, but the choice of which glacier is listed as 2 is arbitrary. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI

`length_m`
: `long_name`: Intersect length <br/> `description`: Length of the intersect in meters. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI

`geometry`
: `long_name`: Geometry <br/> `description`: Intersect geometry (LineString). <br/> `datatype`:  <br/> `units`: deg <br/> `source`: RGI
