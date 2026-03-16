# 09: Russian Arctic

This region encompasses all glaciers on the islands in the Russian Arctic including Novaya Zemlya, Severnaya Zemlya, Franz Josef Land, Ushakov Island and Victoria Island.

```{admonition} Subregions
:class: note, dropdown

- 09-01: Franz Josef Land
- 09-02: Novaya Zemlya
- 09-03: Severnaya Zemlya

```

<!--- Map start -->

:::{figure-md}
<img src="../img/region_plots/RGI09/isrgi6_map_small.jpeg" alt="region map" class="bg-primary mb-1" width="100%">

Regional glacier area.
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI09/isrgi6_map.jpeg).
:::

<!--- Map end -->

## Changes from version 6.0 to 7.0

Basin divides [were corrected](https://github.com/GLIMS-RGI/rgi7_scripts/issues/4) for three outlet glaciers on the northwest side of Novaya Zemlya (`RGI60-09.00741`, `RGI60-09.00743`, `RGI60-09.00744`).

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md}
<img src="../img/region_plots/RGI09/inventory_map_small.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region
[Download high resolution version](https://raw.githubusercontent.com/GLIMS-RGI/rgi_user_guide/main/docs/img/region_plots/RGI09/inventory_map.jpeg).
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 567
: **Submitter**: Koenig, Max.<br/>**Number of outlines**: 1066. **Area**: 50753.2km². **Release date**: 2013-03-25.<br/>**Analysts**: Moholdt, Geir.

Submission 759
: **Submitter**: Kochtitzky, William.<br/>**Number of outlines**: 3. **Area**: 841.8km². **Release date**: 2021-09-09.<br/>**Analysts**: Kochtitzky, William.

Reviewers
: Kochtitzky, William;

```

````{admonition} Regional statistics
:class: seealso, dropdown

```{card} Figure: Outlines source date

:::{figure-md}
<img src="../img/region_plots/RGI09/date_hist.png" alt="region map" class="bg-primary mb-1">

Distribution of the outline dates per area (top) and number (bottom)
:::

```

```{card} Figure: Glacier area histogram

:::{figure-md}
<img src="../img/region_plots/RGI09/area_histogram.png" alt="region histogram" class="bg-primary mb-1">

Number of glaciers per size category (log-log scale).
:::

```

```{card} Table: Terminus type statistics

Regional number of glaciers (N) and area (km²) per terminus type in RGI 7.0 and RGI 6.0. Note that the default designation in RGI 7.0 is now "Not assigned", while in RGI 6.0 lake-terminating glaciers and shelf-terminating glaciers were identified in some regions. The RGI region 19 is entirely labelled as "Not assigned" in RGI 7.0.

|   Value | Terminus type      |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | Land-terminating   |             0 |           690 |                0 |            18158 |
|       1 | Marine-terminating |           415 |           375 |            37299 |            32615 |
|       2 | Lake-terminating   |             0 |             4 |                0 |              819 |
|       3 | Shelf-terminating  |             0 |             0 |                0 |                0 |
|       9 | Not assigned       |           654 |             0 |            14296 |                0 |

```

```{card} Table: Surge type statistics

Regional number of glaciers (N) and area (km²) per surge type attribute in RGI 7.0 and RGI 6.0.

|   Value | Surge type   |   RGI 7.0 (N) |   RGI 6.0 (N) |   RGI 7.0 (Area) |   RGI 6.0 (Area) |
|--------:|:-------------|--------------:|--------------:|-----------------:|-----------------:|
|       0 | No evidence  |          1033 |             0 |            41145 |                0 |
|       1 | Possible     |            15 |            16 |             4440 |             4847 |
|       2 | Probable     |            14 |            13 |             3463 |             3052 |
|       3 | Observed     |             7 |             4 |             2548 |             1554 |
|       9 | Not assigned |             0 |          1036 |                0 |            42138 |

```

````

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: The source for hypsometry was changed from the ASTER GDEM2 to the ViewfinderPanoramas DEM3 (http://www.viewfinderpanoramas.org/).

Changes from Version 4.0 to 5.0
: Four glaciers (RGI50-09.00498, RGI50-09.00515, RGI50-09.00967, RGI50-09.00968) on October Revolution Island, Severnaya Zemlya, formerly with TermType = 1, were given the TermType code 5 because they flow into the Matusevich Ice Shelf.

Changes from Version 3.2 to 4.0
: Topographic and hypsometric attributes were added.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Glaciers were delineated from glacier complexes.

Changes from Version 1.0 to Version 2.0
: The Matusevich Ice Shelf, which was the only ice shelf in the inventory, was removed.

Version 1.0
: The inventory was constructed as part of a mass balance study of the Barents/Kara Sea region {cite:p}`Moholdt2012`. It covers all glaciers and ice caps in Novaya Zemlya (22,100 km2), Severnaya Zemlya (16,400 km2), Franz Josef Land (12,700 km2), Ushakov Island (320 km2) and Victoria Island (6 km2). Glacier complexes were manually digitized from orthorectified satellite imagery acquired during summers between 2000 and 2010. SPIRIT SPOT5 scenes {cite:p}`Korona2009` were used for most of Novaya Zemlya, while the best available Landsat scenes were used elsewhere. All visible nunataks were cut out from the glacier polygons, and snowfields were only included if they seemed to be a part of a glacier. Ice shelves in Franz Josef Land (<50 km2) were included as parts of the glacier polygons, while the Matusevich Ice Shelf in Severnaya Zemlya (~200 km2) was delineated into a separate polygon. The estimated total glacier area of the region (51,500 km2) is 9% smaller than that of the World Glacier Inventory {cite:p}`Ohmura2009`. This large deviation is probably due to a combination of long-term glacier retreat and methodological differences in glacier delineation.

```
