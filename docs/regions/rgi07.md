# 07: Svalbard and Jan Mayen

All glaciers in Svalbard and Jan Mayen.

:::{figure-md} rgi07-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI07/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

No changes to RGI6, except on Jan Mayen.  

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi07-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI07/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 563
: **Submitter**: Koenig, Max (Norwegian Polar Institute).<br/>**Number of outlines**: 1583. **Area**: 33841.4km². **Release date**: 2012-12-04.<br/>**Analysts**: Koenig, Max; Nuth, Chris.

Submission 720
: **Submitter**: Paul, Frank (University of Zurich-Irchel).<br/>**Number of outlines**: 84. **Area**: 117.5km². **Release date**: 2021-08-03.<br/>**Analysts**: Paul, Frank.

Reviewers
: None;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi07-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI07/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: The source for hypsometry was changed from the ASTER GDEM2 to the ViewfinderPanoramas DEM3 (http://www.viewfinderpanoramas.org/).

Changes from Version 4.0 to 5.0
: Links were added to 9 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: One exterior GLIMSId was replaced. Topographic and hypsometric attributes were added.<br/>In earlier versions, dates were omitted for 119 glaciers (total area 9,770 km2). They have now been restored from the inventory of {cite:t}`Nuth2013`. The new dates were extracted from file `cryoclim_gao_sj_2001-2010.zip`, downloaded from 
https://data.npolar.no/dataset/89f430f8-862f-11e2-8036-00505bad0004. The newly-dated glaciers, RGI40-07.01449 to RGI40-07.01567, were matched on-screen one by one between RGI 4.0 and the Nuth shapefile.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: None.

Changes from Version 1.0 to Version 2.0
: Outlines of the glaciers on Jan Mayen (07-02) were digitized by J.G. Cogley from {cite:t}`Hagen1993`.

Version 1.0
: The Svalbard inventory is described in more detail by {cite:t}`Nuth2013`.<br/>Three primary data sets are used. The main sources are SPOT5-HRS DEMs and orthoimages provided within the framework of the IPY-SPIRIT (SPOT 5 stereoscopic survey of Polar Ice: Reference Images and Topographies) Project {cite:p}`Korona2009`. The SPOT5-HRS collects 5m panchromatic stereo images that are stereoscopically processed into 40m DEMs, then used to generate the orthoimages. Five SPIRIT scene acquisitions from 2007-2008 cover 71% of the glacier area. The secondary source is 23 scenes from the ASTER sensor in the form of automatically generated DEMs and orthoimages (AST14DMO products downloaded from NASA) covering 16% of the glacier area. Cloud-free scenes are not available for 2007-2008, and therefore data from as early as 2001 are used. For less than 14% of the glacier area, a suitable SPOT5-HRS or ASTER scene was not available. For these glaciers, 11 orthorectified Landsat scenes are used. Furthermore, additional Landsat and ASTER scenes are used to aid digitization decisions about the seasonal snow cover.<br/>The original glacier delineation and glacier identification system is based on the {cite:t}`Hagen1993` atlas, which conforms to WGI standards but is only available as a hard copy. Therefore, digitized national datasets are the base glacier masks from which to begin the inventory {cite:p}`Konig2014`. From this original dataset, we manually re-delineated the individual glacier basins based upon the {cite:t}`Hagen1993` Atlas and updated by trimming the front position and the lateral edges below the ELA. Since the original national dataset was derived by cartographers, many of the mask segments above the ELA contained snow covered valley walls and gullies (not perennially snow covered). These are, to the best of our ability, clipped from the masks by visually analyzing the recent satellite archives of ASTER and Landsat.

```