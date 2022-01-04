# fossil-fuels-and-greenhouse-gas
A project to use publicly available data to study the interaction between fossil fuel production, greenhouse gas concentrations, and global temperatures. Possibly looking at links among these and COVID-19 data. 

## Table of Contents
* [Data Sources](#datasources)

## Data Sources
* Scripps CO2 Program - AKA The Keeling Curve
  * https://scrippsco2.ucsd.edu/data/atmospheric_co2/mlo.html
  * Atmospheric CO2 measurements
  * 1958 to present
  * Time Resolution: monthly, weekly, daily, every 10 minutes
  * Quality: these are direct measurements, and these data are considered by the American Chemical Society to be the ["authoritative record of atmospheric CO2 concentrations"](https://www.acs.org/content/acs/en/education/whatischemistry/landmarks/keeling-curve.html)
* EIA Finished Gasoline Production - US Energy Information Administration
  * https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WGFRPUS2&f=W
  * US Refiner and Blender Adjusted Net Production of Finished Motor Gasoline
  * 1982 to present
  * Time Resolution: weekly
  * Quality: Not sure... US Government accounting of gasoline production seems legit but maybe we could find some citations or something. 
* CDC Covid Cases and Deaths by State
  * https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data
  * Quality: these data rely on state health department reporting, so there could be variation in quality among the states. It might be worth looking at one or two states or even going to state health departments for data.  
* IPCC
  * temperature vs cumulative CO2 emissions since 1850 - Figure SPM.10 - data located in /data/IPCC/Figure_SPM10_Near_linear_relationship_btwn_cumulative_co2_emissions_and_increase_in_global_surface_temp/Top_panel_HISTORY.csv
  * temperature over time - Figure SPM.1 - the right panel has from 1850 to 2020 observed, simulated natural only, and simulated natural plus human caused warming
