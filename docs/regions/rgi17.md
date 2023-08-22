# 17: Southern Andes

The region encompasses all glaciers in South America south of 25°S.

```{admonition} Subregions
:class: note, dropdown

- 17-01: Patagonia
- 17-02: Central Andes

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI17/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="50%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI17/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

All glaciers in RGI 6.0 were replaced by new outlines.

The RGI 6.0 glacier outlines suffered from reduced quality due to the presence of seasonal snow, missing debris-covered glaciers, incorrectly mapped ice divides and data processing artefacts. RGI 7.0 outlines are based on the new national glacier inventories of Argentina {cite:p}`Zalazar2020` and Chile {cite:p}`Barcaza2017`. The former was derived from a range of sensors (ALOS, ASTER, Landsat, SPOT4) with images acquired between 2004 and 2013. The latter was derived from Landsat ETM+ imagery acquired between 2000 and 2003. Both national inventories included rock glaciers which were removed for RGI 7.0. The classes MN (snow field) and GCGE (mixed debris-covered / rock glacier) in the Argentina inventory were also removed. Data gaps and overlaps along the national boundary as well as wrongly placed drainage divides were corrected in the merged data set using the "World imagery" layer of the ESRI basemap and a flow direction grid derived from the AW3D30 DEM, respectively. In some regions (e.g. Tierra del Fuego) missing glaciers were added and the extent of glaciers that were too large in the Argentian and Chilean inventories was reduced using Landsat images from around the year 2000.

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI17/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI17/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 764
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 30634. **Area**: 27674.4km². **Release date**: 2022-05-11.<br/>**Analysts**: Albornoz, Amapola; Arias, Victor; Barcaza, Gonzalo; Bown, Francisca; Castro, Mariano; Garcia, Juan-Luis; Gargantini, Hernán; Gimenez, Melisa; Hidalgo, Lidia Ferri; Masiokas, Mariano; Nussbaumer, Samuel; Paul, Frank; Pecker Marcosig, Ivanna; Pitte, Pierre.

Reviewers
: Rabatel, Antoine;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI17/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI17/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |         15690 |                0 |            12237 |
|       1 | Marine-terminating |            62 |            85 |             6871 |             7057 |
|       2 | Lake-terminating   |             0 |           133 |                0 |            10135 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |         30572 |             0 |            20804 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |         30603 |             0 |            26132 |                0 |
|       1 | Possible     |             2 |             1 |               21 |               19 |
|       2 | Probable     |             1 |             1 |                4 |                3 |
|       3 | Observed     |            28 |            15 |             1517 |             1538 |
|       9 | Not assigned |             0 |         15891 |                0 |            27869 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Coverage of the North Patagonian Ice Field was replaced with outlines for 2001 {cite:p}`Rivera2007` obtained from GLIMS.<br/>Names of glaciers in the North and South Patagonian Icefields were added.

Changes from Version 4.0 to 5.0
: Links were added to 2 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: 68 exterior GLIMSIds were replaced. Topographic and hypsometric attributes (section 3.2) were added.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Substantial revisions were made by N. Mölg in central Chile {cite:p}`Paul2014` and in the mountains surrounding the North and South Patagonian Icefields.

Changes from Version 1.0 to Version 2.0
: See the RGI v6 Technical Note for an extended summary of quality controls conducted by E.S. Miles, University of British Columbia.

Version 1.0
: Shapefiles were created from late-summer, cloud-free Landsat 7 ETM+ imagery acquired prior to the 2003 SLC failure. To identify glacier surfaces, a normalized difference snow index (NDSI) was calculated using bands 5 and 2 for the red and near-infrared bands respectively. A threshold of approximately 0.5-0.65 was used to identify dirty/shady/bare ice, and one from 0.65-0.99 to identify snow-covered ice. Gridded files were then converted to polygons and additional manual editing was carried out to eliminate incorrectly classified regions.<br/>Shapefiles for the South Patagonian Icefield were provided by H. De Angelis {cite:p}`DeAngelis2014`.


```
