# Data description of RGI 7.0

## Technical specifications

The RGI is provided as [Esri shapefiles](https://en.wikipedia.org/wiki/Shapefile) containing the outlines of glaciers in geographic coordinates (longitude and latitude, in degrees) which are referenced to the WGS84 datum. Data are organized by first-order region. For each region there is one zipped file containing the RGI shapefile (one file for all glaciers in the region) as well as ancillary files containing additional statistics or hypsometric data.

For each region, RGI 7.0 provides four distinct data products:
- [Glacier product](glacier-product): includes outlines, attributes and auxiliary data for each individual glacier.
- [Glacier complex product](glacier-complex) (new in RGI 7.0): includes outlines of the contiguous ice mass that includes all glaciers with share common boundaries, and a reduced number of attributes.
- [Glacier intersects product](glacier-intersects) (new in RGI 7.0): delineates the "divides" or "boundaries" between adjacent glaciers from the glacier product. 
- [Glacier centerlines product](glacier-centerlines) (new in RGI 7.0): glacier centerlines computed with a flow routing algorithm.

These four products and associated files are detailed below.

### File naming convention

The name of each region's zipped file starts with `RGI` followed by three product descriptors:
- target year (so far all RGI versions refer to year 2000)
- RGI version number
- type of data product: 
  - glacier (`G`) 
  - glacier complex (`C`)
  - intersects (`I`)
  - centerlines (`L`)
- RGI region Code (obtained from the [RGI region description table](o1-regions-table))
  
The various product descriptors are separated by hyphens (`-`). For example `RGI2000-v7.0-G-03_arctic_canada_north.zip` refers to year 2000, RGI version 7.0, the glacier product and the region Arctic Canada North.

In addition to the shapefiles (following the same naming convention), each regional zip file comes with additional data files identified by the addition of descriptors in the filename. Examples: 
- `RGI2000-v7.0-C-01_alaska-attributes.csv`
- `RGI2000-v7.0-G-19_subantarctic_antarctic_islands-rgi6_links.csv`

These additional descriptors are documented below.

### Glacier identifiers in the RGI 7.0 glacier product

One RGI outline in the "glacier" product corresponds to one glacier. Glaciers are identified with the following attributes:

`rgi_id` 
: **Unique** identifier attributed by the RGI when constructing the files. These ids are generated automatically (in order of distance to the westernmost outline in a region) and follow the file naming convention described below. **These ids are different from RGI 6.0 and likely to change in future RGI versions**.

`glims_id` 
: **Non-unique** identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC. A single `glims_id` can have multiple outlines, for example at different dates or when a glacier disintegrates.

`anlys_id` 
: **Unique** identifier assigned within GLIMS for a particular outline of a glacier at a particular time and for a particular submission.  **These ids allow to unambiguously trace an outline back to the GLIMS database**, and will not change between future RGI versions if the outline does not change.

### RGI unique identifiers

Each entity in each of the RGI 7.0 products is given a unique identifier. RGI identifiers follow the same convention as the product files, but integrate a unique number per RGI entity. For example:
- `RGI2000-v7.0-G-02-00003` is the third glacier in RGI region 02, for the glacier product of RGI 7.0 and the target year 2000.
- `RGI2000-v7.0-C-11-00005` is the fifth glacier in RGI region 11, for the glacier complex product of RGI 7.0 and the target year 2000.
- `RGI2000-v7.0-I-13-00005` is the fifth intersect in RGI region 13, for the glacier intersects product of RGI 7.0 and the target year 2000.

## Data files

Each regional `.zip` file contains a number of files, depending on the product considered. Details for each of the four data products are given below. In the following, file contents are explained using RGI region 01 (Alaska) as example.

(glacier-product)=
### Glacier product

This product includes the glacier outlines as extracted from GLIMS together with additional data for each individual glacier: 


`RGI2000-v7.0-G-01_alaska.shp`
: RGI glacier outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-G-01_alaska-attributes.csv`
: glacier attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows users to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-G-01_alaska-attributes_metadata.json`
: information about the attributes: full name, description, units, etc.

`RGI2000-v7.0-G-01_alaska-submission_info.csv`
: information about the data providers ordered by submission id. Each glacier outline can be attributed to a specific submission via the `subm_id` attribute.

`RGI2000-v7.0-G-01_alaska-submission_info_metadata.json`
: information about the attributes in the submission info file: full name, description, units, etc.

`RGI2000-v7.0-G-01_alaska-rgi6_links.csv`
: a list of overlapping outline pairs between RGI 7.0 and RGI 6.0 describing 1:1, 1:n, n:1 or n:n relationships as well as the overlapping area between them. For example, a perfect match between an RGI 7.0 and RGI 6.0 outline results in a 1:1 relation with 100% area match in both. If a single RGI 6.0 outline was divided into two glaciers for RGI7, a 2:1 relationship (a cluster) would result with two lines in the table with twice 50% area match in RGI 6.0 and twice 100% match in RGI 7.0. In more complex cases the matches are not always perfect and the relationships less straightforward, for example when an outline was remapped.

`RGI2000-v7.0-G-01_alaska-hypsometry.nc`
: hypsometry files (TODO)

For more information on this product, see [](data_fields/glacier_product.md).


(glacier-complex)=
### Glacier complex product (new in RGI7)

The "glacier complex" product is the result of a spatial merge operation of the glacier product ([dissolve](http://wiki.gis.com/wiki/index.php/Dissolve) in the GIS jargon). The operation is realized on geometries only, which means that any cluster of connected glaciers (however small the connection) will be merged into one entity in the glacier complex product. The resulting inventory has the same area but a smaller or equal number of entities as the glacier product. The only attributes remaining or recomputed after the merge are `o1region`,  `o2region`, `cenlon`, `cenlat`, and `area_km2`. This glacier complex product may be preferred over the glacier product for certain applications, for example for distributed glacier flow modeling or for ice thickness inversions.

The following files are included in the unzipped folder (exemplified with region 01):

`RGI2000-v7.0-C-01_alaska.shp`
: the RGI glacier complex outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-C-01_alaska-attributes.csv`
: glacier complex attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows users to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-C-01_alaska-attributes_metadata.json`
: information about the attributes: full name, description, units, etc.

`RGI2000-v7.0-C-01_alaska-CtoG_links.json`
: links between the glacier complex to the glacier products, in a JSON dictionary. The keys are the glacier complex ids (same length as the glacier complex file) and the values are the corresponding glacier product ids (one or more depending on the cluster).

For more information on this product, see [](data_fields/glacier_complex_product.md).

(glacier-intersects)=
### Glacier intersects product (new in RGI7)

The glacier intersects products delineates the "divides" or "borders" between adjacent ice bodies. The resulting geometries are single lines (each with their own id), with attributes `rgi_g_id_1` and `rgi_g_id_2` indicating which glacier entities are adjacent. This product is useful for describing the connection between two glaciers (for example by its length) or for glacier models able to use this information.

The following files are included in the unzipped folder (exemplified with region 01):

`RGI2000-v7.0-I-01_alaska.shp`
: the RGI glacier intersects outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-I-01_alaska-attributes.csv`
: glacier intersects attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows users to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-I-01_alaska-attributes_metadata.json`
: information about the attributes: full name, description, units, etc.

For more information on this product, see [](data_fields/intersects_product.md).

:::{figure-md} intersects-fig
<img src="img/example_intersects.png" alt="intersects map" class="bg-primary mb-1">

Example of the glacier intersects product (red) drawn over the glacier product (light blue).
:::


(glacier-centerlines)=
### Glacier centerlines product (new in RGI7)

TODO

### Global gridded product

TODO: gridded RGI products

<!--- The outlines of the RGI regions are provided as two shapefiles, one for first-order and one for second-order regions. A summary file containing glacier counts, glacierized area and a hypsometric list for each first-order and each second-order region is also provided. The 0.5°×0.5° grid is provided as a netcdf file in which zonal records of blank-separated glacierized areas in km² are ordered from north to south. Information about RGI glaciers that are present in the mass-balance tables of the WGMS database Fluctuations of Glaciers is provided as an ancillary `.csv` file. The 19 regional attribute files are also provided in the `.csv` format. --->

## Data fields

- [](data_fields/glacier_product.md)
- [](data_fields/glacier_complex_product.md)
- [](data_fields/intersects_product.md)
