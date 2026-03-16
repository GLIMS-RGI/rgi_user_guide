# 18: New Zealand

The region encompasses all glaciers in New Zealand.

```{admonition} Subregions
:class: note, dropdown

- 18-01: New Zealand

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI18/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="70%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI18/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

All glaciers in RGI 6.0 were replaced by new outlines.

Glacier outlines in RGI 6.0 were mostly from 1978 (partly from 1988) and thus outdated due to large changes in glacier area by year 2000.  Outlines were replaced by new outlines based on the glacier inventory by {cite:t}`Baumann2021`, which had been derived from Sentinel-2 and Landsat 8 images acquired in 2016. Most of their outlines were manually adjusted for RGI 7.0 to come closer to the target year 2000 using Landsat 7 ETM+ images (pan-band) mostly acquired in 2000 (partly in 2002). Interpretation was further supported by Sentinel-2 images from 2016 and 2019 as well as the "World imagery" layer of the ESRI Basemap. The extent of several (mostly small) glaciers was not adjusted when the available satellite images from 2000 or 2002 suffered from clouds or adverse snow conditions. All ice divides were recalculated from the national 15 m resolution DEM of New Zealand. The modifications applied to the inventory by {cite:t}`Baumann2021` are further detailed in {cite:t}`Paul2023`.



## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI18/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI18/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 749
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 3018. **Area**: 886.4km². **Release date**: 2021-09-02.<br/>**Analysts**: Baumann, Sabine; Paul, Frank; Rastner, Philipp.

Reviewers
: None;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI18/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI18/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |          3537 |                0 |             1162 |
|       1 | Marine-terminating |             0 |             0 |                0 |                0 |
|       2 | Lake-terminating   |             0 |             0 |                0 |                0 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |          3018 |             0 |              886 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |          3018 |             0 |              886 |                0 |
|       1 | Possible     |             0 |             0 |                0 |                0 |
|       2 | Probable     |             0 |             0 |                0 |                0 |
|       3 | Observed     |             0 |             0 |                0 |                0 |
|       9 | Not assigned |             0 |          3537 |                0 |             1162 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: None.

Changes from Version 4.0 to 5.0
: Links were added to 4 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: 89 exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Glaciers were delineated from glacier complexes.

Changes from Version 1.0 to Version 2.0
: None.

Version 1.0
: New Zealand outlines are derived from 1978 aerial imagery at a scale of 1:150,000 as used for the NZ Topo50 maps (Chinn, 2001). The shapefile can be downloaded from:
http://data.linz.govt.nz/#/layer/287-nz-mainland-ice-polygons-topo-150k/.


```
