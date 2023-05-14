# 18: New Zealand

New Zealand.

```{admonition} Subregions
:class: note, dropdown

- 18-01: New Zealand

```

:::{figure-md} rgi18-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI18/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1" width="60%">

Glacier locations and changes between RGI6 and RGI7.
:::

Completely new inventory in RGI7.

Glacier outlines in RGI6 for New Zealand were mostly from 1978 (partly 1988) and were outdated due to strong glacier changes since then. The new glacier inventory by {cite:t}`Baumann2021` was derived from Sentinel-2 and Landsat 8 images acquired in 2016. To get outlines closer to the year 2000 and accommodate to the always challenging snow and cloud conditions in this region, it was decided to manually adjust the 2016 outlines with Landsat 7 ETM+ images (pan-band) mostly acquired in the year 2000 (partly in 2002) in the background. Interpretation was facilitated with Sentinel-2 images from 2016 and 2019 as well as the "World imagery" layer of the ESRI Basemap. The extent of several (mostly small) glaciers was not changed when the available satellite images from 2000 or 2002 suffered from clouds or adverse snow conditions. New ice divides were calculated from the national 15 m resolution DEM of New Zealand. Further details about the processing can be found in {cite:t}`Paul2023`.


## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi18-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI18/inventory_map.jpeg" alt="region map" class="bg-primary mb-1" width="60%">

Submission IDs used for this region.
:::

Submission 749
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 3018. **Area**: 886.4km². **Release date**: 2021-09-02.<br/>**Analysts**: Baumann, Sabine; Paul, Frank; Rastner, Philipp.

Reviewers
: None;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi18-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI18/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

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