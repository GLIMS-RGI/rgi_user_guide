# 09: Russian Arctic

Covers all glaciers and ice caps in Novaya Zemlya, Severnaya Zemlya, Franz Josef Land, Ushakov Island and Victoria Island.

```{admonition} Subregions
:class: note, dropdown

- 09-01: Franz Josef Land
- 09-02: Novaya Zemlya
- 09-03: Severnaya Zemlya

```

:::{figure-md} rgi09-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI09/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::


The primary source of glacier outlines for this region were manually digitized as part of {cite:p}`Moholdt2012`. The main data source for Novaya Zemlya is SPIRIT SPOT5 scenes {cite:p}`Korona2009`, with best available Landsat scenes used elsewhere. Outline dates range between 2000 and 2010, with most of the area (40%) dating to 2004.

Three outlines were corrected in RGI7 ([discussion](https://github.com/GLIMS-RGI/rgi7_scripts/issues/4)) in order to correct the basin divides for three outlet glaciers (`RGI60-09.00741`, `RGI60-09.00743`, `RGI60-09.00744`). 

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi09-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI09/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 567
: **Submitter**: Koenig, Max.<br/>**Number of outlines**: 1066. **Area**: 50753.2km². **Release date**: 2013-03-25.<br/>**Analysts**: Moholdt, Geir.

Submission 759
: **Submitter**: Kochtitzky, William.<br/>**Number of outlines**: 3. **Area**: 841.8km². **Release date**: 2021-09-09.<br/>**Analysts**: Kochtitzky, William.

Reviewers
: Kochtitzky, William;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi09-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI09/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

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
