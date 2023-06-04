# 05: Greenland Periphery

The region encompasses all glaciers not connected or only weakly connected to the ice sheet as defined by connectivity levels 0 and 1 in {cite:p}`Rastner2012`.

```{admonition} Subregions
:class: note, dropdown

- 05-01: Greenland Periphery

```

:::{figure-md} rgi05-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI05/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Regional glacier area.
:::

## Changes from version 6.0 to 7.0

**Northernmost part of Greenland**

RGI 6.0 glacier outlines in the very north of Greenland suffered from low quality due to their location outside the Landsat field of view. Therefore glaciers in two areas in the very north of Greenland were replaced in Version 7.0 by new outlines derived from orthoimages from 1978 provided by {cite:t}`Korsgaard2016` and hillshade representations of the ArcticDEM. Some seasonal snow complicated outline detection at higher elevations; thus some overestimation of glacier area is likely. ASTER scenes closer to the target year (2000) were not considered since these are affected by clouds or seasonal snow, however, it was assumed that glacier area changes in this region between 1978 and 2000 are relatively small.

**Other changes**

**Glaciers with connectivity level 2** {cite:p}`Rastner2012` **have been removed entirely from the RGI 7.0**, since they are typically not included in mass change assessments or projections of glaciers outside the ice sheet. This change removes a source of confusion when differentiating between glacier and the ice sheet proper. The Flade Isblink Icecap, which represented one single entity in RGI 6.0, was divided into separate glaciers by [adding ice divides](https://github.com/GLIMS-RGI/rgi7_scripts/issues/39). See the "Version history" section below for a description of the connectivity levels and why they have been included.


## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi05-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI05/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 729
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 715. **Area**: 3233.0km². **Release date**: 2021-07-12.<br/>**Analysts**: Paul, Frank; Rastner, Philipp.

Submission 751
: **Submitter**: Cogley, Graham.<br/>**Number of outlines**: 19081. **Area**: 77020.5km². **Release date**: 2014-12-01.<br/>**Analysts**: Bolch, Tobias; Howat, Ian; LeBris, Raymond; Moelg, Nico; Negrete, A.; Paul, Frank; Rastner, Philipp.

Submission 813
: **Submitter**: McNabb, Robert.<br/>**Number of outlines**: 200. **Area**: 10228.3km². **Release date**: 2023-02-01.<br/>**Analysts**: McNabb, Robert.

Reviewers
: Langley, Kirsty;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi05-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI05/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: None.

Changes from Version 4.0 to 5.0
: A link was added to the record of Mittivakkat Glacier in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: 46 exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.<br/>19 glaciers appeared twice in version 3.2. One member of each such pair was removed.

Changes from Version 3.0 to 3.2
: A planimetric offset was discovered in parts of Greenland in version 3.0. This offset was repaired.

Changes from Version 2.0 to Version 3.0
: Coverage of Greenland is new in version 3.0, and is described in detail by {cite:t}`Rastner2012`. In all, 73 satellite images were processed. Glacier complexes were subdivided using a flowshed algorithm. An enhanced form of the algorithm for identifying glaciers other than the Greenland Ice Sheet was developed. In addition to the connectivity rule described below (see Version 1.0), a “topographic heritage rule” was added. Glaciers adjoining the ice sheet were first assigned to level CL2 (strongly connected) or level CL1 (weakly connected). Unassigned glaciers adjoining one or more level-2 glaciers were then assigned the same connectivity, and likewise for glaciers adjoining level-1 glaciers. The remaining unassigned glaciers, those not connected to the ice sheet at all, were assigned to level CL0.<br/>Glaciers of all three connectivity levels are included in the RGI. Rastner et al. recommend that CL2 glaciers be treated as part of the ice sheet, for which purpose they can be identified using Connect. The total extent of CL0 and CL1 glaciers, 89731 km2, is well in excess of any previous estimate of the extent of glaciers in the Greenland periphery. Adding the CL2 glaciers and the ice sheet, Rastner et al. estimate a glacierized area for Greenland as a whole of 1.808±0.004 × 106 km2. This lies between the two estimates suggested by {cite:t}`Kargel2012`, 1.801±0.016 × 106 km2 and 1.824±0.016 × 106 km2; these estimates are statistically indistinguishable from but more uncertain than that of Rastner et al.

Changes from Version 1.0 to Version 2.0
: None.

Version 1.0
: Distinguishing between what is considered ice sheet versus glaciers is a challenge, and depends on the scientific application. While the distinction is clear for the numerous fully detached glaciers, there are several regions where, although there is a physical connection to the main ice sheet, the ice mass is either a valley glacier in mountainous terrain, or it forms its own ice dome and is largely uncoupled from the ice sheet dynamics. Therefore, for applications such as extrapolation of laser altimetry data, some researchers consider that such ice masses should be categorized as glaciers rather than as part of the ice sheet.<br/>In the RGI, all ice masses with a possible but uncertain drainage divide are assigned to the ice sheet (e.g. on the Geikie Plateau), and all others to the local (or peripheral) glaciers. The latter are either not connected to the ice sheet at all, clearly separable (e.g. by mountain ridges) in the accumulation region, or only in contact with ice sheet outlets in the ablation region.<br/>Indeed, there is room for discussion on individual decisions, but for the purpose of the RGI we just need to start somewhere. The separation in the accumulation area is done along drainage divides derived from DEM-based watershed analysis.<br/>The glaciers north of ~81°N were not available from Landsat data and were provided by the Greenland Mapping Project {cite:p}`Howat2014a`.<br/>The semi-automated glacier mapping applied to the 64 Landsat scenes that were processed is based on a band ratio (ETM+ Band 3/Band 5) with an additional threshold in band 1 for better mapping of glacier areas in cast shadow. It is based on {cite:t}`Paul2005` and described for a part of western Greenland in {cite:t}`Citterio2009`. Debris-covered glacier parts as well as wrongly classified sea ice, icebergs or lakes were corrected manually in the vector domain. A 3 by 3 median filter is applied for image smoothing and glaciers smaller than 0.05 km2 are not considered. Wrongly classified regions with seasonal snow could not always be corrected.

```