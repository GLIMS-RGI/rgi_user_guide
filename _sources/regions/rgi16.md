# 16: Low Latitudes

Central and Tropical South America, Africa, Papua.

```{admonition} Subregions
:class: note, dropdown

- 16-01: Low-latitude Andes
- 16-02: Mexico
- 16-03: East Africa
- 16-04: New Guinea

```

:::{figure-md} rgi16-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI16/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Glacier locations and changes between RGI6 and RGI7.
:::

New inventories for Peru, Bolivia, Chile and Argentina. RGI6 is used elsewhere.

**Peru and Bolivia 1998**

The glacier outlines in RGI6 for Peru and Bolivia were derived from satellite images with adverse snow conditions, outlines received a triangular shape during raster-vector conversion, ice divides were at the wrong place and scenes were acquired over a 10-year period. For the new inventory we used 17 Landsat 5 TM scenes that were all acquired in 1998 with excellent snow conditions. Outlines for clean glaciers were created from a simple red/SWIR band ratio with scene specific thresholds. After raster-vector conversion wrongly mapped lakes were removed and missing debris-cover was manually added. New ice divides were derived from the 30 m resolution Copernicus DEM using the divides in RGI6 as a guide. The interpretation was supported by glacier outlines from the national glacier inventory of Peru and the "World imagery" layer of the ESRI basemap.

**Chile and Argentina**

See [](rgi17).

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi16-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI16/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

Submission 591
: **Submitter**: Cogley, Graham.<br/>**Number of outlines**: 158. **Area**: 169.2km². **Release date**: 2015-07-16.<br/>**Analysts**: Kienholz, Christian; Miles, Evan; Sharp, Martin; Wyatt, F..

Submission 700
: **Submitter**: Hidalgo, Lidia Ferri.<br/>**Number of outlines**: 17. **Area**: 1.5km². **Release date**: 2018-09-04.<br/>**Analysts**: Castro, Mariano; Gargantini, Hernán; Gimenez, Melisa; Hidalgo, Lidia Ferri; Masiokas, Mariano; Pecker Marcosig, Ivanna; Pitte, Pierre; Ruiz, Lucas; Zalazar, Laura.

Submission 730
: **Submitter**: Barcaza, Gonzalo.<br/>**Number of outlines**: 20. **Area**: 9.4km². **Release date**: 2018-07-24.<br/>**Analysts**: Albornoz, Amapola; Arias, Victor; Barcaza, Gonzalo; Garcia, Juan-Luis; Nussbaumer, Samuel; Tapia, Guillermo; Valdes, Javier; Videla, Yohan.

Submission 748
: **Submitter**: Paul, Frank.<br/>**Number of outlines**: 3495. **Area**: 1734.7km². **Release date**: 2021-09-02.<br/>**Analysts**: Goerlich, Franz; Paul, Frank; Rastner, Philipp.

Submission 753
: **Submitter**: Maussion, Fabien.<br/>**Number of outlines**: 4. **Area**: 13.6km². **Release date**: 2022-04-18.<br/>**Analysts**: Cáceres, B.; Francou, B.; Jordan, S.; Peñafiel, A.; Ungerechts, L..

Submission 760
: **Submitter**: Maussion, Fabien.<br/>**Number of outlines**: 1. **Area**: 0.1km². **Release date**: 2022-04-19.<br/>**Analysts**: Kienholz, Christian; Miles, Evan; Sharp, Martin; Wyatt, F..

Reviewers
: Prinz, Rainer; Rabatel, Antoine;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi16-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI16/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: Coverage of the glaciers of Cotopaxi, Ecuador, was replaced with outlines for 1997 digitized from {cite:t}`Jordan2005`).

Changes from Version 4.0 to 5.0
: Links were added to 2 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: 94 exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.<br/>The 81 remaining glacier complexes in the Bolivian Andes were subdivided by C. Kienholz into 159 glaciers. RGIIds for the whole of region 16 were altered in consequence.

Changes from Version 3.0 to 3.2
: Outlines of the glaciers of Mexico were replaced with outlines provided by E. Burgess, and the nominal glaciers of east Africa and New Guinea were replaced with outlines provided by N.J. Cullen and A. Klein respectively. Note that several glacier complexes are still present in southern Peru and western Bolivia.

Changes from Version 2.0 to Version 3.0
: Some outlines in northern Chile were improved.

Changes from Version 1.0 to Version 2.0
: Outlines of the glaciers of Mexico (16-02) were digitized by J.G. Cogley from maps in "Satellite Image Atlas of Glaciers of the World – North America". 59 glaciers in east Africa (16-03) and seven in New Guinea (16-04) were added as nominal circles from WGI-XF.<br/> See the RGI v6 Technical Note for an extended summary of quality controls conducted by E.S. Miles, University of British Columbia.

Version 1.0
: Shapefiles were created from late-summer, cloud-free Landsat 7 ETM+ imagery acquired prior to the 2003 scan line corrector (SLC) failure. To identify glacier surfaces, a normalized difference snow index (NDSI) was calculated using bands 5 and 2 for the red and near-infrared bands respectively. A threshold of approximately 0.5-0.65 was used to identify dirty/shady/bare ice, and one from 0.65-0.99 to identify snow-covered ice. Gridded files were then converted to polygons and additional manual editing was carried out to eliminate incorrectly classified regions.

```