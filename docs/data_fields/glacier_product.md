# Data fields: glacier product 

The following attributes are available in the RGI 7.0 shapefiles. For more details on some of them, see the specific sections below.

## Full list

`rgi_id`
: `long_name`: RGI identifier <br/> `description`: Unique identifier assigned to a single outline by the RGI <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: RGI_Id

`o1region`
: `long_name`: First order region <br/> `description`: The code of the first-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: O1Region

`o2region`
: `long_name`: Second order region <br/> `description`: The code of the second-order region to which the glacier belongs. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: O2Region

`glims_id`
: `long_name`: GLIMS identifier <br/> `description`: Non-unique identifier assigned to glaciers by the Global Land Ice Measurements from Space service at NSIDC <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: GLIMS_Id

`anlys_id`
: `long_name`: Analysis identifier <br/> `description`: The unique identifier assigned within GLIMS for a particular outline of a glacier at a particular time. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`subm_id`
: `long_name`: Submission identifier <br/> `description`: Unique identifier assigned by GLIMS to a specific data submission. Allows to obtain information about the analysts and data submitters. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`src_date`
: `long_name`: Outline source date <br/> `description`: The as-of date for the outline (usually the acquisition date of the image), in the format ISO 8601. <br/> `datatype`: str <br/> `units`: date <br/> `source`: GLIMS <br/> `rgi6_name`: BgnDate

`cenlon`
: `long_name`: Center longitude <br/> `description`: Longitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: CenLon

`cenlat`
: `long_name`: Center latitude <br/> `description`: Latitude of the representative point of the glacier, guaranteed to be located within the glacier outlines and approximatively central (not the centroid). <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: CenLat

`utm_zone`
: `long_name`: UTM zone <br/> `description`: Number of the UTM zone for this glacier, based on its representative point. Note that this attribute is for information only, the geometries are all in WGS84. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`area_km2`
: `long_name`: Glacier area <br/> `description`: Area of the glacier. <br/> `datatype`: float <br/> `units`: km2 <br/> `source`: RGI <br/> `rgi6_name`: Area

`primeclass`
: `long_name`: Primary classification <br/> `description`: WGMS primary classification of the glacier. For a categories description, see user guide. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`conn_lvl`
: `long_name`: Connectivity level <br/> `description`: Level of connection to the Greenland Icesheet (0: no connection; 1: weak connection). <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: Connect

`surge_type`
: `long_name`: Evidence for surging <br/> `description`: Flag indicating if surging behavior has been documented for this glacier. For a categories description, see user guide. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: Surging

`term_type`
: `long_name`: Glacier terminus type <br/> `description`: Flag indicating the terminus type of the glacier. For a categories description, see user guide. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: TermType

`glac_name`
: `long_name`: Glacier name <br/> `description`: Glacier name (when available). <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: Name

`is_rgi6`
: `long_name`: Same as RGI 6.0 outline <br/> `description`: Flag indicating if the outline is the same as in RGI 6.0 (1) or was remapped (0). Note that it does not guarantee strict equivalence of the polygon (in most of the cases it does). <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`termlon`
: `long_name`: Terminus longitude <br/> `description`: Longitude of the lowest elevation point on the glacier outline. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: 

`termlat`
: `long_name`: Terminus latitude <br/> `description`: Latitude of the lowest elevation point on the glacier outline. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: 

`zmin_m`
: `long_name`: Minimum elevation <br/> `description`: Minimum elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: Zmin

`zmax_m`
: `long_name`: Maximum elevation <br/> `description`: Maximum elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: Zmax

`zmed_m`
: `long_name`: Median elevation <br/> `description`: Median elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: Zmed

`zmean_m`
: `long_name`: Mean elevation <br/> `description`: Mean elevation (m above sea level) of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: 

`slope_deg`
: `long_name`: Mean slope <br/> `description`: Mean slope of the glacier surface. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: Slope

`aspect_deg`
: `long_name`: Aspect <br/> `description`: The aspect (orientation) of the glacier surface presented as an azimuth relative to 0° at due north. <br/> `datatype`: float <br/> `units`: degrees <br/> `source`: RGI <br/> `rgi6_name`: Aspect

`aspect_sec`
: `long_name`: Aspect sector <br/> `description`: The aspect (orientation) of the glacier surface presented as a category. For a categories description, see user guide. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`dem_source`
: `long_name`: DEM data source <br/> `description`: The name of the dataset that was used to compute the topography attributes. <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`lmax_m`
: `long_name`: Maximum length <br/> `description`: Length (m) of the longest surface centerline of the glacier. <br/> `datatype`: float <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: Lmax

`geometry`
: `long_name`: Geometry <br/> `description`: Glacier geometry (polygon) <br/> `datatype`:  <br/> `units`: deg <br/> `source`: GLIMS <br/> `rgi6_name`: geometry

## Additional information

### `primeclass`

WGMS primary classification of the glacier. Obtained from the GLIMS database. Poorly populated. Categories:

|   Digit | Class                   | Description                                                                                                                                                                                                                                                                                    |
|--------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       0 | Miscellaneous           | Any type not listed below (please explain)                                                                                                                                                                                                                                                     |
|       1 | Continental ice sheet   | Inundates areas of continental size                                                                                                                                                                                                                                                            |
|       2 | Icefield                | Ice masses of sheet or blanket type of a thickness that is insufficient to obscure the subsurface topography                                                                                                                                                                                   |
|       3 | Ice cap                 | Dome-shaped ice masses with radial flow                                                                                                                                                                                                                                                        |
|       4 | Outlet glacier          | Drains an ice sheet, icefield or ice cap, usually of valley glacier form; the catchment area may not be easily defined                                                                                                                                                                         |
|       5 | Valley glacier          | Flows down a valley; the catchment area is well defined                                                                                                                                                                                                                                        |
|       6 | Mountain glacier        | Cirque, niche or crater type, hanging glacier; includes ice aprons and groups of small units                                                                                                                                                                                                   |
|       7 | Glacieret and snowfield | Small ice masses of indefinite shape in hollows, river beds and on protected slopes, which has developed from snow drifting, avalanching, and/or particularly heavy accumulation in certain years; usually no marked flow pattern is visible; in existence for at least two consecutive years. |
|       8 | Ice shelf               | Floating ice sheet of considerable thickness attached to a coast nourished by a glacier(s); snow accumulation on its surface or bottom freezing                                                                                                                                                |
|       9 | Rock glacier            | Lava-stream-like debris mass containing ice in several possible forms and moving slowly downslope


### `surge_type`

The `surge_type` attribute contains information on evidence for surging, and is based on the inventory of {cite:t}`Sevestre2015` as well as TODO.

Categories:

|   Value | Surging      |
|--------:|:-------------|
|       0 | No evidence  |
|       1 | Possible     |
|       2 | Probable     |
|       3 | Observed     |
|       9 | Not assigned |

### `term_type`

The `term_type` attribute contains information on terminus type. All glaciers in RGI 7.0 have been assigned the "Not assigned" category, except for the marine-terminating glaciers in the northern hemisphere (after {cite:t}`Kochtitzky2022`) and in region 17 (Southern Andes). The marine-terminating term_type is valid for ~2000. The only region missing classification for marine-terminating glaciers is RGI 19 (Antarctic and Subantarctic), thus all glaciers that are "not assigned" outside of RGI 19 can be assumed to be non-marine-terminating for ~2000. No region or glacier has any attributes availible for lake-terminating or shelf-terminating glaciers.

|   Value | Terminus type      |
|--------:|:-------------------|
|       0 | Land-terminating   |
|       1 | Marine-terminating |
|       2 | Lake-terminating   |
|       3 | Shelf-terminating  |
|       9 | Not assigned       |


### `aspect_sec`

The `aspect_sec` attribute contains information on the orientation of the glacier. Categories:

|   Value | Aspect sector   | Aspect range     |
|--------:|:----------------|:-----------------|
|       1 | North           | [-22.°; 22.5°]   |
|       2 | North-east      | [22.5°; 67.5°]   |
|       3 | East            | [67.5°; 112.5°]  |
|       4 | South-east      | [112.5°; 157.5°] |
|       5 | South           | [157.5°; 202.5°] |
|       6 | South-west      | [202.5; 247.5°]  |
|       7 | West            | [247.5°; 292.5°] |
|       8 | North-west      | [292.5°; 337.5°] |
|       9 | Not assigned    |                  |


### Submission info files

A csv file containing the following columns:

`subm_id`
: `long_name`: submission_id <br/> `description`: Unique identifier assigned by GLIMS to a specific data submission. Allows to obtain information about the analysts and data submitters. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`n_outlines`
: `long_name`: number_of_outlines <br/> `description`: Number of outlines from this submission used in RGI7. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`area_km2`
: `long_name`: total_area_of_outlines <br/> `description`: Total area of the outlines from this submission used in RGI7. <br/> `datatype`: float <br/> `units`: km2 <br/> `source`: RGI <br/> `rgi6_name`: 

`anlys_time`
: `long_name`: analysis_time <br/> `description`: Representative time the outline analysis was carried out. <br/> `datatype`: str <br/> `units`: date <br/> `source`: GLIMS <br/> `rgi6_name`: 

`release_dt`
: `long_name`: release_date <br/> `description`: Date at which the submission was realeased on GLIMS. <br/> `datatype`: str <br/> `units`: date <br/> `source`: GLIMS <br/> `rgi6_name`: 

`proc_desc`
: `long_name`: processing_description <br/> `description`: Description of the processing done to create the glacier outlines. <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`chief_affl`
: `long_name`: chief_affiliation <br/> `description`: Affiliation of the chief of the regional center or the person(s) who submitted the data. <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`submitters`
: `long_name`: submitters <br/> `description`: Person(s) who submitted the data. <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`analysts`
: `long_name`: analysts <br/> `description`: Person(s) who created the data. <br/> `datatype`: str <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 

`rc_id`
: `long_name`: regional_center_id <br/> `description`: GLIMS ID for the regional center. <br/> `datatype`: int <br/> `units`:  <br/> `source`: GLIMS <br/> `rgi6_name`: 
