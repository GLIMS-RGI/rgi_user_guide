# 13: Central Asia

Regions `13`, `14`, `15` comprise the region that is often referred to as High Mountain Asia. Region 13 encompasses all glaciers south of 46°N in the Tien Shan (also called Tian Shan), the Pamir and the mountain ranges on the Tibetan Plateau but excluding those included in regions `14` and `15`. The term "Central Asia" has been chosen to differentiate the four RGI regions in Asia outside the Arctic, fully aware that the geographical extent is commonly different when used in other contexts. 

```{admonition} Subregions
:class: note, dropdown

- 13-01: Hissar Alay
- 13-02: Pamir (Safed Khirs / West Tarim)
- 13-03: West Tien Shan
- 13-04: East Tien Shan (Dzhungaria)
- 13-05: West Kun Lun
- 13-06: East Kun Lun (Altyn Tagh)
- 13-07: Qilian Shan
- 13-08: Inner Tibet
- 13-09: Southeast Tibet

```

:::{figure-md} rgi13-new-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI13/isrgi6_map.jpeg" alt="region map" class="bg-primary mb-1">

Regional glacier area.
:::

## Changes from version 6.0 to 7.0

All previous outlines have been replaced by the GAMDAM glacier inventory version 2 GGI {cite:p}`Sakai2019`, also named GGI18. The glaciers were manually mapped based on Landsat TM and ETM+ summer imagery with most scenes being from the year 2002. Earlier and later scenes were used in case of unsuitable scenes within this year.

## Additional information 

```{admonition} Data sources and analysts
:class: important, dropdown

:::{figure-md} rgi13-source-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI13/inventory_map.jpeg" alt="region map" class="bg-primary mb-1">

Submission IDs used for this region.
:::

**Glacier outline providers to GLIMS**

*This list includes the providers of the outlines used in the RGI 7.0 as generated automatically from the GLIMS outlines metadata. We acknowledge that the list may be incomplete due to omissions in the GLIMS database.*

Submission 752
: **Submitter**: Sakai, Akiko.<br/>**Number of outlines**: 75613. **Area**: 50344.0km². **Release date**: 2018-08-24.<br/>**Analysts**: Sakai, Akiko.

Reviewers
: None;

```

```{admonition} Outlines date distribution
:class: seealso, dropdown

:::{figure-md} rgi13-hist-fig
<img src="https://cluster.klima.uni-bremen.de/~fmaussion/misc/rgi7_data/l4_rgi7b0_plots/RGI13/date_hist.png" alt="region map" class="bg-primary mb-1">

Relative glacier area distribution per outline date.
:::

```

```{admonition} Version history
:class: note, dropdown

Changes from Version 5.0 to 6.0
: None.

Changes from Version 4.0 to 5.0
: Regions 13, 14 and 15 are entirely new in version 5.0. being taken from {cite:t}`Nuimura2015`, {cite:t}`Guo2015` and as-yet unpublished work at the Technical University of Dresden and University of Zürich. *Remark (2023): the outlines have now been published: {cite:t}`Molg2018`*. The Dresden/Zürich outlines cover the Karakoram in region 14.<br/>The GAMDAM inventory of {cite:t}`Nuimura2015` covers all of High Mountain Asia (including RGI region 10-04). The Second Chinese Glacier Inventory (CGI2) of {cite:t}`Guo2015` covers China. The GAMDAM outlines are nearly all from 1999–2003 and thus conform with the recommendation of {cite:t}`Paul2009` to select imagery as close to 2000 as possible. However they exclude thin ice on headwalls and tend to have areas smaller than those measured in conformance with GLIMS guidelines {cite:p}`Raup2007`. The CGI2 inventory has outlines mostly from a target period of 2006–2010, but includes older outlines from the First Chinese Glacier Inventory (CGI1) where suitable imagery could not be found within the target period.<br/>A final decision about selection for the RGI from these extensive sources awaits detailed intercomparison. RGI version 5.0 incorporates those CGI2 outlines that are not from CGI1, and GAMDAM outlines in areas of remaining CGI1 coverage as well as areas outside China other than the Karakoram.<br/>Glacier outlines retired from version 4.0 will be added to GLIMS if they are not in GLIMS already.<br/>Links were added to 17 glaciers in the WGMS mass-balance database.

Changes from Version 3.2 to 4.0
: 45 exterior GLIMSIds were replaced. Topographic and hypsometric attributes were added.</br>An effort was made to recover as many dates as possible for High Mountain Asia as a whole. Duplication was avoided by creating disjunct polygons for each source, including the Chinese Glacier Inventory (CGI). The outlines of most RGI glaciers on Chinese territory were obtained from the GLIMS database before the RGI system of attributes was adopted. Some of the other sources of dates for High Mountain Asia were partly on Chinese territory.<br/>The dates of CGI glaciers were recovered from the 24 May 2011 version of GLIMS. The CGI and RGI outlines were matched by computing arc distances between their GLIMSId locations. Because some work was done for the RGI on correcting mislocated CGI glaciers, this operation was not straightforward. By inspection of trial results, and bearing in mind that the aim was only to place the glacier within the outline of its source image or air photograph, a separation not exceeding 2 km was found sufficient to assign the CGI date accurately to its closest RGI counterpart. Of 50,458 glaciers within the CGI polygon, 38% had exactly matching locations, 43% had separations within 300 m, and 1.4% (709) failed the 2-km test of proximity. Thus the CGI yielded 37,769 new dates, covering 53,192 km2, for RGI 4.0.<br/>The glacier inventory of the Nyainqentanghla Range in southeastern Tibet by {cite:t}`Bolch2010` was one of the sources for RGI 3.2, and the necessary dates for 789 glaciers (area 796 km2) were recovered from that paper. The mountain range was subdivided into three dated polygons, each representing a different source image or set of images.<br/>Most of the O2Region codes in earlier versions were incorrect and have been corrected.<br/>Where Chinese RGI glaciers could be matched with confidence to their equivalents in GLIMS, their 12-character WGI identification codes were added to the Name field.

Changes from Version 3.0 to 3.2
: None.

Changes from Version 2.0 to Version 3.0
: Glacier outlines in much of the central Tien Shan were replaced by the inventory of {cite:t}`Osmonov2013`. The outlines were mapped semi-automatically and manually based on Landsat TM data from ~2008. This inventory is superior to the former data as the geolocation is correct while the other data obtained from the GLIMS data base had inhomogeneous shifts. In the Pamir, several outlines from the DCW were replaced by semi-automatically mapped outlines based on Landsat TM/ETM+ data from ~2000. The large offset between the GLIMS data and data from the CGI in eastern Pamir was reduced.

Changes from Version 1.0 to Version 2.0
: None.

Version 1.0
: Large parts of Central Asia are covered by the GLIMS database, which consists in China of data from the first Chinese Glacier Inventory {cite:p}`Shi2009a` and is of heterogeneous and generally slightly lower quality (more generalized) than the other glacier data used here. It has also to be noted that some of the GLIMS data in Central Asia have a shift in location. Large parts of the Tien Shan in Kazakhstan and Kyrgyzstan were mapped manually or semi-automatically using ratio images from ASTER and Landsat data (e.g. Kutuzov and Shahgedanova, 2009; {cite:t}`Kriegel2013`). Important missing areas such as the Central Pamirs, Naryn basin, northern Tien Shan {cite:p}`Bolch2007` and the Dzhungarian Alatau were mapped semi-automatically with manual corrections using Landsat TM/ETM+ scenes. The glacier inventory for the Nyainqentanglha Range in Tibet was taken from {cite:t}`Bolch2010`.<br/>Remaining missing areas were filled by a glacier layer compiled by B. Raup {cite:p}`Raup2000` from the Digital Chart of the World (DCW) and the World Glacier Inventory. The DCW outlines are in western Kyrgyzstan (region 13-03), the Hissar Alay (13-01), the Safed Khirs (northern Afghanistan) and parts of the southwest Pamir (13-02).

```
