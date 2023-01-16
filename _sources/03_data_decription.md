# Data Description

## Technical Specifications

The RGI is provided as [Esri shapefiles](https://en.wikipedia.org/wiki/Shapefile) containing the outlines of glaciers in geographic coordinates (longitude and latitude, in degrees) which are referenced to the WGS84 datum. Data are organized by first-order region. For each region there is one shapefile (`.shp` with accompanying `.dbf`, `.prj` and `.shx` files) containing all glaciers and ancillary `.csv` files containing additional statistics and hypsometric data. 

Each object in the RGI conforms to the data-model conventions of ESRI ArcGIS shapefiles. That is, each geometry object consists of a polygon with an exterior outline encompassing the glacier and any umber of interior outlines representing all of its nunataks (ice-free areas enclosed by the glacier). This data model is not the same as the current GLIMS data model, in which nunataks are independent objects (in fact, part of the RGI 7.0 processing workflow is to convert the GLIMS data model to the RGI data model).

The outlines of the RGI regions are provided as two shapefiles, one for first-order and one for second-order regions. A summary file containing glacier counts, glacierized area and a hypsometric list for each first-order and each second-order region is also provided. The 0.5°×0.5° grid is provided as a netcdf file in which zonal records of blank-separated glacierized areas in km2 are ordered from north to south. Information about RGI glaciers that are present in the mass-balance tables of the WGMS database Fluctuations of Glaciers is provided as an ancillary `.csv` file. The 19 regional attribute files are also provided in the `.csv` format.

## New in RGI 7.0: "glacier" and "glacier complex" data products

A "glacier" outline in the RGI (and GLIMS) is supposed to represent one dynamical entity with one terminus. TODO ...


## File naming convention

RGI2000-v7.0-G-02-00001

## Quality control 

RGI is a subset of GLIMS. All quality controls applied by GLIMS are therefore available for RGI. 

Quality checks were conducted on all glacier polygons. These include geometry, topology and attribute-field checks. As of version 3.2, the following steps are carried out:
The ArcGIS Repair Geometry tool is run on all polygons. Among other tasks, this routine checks for polygon closure, corrects the ring ordering and eliminates duplicate vertices.
Glaciers with areas less than 0.01 km2, the recommended minimum of the WGI, are removed. Nunataks are retained whatever their area.
A common error occurs when glacier polygons are adjusted during editing without ensuring that the shared boundary with an adjacent polygon is also updated (for example, at a glacier divide). Such errors result in overlapping polygons, or gaps between polygons, yielding small “sliver” polygons that must be removed or corrected. To check for these errors we constructed topology rules within ArcGIS. We began by checking topology using the ‘Does Not Overlap’ rule. Next, we removed each glacier with errors and wrote it to its own single-polygon shapefile. In an iterative procedure, each single glacier was updated on all others, such that areas with overlap were eliminated. The final subset of corrected outlines was merged back into the set of error-free outlines.
Attribute tables are checked, using Fortran subroutines and scripts written in Python, for things such as empty fields, GLIMSIds outside their glaciers, incorrectly formatted dates, incorrect assignments to RGI regions, and inconsistent minimum and maximum elevations.


## Data fields


- **`rgi_id`**:
    - `long_name`: rgi_identifier
    - `description`: Unique identifier assigned to a single outline by the RGI
    - `datatype`: str
    - `units`: 
    - `source`: RGI
    - `rgi6_name`: RGI_Id
- **`o1region`**:
    - `long_name`: first_order_region
    - `description`: The code of the first-order region to which the glacier belongs.
    - `datatype`: str
    - `units`: 
    - `source`: RGI
    - `rgi6_name`: O1Region
- **`o2region`**:
    - `long_name`: second_order_region
    - `description`: The code of the second-order region to which the glacier belongs.
    - `datatype`: str
    - `units`: 
    - `source`: RGI
    - `rgi6_name`: O2Region
- **`glims_id`**:
    - `long_name`: glims_identifier
    - `description`: Non-unique identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC
    - `datatype`: str
    - `units`: 
    - `source`: GLIMS
    - `rgi6_name`: GLIMS_Id
- **`anlys_id`**:
    - `long_name`: analysis_identifier
    - `description`: The unique identifier assigned within GLIMS for a particular outline of a glacier at a particular time.
    - `datatype`: int
    - `units`: 
    - `source`: GLIMS
    - `rgi6_name`: 
- **`src_date`**:
    - `long_name`: source_date
    - `description`: The as-of date for the outline (usually the acquisition date of the image), in the format ISO 8601.
    - `datatype`: str
    - `units`: date
    - `source`: GLIMS
    - `rgi6_name`: BgnDate
- **`primeclass`**:
    - `long_name`: primary_classification
    - `description`: Primary WGMS classification of the glacier.
    - `datatype`: int
    - `units`: 
    - `source`: GLIMS
    - `rgi6_name`: 
- **`conn_lvl`**:
    - `long_name`: connectivity_level
    - `description`: Level of connection to the Greenland Icesheet (0: no connection; 1: weak connection, 2: not in RGI).
    - `datatype`: int
    - `units`: 
    - `source`: GLIMS
    - `rgi6_name`: Connect
- **`glac_name`**:
    - `long_name`: glacier_name
    - `description`: Glacier name (when available).
    - `datatype`: str
    - `units`: 
    - `source`: GLIMS
    - `rgi6_name`: Name
- **`cenlon`**:
    - `long_name`: center_longitude
    - `description`: Longitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid).
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: CenLon
- **`cenlat`**:
    - `long_name`: center_latitude
    - `description`: Latitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid).
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: CenLat
- **`termlon`**:
    - `long_name`: terminus_longitude
    - `description`: Longitude of the lowest elevation point on the glacier outline.
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: 
- **`termlat`**:
    - `long_name`: terminus_latitude
    - `description`: Latitude of the lowest elevation point on the glacier outline.
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: 
- **`area_km2`**:
    - `long_name`: area_km2
    - `description`: Area of the glacier.
    - `datatype`: float
    - `units`: km2
    - `source`: Automated
    - `rgi6_name`: Area
- **`zmin_m`**:
    - `long_name`: minimum_elevation_m
    - `description`: Minimum elevation (m above sea level) of the glacier.
    - `datatype`: float
    - `units`: m
    - `source`: Automated
    - `rgi6_name`: Zmin
- **`zmax_m`**:
    - `long_name`: maximum_elevation_m
    - `description`: Maximum elevation (m above sea level) of the glacier.
    - `datatype`: float
    - `units`: m
    - `source`: Automated
    - `rgi6_name`: Zmax
- **`zmed_m`**:
    - `long_name`: median_elevation_m
    - `description`: Median elevation (m above sea level) of the glacier.
    - `datatype`: float
    - `units`: m
    - `source`: Automated
    - `rgi6_name`: Zmed
- **`zmean_m`**:
    - `long_name`: mean_elevation_m
    - `description`: Mean elevation (m above sea level) of the glacier.
    - `datatype`: float
    - `units`: m
    - `source`: Automated
    - `rgi6_name`: 
- **`slope_deg`**:
    - `long_name`: slope_degrees
    - `description`: Mean slope of the glacier surface.
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: Slope
- **`aspect_deg`**:
    - `long_name`: aspect_degrees
    - `description`: The aspect (orientation) of the glacier surface presented as an azimuth relative to 0° at due north.
    - `datatype`: float
    - `units`: degrees
    - `source`: Automated
    - `rgi6_name`: Aspect
- **`lmax_m`**:
    - `long_name`: max_length_m
    - `description`: Length (m) of the longest surface centerline of the glacier.
    - `datatype`: float
    - `units`: m
    - `source`: Automated
    - `rgi6_name`: Lmax
- **`geometry`**:
    - `long_name`: geometry
    - `description`: Glacier geometry (Polygon)
    - `datatype`: 
    - `units`: deg
    - `source`: GLIMS
    - `rgi6_name`: geometry
    