# 03: Arctic Canada North

The region encompasses all glaciers in Canada north of 74°N including  the heavily glacierized Ellesmere and Devon Islands.

```{admonition} Subregions
:class: note, dropdown

- 03-01: North Ellesmere Island
- 03-02: Axel Heiberg and Meighen Island
- 03-03: North Central Ellesmere Island
- 03-04: South Central Ellesmere Island
- 03-05: South Ellesmere Island (Northwest Devon)
- 03-06: Devon Island
- 03-07: Melville Island

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI03/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="100%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI03/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

**Ellesmere Island: Second-order region 03-01**

Glacier outlines and ice divdes were replaced as RGI 6.0 outlines suffered from incorrect ice divides, missing rock outcrops, missing (mostly very small) glaciers and a geolocation shift. Glaciers were remapped using glacier outlines by {cite:t}`white2019glacier` as a base but modifying them using four Landsat ETM+ scenes acquired in July 2000. The editing included a mix of manual and automated corrections. For the northernmost regions outside the coverage of Landsat the "World imagery" layer of the ESRI Basemap was used instead. Some smaller ice shelves were excluded. 

**Other regions**

For other subregions on Ellesmere Island as well as the Axel Heiberg Island ice caps, Sydkap Ice Cap, Agassiz Ice Cap, and glaciers west of Sydkap, and west of Manson Ice Field, RGI 6.0 outlines were adjusted to improve their quality, and glacier divides were replaced. Several previously omitted glaciers west of Prince of Wales Ice Cap were added.


## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI03/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI03/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 590
: **Submitter**: Bolch, Tobias.<br/>**Number of outlines**: 652. **Area**: 39842.3km². **Release date**: 2015-07-15.<br/>**Analysts**: Barrand, Nick; Burgess, Dave; Cawkwell, Fiona; Copland, Luke; Filbert, Katie; Gardner, Alex; Hartmann, G; OCallaghan, P; Paul, Frank; Sharp, Martin; Wolken, G.; Wyatt, F..

Submission 635
: **Submitter**: Cogley, Graham.<br/>**Number of outlines**: 7. **Area**: 128.2km². **Release date**: 2015-07-16.<br/>**Analysts**: Berthier, Etienne; Bolch, Tobias; Cogley, Graham; Kienholz, Christian.

Submission 723
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 2573. **Area**: 27690.4km². **Release date**: 2021-09-03.<br/>**Analysts**: Paul, Frank; Rastner, Philipp; White, Adrienne.

Submission 728
: **Submitter**: Kochtitzky, William.<br/>**Number of outlines**: 1961. **Area**: 37675.5km². **Release date**: 2021-08-27.<br/>**Analysts**: Copland, Luke; Kochtitzky, William; Thomson, Laura; Zajaczkiwsky, Sophie.

Submission 755
: **Submitter**: Kochtitzky, William.<br/>**Number of outlines**: 23. **Area**: 33.9km². **Release date**: 2021-12-26.<br/>**Analysts**: Kochtitzky, William.

Reviewers
: Kochtitzky, William;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI03/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI03/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |          4298 |                0 |            56000 |
|       1 | Marine-terminating |           238 |           258 |            49691 |            49111 |
|       2 | Lake-terminating   |             0 |             0 |                0 |                0 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |          4978 |             0 |            55680 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |          5145 |          4499 |            69295 |            75945 |
|       1 | Possible     |            34 |            25 |            13457 |            12279 |
|       2 | Probable     |            16 |            11 |             5639 |             4098 |
|       3 | Observed     |            21 |            15 |            16979 |            12731 |
|       9 | Not assigned |             0 |             6 |                0 |               59 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Glacier complex RGI50-03.04540, added in version 5.0, was subdivided into 11 outlet glaciers with ids 03.04541 to 03.04551. The seven glaciers on Melville Island were transferred from former region 02-01 to region 03-07, with ids 03.04552 to 03.04558.<br/>The source for hypsometry was changed from the ASTER GDEM2 to the [ViewfinderPanoramas DEM3](http://www.viewfinderpanoramas.org).

Changes from Version 4.0 to 5.0
: Names were assigned to some glaciers on Axel Heiberg Island. Glacier RGI40-03.00840 was subdivided into RGI50-03.04538 (Thompson Glacier) and RGI50-03.04539 (White Glacier). Alexander Trishchenko (Canada Centre for Remote Sensing, Ottawa) pointed out that an ice cap of 126 km2 on Colin Archer Peninsula, northwest Devon Island was missing, and it was added (RGI50-03.04540).<br/>Links were added to 4 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: One exterior GLIMSId was replaced. Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: Glaciers were delineated from the glacier complexes using the delineation algorithm developed by {cite:t}`Kienholz2013` and applied to the 1:250000 Canadian Digital Elevation Data (CDED). Some minor manual editing was done to remove obvious blunders.

Changes from Version 2.0 to 3.0
: None

Changes from Version 1.0 to Version 2.0
: Canvec outlines of the Melville Island glaciers, which were mistakenly duplicated in region 03 in version 1.0, were transferred to region 02.


Version 1.0
: Glacier outlines were created from late summer, cloud-free 1999-2003 Landsat 7 (ETM+) imagery and from 2000-2003 ASTER imagery. A normalized-difference snow index (NDSI) was calculated for all Landsat imagery to identify snow- and ice-covered terrain. Empirically derived thresholds were applied to refine these classifications and to separate snow from glacier ice. A clumping procedure was then applied to the classified snow and ice data to delineate contiguous groups of pixels, followed by an elimination procedure, which removed small clusters of non-ice pixels. Gridded snow and ice data were then converted to polygons and edited manually to correct misclassifications. Small portions of some areas within this region were not adequately imaged by Landsat, due to either persistent cloudiness or shadowing. Consequently, in these areas manual digitization of ASTER imagery was used to capture glacier outlines.<br/>Outlines for Devon Island were provided by D. Burgess and were derived from 1999/2000 velocity maps.


```
