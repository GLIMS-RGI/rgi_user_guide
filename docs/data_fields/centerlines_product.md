# Data attributes: centerlines product 

The following attributes are available in the RGI 7.0 shapefiles. For more details on some of them, see the specific sections below.

## Full list

`rgi_id`
: `long_name`: RGI identifier <br/> `description`: Unique identifier assigned to a single centerline by the RGI <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`rgi_g_id`
: `long_name`: RGI glacier identifier <br/> `description`: Glacier ID to which the centerline belongs <br/> `datatype`: str <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`segment_id`
: `long_name`: Segment identifier <br/> `description`: Integer number uniquely identifying this centerline within the glacier. The main centerline is always last. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`is_main`
: `long_name`: Is main centerline <br/> `description`: Integer number indicating wether the centerline in the main centerline (1) or not (0). There is only one main centerline per glacier. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`outflow_id`
: `long_name`: Outflow segment identifier <br/> `description`: Each secondary centerline flows into another centerline. This identifier points to the `segment_id` to which this centerline flows to. <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`strahler_n`
: `long_name`: Strahler number of this centerline. <br/> `description`: Strahler number (Hydrological order) of the centerline, from lowest (0, line without tributaries but with possible descendants) to highest (the main centerline). <br/> `datatype`: int <br/> `units`:  <br/> `source`: RGI <br/> `rgi6_name`: 

`length_m`
: `long_name`: Centerline length <br/> `description`: Length of the centerline in meters <br/> `datatype`: int <br/> `units`: m <br/> `source`: RGI <br/> `rgi6_name`: 

`geometry`
: `long_name`: Geometry <br/> `description`: Centerline geometry (LineString) <br/> `datatype`:  <br/> `units`: deg <br/> `source`: RGI <br/> `rgi6_name`: 


## Additional information

The centerlines and their attributes are computed by OGGM {cite:p}`Maussion2019` which implements an algorithm described by {cite:t}`Kienholz2014`. The algorithm implemented in OGGM is very close to the original one, with slight differences in parameters choices and implementation details. Neither the algorithm nor its implementation are perfect, and the centerlines should be used with due caution.

### `strahler_n` (Strahler number)

The Strahler number is a measure of branching complexity defined by {cite:p}`Strahler1952` commonly used in hydrological applications. A Strahler number of 0 indicates a centerlines with no upstream tributaries. A Strahler number of 1 indicates a centerline with one or more upstream tributaries, each of them with a Strahler number of 0. If a centerline with a Strahler number of 1 flows into a downstream centerline, this centerline automatically get a Strahler number of 2. This ordering is important for mass flow routing. Each centerline contains a reference to its descendant, and this reference might be used by models to transfer mass from the tributaries towards the main centerline.