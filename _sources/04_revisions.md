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

TODO - more text

:::{figure-md} fig-workflow
<img src="img/workflow.png" alt="data workflow" class="bg-primary mb-1">

Schematic illustration of the RGI7 data production workflow.
:::


## Data format

TODO - more text
