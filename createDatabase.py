from sqlalchemy import create_engine
import pandas as pd
import numpy as np

def create_db(DB_USER,DB_KEY,DB_NAME):
    
    #from postgres_key import DB_USER,DB_KEY,DB_NAME
    bp_data=pd.read_csv('FinalDataFiles\\bp2021consolidateddataset.csv')
    #Create list of metrics that are to be used for analysis
    AnalysisMetrics=['biodiesel_cons_pj','biodiesel_prod_pj','biofuels_cons_ej','biofuels_prod_pj','co2_mtco2','coalcons_ej',
                'coalprod_ej','ethanol_cons_pj','ethanol_prod_pj','gascons_ej','gasprod_ej','oilcons_ej','oilprod_kbd']
    
    #Filter BP data to have data for just the metrics identified above
    bp_data=bp_data[bp_data['Var'].isin(AnalysisMetrics)]
    #Remove rows which have NULL value for Country IDs, i.e remove regions,continents consolidated data
    bp_data=bp_data[bp_data['ISO3166_numeric'].notnull()]

    #Create Countries Dataset
    #Create a countries data frame using the distinct values of countries in BP data
    countries_df=bp_data[['ISO3166_numeric','Country','Region']].drop_duplicates()
    countries_df.reset_index(inplace=True,drop=True)
    #Rename Columns
    countries_df.rename(columns={'ISO3166_numeric':'country_id','Country':'country','Region':'region'},inplace=True)
    #Create connection to postgres DB
    engine=create_engine(f'postgresql://{DB_USER}:{DB_KEY}@localhost:5432/{DB_NAME}')
    #Drop table if it exits
    engine.execute('DROP TABLE IF EXISTS COUNTRY_MASTER')
    #Create table if it does not exist
    engine.execute('CREATE TABLE IF NOT EXISTS COUNTRY_MASTER(COUNTRY_ID INT,COUNTRY VARCHAR(25),REGION VARCHAR(20))')
    #insert data into country_master table
    countries_df.to_sql('country_master',engine,if_exists='append',index=False)
    bp_data.reset_index(inplace=True,drop=True)

    #----------------------Create Consumption Dataset----------------

    #Create DF with all consumption metrics in BP data
    consumption_df=bp_data[bp_data['Var'].isin(['biodiesel_cons_pj','biofuels_cons_ej','coalcons_ej','ethanol_cons_pj'
                                    ,'gascons_ej','oilcons_ej'])]
    consumption_df.reset_index(inplace=True,drop=True)
    pd.set_option('mode.chained_assignment',None)
    #Create a Range of years for every decade
    consumption_df['year_range']=["1965-1975" if x<1975 else "1975-1985" if x<1985 
                              else "1985-1995" if x<1995 else "1995-2005" if x<2005 
                              else "2005-2015" if x<2015 else "2015-2020" for x in consumption_df['Year'] ]
    #1 ej=1000 pj, converting pj units to ej for biodiesel
    consumption_df['Value']=np.where((consumption_df.Var=='biodiesel_cons_pj'),consumption_df.Value*0.001,consumption_df.Value)
    #Replace the converted 'biodiesel_cons_pj'with 'biodiesel_cons_ej'
    consumption_df['Var'].replace('biodiesel_cons_pj','biodiesel_cons_ej',inplace=True)
    #1 ej=1000 pj, converting pj units to ej for ethanol
    consumption_df['Value']=np.where((consumption_df.Var=='ethanol_cons_pj'),consumption_df.Value*0.001,consumption_df.Value)
    #Replace the converted 'ethanol_cons_pj'with 'ethanol_cons_ej'
    consumption_df['Var'].replace('ethanol_cons_pj','ethanol_cons_ej',inplace=True)
    consumption_df=consumption_df[['ISO3166_numeric','Country','Year','year_range','Var','Value']]
    consumption_df.rename(columns={'ISO3166_numeric':'country_id','Country':'country','Year':'year',
                              'Var':'fuel_type','Value':'consumption_value'},inplace=True)
    #Drop table if it exits
    engine.execute('DROP TABLE IF EXISTS FUEL_CONSUMPTION')
    #Create table if it does not exist
    engine.execute('CREATE TABLE IF NOT EXISTS FUEL_CONSUMPTION(COUNTRY_ID INT,COUNTRY VARCHAR(25),YEAR INT,YEAR_RANGE VARCHAR(12),\
              FUEL_TYPE VARCHAR(20),CONSUMPTION_VALUE DOUBLE PRECISION)')
    consumption_df.to_sql('fuel_consumption',engine,if_exists='append',index=False)


    #-------------------------Create Production Dataset----------------------------
    #Create DF with all production metrics in BP data
    production_df=bp_data[bp_data['Var'].isin(['biodiesel_prod_pj','biofuels_prod_pj','coalprod_ej','ethanol_prod_pj'
                                        ,'gasprod_ej','oilprod_kbd'])]
    production_df.reset_index(inplace=True,drop=True)
    #Create a Range of years for every decade
    production_df['year_range']=["1965-1975" if x<1975 else "1975-1985" if x<1985 
                              else "1985-1995" if x<1995 else "1995-2005" if x<2005 
                              else "2005-2015" if x<2015 else "2015-2020" for x in production_df['Year'] ]
    #1 ej=1000 pj, converting pj units to ej for biodiesel
    production_df['Value']=np.where((production_df.Var=='biodiesel_prod_pj'),production_df.Value*0.001,production_df.Value)
    #Replace the converted 'biodiesel_prod_pj'with 'biodiesel_prod_ej'
    production_df['Var'].replace('biodiesel_prod_pj','biodiesel_prod_ej',inplace=True)
    #1 ej=1000 pj, converting pj units to ej for biofuel
    production_df['Value']=np.where((production_df.Var=='biofuels_prod_pj'),production_df.Value*0.001,production_df.Value)
    #Replace the converted 'biofuels_prod_pj'with 'biofuels_prod_ej'
    production_df['Var'].replace('biofuels_prod_pj','biofuels_prod_ej',inplace=True)
    #1 ej=1000 pj, converting pj units to ej for ethanol
    production_df['Value']=np.where((production_df.Var=='ethanol_prod_pj'),production_df.Value*0.001,production_df.Value)
    #Replace the converted 'ethanol_prod_pj'with 'ethanol_prod_ej'
    production_df['Var'].replace('ethanol_prod_pj','ethanol_prod_ej',inplace=True)
    #1kilo barrel per day =1*1000*365 barrels per year
    #1 barrel of oil = 6.2 Gigajoules(GJ)
    #1 GJ=0.000000001 EJ
    production_df['Value']=np.where((production_df.Var=='oilprod_kbd')
                                    ,production_df.Value*1000*365*6.12*0.000000001,production_df.Value)
    #Replace the converted 'oilprod_kbd'with 'oilprod_ej'
    production_df['Var'].replace('oilprod_kbd','oilprod_ej',inplace=True)
    production_df=production_df[['ISO3166_numeric','Country','Year','year_range','Var','Value']]
    production_df.rename(columns={'ISO3166_numeric':'country_id','Country':'country','Year':'year',
                              'Var':'fuel_type','Value':'production_value'},inplace=True)
    #Drop table if it exits
    engine.execute('DROP TABLE IF EXISTS FUEL_PRODUCTION')
    #Create table if it does not exist
    engine.execute('CREATE TABLE IF NOT EXISTS FUEL_PRODUCTION(COUNTRY_ID INT,COUNTRY VARCHAR(25),YEAR INT,YEAR_RANGE VARCHAR(12),\
              FUEL_TYPE VARCHAR(20),PRODUCTION_VALUE DOUBLE PRECISION)')
    production_df.to_sql('fuel_production',engine,if_exists='append',index=False)

    #-------------------------------------------Create Co2Emission Dataset--------------------------------------
    co2emission_df=bp_data[bp_data['Var']=='co2_mtco2']
    co2emission_df.reset_index(inplace=True,drop=True)
    #Calculate Year Range
    co2emission_df['year_range']=["1965-1975" if x<1975 else "1975-1985" if x<1985 
                              else "1985-1995" if x<1995 else "1995-2005" if x<2005 
                              else "2005-2015" if x<2015 else "2015-2020" for x in co2emission_df['Year'] ]
    #Select needed columns and rename them as needed
    co2emission_df=co2emission_df[['ISO3166_numeric','Country','Year','year_range','Var','Value']]
    co2emission_df.rename(columns={'ISO3166_numeric':'country_id','Country':'country','Year':'year',
                                'Var':'fuel_type','Value':'emission_value'},inplace=True)
    engine.execute('DROP TABLE IF EXISTS CO2_EMISSION')
    #Create table if it does not exist
    engine.execute('CREATE TABLE IF NOT EXISTS CO2_EMISSION(COUNTRY_ID INT,COUNTRY VARCHAR(25),YEAR INT,YEAR_RANGE VARCHAR(12),\
              FUEL_TYPE VARCHAR(20),EMISSION_VALUE DOUBLE PRECISION)')
    co2emission_df.to_sql('co2_emission',engine,if_exists='append',index=False)

    
    #------------------------------Create GDP Dataset based on World Bank Data--------------------------------------------
    wb_gdp=pd.read_csv('FinalDataFiles\\WorldBank_GDP.csv',skiprows=4)
    #Convert GPD by year in Columns to Rows i.e Pivot data
    gdp=wb_gdp.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'],var_name='Year',
            value_vars=[str(x) for x in np.arange(1960,2020)],value_name='GDP')
    #Selcted needed columns
    gdp=gdp[['Country Name','Country Code','Year','GDP']]
    #Drop countires and years which do not have GDP data
    gdp.dropna(inplace=True)
    #Get country dataset from BP Data
    country_code=bp_data[['ISO3166_numeric','ISO3166_alpha3','Country']].drop_duplicates()
    country_code.reset_index(inplace=True,drop=True)
    # Merge gdp dand country data(from BP) and get country ID.
    #Get GPD pnly for those countries that exist in BP data set
    final_gdp=gdp.merge(country_code,how='inner',left_on='Country Code',right_on='ISO3166_alpha3')
    final_gdp=final_gdp[['Country','ISO3166_numeric','Year','GDP',]]
    #Convert Year to Number
    final_gdp['Year']=pd.to_numeric(final_gdp['Year'])
    final_gdp['year_range']=["1965-1975" if x<1975 else "1975-1985" if x<1985 
                              else "1985-1995" if x<1995 else "1995-2005" if x<2005 
                              else "2005-2015" if x<2015 else "2015-2020" for x in final_gdp['Year'] ]
    final_gdp=final_gdp[['ISO3166_numeric','Country','Year','year_range','GDP']]
    final_gdp.rename(columns={'ISO3166_numeric':'country_id','Country':'country','Year':'year','GDP':'gdp'},inplace=True)
    # 1Billion$=1000000000, Converting GDP is US$ to US$(in Billions)
    final_gdp['gdp']=final_gdp['gdp']/1000000000
    #Drop table if it exits
    engine.execute('DROP TABLE IF EXISTS GDP')
    #Create table if it does not exist
    engine.execute('CREATE TABLE IF NOT EXISTS GDP(COUNTRY_ID INT,COUNTRY VARCHAR(25),YEAR INT,YEAR_RANGE VARCHAR(12),\
              GDP DOUBLE PRECISION)')
    final_gdp.to_sql('gdp',engine,if_exists='append',index=False)
    return














    
