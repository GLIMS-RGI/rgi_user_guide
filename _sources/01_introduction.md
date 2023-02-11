# Introduction

## What is the RGI?

The [Randolph Glacier Inventory](https://www.glims.org/RGI) (RGI) is a globally complete inventory of glacier outlines. It is a subset of the database compiled by the [Global Land Ice Measurements from Space](https://www.glims.org) initiative (GLIMS). While GLIMS is a multi-temporal database, the RGI is intended to be a snapshot of the world’s glaciers as they were near to a target date (currently: the year 2000). Production of the RGI was motivated by the preparation of the Fifth Assessment Report of the Intergovernmental Panel on Climate Change (IPCC AR5, 2013). The RGI was released initially with little documentation in view of the IPCC’s tight deadlines during 2012, and continuously updated afterwards. Much more documentation is available today.

The RGI was not designed for the measurement of glacier-by-glacier rates of area change, for which the greatest possible accuracy in dating, delineation and georeferencing is essential. Many RGI outlines pass this test, but in general completeness of coverage, consistency, and closeness to the year 2000 has higher priority. The strength of the RGI lies in the capacity it offers for handling many glaciers at once, for example for estimating glacier volumes and rates of elevation change at regional and global scales and for simulating cryospheric responses to climatic forcing.

## Who develops and hosts the RGI?

In 2014 development of the RGI became the responsibility of the [Working Group on the Randolph Glacier Inventory and Infrastructure for Glacier Monitoring](https://cryosphericsciences.org/activities/wg-rgi/), a body of the [International Association of Cryospheric Sciences](https://cryosphericsciences.org) (IACS). In 2019, a new Working Group was created to pursue the work of the first group and extend its objectives: the [IACS Working Group on the Randolph Glacier Inventory (RGI) and its role in future glacier monitoring and GLIMS](https://cryosphericsciences.org/activities/working-groups/rgi-working-group/).

The RGI datasets are hosted and documented on [glims.org](https://www.glims.org/RGI), and the RGI files are available for download via the [NSIDC data protal](https://nsidc.org/data/nsidc-0770) (GLIMS is part of NSIDC). The RGI datasets versions 1 to 6 were created independently from GLIMS: while some glacier outlines originated from GLIMS, others did not (either because they weren't submitted to GLIMS, didn't comply to GLIMS standards, or did not agree to the GLIMS license agreement). With the ingestion of the entire RGI version 6 into the GLIMS database in 20XX (@Bruce, info?), GLIMS became globally complete. As of RGI version 7, the RGI is now entirely drawn from the GLIMS database, making of RGI a subset of GLIMS (see [](04_revisions) for more details).

## Version History

**Version 1.0** of the RGI was released in February 2012. It included a considerable number of unsubdivided ice bodies, which we refer to as glacier complexes, and a considerable number of nominal glaciers, which are glaciers for which only a location and an area are known; they are represented by circles of the appropriate area at the given location. An unofficial update of version 1.0 was provided in April 2012 to replace several regions that had topology errors and repeated polygons. Version 2.0, released in June 2012, eliminated a number of flaws and provided a uniform set of attributes for each glacier. Several outlines were improved, and a number of outlines were added in previously omitted regions. 

**Version 2.0** also added shapefiles for its first-order and second-order regions.

**Version 3.0** was an interim release representing the RGI as of 7 April 2013. It was the basis for the work of {cite:t}`Gardner2013`. The main improvements included identification of all tidewater basins, and separation of glacier complexes into glaciers in nearly all regions. Version 3.2, released in August 2013, included additional separation of glacier complexes into glaciers, and repairs of some geometry errors. It is the basis for the scientific description and analysis of the RGI by {cite:t}`Pfeffer2014`.

**Version 4.0** was released in December 2014. The most significant enhancement was the addition of topographic and hypsometric attributes for nearly all glaciers. These new attributes are described in detail below. Many glacier outlines were unchanged in version 4.0, but many more glaciers were assigned dates or date ranges, some names were added or corrected, and the inventory of Alaska was new. Remaining glacier complexes in Bolivia were subdivided, and nominal glaciers were added to correct omissions in the Greater Caucasus. A global grid of glacierized area with 0.5-degree resolution was added.

**Version 5.0**, released in July 2015, had new coverage of most of Asia (RGI regions 10, 13, 14 and 15), with some improved outlines elsewhere. Linkages to the Fluctuations of Glaciers database of the World Glacier Monitoring Service were provided for some glaciers with mass-balance measurements.

**Version 6.0**, released in July 2017, has improved coverage of the conterminous US (regions 02-05 and 02-06), Scandinavia (region 08) and Iran (region 12-2). In Scandinavia several hundred smaller glaciers have been added and most glaciers now have exact dates. The flag attributes `RGIFlag` and `GlacType` were reorganized. Surging codes have been added from Sevestre and Benn (2015). This version would be the last to be released under the leadership of Graham Cogley, [who passed in 2018](https://www.igsoc.org/j-graham-cogley-1948-2018),

**Version 7.0**, released in xx 2023, comes with major outline quality improvements in nearly all RGI regions. Furthermore, the RGI production has been entirely redesigned to use GLIMS as the sole data provider. The file generation process is now largely automated, relying on expert decision for the choice of the outlines but using open source scripts for all dataset creation steps. The file naming convention and attributes have changed substantially, requiring returning users to adapt their data analysis workflow (see [](04_revisions) for more details).

## Data Distribution Policy

The RGI may be used freely under the [Creative Commons License](https://creativecommons.org/licenses/by/4.0) with due acknowledgement (by citing this note for technical details or {cite:t}`Pfeffer2014` for scientific background). The inventory can be downloaded from XXX. Where appropriate (for example for regional studies), users are invited to cite the analysts who provided the RGI outlines. See [](03_data_decription) for more details about how to retrieve this information from the RGI.

## Data Sources

The RGI is a combination of new and previously-published glacier outlines. All outlines are part of the GLIMS database and comply to the GLIMS license agreement. Many outlines used in RGI version 7 were provided by the community in response to requests for data on the GLIMS and Cryolist e-mail listservers ([2020-05-13](https://lists.cryolist.org/pipermail/cryolist/2020-May/005135.html)). See [](tables/data_sources) for a list of RGI contributors.

## RGI source code

All RGI related codebase is available on the [GLIMS-RGI Github organization](https://github.com/GLIMS-RGI):
- [GLIMS-RGI/rgi7_scripts](https://github.com/GLIMS-RGI/rgi7_scripts): code and scripts generating the RGI out of GLIMS
- [GLIMS-RGI/rgi_user_guide](https://github.com/GLIMS-RGI/rgi_user_guide): this documentation

## Dataset Reference

Earlier versions of this technical note were referenced as "Arendt et al." (various dates). The following form of reference is now recommended: 

**Add RGI7 Ref.**

A detailed scientific description of the RGI version 3.2 is given by {cite:t}`Pfeffer2014`.

A detailed scientific description of the RGI version 7 is in preparation.
