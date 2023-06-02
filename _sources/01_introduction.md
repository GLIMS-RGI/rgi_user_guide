# Introduction

## What is the RGI?

The Randolph Glacier Inventory ([RGI](https://www.glims.org/RGI)) is a globally complete inventory of glacier outlines (excluding the ice sheets in Greenland and Antarctica). It is a subset of the database compiled by the Global Land Ice Measurements from Space initiative ([GLIMS](https://www.glims.org)). While GLIMS is a multi-temporal database with an extensive set of attributes, the RGI is intended to be a snapshot of the world’s glaciers at a specific target date, which in RGI7.0 and all previous versions has been set to as close as possible to the year 2000 (although in fact its range of dates can still be substantial in some regions). The RGI includes outlines of all glaciers with areas larger than 0.01 km², which is the recommended minimum of the World Glacier Inventory.

The RGI was not designed for the measurement of glacier-by-glacier rates of area change, for which the greatest possible accuracy in dating, delineation and georeferencing is essential. While many RGI outlines meet these requirements, the primary focus of the RGI is on achieving global coverage, consistency, and proximity in a specific year. The strength of the RGI lies in its ability to handle large numbers of glaciers simultaneously. This allows, for example, for the estimation of glacier volumes and rates of elevation change at regional and global scales, as well as the simulation of cryospheric responses to climatic forcing.

## Who develops and hosts the RGI?

In 2014 development of the RGI became the responsibility of the [Working Group on the Randolph Glacier Inventory and Infrastructure for Glacier Monitoring](https://cryosphericsciences.org/activities/wg-rgi/), which operates under the International Association of Cryospheric Sciences([IACS](https://cryosphericsciences.org)). In 2019, a new Working Group was established to build upon the previous achievements and further expand its objectives: the [IACS Working Group on the Randolph Glacier Inventory (RGI) and its role in future glacier monitoring and GLIMS](https://cryosphericsciences.org/activities/working-groups/rgi-working-group/).

The RGI datasets are listed on [glims.org](https://www.glims.org/RGI), and the RGI files can be downloaded through the [data portal](https://nsidc.org/data/nsidc-0770) at the National Snow and Ice Data Center ([NSIDC](https://nsidc.org)), which is the host for GLIMS.

## Version History

**Version 1.0** of the RGI was released in February 2012. It included a considerable number of unsubdivided ice bodies, which we refer to as glacier complexes, and a considerable number of nominal glaciers, which are glaciers for which only a location and an area are known; they are represented by circles of the appropriate area at the given location. An unofficial update of version 1.0 was provided in April 2012 to replace several regions that had topology errors and repeated polygons. Version 2.0, released in June 2012, eliminated a number of flaws and provided a uniform set of attributes for each glacier. Several outlines were improved, and a number of outlines were added in previously omitted regions. 

**Version 2.0** also added shapefiles for its first-order and second-order regions.

**Version 3.0** was an interim release representing the RGI as of 7 April 2013. It was the basis for the work of {cite:t}`Gardner2013`. The main improvements included identification of all tidewater basins, and separation of glacier complexes into glaciers in nearly all regions. Version 3.2, released in August 2013, included additional separation of glacier complexes into glaciers, and repairs of some geometry errors. It is the basis for the scientific description and analysis of the RGI by {cite:t}`Pfeffer2014`.

**Version 4.0** was released in December 2014. The most significant enhancement was the addition of topographic and hypsometric attributes for nearly all glaciers. These new attributes are described in detail below. Many glacier outlines were unchanged in version 4.0, but many more glaciers were assigned dates or date ranges, some names were added or corrected, and the inventory of Alaska was new. Remaining glacier complexes in Bolivia were subdivided, and nominal glaciers were added to correct omissions in the Greater Caucasus. A global grid of glacierized area with 0.5-degree resolution was added.

**Version 5.0**, released in July 2015, had new coverage of most of Asia (RGI regions 10, 13, 14 and 15), with some improved outlines elsewhere. Linkages to the Fluctuations of Glaciers database of the World Glacier Monitoring Service were provided for some glaciers with mass-balance measurements.

**Version 6.0**, released in July 2017, has improved coverage of the conterminous US (regions 02-05 and 02-06), Scandinavia (region 08) and Iran (region 12-2). In Scandinavia several hundred smaller glaciers have been added and most glaciers now have exact dates. The flag attributes `RGIFlag` and `GlacType` were reorganized. Surging codes have been added from Sevestre and Benn (2015). This version would be the last to be released under the leadership of Graham Cogley, [who passed in 2018](https://www.igsoc.org/j-graham-cogley-1948-2018),

**Version 7.0**, released in July 2023, comes with major outline quality improvements in nearly all RGI regions. Furthermore, the RGI production has been entirely redesigned to use GLIMS as the sole source of data. The file generation process is now largely automated, extracting from GLIMS the outlines closest to the target date while also relying on expert judgment for the exact choice of available outlines. Open source scripts are used for all dataset creation steps. The file naming convention and attributes have changed substantially, requiring users of previous versions to adapt their data analysis workflow (see [](04_revisions) for more details).

## Data Distribution Policy

The RGI may be used freely under the [Creative Commons License](https://creativecommons.org/licenses/by/4.0) with due acknowledgement (by proper referencing, see below). Where appropriate (for example for regional studies), users are invited to cite the analysts who provided the RGI outlines. See [](03_data_decription) for more details about how to retrieve this information from the RGI.

## Dataset Reference

The RGI7.0 data set should be cited by
**Add RGI7 Ref.**

This Technical Report (focusing on RGI 7.0) should be cited by
**Add Ref.**

Earlier versions of the Technical Report are referenced as XXXX (focusing on RGI6.0) and "Arendt et al." (various dates, prior RGI6.0).

A detailed scientific description of the RGI version 3.2 is given by {cite:t}`Pfeffer2014`.

A detailed scientific description of the RGI version 7 is in preparation.


## Data Sources

All outlines for RGI7.0 are derived from the GLIMS database and comply with the GLIMS license agreement. Many new outlines used in RGI version 7 were submitted by the community to GLIMS in response to requests for data on the GLIMS and Cryolist e-mail listservers ([2020-05-13](https://lists.cryolist.org/pipermail/cryolist/2020-May/005135.html)). See [](tables/data_sources) for a list of RGI7.0 contributors.

Since GLIMS was globally incomplete, earlier RGI versions combined outlines from GLIMS with outlines from other sources, the latter including outlines specifically generated for the purpose of the RGI. These outlines had not yet been submitted to GLIMS, did not meet GLIMS standards, or did not comply with the GLIMS license agreement. GLIMS achieved global coverage by incorporating the missing glacier outlines from RGI version 6. Starting from RGI version 7.0, the workflow has been revised and optimized. The RGI is now entirely derived from the GLIMS database, with the RGI functioning as a subset of GLIMS.

## RGI source code

All code used to generate RGI7.0 is available on the [GLIMS-RGI Github organization](https://github.com/GLIMS-RGI):
- [GLIMS-RGI/rgi7_scripts](https://github.com/GLIMS-RGI/rgi7_scripts): code and scripts generating the RGI out of GLIMS
- [GLIMS-RGI/rgi_user_guide](https://github.com/GLIMS-RGI/rgi_user_guide): this Technical Report
