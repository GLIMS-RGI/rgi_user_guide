# 08: Scandinavia

All glaciers in Scandinavia.

```{admonition} Subregions
:class: note, dropdown

- 08-01: North Scandinavia
- 08-02: Southwest Scandinavia
- 08-03: Southeast Scandinavia

```


:::{figure-md} rgi08-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI08/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

The primary sources of glacier outlines for this region were mapped using a combination of Landsat TM/ETM+
and SPOT4 and SPOT5 imagery acquired between 1999 and 2006 (see {cite:t}`Andreassen2008a`, {cite:t}`Paul2009a`, and {cite:t}`Paul2011`
for details). Additional updates come from {cite:t}`Andreassen2012`. 

For RGI7, the only changes are in Sweden, where RGI6 glaciers [have been corrected for a map projection shift](https://github.com/GLIMS-RGI/rgi7_scripts/issues/36). 
Additionally, 4 "nominal glaciers" (potential glaciers without outlines) in the east of the region were deleted, as they did not seem to correspond to real glaciers.

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi08-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI08/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 611
: **Submitter**: Winsvold, Solveig Havstad.<br/>**Number of outlines**: 3142. **Area**: 2674.9km². **Release date**: 2012-12-13.<br/>**Analysts**: Andreassen, Liss Marie; Winsvold, Solveig Havstad.

Submission 812
: **Submitter**: Frank, Thomas.<br/>**Number of outlines**: 269. **Area**: 273.0km². **Release date**: 2023-01-02.<br/>**Analysts**: Brown, Ian; Frank, Thomas; Hansson, Erik.

Reviewers
: Mannerfelt, Erik;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi08-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI08/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

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
: The glacier outlines for Norway are based on Landsat (TM and ETM+) imagery from 1999-2006.<br/>The Swedish glacier outlines use imagery from SPOT5 and SPOT4 (dates not provided). In some regions these outlines were updated against September 2008 Swedish Land Survey imagery available on Google Earth.<br/>The glacier mapping to which GlobGlacier contributed is documented in {cite:t}`Andreassen2008a` for Jotunheimen, {cite:t}`Paul2009a` for Svartisen, and {cite:t}`Paul2011` for the Jostedalsbreen region.

```