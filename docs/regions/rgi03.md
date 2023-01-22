# 03: Arctic Canada, North

The  Arctic Canada, North region encompasses all glaciers in northern Canada above 74°N (Ellesmere and Devon Islands).

## New in RGI7

:::{figure-md} rgi03-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI03/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

Several improvements to RGI6.

## Additional information 

```{admonition} Data sources and analysts
:class: tip, dropdown

:::{figure-md} rgi03-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI03/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 590
: **Submitter**: Bolch, Tobias (University of Colorado).<br/>**Number of outlines**: 653. **Area**: 39842.3km². **Release date**: 2015-07-15.<br/>**Analysts**: Barrand, Nick; Burgess, Dave; Cawkwell, Fiona; Copland, Luke; Filbert, Katie; Gardner, Alex; Hartmann, G; OCallaghan, P; Paul, Frank; Sharp, Martin; Wolken, G.; Wyatt, F..

Submission 635
: **Submitter**: Cogley, Graham (University of Colorado).<br/>**Number of outlines**: 7. **Area**: 128.2km². **Release date**: 2015-07-16.<br/>**Analysts**: Berthier, Etienne; Bolch, Tobias; Cogley, Graham; Kienholz, Christian.

Submission 723
: **Submitter**: Paul, Frank (University of Zurich-Irchel).<br/>**Number of outlines**: 2583. **Area**: 27691.6km². **Release date**: 2021-09-03.<br/>**Analysts**: Paul, Frank; Rastner, Philipp; White, Adrienne.

Submission 728
: **Submitter**: Kochtitzky, William (University of Alberta).<br/>**Number of outlines**: 1961. **Area**: 37675.5km². **Release date**: 2021-08-27.<br/>**Analysts**: Copland, Luke; Kochtitzky, William; Thomson, Laura; Zajaczkiwsky, Sophie.

Submission 755
: **Submitter**: Kochtitzky, William (University of Alberta).<br/>**Number of outlines**: 23. **Area**: 33.9km². **Release date**: 2021-12-26.<br/>**Analysts**: Kochtitzky, William.

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi03-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI03/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Glacier complex RGI50-03.04540, added in version 5.0, was subdivided into 11 outlet glaciers with ids 03.04541 to 03.04551. The seven glaciers on Melville Island were transferred from former region 02-01 to region 03-07, with ids 03.04552 to 03.04558.<br/>The source for hypsometry was changed from the ASTER GDEM2 to the [ViewfinderPanoramas DEM3](http://www.viewfinderpanoramas.org).

Changes from Version 4.0 to 5.0
: Names were assigned to some glaciers on Axel Heiberg Island. Glacier RGI40-03.00840 was subdivided into RGI50-03.04538 (Thompson Glacier) and RGI50-03.04539 (White Glacier). Alexander Trishchenko (Canada Centre for Remote Sensing, Ottawa) pointed out that an ice cap of 126 km2 on Colin Archer Peninsula, northwest Devon Island was missing, and it was added (RGI50-03.04540).<br/>Links were added to 4 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: One exterior GLIMSId was replaced. Topographic and hypsometric attributes (section 3.2) were added.

Changes from Version 3.0 to 3.2
: Glaciers were delineated from the glacier complexes using the delineation algorithm developed by {cite:t}`Kienholz2013` and applied to the 1:250000 Canadian Digital Elevation Data (CDED). Some minor manual editing was done to remove obvious blunders.

Changes from Version 2.0 to 3.0
: None

Changes from Version 1.0 to Version 2.0
: Canvec outlines of the Melville Island glaciers, which were mistakenly duplicated in region 03 in version 1.0, were transferred to region 02.


Version 1.0
: Glacier outlines were created from late summer, cloud-free 1999-2003 Landsat 7 (ETM+) imagery and from 2000-2003 ASTER imagery. A normalized-difference snow index (NDSI) was calculated for all Landsat imagery to identify snow- and ice-covered terrain. Empirically derived thresholds were applied to refine these classifications and to separate snow from glacier ice. A clumping procedure was then applied to the classified snow and ice data to delineate contiguous groups of pixels, followed by an elimination procedure, which removed small clusters of non-ice pixels. Gridded snow and ice data were then converted to polygons and edited manually to correct misclassifications. Small portions of some areas within this region were not adequately imaged by Landsat, due to either persistent cloudiness or shadowing. Consequently, in these areas manual digitization of ASTER imagery was used to capture glacier outlines.<br/>Outlines for Devon Island were provided by D. Burgess and were derived from 1999/2000 velocity maps.


```