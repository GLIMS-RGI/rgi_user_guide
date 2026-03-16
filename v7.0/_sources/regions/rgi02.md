# 02: Western Canada and USA

The region encompasses all glaciers in western Canada and the USA not included in Region 01.

```{admonition} Subregions
:class: note, dropdown

- 02-01: Mackenzie and Selwyn Mountains
- 02-02: South Coast Ranges
- 02-03: North Rocky Mountains
- 02-04: Cascade Range and Sierra Nevada
- 02-05: South Rocky Mountains

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI02/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="60%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI02/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

None.

## Additional information

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI02/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI02/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 616
: **Submitter**: Hoffman, Matthew.<br/>**Number of outlines**: 32. **Area**: 1.1km². **Release date**: 2016-07-26.<br/>**Analysts**: Fountain, Andrew G.; Hoffman, Matthew.

Submission 623
: **Submitter**: Bolch, Tobias.<br/>**Number of outlines**: 12459. **Area**: 13046.6km². **Release date**: 2009-06-27.<br/>**Analysts**: Bolch, Tobias.

Submission 635
: **Submitter**: Cogley, Graham.<br/>**Number of outlines**: 1235. **Area**: 656.5km². **Release date**: 2015-07-16.<br/>**Analysts**: Berthier, Etienne; Bolch, Tobias; Cogley, Graham; Kienholz, Christian.

Submission 721
: **Submitter**: Bolch, Tobias.<br/>**Number of outlines**: 1. **Area**: 136.9km². **Release date**: 2009-06-27.<br/>**Analysts**: Bolch, Tobias.

Submission 722
: **Submitter**: Bolch, Tobias.<br/>**Number of outlines**: 1. **Area**: 10.2km². **Release date**: 2009-06-27.<br/>**Analysts**: Bolch, Tobias.

Submission 744
: **Submitter**: Fountain, Andrew G..<br/>**Number of outlines**: 5002. **Area**: 670.2km². **Release date**: 2016-02-26.<br/>**Analysts**: Fountain, Andrew G..

Reviewers
: None

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI02/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI02/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |         18855 |                0 |            14524 |
|       1 | Marine-terminating |             0 |             0 |                0 |                0 |
|       2 | Lake-terminating   |             0 |             0 |                0 |                0 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |         18730 |             0 |            14521 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |         18730 |         17619 |            14521 |            13867 |
|       1 | Possible     |             0 |             0 |                0 |                0 |
|       2 | Probable     |             0 |             0 |                0 |                0 |
|       3 | Observed     |             0 |             0 |                0 |                0 |
|       9 | Not assigned |             0 |          1236 |                0 |              657 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: The seven glaciers on Melville Island were transferred from former region 02-01 to region 03-07, with ids 03.04552 to 03.04558.<br/> In regions 02-04 (Cascade Ra and Sa Nevada) and 02-05 (S Rocky Mtns), all but a few Canadian outlines were replaced from an inventory taken from maps of scale 1:24,000 {cite:p}`Fountain2006` and from outlines provided for Rocky Mountain National Park by M. Hoffman {cite:p}`Hoffman2007`. (These regions were formerly numbered 02-05 and 02-06.) The previous coverage, also from {cite:t}`Fountain2006`, was from 1:100,000-scale maps. In consequence the glacier counts in the two regions increased several-fold, to 3202 in region 02-04 and 1967 in region 02-05, and their total areas increased to 529 km2 and 149 km2 respectively. The new outlines all have dates, unlike the old outlines, and it was possible to identify all 28 of those with measurements in the WGMS mass-balance database. The map dates range from the 1940s to the 1980s. The Rocky Mountain National Park outlines are from 2001.

Changes from Version 4.0 to 5.0
: The boundary between region 01-06 (N Coast Ranges) and regions 02-03 (S Coast Ranges) and 02-04 (N Rocky Mtns) was refined, with transfers of three glaciers to region 01-06 from 02-03 and four to 02-03 from 01-06 in consequence.<br/>Links were added to 21 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to Version 4.0
: 145 exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Glacier complexes were separated into single glaciers in the northern part of the region. 

Changes from Version 1.0 to Version 2.0
: The glaciers on Melville Island (formerly region 02-01, now "03-07")  were represented in version 1.0 by DCW outlines and have been replaced by Canvec outlines taken from Region 03. DCW outlines for the Mackenzie Mountains and Selwyn Mountains (formerly region 02-02, now "02-01"), on the boundary between Yukon and the North West Territories, were replaced by Canvec outlines provided by M. Sharp and J.G. Cogley.

Version 1.0
: Glaciers in BC and Alberta (2nd order regions: 02-02: S Coast Ranges, 02-03: N Rocky Mountains) were mapped using orthorectified Landsat 5 TM scenes from the years 2004 and 2006 obtained by British Columbia Government, Ministry of Forests and Range. We selected the TM3/TM5 band ratio for glacier mapping. For the entire study area, we used improved British Columbia TRIM glacier outlines as a mask to minimize misclassification due to factors such as seasonal snow. When using this mask, we assumed that glaciers did not advance between 1985 and 2005, an assumption that holds for practically all non-tidewater glaciers in western North America. The mask also maintained consistency in the location of the upper glacier boundary and the margins of nunataks. This consistency is important where seasonal snow hampers correct identification of the upper glacier boundary. We mapped only glaciers larger than 0.05 km2, as a smaller threshold would include many features that were most likely snow patches. In addition, all snow and ice patches that were not considered to be perennial ice in the TRIM data were eliminated and hence, we minimize deviations in glacier areas that could arise from interpretative errors or major variations in snow cover. The resulting glacier polygons were visually checked for gross errors based on the procedures previously discussed, and fewer than 5% of the glaciers were manually improved. We derived glacier drainage basins based on a flowshed algorithm using the TRIM DEM and a buffer around each glacier. More information can be found in {cite:t}`Bolch2010b`.<br/>Data for the US south of 49°N (02-04: Cascade Ra and Sa Nevada, 02-05: S Rocky Mtns, Fountain et al., 2007; http://glaciers.us) were derived from the GLIMS database. Glaciers in Yukon (Mackenzie Mountains and Selwyn Mountains (formerly region 02-02, now 02-01)) and Mellville Island (formerly region 02-01, now 03-07) were taken from the digital chart of the world (DCW).

```
