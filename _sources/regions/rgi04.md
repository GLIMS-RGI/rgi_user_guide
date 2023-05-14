# 04: Arctic Canada, South

The  Arctic Canada, South region encompasses all glaciers in northwest Canada below 74°N: it comprises Baffin Island and Northern Newfoundland. 

```{admonition} Subregions
:class: note, dropdown

- 04-01: Bylot Island
- 04-02: West Baffin Island
- 04-03: North Baffin Island
- 04-04: Northeast Baffin Island
- 04-05: East Central Baffin Island
- 04-06: South East Baffin Island
- 04-07: Cumberland Sound
- 04-08: Frobisher Bay
- 04-09: Labrador

```


:::{figure-md} rgi04-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI04/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

With the exception of Newfoundland, all outlines have been revised for RGI7:

**Baffin Island and Bylot Island**

For the largest part of the region covered by submission 817, RGI6 glacier outlines were modified using end of summer Landsat 7 ETM+ images acquired from 1999 to 2002. The related corrections added missing glaciers or glacier parts (incl. debris cover), removed seasonal snow and provided new drainage divides based on a flow direction grid derived from the ArcticDEM at 10 m resolution and flow fields (magnitudes) provided by {cite:t}`Millan2022`. For the southern part of Baffin Island (incl. parts of Penny Ice Cap) RGI6 outlines were replaced with extents from a fresh processing of three Landsat 7 ETM+ scenes. Several small ice patches in the south of Baffin Island were added after visual inspection of the ESRI Basemap.


## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi04-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI04/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 589
: **Submitter**: Bolch, Tobias.<br/>**Number of outlines**: 103. **Area**: 19.8km². **Release date**: 2015-07-15.<br/>**Analysts**: Barrand, Nick; Burgess, Dave; Cawkwell, Fiona; Copland, Luke; Filbert, Katie; Gardner, Alex; Hartmann, G; OCallaghan, P; Paul, Frank; Sharp, Martin; Wolken, G.; Wyatt, F..

Submission 817
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 10908. **Area**: 40518.3km². **Release date**: 2023-03-01.<br/>**Analysts**: Mabileau, Laure; Paul, Frank; Rastner, Philipp.

Reviewers
: Kochtitzky, William;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi04-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI04/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Seven pairs of glacier outlines in east-central Baffin Island were found to have spurious divides that were actually the edges of maps. These pairs were merged: the surviving members of each pair, with the deleted members in parentheses, are RGI60-04.00408 (04.00465); 04.00413 (04.00415); 04.00416 (04.00412) 04.00420 (04.00419); 04.00424 (04.00425); 04.00433 (04.00423); 04.00467 (04.00464).<br/>The source for hypsometry was changed from the ASTER GDEM2 to the ViewfinderPanoramas DEM3 (http://www.viewfinderpanoramas.org/).

Changes from Version 4.0 to 5.0
: All glaciers in region 04-09, Labrador, were replaced with information from the inventory of {cite:t}`Way2014`.<br/>Links were added to 5 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: Eight exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.<br/>Glacier 04.06811, which duplicated glacier 04.06813 in version 3.2, was removed.

Changes from Version 3.0 to 3.2
: Glaciers were delineated from the glacier complexes using the delineation algorithm developed by {cite:t}`Kienholz2013` and applied to the 1:250000 Canadian Digital Elevation Data (CDED). Some minor manual editing was done to remove obvious blunders.

Changes from Version 2.0 to 3.0
: None.

Changes from Version 1.0 to Version 2.0
: Outlines for 27 glaciers in Labrador (region 04-09) were added, provided by P. O’Callaghan, N. Barrand, F. Wyatt and M. Sharp, University of Alberta.

Version 1.0
: Glacier complex outlines were compiled from 214 CanVec maps, a digital cartographic reference product of Natural Resources Canada. An additional 5500 km2 of glacier area in central Baffin Island not covered by Edition 9 of the CanVec data set were taken from an expanded inventory based on {cite:t}`Paul2005` and {cite:t}`Svoboda2009`. All outlines in this expanded inventory were created from late-summer Landsat 7 ETM+ imagery acquired between 1999 and 2002. Of the CanVec maps, 13 were based on late-summer SPOT 5 imagery acquired between 2006–2010 and seven on 1958 or 1982 aerial photographs. A small fraction of ice coverage is missed by the Canvec dataset because of incorrect classification over debris-covered ice and supraglacial lakes. The misclassification is very noticeable for outlet glaciers where medial moraines are not identified as glacier ice. Glaciers were delineated with the algorithm of {cite:t}`Kienholz2013` and edited manually where necessary.

```