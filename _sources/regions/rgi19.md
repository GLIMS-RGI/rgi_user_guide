# 19: Subantarctic and Antarctic Islands

The Subantarctic and Antarctic Islands region encompasses all glaciers in the periphery of mainland Antarctica, including some remote islands in the Southern ocean. It does not include any outline on mainland Antarctica.

:::{figure-md} rgi19-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI19/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

Most RGI6 outlines where compiled by {cite:t}`Bliss2013` based on topographical maps from the Antarctic Digital Database {cite:p}`add2000` (see {cite:t}`Bliss2013` for details). For RGI7, most peripheral islands where remapped and corrected for problematic georeferencing issues (shifts, deformation, etc. See [github discussion](https://github.com/GLIMS-RGI/rgi7_scripts/issues/61)). Several wrongly mapped icebergs and other bodies where removed. Altogether, area changes are small (+0.1%) but the usability of the inventory has considerably improved.

An important discussion about RGI outlines in region 19 has originated from two recent publications: {cite:t}`Millan2022` and Hock et al (in press), opening the question whether certain outlines in RGI belong to the ice sheet or to the mountain glaciers category. We acknowledge the need for discussion and coordination within the scientific community to avoid double counting, but preferred not to change RGI without a consensus agreement from both the glacier and ice-sheet research communities. 


## Additional information 

```{admonition} Data sources and analysts
:class: tip, dropdown

:::{figure-md} rgi19-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI19/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 585
: **Submitter**: Bliss, Andrew (University of Colorado).<br/>**Number of outlines**: 1794. **Area**: 98181.2km². **Release date**: 2015-07-01.<br/>**Analysts**: Berthier, Etienne; Bliss, Andrew; Cogley, Graham; LeBris, Raymond; Paul, Frank.

Submission 700
: **Submitter**: Hidalgo, Lidia Ferri (IANIGLA).<br/>**Number of outlines**: 31. **Area**: 242.8km². **Release date**: 2018-09-04.<br/>**Analysts**: Castro, Mariano; Gargantini, Hernán; Gimenez, Melisa; Hidalgo, Lidia Ferri; Masiokas, Mariano; Pecker Marcosig, Ivanna; Pitte, Pierre; Ruiz, Lucas; Zalazar, Laura.

Submission 769
: **Submitter**: Paul, Frank (OMP-LEGOS).<br/>**Number of outlines**: 340. **Area**: 536.8km². **Release date**: 2022-07-19.<br/>**Analysts**: Mabileau, Laure; Paul, Frank; Rastner, Philipp.

Submission 798
: **Submitter**: Berthier, Etienne (OMP-LEGOS).<br/>**Number of outlines**: 7. **Area**: 2684.6km². **Release date**: 2022-10-01.<br/>**Analysts**: Berthier, Etienne; Lebreton, Jerome.

Submission 805
: **Submitter**: McNabb, Robert (OMP-LEGOS).<br/>**Number of outlines**: 69. **Area**: 6529.7km². **Release date**: 2022-10-01.<br/>**Analysts**: McNabb, Robert.

Submission 806
: **Submitter**: McNabb, Robert (OMP-LEGOS).<br/>**Number of outlines**: 23. **Area**: 2985.6km². **Release date**: 2022-10-01.<br/>**Analysts**: McNabb, Robert.

Submission 807
: **Submitter**: Kochtitzky, William (OMP-LEGOS).<br/>**Number of outlines**: 213. **Area**: 1656.7km². **Release date**: 2022-11-11.<br/>**Analysts**: Cha, Leo; Gould, Luke; Kochtitzky, William; Merrill, Paige-Marie.

Submission 808
: **Submitter**: Kochtitzky, William (OMP-LEGOS).<br/>**Number of outlines**: 11. **Area**: 43.5km². **Release date**: 2022-12-15.<br/>**Analysts**: Kochtitzky, William.

Submission 811
: **Submitter**: McNabb, Robert (OMP-LEGOS).<br/>**Number of outlines**: 174. **Area**: 20568.3km². **Release date**: 2022-10-01.<br/>**Analysts**: McNabb, Robert.

Reviewers
: Berthier, Etienne; McNabb, Robert; Kochtitzky, William;


```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi19-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI19/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: None.

Changes from Version 4.0 to 5.0
: Links were added to 2 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to Version 4.0
: Two exterior GLIMSIds were replaced. Topographic and hypsometric attributes (section 3.2) were added.<br/>The main source for RGI region 19 was the Antarctic Digital Database ADD {cite:p}`add2000`, compiled for glaciological purposes by {cite:t}`Bliss2013`. In RGI 3.2, 34,041 km2 of Antarctic glaciers had dates and 47,961 km2 had date ranges. Most of these were obtained from attributes of coastal and other line segments in the ADD. Of the remaining 50,866 km2 of glaciers, it was possible to recover dates and date ranges for 35,148 km2 from chapter 5 (Bibliography) of the ADD manual {cite:p}`add2000`. This bibliography gives detailed summaries of ADD revisions organized by the tiles into which the database is subdivided, and further by the 16 maps into which each tile is subdivided. For many tiles, but not all, the bibliography lists source images and their dates. Unfortunately the bibliography has not been updated since 2000, and so there is some doubt about the assignment of dates. Often, however, it was possible to verify, for example by inspecting Google Earth, that there have been no perceptible revisions in recent years.

Changes from Version 2.0 to Version 3.2
: None.

Changes from Version 2.0 to Version 3.0
: The TerminusType character of the GlacType attribute was coded following {cite:t}`Paul2009`, with the addition of code 5 for shelf-terminating glaciers. Classification was done visually using imagery from a variety of sources. In a few instances, more than one terminus type applied to a particular glacier. Each such glacier was assigned the code representing the longest part of its perimeter.

Changes from Version 1.0 to Version 2.0
: The ice cover of Peter the First Island in the Bellingshausen Sea was taken from the ADD in version 1.0. In version 2.0 it is replaced by the outlines of 26 glaciers from an inventory by J.G. Cogley {cite:p}`Cogley2014`.

Version 1.0
: Outlines of glacier complexes on islands peripheral to the mainland of Antarctica were obtained from the Antarctic Digital Database (ADD Consortium, 2000). A. Bliss manually classified the ADD’s “land” polygons into continent, ice rise, ice cap, and glacier-complex polygons. Ice rises, and ice bodies on the continental mainland, are not included in this inventory. Nor are ice shelves. The classification was based on the surface morphology and surface flow velocities observed in data from Landsat, the RADARSAT Antarctic Mapping Project DEM, and the MEaSUREs InSAR-based Antarctic Velocity Map. On islands with prominent nunataks, glacier complexes were subdivided into individual glaciers following {cite:t}`Kienholz2013`. More details on the processing of these outlines are given by {cite:t}`Bliss2013`.<br/>Outlines of glaciers on most of the Subantarctic islands were obtained by E. Berthier and J.G. Cogley from various sources including satellite imagery and maps {cite:p}`Cogley2014`. For King George Island in the South Shetland Islands, outlines were downloaded from KGIS, the King George Island Geographic Information System, a now defunct web site created by F. Rau and S. Vogt, University of Freiburg. Separate outlines of “glacier basins” and ice-free areas were harmonized and merged to form glacier outlines containing nunataks. For Kerguelen, outlines are from {cite:t}`Berthier2009`. <br/>Outlines of South Georgia glaciers were mapped by F. Paul from a Landsat ETM+ scene from 2003 using a band 3/5 ratio and manual corrections for icebergs and water (removed), and debris-cover (added); some regions covered by seasonal snow might be included.

```