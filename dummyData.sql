CREATE TABLE IF NOT EXISTS COUNTRY_MASTER(
	COUNTRY_ID INT,
	COUNTRY VARCHAR(25),
	REGION VARCHAR(20)
);

INSERT INTO COUNTRY_MASTER(COUNTRY_ID, COUNTRY, REGION)
VALUES (1, 'Algeria', 'Africa'),
	(2, 'Brazil', 'SAmerica'),
	(3, 'Ireland', 'Europe'),
	(4, 'US', 'NAmerica');

CREATE TABLE IF NOT EXISTS FUEL_CONSUMPTION(
	COUNTRY_ID INT,
	COUNTRY VARCHAR(25),
	FUEL_TYPE VARCHAR(20),
	CONSUMPTION_VALUE DOUBLE PRECISION
);

INSERT INTO FUEL_CONSUMPTION(COUNTRY_ID, COUNTRY, FUEL_TYPE, CONSUMPTION_VALUE)
VALUES (1, 'Algeria', 'Gas', 1.36521),
	(2, 'Brazil', 'Gas', 1.545715),
	(3, 'Ireland', 'Gas', 0.157549),
	(4, 'US', 'Gas', 26.76886),
	(1, 'Algeria', 'Ethanol', 5.83159),
	(2, 'Brazil', 'Ethanol', 6.32743),
	(3, 'Ireland', 'Ethanol', 2.53187),
	(4, 'US', 'Ethanol', 11.23651),
	(1, 'Algeria', 'Coal', 0.005568),
	(2, 'Brazil', 'Coal', 0.73792),
	(3, 'Ireland', 'Coal', 0.091819),
	(4, 'US', 'Coal', 15.58468),
	(1, 'Algeria', 'Biodiesel', 0.984652),
	(2, 'Brazil', 'Biodiesel', 1.299179),
	(3, 'Ireland', 'Biodiesel', 1.11368),
	(4, 'US', 'Biodiesel', 1.861788);

CREATE TABLE IF NOT EXISTS FUEL_PRODUCTION(
COUNTRY_ID INT,
COUNTRY VARCHAR(25),
FUEL_TYPE VARCHAR(20),
PRODUCTION_VALUE DOUBLE PRECISION
);

INSERT INTO FUEL_PRODUCTION(COUNTRY_ID, COUNTRY, FUEL_TYPE, PRODUCTION_VALUE)
VALUES (1, 'Algeria', 'Gas', 2.930801),
	(2, 'Brazil', 'Gas', 0.856962),
	(3, 'Ireland', 'Gas', 0.681521),
	(4, 'US', 'Gas', 26.65092),
	(1, 'Algeria', 'Ethanol', 4.521684),
	(2, 'Brazil', 'Ethanol', 6.243279),
	(3, 'Ireland', 'Ethanol', 1.562354),
	(4, 'US', 'Ethanol', 11.92982),
	(1, 'Algeria', 'Coal', 0.216584),
	(2, 'Brazil', 'Coal', 0.121682),
	(3, 'Ireland', 'Coal', 0.56843),
	(4, 'US', 'Coal', 17.98743),
	(1, 'Algeria', 'Biodiesel', 1.65424),
	(2, 'Brazil', 'Biodiesel', 1.29603),
	(3, 'Ireland', 'Biodiesel', 0.98426),
	(4, 'US', 'Biodiesel', 1.574253);

CREATE TABLE IF NOT EXISTS GDP(
COUNTRY_ID INT,
COUNTRY VARCHAR(25),
GDP_VALUE DOUBLE PRECISION
);

INSERT INTO GDP(COUNTRY_ID, COUNTRY, GDP_VALUE)
VALUES (1, 'Algeria', 145009.18),
	(2, 'Brazil', 1444733.26),
	(3, 'Ireland', 425888.95),
	(4, 'US', 20893746);

SELECT * FROM COUNTRY_MASTER;

SELECT * FROM FUEL_CONSUMPTION;

SELECT * FROM FUEL_PRODUCTION;

SELECT * FROM GDP;