# Revisions in RGI7 

```{important}
While being largely consistent with previous RGI versions, the RGI version 7 represents a fundamental change in the data processing workflow and file formatting. Returning users will have to adapt their analysts scripts and routines, hopefully for the better.
```

## Data sources and outlines

RGI7 contains several considerable improvements in outline quality for many regions of the world.
Refer to [](05_description_by_region) for the changes in outlines and data sources.

## Data processing workflow

Historically, RGI versions have been generated and updated "manually", using GIS tools to merge, edit, and prepare the RGI data files. Contributions to the RGI were sent directly to the dataset maintainer (per mail or otherwise), and this person was in charge of processing them and ensuring consistency. This efficient, ad-hoc workflow contributed to the speed at which the RGI could be created and lead to its success. However, this process was prone to human errors and relied in a few key persons without whom the dataset could not be maintained or updated. This process also led to confusion, since there were two databases of glacier outlines: GLIMS and RGI, with different data models and glacier ids.

With RGI7, the two data products are now related and each have a clear mandate. GLIMS is the central database for all glacier outlines, while the RGI is a curated snapshot of GLIMS for a target year ([Figure 2](fig-workflow)).

:::{figure-md} fig-workflow
<img src="img/workflow.png" alt="data workflow" class="bg-primary mb-1">

Schematic illustration of the RGI7 data production workflow.
:::

The entire production workflow for RGI7 is implemented in Python and is accessible through [this repository](https://github.com/GLIMS-RGI/rgi7_scripts). Here, we provide a summary of the key production steps:

1. **Submission of glacier inventories**: Working groups and analysts continuously submit glacier inventories to GLIMS. This process is often unguided, with data submissions made alongside publications or national inventory deliveries. The RGI consortium occasionally guides the process by setting priorities, such as focusing on poorly covered regions or addressing obviously incorrect outlines. The RGI consortium has also made public requests for data on the GLIMS and Cryolist e-mail listservers ([2020-05-13](https://lists.cryolist.org/pipermail/cryolist/2020-May/005135.html)). Regardless of the reason for mapping a region, all inventories must be submitted to GLIMS.
2. **GLIMS database processing**: The complete GLIMS database is downloaded and processed on the RGI7 production server. This processing involves converting GLIMS outlines to the RGI format (a different data model), cropping the GLIMS files to RGI regions, and performing preliminary data quality checks.
3. **Outline selection and data integrity checks (alpha version)**: A Python script is generated for each RGI region based on the decisions made by the RGI consortium regarding which inventories to include in the RGI. This selection process is documented in [](inventory-selection). After the outline selection, stricter data integrity checks are conducted (see [data-integrity]). The output at this stage is referred to as the "alpha version." While it is a subset of GLIMS, it does not yet have RGI attributes or follow RGI conventions (except for the organization in first order regions). The alpha version is shared with the RGI consortium for review and comments. The community is also invited to provide feedback or updated inventories via email or GitHub, leading to changes in the inventories themselves and subsequently in GLIMS. Once an inventory is amended or replaced, it needs to be downloaded from GLIMS again.
4. **Attributes generation (beta Version)**: Following the completion of the alpha phase, the regional files are automatically processed into their "beta version," which is the pre-final dataset. Beta files adhere to all RGI requirements, including attributes, names, identifiers, etc. A significant part of the processing workflow involves computing automated attributes such as glacier topography or generating additional products (e.g., the "intersects" or "glacier complex" products). To ensure consistency, the same processing script is applied to all regions. Similar to the alpha phase, the beta version is shared with the community for review and discussion. At this stage, no additional changes to the outlines are permitted, except for cases where major flaws in the outlines are discovered.
5. **Generation of RGI7**: Once the beta files are accepted, the final RGI7 dataset is created by renaming the beta files and storing them in a permanent repository.

(inventory-selection)=
## Inventory selection process

For the majority of the regions, several inventories are available. TODO: describe decision process.

## Data and file format

The RGI7 files have been revised to enhance readability and accessibility for both humans and machines. While maintaining a general familiarity with the RGI6 format, we have addressed inconsistencies and implemented a set of rules for generating the data files and data fields. These rules include:

- Script-generated files: All files have been generated using scripts, minimizing the likelihood of human errors during typing or processing. However, it is important to note that this does not guarantee the absence of all types of errors.
- Lowercase naming conventions: File names and field attribute names have been converted to lowercase, making their use more predictable (no mix between lower case and upper case).
- Metadata and documentation: All file attributes are expected to have accompanying metadata and documentation, providing additional information and context.
- Standardized file naming conventions: Files have been named according to predefined conventions, allowing for easier machine reading and processing. For instance, the region identifiers are stored in the region description shapefile, enabling the opening of corresponding outline shapefiles in a scripted manner.

Any deviations from these rules should be considered as errors or oversights and will be addressed in future versions to ensure continuous improvement.

(data-integrity)=
## Quality control and data integrity

The RGI is a subset of GLIMS, which means that all characteristics of GLIMS are inherited by the RGI, including any problems or inaccuracies present in the outlines. However, the RGI incorporates several data integrity checks on the GLIMS data:

1. **Removal of small glaciers**: Glaciers with areas smaller than 0.01 km², which is the recommended minimum of the World Glacier Inventory, are eliminated. However, nunataks (rocky peaks protruding from glaciers) are retained regardless of their size.
2. **Comparison with original datasets**: Whenever possible, such as when access to the original inventories is available (e.g., GAMDAMv2, which is openly accessible), the RGI (and consequently GLIMS) is verified against the original dataset. This process has helped identify a few bugs in the GLIMS data ingestion workflow. It serves as a rough data integrity check.
3. **Detection of duplicated outlines**: The RGI identifies duplicated outlines by ensuring that no representative point of one outline overlaps with another outline. This filtering process removes a small number of outlines from GLIMS.
4. **Polygon geometry validity**: The RGI checks and corrects the validity of polygon geometries. Approximately 2% of the geometries extracted from GLIMS for RGI7 are considered "invalid" based on the Open Geospatial Consortium Implementation Standard. To rectify this, the RGI employs Shapely's make_valid function, which eliminates erroneous figures of 8 or similar sliver polygons. The correction process ensures that each glacier's area is preserved within a tolerance of 0.1 km² or 0.1%. In rare cases where this cannot be achieved, one GLIMS entry is split into two geometries, effectively adding two glaciers to the RGI instead of one in GLIMS.
5. **Overlapping area correction**: The RGI checks for and resolves overlapping areas by intersecting geometries with a common boundary and removing overlaps where necessary. However, such cases are rare.

It's important to note that these data integrity checks may result in some outlines in RGI7 being slightly different from the ones stored in GLIMS, although the differences are often imperceptible. Despite these minor discrepancies, the benefits of these data integrity checks are considered to outweigh any deviations from the GLIMS database.
