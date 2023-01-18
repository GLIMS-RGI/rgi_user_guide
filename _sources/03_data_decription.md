# Data Description

## Technical Specifications

The RGI is provided as [Esri shapefiles](https://en.wikipedia.org/wiki/Shapefile) containing the outlines of glaciers in geographic coordinates (longitude and latitude, in degrees) which are referenced to the WGS84 datum. Data are organized by first-order region. For each region there is one shapefile (`.shp` with accompanying `.dbf`, `.prj` and `.shx` files) containing all glaciers and ancillary `.csv` files containing additional statistics and hypsometric data. 

Each object in the RGI conforms to the data-model conventions of ESRI ArcGIS shapefiles. That is, each geometry object consists of a polygon with an exterior outline encompassing the glacier and any umber of interior outlines representing all of its nunataks (ice-free areas enclosed by the glacier). This data model is not the same as the current GLIMS data model, in which nunataks are independent objects (in fact, part of the RGI 7.0 processing workflow is to convert the GLIMS data model to the RGI data model).

### File naming convention

TODO

RGI2000-v7.0-G-02-00001

### Glacier identifiers in RGI and GLIMS

One RGI outline in the "glacier" product (see below) corresponds to one glacier. Glaciers are identified with the following attributes:

`rgi_id` 
: **Unique** identifier attributed by the RGI when constructing the files. These ids are generated automatically (in order of distance to the westernmost outline in a region) and follow the file naming convention described above. **These ids are likely to change between RGI versions**.

`glims_id` 
: **Non-unique** identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC. A single `glims_id` can have multiple outlines, for example at different dates or when a glacier disintegrates.

`anlys_id` 
: **Unique** identifier assigned within GLIMS for a particular outline of a glacier at a particular time and for a particular submission.  **These ids allow to unambiguously trace an outline back to the GLIMS database**, and will not change between future RGI versions if the outline does not change.


### Data files

#### Regional products

With the example of RGI region 01:

`RGI2000-v7.0-G-01_alaska.shp`
: the RGI glacier outlines as a shapefile (with accompanying `.dbf`, `.prj`, `.cpg` and `.shx` files).

`RGI2000-v7.0-G-01_alaska_attributes.csv`
: glacier attributes in a `.csv` file. The attributes are strictly the same as those encountered in the shapefile. 

`RGI2000-v7.0-G-01_alaska_subm_info.csv`
: information about the data providers ("submission info"). Each glacier outline can be attributed to a specific submission via the `subm_id` attribute.

`RGI2000-v7.0-G-01_alaska_hypsometry.csv`
: hypsometry files (as csv? NetCDF?)

#### Global products

TODO

<!--- The outlines of the RGI regions are provided as two shapefiles, one for first-order and one for second-order regions. A summary file containing glacier counts, glacierized area and a hypsometric list for each first-order and each second-order region is also provided. The 0.5°×0.5° grid is provided as a netcdf file in which zonal records of blank-separated glacierized areas in km² are ordered from north to south. Information about RGI glaciers that are present in the mass-balance tables of the WGMS database Fluctuations of Glaciers is provided as an ancillary `.csv` file. The 19 regional attribute files are also provided in the `.csv` format. --->

### New in RGI 7.0: "glacier" and "glacier complex" data products

TODO

## Quality control and data integrity

RGI is a subset of GLIMS, without any modification to the outlines. All quality controls applied by GLIMS are therefore inherited by RGI - this is also true for issues or problems in the outlines. Glaciers with areas less than 0.01 km², the recommended minimum of the World Glacier Inventory, are removed. Nunataks are retained whatever their area. Attributes which are not part of RGI are computed, filled and checked using scripts written in Python.

RGI applies the following data integrity checks on GLIMS data:
- where possible (i.e. when we had access to the original inventories, for example GAMDAMv2 which is openly available), we check that the RGI (and hence GLIMS) are equivalent to the original dataset. This helped to discover a few bugs in the GLIMS data ingest workflow.
- we roughly check for duplicated outlines by checking that no outline's representative point overlaps with another outline (less then a dozen outlines are filtered from GLIMS this way)

However, we do not check for polygon geometry validity, as this is a step that should be done by the outline submitters prior to GLIMS. About 2% of all geometries in RGI7 are "invalid" according to the [Open Geospatial Consortium Implementation Standard](https://www.ogc.org/standards/sfa) (for reference, about 5% of all RGI6 outlines did not pass this test). Examples of invalid geometries are outlines containing a "figure of 8" or similar singularities. Most applications (such as vector to raster conversion or area computation) do not require valid geometries in this strict sense.

## Data fields

The following attributes are available in the RGI shapefiles:

`rgi_id`
: `long_name`: rgi_identifier <br/> `description`: Unique identifier assigned to a single outline by the RGI <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: RGI_Id

`o1region`
: `long_name`: first_order_region <br/> `description`: The code of the first-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: O1Region

`o2region`
: `long_name`: second_order_region <br/> `description`: The code of the second-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: O2Region

`glims_id`
: `long_name`: glims_identifier <br/> `description`: Non-unique identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: GLIMS_Id

`anlys_id`
: `long_name`: analysis_identifier <br/> `description`: The unique identifier assigned within GLIMS for a particular outline of a glacier at a particular time. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`subm_id`
: `long_name`: submission_id <br/> `description`: Unique identifier assigned by GLIMS to a specific data submission. Allows to obtain information about the analysts and data submitters. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`src_date`
: `long_name`: source_date <br/> `description`: The as-of date for the outline (usually the acquisition date of the image), in the format ISO 8601. <br/> `datatype`: str <br/> `units`: date <br/> `source`: GLIMS <br/> `rgi6_name`: BgnDate

`primeclass`
: `long_name`: primary_classification <br/> `description`: Primary WGMS classification of the glacier. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`conn_lvl`
: `long_name`: connectivity_level <br/> `description`: Level of connection to the Greenland Icesheet (0: no connection; 1: weak connection, 2: not in RGI). <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: Connect

`glac_name`
: `long_name`: glacier_name <br/> `description`: Glacier name (when available). <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: Name

`is_rgi6`
: `long_name`: same_as_rgi6 <br/> `description`: Flag indicating if the outline is the same as in RGI6 (1) or was remapped (0). Note that it does not guarantee strict equivalence of the polygon. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`cenlon`
: `long_name`: center_longitude <br/> `description`: Longitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: CenLon

`cenlat`
: `long_name`: center_latitude <br/> `description`: Latitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: CenLat

`termlon`
: `long_name`: terminus_longitude <br/> `description`: Longitude of the lowest elevation point on the glacier outline. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: 

`termlat`
: `long_name`: terminus_latitude <br/> `description`: Latitude of the lowest elevation point on the glacier outline. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: 

`area_km2`
: `long_name`: area_km2 <br/> `description`: Area of the glacier. <br/> `datatype`: float <br/> `units`: km2 <br/> `source`: Automated <br/> `rgi6_name`: Area

`zmin_m`
: `long_name`: minimum_elevation_m <br/> `description`: Minimum elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: Automated <br/> `rgi6_name`: Zmin

`zmax_m`
: `long_name`: maximum_elevation_m <br/> `description`: Maximum elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: Automated <br/> `rgi6_name`: Zmax

`zmed_m`
: `long_name`: median_elevation_m <br/> `description`: Median elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: Automated <br/> `rgi6_name`: Zmed

`zmean_m`
: `long_name`: mean_elevation_m <br/> `description`: Mean elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: Automated <br/> `rgi6_name`: 

`slope_deg`
: `long_name`: slope_degrees <br/> `description`: Mean slope of the glacier surface. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: Slope

`aspect_deg`
: `long_name`: aspect_degrees <br/> `description`: The aspect (orientation) of the glacier surface presented as an azimuth relative to 0° at due north. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: Automated <br/> `rgi6_name`: Aspect

`lmax_m`
: `long_name`: max_length_m <br/> `description`: Length (m) of the longest surface centerline of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: Automated <br/> `rgi6_name`: Lmax

`geometry`
: `long_name`: geometry <br/> `description`: Glacier geometry (Polygon) <br/> `datatype`:  <br/> `units`: deg <br/> `source`: GLIMS <br/> `rgi6_name`: geometry

## Additional information on data fields

TODO: description of topo data, etc.
