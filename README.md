# fossil-fuels-and-greenhouse-gas
Study of interaction between consumption of fuel across the world and its relation to carbon emission. The analysis will also compare the GDP for each country to the amount of carbon emitted by that country. The analysis may include the atmospheric temperature in relation to carbon emissions.

## Table of Contents
* [Visualizations](#visualizations)
* [Data Sources](#datasources)
* [Contributors](#contributors)

## Visualizations
* Filter by country and view the information on GDP vs. Fuel Production vs. CO2 Emission
* Chart displaying different types fuel produced by volume
* Temperature heatmap across the world, ability to view the data by year and by country
* Fuel consumption heatmap across the world, ability to view the data by year and by country


## Data Sources
### Possible New Sources
#### Conflict / War
* Uppsala Conflict Data Program
  * API: https://ucdp.uu.se/apidocs/
  * UCDP/PRIO Armed Conflict Dataset - at least one state actor
  * UCDP/PRIO Dyadic Dataset - IDK...
  * UCDP NonState Conflict Dataset - nonstate
  * UCDP One-sided Violence Dataset - govts or organized groups on civilians
  * UCDP Battle-Related Deaths Dataset - number of deaths in conflicts appearing in UCDP/PRIO Armed Conflict Dataset
* GDELT (access with BigQuery or download CSV)
  * https://www.gdeltproject.org/
  * "GDELT provides the ultimate mappable database of global conflict translating the world’s textual news reports into quantitative spreadsheet entries each geocoded to the level of a specific city or landmark worldwide."
  * IDK how reliable this is - research further
## Current Sources
* IEA energy data
  * International Energy Administration, collects global energy data by country, region, and energy source
* Scripps CO2 Program - AKA The Keeling Curve
  * https://scrippsco2.ucsd.edu/data/atmospheric_co2/mlo.html
  * Atmospheric CO2 measurements
  * 1958 to present
  * Time Resolution: monthly, weekly, daily, every 10 minutes
  * Quality: these are direct measurements, and these data are considered by the American Chemical Society to be the ["authoritative record of atmospheric CO2 concentrations"](https://www.acs.org/content/acs/en/education/whatischemistry/landmarks/keeling-curve.html)
  * 3242 rows in weekly data set
* IPCC temperature data
  * temperature vs cumulative CO2 emissions from 1850 to 2019 
    * Figure SPM.10 - data located in /data/IPCC/Figure_SPM10_Near_linear_relationship_btwn_cumulative_co2_emissions_and_increase_in_global_surface_temp/Top_panel_HISTORY.csv
    * 170 rows - actually in columns, will need to transpose I think
  * temperature over time 
    * Figure SPM.1 - the right panel has from 1850 to 2020 observed, simulated natural only, and simulated natural plus human caused warming
    * do we want to include any simulations? IDK...
* BP Statistical Review of World Energy
  * Historical energy consumption by country, year, and energy source
  * 1965 to present
  * [Data Set on bp.com](https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html)
* CDC Covid Cases and Deaths by State
  * [CDC Covid Cases and Deaths by State Landing Page](https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36/data)
  * Quality: these data rely on state health department reporting, so there could be variation in quality among the states. It might be worth looking at one or two states or even going to state health departments for data.  
* EIA Finished Gasoline Production - US Energy Information Administration
  * https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WGFRPUS2&f=W
  * US Refiner and Blender Adjusted Net Production of Finished Motor Gasoline
  * 1982 to present
  * Time Resolution: weekly
  * Quality: Not sure... US Government accounting of gasoline production seems legit but maybe we could find some citations or something. 
  * 2048 rows in data set
  * can we get global production data?
  * can we get data for all fossil fuels?
  * EIA Monthly Energy Review
* Historical data including energy production, consumption, net imports, and non-combustion use by source (petrolium, nat gas, coal, nuclear, etc)
  * Carbon dioxide emissions from energy consumption by source - in the "Environment" section
  * [EIA Monthly Energy Review Landing Page](https://www.eia.gov/totalenergy/data/monthly/index.php)

## Contributors
* Jennifer Long
* Danelle Cook
* Chineze Okpala
* Hari Somayajula
* Abishua Prashanth
* Randy Weaver
