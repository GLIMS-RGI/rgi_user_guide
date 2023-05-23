# Data Description

## Technical specifications

The RGI is provided as [Esri shapefiles](https://en.wikipedia.org/wiki/Shapefile) containing the outlines of glaciers in geographic coordinates (longitude and latitude, in degrees) which are referenced to the WGS84 datum. Data are organized by first-order region. For each region there is one zipped file containing the RGI shapefile (on file for all glaciers in the region) as well as ancillary files containing additional statistics or hypsometric data. 

### File naming convention

Here is an example of an RGI zipped file name:

`RGI2000-v7.0-G-03_arctic_canada_north.zip`

The various product descriptors are separated by hyphens (`-`):

- `RGI2000` indicates that this file belongs to the RGI products with target year 2000. Note that there is currently only one target year for RGI, but that future versions might target different years.
- `v7.0` is the RGI version number. RGI reserves the right to publish small (e.g. `v7.1`) or larger (e.g. `v8.0`) increments.
- `G` designates the "glacier" product, which is the default RGI product. As of RGI v7, RGI also provides a "glacier complex" product, designated by the letter `C`, an "intersects" product (designated by the letter `I`) and a "centerlines" product (designated by the letter `L`). See below for details.
- `03_arctic_canada_north` is the region indentifier. The first two digits indicate the region's first order id (`01` to `19`), followed by region name (lower case names separated by underscores). This identifier is provided in the RGI region files.

### Glacier identifiers in RGI and GLIMS

One RGI outline in the "glacier" product corresponds to one glacier. Glaciers are identified with the following attributes:

`rgi_id` 
: **Unique** identifier attributed by the RGI when constructing the files. These ids are generated automatically (in order of distance to the westernmost outline in a region) and follow the file naming convention described below. **These ids are likely to change between RGI versions**.

`glims_id` 
: **Non-unique** identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC. A single `glims_id` can have multiple outlines, for example at different dates or when a glacier disintegrates.

`anlys_id` 
: **Unique** identifier assigned within GLIMS for a particular outline of a glacier at a particular time and for a particular submission.  **These ids allow to unambiguously trace an outline back to the GLIMS database**, and will not change between future RGI versions if the outline does not change.

### RGI unique identifiers

RGI identifiers follow the same convention ad the product files, but integrate a unique number per RGI entity. 
For example:
- `RGI2000-v7.0-G-02-00003` is the third glacier in RGI region 02, for the glacier product of RGI v7.0 and the target year 2000.
- `RGI2000-v7.0-C-11-00005` is the fifth glacier in RGI region 11, for the glacier complex product of RGI v7.0 and the target year 2000.

## Data files

Each regional `.zip` file contains a number of files, depending on the product considered. 

### Glacier product

This is the main RGI product. It contains the individual glacier outlines and is similar to RGI6.

You will find the following files in the unzipped folder for region 01:

`RGI2000-v7.0-G-01_alaska.shp`
: the RGI glacier outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-G-01_alaska_attributes.csv`
: glacier attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-G-01_alaska_attributes_metadata.json`
: information about the attributes: long name, description, units, etc.

`RGI2000-v7.0-G-01_alaska_submission_info.csv`
: information about the data providers ordered by submission id. Each glacier outline can be attributed to a specific submission via the `subm_id` attribute.

`RGI2000-v7.0-G-01_alaska_submission_info_metadata.json`
: information about the attributes in the submission info file: long name, description, units, etc.

`RGI2000-v7.0-G-01_alaska_rgi6_links.csv`
: a list of overlapping geometry pairs between RGI7 and RGI6 describing 1:1, 1:n, n:1 or n:n relationships as well as the overlapping area between them. For example, a perfect match between an RGI7 and RGI6 results in a 1:1 relation with 100% area match in both. A single RGI6 outline was was divided for RGI7 results in a 2:1 relationship (a cluster) with two lines in the table with twice 50% area match in RGI6 and twice 100% match in RGI7. In more complex cases the matches are not always perfect and the relationships less straightforward: for example when an outline was remapped.

`RGI2000-v7.0-G-01_alaska_hypsometry.nc`
: hypsometry files (TODO)

For more information on this product, see [](data_fields/glacier_product.md).


(glacier-complex)=
### Glacier complex product (new in RGI7)

The "glacier complex" product is the result of a spatial merge operation of the glacier product ([dissolve](http://wiki.gis.com/wiki/index.php/Dissolve) in the GIS jargon). The operation is realized on geometries only, which means that any cluster of connected glaciers (however small the connection) will be merged into one entity in the glacier complex product. The resulting inventory has the same area but a smaller or equal number of entities as the glacier product. The only attributes remaining or recomputed after the merge are `o1region`,  `o2region`, `cenlon`, `cenlat`, and `area_km2`. This glacier complex product might be used by distributed models of ice thickness, for example.

You will find the following files in the unzipped folder for region 01:

`RGI2000-v7.0-C-01_alaska.shp`
: the RGI glacier complex outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-C-01_alaska_attributes.csv`
: glacier complex attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-G-01_alaska_attributes_metadata.json`
: information about the attributes: long name, description, units, etc.

`RGI2000-v7.0-C-01_alaska_C-to-G-links.json`
: links between the glacier complex to the glacier products, in a JSON dictionary. The keys are the glacier complex ids (same length as the glacier complex file) and the values are the corresponding glacier product id (one ore more, depending on the cluster). 

For more information on this product, see [](data_fields/glacier_complex_product.md).

(glacier-intersects)=
### Glacier intersects product (new in RGI7)

The glacier intersects products delineates the "divides" or "borders" between adjacent ice bodies. The resulting geometries are single lines (each with their own id), with attributes `rgi_g_id_1` and `rgi_g_id_2` indicating which glacier entities are adjacent. This product is useful for describing the connection between two glaciers (for example by its length) or for glacier models able to use this information. 

You will find the following files in the unzipped folder for region 01:

`RGI2000-v7.0-I-01_alaska.shp`
: the RGI glacier intersects outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-I-01_alaska_attributes.csv`
: glacier intersects attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. This file allows to read glacier attributes without reading the entire shapefile.

`RGI2000-v7.0-I-01_alaska_attributes_metadata.json`
: information about the attributes: long name, description, units, etc.

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
