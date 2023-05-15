# RGI and GTN-G Glacier Regions

RGI outlines are organized into 19 first-order glacier regions ([Figure 1](global-fig); [Table 1a](o1-regions-table)). We further subdivide the first-order regions into second-order regions, of which there are 89 in total ([Table 1b](o2-regions-table)). Glacier regions are useful for regional assessments of glacier change and other parameters.

:::{figure-md} global-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l3_rgi7a_plots/global_map_small.jpeg" alt="global map" class="bg-primary mb-1">

First-order regions of the Randolph Glacier Inventory (version 7.0) and glacier locations in red. [Download high resolution version](https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l3_rgi7a_plots/global_map.png).
:::

First-order regions 10 and 19 straddle the 180th meridian, and so does the second-order region 19-15. For convenience of analysis in a cylindrical-equidistant coordinate system centred on longitude 0°, as in [Figure 1](global-fig), each of these regions appears in the accompanying shapefiles as two polygons, eastern and western.

The region outlines were published as a joint set of regions recommended by the Global Terrestrial Network for Glaciers (GTN-G) Advisory Board, the Global Land Ice Measurements from Space initiative (GLIMS), the Randolph Glacier Inventory (RGI) Working Group of the International Association of Cryospheric Sciences (IACS), and the World Glacier Monitoring Service (WGMS). These glacier regions were implemented in RGI 6.0 and are available [on the GTN-G website](https://www.gtn-g.ch/data_catalogue_glacreg). **In RGI 7.0, the following minor changes have been implemented**:
- The southern boundary of region 12 (Caucasus and Middle East) has been shifted south by 2° (from 32°N to 30°N) to encompass a cluster of glaciers which were previously unassigned.
- The region boxes for region 01 (Alaska) used to encompass some islands in the Bering Sea East of Kamtchatka. This subregion contains no glaciers (and probably hasn't for a long time) and is now removed. 
- The data type of the `rgi_code` attribute in the first-order region file is now `str` (was `int`). The `rgi_code` now has a leading zero, for example `02` instead of `2`. 
- Region 19 has been renamed to "*Subantarctic and Antarctic Islands*" (was: "*Antarctic and Subantarctic*")
- The polygon of RGI region 19 has been updated to remove antarctic mainland. Potentially, a new region (20, "*Antarctic Mainland*") might be used in the future if glaciers are inventorized there.
- All abbreviations in the second-order regions file have been replaced by their full name (e.g. "East Central" instead of "EC")
- The first-order and second-order region files now have a field called `long_code` which contains a string representing the full region name, using the lowercase with underscores format (e.g. `02_western_canada_usa`). This field is used to name the corresponding RGI shapefiles.
- The subregion `05-11` (Greenland Ice Sheet) has been removed (it contained no glaciers).
- The `WGMS_CODE` column has been deleted from all files.
- The `RGI_CODE` column is now called `o1region` (first order files) and `o2region` (second-order files)

These changes will be uploaded to the GTN-G website in due course.

```{admonition} Additional details: RGI regions version history
:class: note, dropdown

In **RGI 6.0**, the eastern boundaries of regions 13 (Central Asia) and 15 (South Asia East) were extended slightly to the east. A new second-order region 10-07 covering Japan was added to region 10 (North Asia). Region 08-01 (S Norway) was subdivided into regions 08-02 (SW Scandinavia) and 08-03 (SE Scandinavia), with former region 08-02 (N Scandinavia) assuming the code 08-01. Region 02-01 (Melville Island) was transferred to first-order region 03 (Arctic Canada North) as region 03-07, and the other second-order regions of region 02 (Western Canada and US) were renumbered as 02-01 to 02-05. These changes ensure the compatibility of the Glacier Regions dataset of the [Global Terrestrial Network for Glaciers](http://www.gtn-g.ch/data_catalogue_glacreg) (GTN-G) with the RGI regions.

In **RGI 5.0**, the boundary between regions 01 (Alaska) and 02 (Western Canada and US) was refined, and in region 10 (North Asia) the former four second-order regions became six regions conforming with those described by Earl and Gardner (2016). In RGI 4.0, region 10-01, North Asia (North), was extended slightly to the west for better visibility of glaciers in the Polar Urals. Region 11-02, formerly the Pyrenees and Apennines, was enlarged and renamed Southern and Eastern Europe. First-order regions 10 (North Asia) and 11 (Central Europe) were enlarged accordingly.
```
