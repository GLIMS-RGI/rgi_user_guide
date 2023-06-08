# RGI glacier regions

RGI outlines are organized into 20 first-order glacier regions (one more than in RGI 6.0 and earlier versions, since former region 19 was split into two regions ([Figure 1](global-fig); [Table 1a](o1-regions-table)). These are further subdivided into second-order regions, of which there are 90 in total in RGI 7.0 ([Table 1b](o2-regions-table)). Glacier regions are useful for regional assessments of glacier change and other variables.

:::{figure-md} global-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l3_rgi7a_plots/global_map_small.jpeg" alt="global map" class="bg-primary mb-1">

First-order regions of the RGI version 7.0 and glacier locations in red. [Download high resolution version](https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l3_rgi7a_plots/global_map.png).
:::

```{admonition} Data download

[Download the RGI 7.0 region files](https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l5_rgi7b1_zip/RGI2000-v7.0-regions.zip). For review only!
```

First-order regions `10`, `19` and `20` straddle the 180th meridian, and so do the second-order regions `19-15` and `20-01`. For convenience of analysis in a cylindrical-equidistant coordinate system centered on longitude 0°, as in [Figure 1](global-fig), the region outlines of `10` and `19-15` appear in the accompanying shapefiles as two polygons, eastern and western. 

The region outlines have changed slightly between RGI versions, for example to avoid the splitting of glaciers between two regions, to make further analyses more convenient, or because previously not included glaciers were located outside existing region boundaries. For the sake of consistency between global glacier datasets a joint set of regions was recommended by the Global Terrestrial Network for Glaciers (GTN-G) Advisory Board, the Global Land Ice Measurements from Space initiative (GLIMS), the RGI Working Group of the International Association of Cryospheric Sciences (IACS), and the World Glacier Monitoring Service (WGMS). These glacier regions were implemented first in RGI version 6.0 and are available [on the GTN-G website](https://www.gtn-g.ch/data_catalogue_glacreg). These region boundaries were slightly modified in RGI version 7.0 and changes also integrated in the GTN-G data set (NEW REFERENCE)


## Changes from RGI 6.0 to 7.0

**Region boundary and name changes:**

- The region boxes for region `01` (Alaska) used to encompass some islands in the Bering Sea East of Kamtchatka. One of the two boxes, part of subregion `01-03` Alaska Peninsula (Aleutians), contains no glaciers (and probably hasn't for a long time) and is now removed.
- Region names in the region shapefiles (and therefore of the associated RGI product files) have been harmonized to reflect the most commonly used version in various documents and publications of the RGI. "Arctic Canada, North" and "Arctic Canada, South" have been renamed "Arctic Canada North" and "Arctic Canada South" (comma removed). The four regions in Asia ("North", "Central", "South West" and "South East") were renamed to "North Asia", "Central Asia", "South Asia West" and "South Asia East". With this change, none of the regions and subregions in RGI 7.0 have a comma in them.
- Subregion `05-11` (Greenland Ice Sheet) has been removed since it was coarsely defined and the RGI does not include the ice sheet proper.
- The southern boundary of region `12` (Caucasus and Middle East) has been shifted south by 2° (from 32°N to 30°N) to encompass a cluster of glaciers which were previously not included.
- The Antarctic mainland has been removed from the polygon of RGI region `19`. 
- Region `19` ("Antarctic and Subantarctic") was split into two first-order regions. Region `19` now solely includes the islands in the periphery of Antarctica, and was renamed to "Subantarctic and Antarctic Islands". A new region `20`, ("Antarctic Mainland") was added to encompass the remaining subregion ("Antarctic Ice Sheet", previously `19-31` and now `20-01`), but it presently contains no glaciers in the RGI (nor has the corresponding former subregion `19-31` in all previous RGI versions).

**Technical changes:**

- The data type of the `rgi_code` attribute in the first-order region file is now `str` (instead of `int`). The `rgi_code` now has a leading zero, for example `02` instead of `2`.
- All abbreviations in the second-order regions file have been replaced by their full name (e.g. "East Central" instead of "EC")
- The first-order and second-order region files now have a field called `long_code` which contains a string representing the full region name, using the lowercase with underscores format (e.g. `02_western_canada_usa`). This field is used to name the corresponding RGI shapefiles.
- The `WGMS_CODE` column has been deleted from all files.
- The `RGI_CODE` column is now called `o1region` (first order files) and `o2region` (second-order files)


```{admonition} Additional details: RGI regions version history
:class: note, dropdown

In **RGI 6.0**, the eastern boundaries of regions 13 (Central Asia) and 15 (South Asia East) were extended slightly to the east. A new second-order region 10-07 covering Japan was added to region 10 (North Asia). Region 08-01 (S Norway) was subdivided into regions 08-02 (SW Scandinavia) and 08-03 (SE Scandinavia), with former region 08-02 (N Scandinavia) assuming the code 08-01. Region 02-01 (Melville Island) was transferred to first-order region 03 (Arctic Canada North) as region 03-07, and the other second-order regions of region 02 (Western Canada and US) were renumbered as 02-01 to 02-05. These changes ensure the compatibility of the Glacier Regions dataset of the [Global Terrestrial Network for Glaciers](http://www.gtn-g.ch/data_catalogue_glacreg) (GTN-G) with the RGI regions.

In **RGI 5.0**, the boundary between regions 01 (Alaska) and 02 (Western Canada and US) was refined, and in region 10 (North Asia) the former four second-order regions became six regions conforming with those described by Earl and Gardner (2016). In RGI 4.0, region 10-01, North Asia (North), was extended slightly to the west for better visibility of glaciers in the Polar Urals. Region 11-02, formerly the Pyrenees and Apennines, was enlarged and renamed Southern and Eastern Europe. First-order regions 10 (North Asia) and 11 (Central Europe) were enlarged accordingly.
```
