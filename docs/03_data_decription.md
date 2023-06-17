# Data description of RGI 7.0

The RGI is provided as [Esri shapefiles](https://en.wikipedia.org/wiki/Shapefile) containing the outlines of glaciers and related products in geographic coordinates (longitude and latitude, in degrees) which are referenced to the WGS84 datum. Data are organized by first-order region. For each region there is one zipped file containing the RGI shapefile (one file for all glaciers in the region) as well as ancillary files containing additional statistics or hypsometric data.

For each region, RGI 7.0 provides four distinct data products:
- [](products/glacier_product): includes outlines, attributes and auxiliary data for each individual glacier.
- [](products/glacier_complex_product) (new in RGI 7.0): includes outlines of all glacier complexes (defined as contiguous ice masses that encompass all glaciers that share common boundaries), and a reduced number of attributes.
- [](products/intersects_product) (new in RGI 7.0): shapefiles of the "divides" or "boundaries" between adjacent glaciers derived from the glacier product. 
- [](products/centerlines_product) (new in RGI 7.0): glacier centerlines computed with a flow routing algorithm.

These four products and associated files are detailed in their corresponding section.

## File naming convention

The name of each region's zipped file starts with `RGI` followed by three product descriptors:
- target year (so far all RGI versions refer to year 2000)
- RGI version number
- type of data product: 
  - glacier (`G`) 
  - glacier complex (`C`)
  - intersects (`I`)
  - centerlines (`L`)
- RGI region code (obtained from the [RGI region description table](o1-regions-table)), which consists of the region number and a standardized name
  
The various product descriptors are separated by hyphens (`-`). For example, `RGI2000-v7.0-G-03_arctic_canada_north.zip` refers to year 2000, RGI version 7.0, the glacier product and the region Arctic Canada North.

In addition to the shapefiles (following the same naming convention), each regional zip file comes with additional data files identified by the addition of descriptors in the filename. Examples: 
- `RGI2000-v7.0-C-01_alaska-attributes.csv`
- `RGI2000-v7.0-G-19_subantarctic_antarctic_islands-rgi6_links.csv`

These additional descriptors are documented in each product's description page.

## Entity identifiers

Each entity in each of the RGI 7.0 products (i.e. each glacier, glacier complex, centerline or intersect) is given a unique identifier. The identifiers follow the same convention as the product files, but add an additional unique number per entity to the name. For example:
- `RGI2000-v7.0-G-02-00003` is the third glacier in RGI region 02, for the glacier product of RGI 7.0 and the target year 2000.
- `RGI2000-v7.0-C-11-00005` is the fifth glacier complex in RGI region 11, for the glacier complex product of RGI 7.0 and the target year 2000.
- `RGI2000-v7.0-I-13-00005` is the fifth intersect in RGI region 13, for the glacier intersects product of RGI 7.0 and the target year 2000.


## Detailed product description

- [](products/glacier_product)
- [](products/glacier_complex_product)
- [](products/intersects_product)
- [](products/centerlines_product)
