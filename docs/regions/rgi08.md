# 08: Scandinavia

This region encompasses all glaciers in Scandinavia. Glaciers on Svalbard are included in region 07.

```{admonition} Subregions
:class: note, dropdown

- 08-01: North Scandinavia
- 08-02: Southwest Scandinavia
- 08-03: Southeast Scandinavia

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI08/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="80%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI08/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

**Kebnekaise massif in Sweden**

All glaciers near the Kebnekaise massif [have been corrected for a map projection shift](https://github.com/GLIMS-RGI/rgi7_scripts/issues/36). Four "nominal glaciers" (glaciers represented by a circle since no outlines were available) in the east of the region were deleted, as they do not appear to be glaciers.

## Additional information

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI08/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI08/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 611
: **Submitter**: Winsvold, Solveig Havstad.<br/>**Number of outlines**: 3141. **Area**: 2674.8km². **Release date**: 2012-12-13.<br/>**Analysts**: Andreassen, Liss Marie; Winsvold, Solveig Havstad.

Submission 812
: **Submitter**: Frank, Thomas.<br/>**Number of outlines**: 269. **Area**: 273.0km². **Release date**: 2023-01-02.<br/>**Analysts**: Brown, Ian; Frank, Thomas; Hansson, Erik.

Reviewers
: Mannerfelt, Erik;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI08/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI08/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |          3417 |                0 |             2949 |
|       1 | Marine-terminating |             0 |             0 |                0 |                0 |
|       2 | Lake-terminating   |             0 |             0 |                0 |                0 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |          3410 |             0 |             2948 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |          3410 |             0 |             2948 |                0 |
|       1 | Possible     |             0 |             0 |                0 |                0 |
|       2 | Probable     |             0 |             0 |                0 |                0 |
|       3 | Observed     |             0 |             0 |                0 |                0 |
|       9 | Not assigned |             0 |          3417 |                0 |             2949 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Exact dates were obtained for Norwegian glaciers from information submitted to GLIMS by L.M. Andreassen after the release of RGI version 1.0; see {cite:t}`Andreassen2012`. A further 885 glaciers, mostly small, were added from the same source. The Swedish and Norwegian parts of Salajekna (RGI60-08.03553), area 26.8 km², were merged.<br/>The source for hypsometry was changed from the ASTER GDEM2 to the ViewfinderPanoramas DEM3 (http://www.viewfinderpanoramas.org/).

Changes from Version 4.0 to 5.0
: Links were added to 24 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: Four exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Glaciers were delineated from glacier complexes.

Changes from Version 1.0 to Version 2.0
: Four glaciers in the Khibiny Mountains of the Kola Peninsula (08-02) were added as nominal circles from WGI-XF.

Version 1.0
: The glacier outlines for Norway are based on Landsat (TM and ETM+) imagery from 1999-2006.<br/>The Swedish glacier outlines use imagery from SPOT5 and SPOT4 (dates not provided). In some regions these outlines were updated against September 2008 Swedish Land Survey imagery available on Google Earth.<br/>The glacier mapping is a contribution to the CryoClim and GloGlacier projects and is documented in {cite:t}`Andreassen2012` for whole of Norway. Mapping of subregions is described in {cite:t}`Andreassen2008a` for Jotunheimen, {cite:t}`Paul2009a` for Svartisen, and {cite:t}`Paul2011` for the Jostedalsbreen region.

```
