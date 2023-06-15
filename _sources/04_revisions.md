# General revisions in RGI 7.0 

## Overview

RGI 7.0 includes several major changes compared to RGI 6.0:
- The quality of outlines is substantially improved in many regions due to inclusion of new updated inventory data.
- New attributes are available, while others were removed or renamed/redefined.
- Outlines of contiguous glacier complexes are available ("glacier complex" product) in addition to the outlines of each individual glaciers.
- New data files including shapefiles of common boundaries of individual glaciers as well as glacier centerlines have been added ("intersects" and "centerlines" products).
- All outlines and attributes are derived exclusively from GLIMS.
- A new largely automated workflow was developed to generate the RGI from the GLIMS database with the code publicly available to ensure reproducibility.
- Filename conventions are updated.

```{important}
Compared to previous versions, the RGI version 7 represents a fundamental change in the data processing workflow and file formatting. Returning users will have to adapt their analysis scripts and routines for them to work with RGI 7.0.
```

## Glacier outlines

RGI 7.0 contains substantial improvements in outline quality in many regions of the world. See [](05_description_by_region) for detailed description of changes in each region.

## Data processing workflow

Previous RGI versions were generated largely in an ad-hoc manner based on data collected from GLIMS and many individual contributors. Although highly successful in generating the first near-complete global glacier inventory and releasing almost annual updates until 2017, the exact procedures are not fully documented, and code and tools used to generate the dataset not publicly available. A major goal in RGI 7.0 was to largely automate the process with open-source code, and rely exclusively on GLIMS as data source for the generation of the RGI.

:::{figure-md} fig-workflow
<img src="img/workflow.png" alt="data workflow" class="bg-primary mb-1">

Schematic illustration of the RGI 7.0 data production workflow.
:::

The entire production workflow for RGI 7.0 is implemented in Python and is accessible through [this repository](https://github.com/GLIMS-RGI/rgi7_scripts). Here, we provide a summary of the key production steps:

1. **Submission of glacier inventories**: Working groups and analysts continuously submit glacier inventories to GLIMS. This process is often unguided, with data submissions made alongside publications or national inventory deliveries. The RGI Working Group occasionally guided mapping priorities by identifying regions that require improvements, and issuing public requests for data on the GLIMS and Cryolist e-mail listservers ([2020-05-13](https://lists.cryolist.org/pipermail/cryolist/2020-May/005135.html)). 
2. **GLIMS database processing**: The complete GLIMS database was downloaded and processed on the RGI 7.0 production server. This processing involves converting GLIMS outlines to the RGI format (a different data model), cropping the GLIMS files to RGI regions, and performing preliminary data quality checks.
3. **Outline selection and data integrity checks (alpha version)**: A Python script was generated for each RGI region based on the decisions made by the RGI consortium regarding which inventories to include in the RGI. This selection process is documented in [](inventory-selection). Technical data integrity checks were then conducted for the outlines to be integrated into the RGI 7.0 (see [](data-integrity)). The output at this stage is referred to as the "alpha version." The alpha version is a subset of GLIMS, and it does not yet have RGI attributes or follow RGI naming conventions (except for the organization in first order regions).<br>**Alpha version review process**: The alpha version was shared with the RGI consortium for review and comments, and the community was invited to provide feedback via email or GitHub. This process sometimes led to changes or updates in the inventories themselves. For example in Region 19 (Subantarctic and Antarctic Islands) the review process revealed several problems that were addressed by remapping several outlines. Once an inventory was amended or replaced, it was uploaded to GLIMS as a new submission and needed to be downloaded again for the RGI. Thus, the RGI alpha review process was an iterative process spanning over the course of roughly one year. 
4. **Attributes generation (beta version)**: Following the completion of the alpha phase, the regional files were automatically processed into their "beta version," which is the pre-final dataset. Beta files adhere to all RGI requirements, including attributes, names, identifiers, etc. A significant part of the processing workflow involved computing automated attributes such as glacier topography or generating additional products (e.g., the "intersects" or "glacier complex" products). To ensure consistency, the same processing script was applied to all regions.<br>**Beta version review process**: Similar to the alpha phase, the beta version was shared with the RGI consortium for review and discussion with feedback requested within 15 days. After addressing the review comments, no further changes to the outlines were permitted, except for cases where major flaws in the outlines were discovered subsequently.
5. **Generation of RGI 7.0**: The RGI steering committee approved the RGI 7.0 dataset during a meeting on XX MONTH 2023. The final RGI 7.0 dataset was created by renaming the beta files and storing them in a permanent repository on XX MONTH 2023.

(inventory-selection)=
## Inventory selection process

For many regions, several inventories close to the target date are available. TODO: describe the decision process.

## Data and file format

In RGI 7.0 data and file formats were revised to enhance readability and accessibility for both humans and machines. While maintaining a general familiarity with the RGI 6.0 format, we addressed inconsistencies and implemented a set of rules for generating the data files and data fields. These rules include:

- Script-generated files: All files were generated using scripts, minimizing the likelihood of human errors during typing or processing. However, it is important to note that this does not guarantee the absence of errors.
- Metadata and documentation: All file attributes received accompanying metadata and documentation, providing additional information and context.
- Lowercase naming conventions: File names and field attribute names were converted to lowercase to avoid the previous mix of lower case and upper case notation.
- Standardized file naming conventions: Files were named according to predefined conventions, allowing for easier machine reading and processing. For instance, the region identifiers are stored in the region description shapefile, enabling the opening of corresponding outline shapefiles in a scripted manner.

Any deviations from these rules should be considered as errors or oversights and will be addressed in future versions.

(data-integrity)=
## Quality control and data integrity

Since the RGI is a subset of GLIMS, all characteristics of GLIMS are inherited by the RGI, including any problems or inaccuracies present in the outlines. However, the RGI workflow incorporates several data integrity checks on the GLIMS data:

1. **Comparison with original datasets**: Whenever possible, such as when access to the original inventories is available (e.g., GAMDAMv2, {cite:t}`Sakai2019`), the RGI dataset (and thus the associated GLIMS data) could be verified against the original dataset. This process helped to identify a few errors in the GLIMS data ingestion workflow. It served as a rough data integrity check.
2. **Detection of duplicated outlines**: The RGI workflow identifies duplicated outlines by ensuring that no representative point of one outline overlaps with another outline. This filtering process removed a small number of duplicate outlines that exist in GLIMS.
3. **Polygon validity**: The RGI workflow checks the validity of [polygon geometries](https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm). Approximately 2% of the geometries extracted from GLIMS for RGI 7.0 were considered "invalid" based on the Open Geospatial Consortium Implementation Standard. To rectify this, the RGI workflow employs Shapely's `make_valid` function, which eliminates erroneous self-intersections or sliver polygons. The correction process ensures that each glacier's area is preserved within a tolerance of 0.1 km² or 0.1 %. In rare cases where this could not be achieved, one GLIMS entry was split into two geometries, effectively adding two glaciers to the RGI instead of just one.
4. **Overlapping area correction**: The RGI workflow checks for and resolves overlapping areas by intersecting geometries with a common boundary and removing overlaps where necessary. However, such cases were rare.

It is important to note that these data integrity checks may result in some outlines in RGI 7.0 differing slightly from the ones stored in GLIMS, although the differences are often imperceptible. Despite these minor discrepancies, the benefits of correcting outlines in response to these data integrity checks are considered to outweigh any deviations from the GLIMS database.
