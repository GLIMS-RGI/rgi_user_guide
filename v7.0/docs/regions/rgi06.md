# 06: Iceland

This region encompasses all glaciers in Iceland.

```{admonition} Subregions
:class: note, dropdown

- 06-01: Iceland

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI06/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="100%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI06/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

None.

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI06/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI06/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 437
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 26. **Area**: 7.1km². **Release date**: 2007-03-21.<br/>**Analysts**: Sigurdsson, Oddur.

Submission 438
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 5. **Area**: 0.8km². **Release date**: 2007-03-21.<br/>**Analysts**: Sigurdsson, Oddur.

Submission 439
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 154. **Area**: 95.2km². **Release date**: 2007-03-21.<br/>**Analysts**: Sigurdsson, Oddur.

Submission 452
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 16. **Area**: 7.0km². **Release date**: 2007-03-21.<br/>**Analysts**: Sigurdsson, Oddur.

Submission 719
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 365. **Area**: 10947.5km². **Release date**: 2014-12-01.<br/>**Analysts**: Sigurdsson, Oddur.

Submission 757
: **Submitter**: Sigurdsson, Oddur.<br/>**Number of outlines**: 2. **Area**: 2.1km². **Release date**: 2021-10-10.<br/>**Analysts**: Sigurdsson, Oddur.

Reviewers
: None;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI06/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI06/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |           568 |                0 |            11060 |
|       1 | Marine-terminating |             1 |             0 |             1068 |                0 |
|       2 | Lake-terminating   |             0 |             0 |                0 |                0 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |           567 |             0 |             9992 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |           544 |           545 |             3169 |             3195 |
|       1 | Possible     |             0 |             1 |                0 |                1 |
|       2 | Probable     |             0 |             1 |                0 |              130 |
|       3 | Observed     |            24 |            21 |             7891 |             7734 |
|       9 | Not assigned |             0 |             0 |                0 |                0 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: The source for hypsometry was changed from the ASTER GDEM2 to the ViewfinderPanoramas DEM3 (http://www.viewfinderpanoramas.org/).

Changes from Version 4.0 to 5.0
: Links were added to 9 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: One exterior GLIMSId was replaced. Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: Glaciers were delineated from the glacier complexes.

Changes from Version 2.0 to Version 3.0
: None.

Changes from Version 1.0 to Version 2.0
: None.

Version 1.0
: Outlines of glacier complexes in Iceland were added to the GLIMS database by O. Sigurðsson and extracted therefrom by J.G. Cogley, who merged nunataks with the glacier complexes containing them. Most outlines were acquired from 1999–2004 ASTER and SPOT5 imagery; some in the north of Iceland were acquired from oblique aerial photographs. 
```