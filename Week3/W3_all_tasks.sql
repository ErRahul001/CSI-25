--task 1 : Query all columns for all rows from the table CITY
select * from CITY
--task 2 : Query all the cities with ID = 1661 from the table CITY
select * from CITY where ID = 1661
--task 3 : Query name of empoloyees from the EMPLOYEE table and order them alphabatically
select name from Employee order by name asc
--task 4 : Query all the attributes for the  japanese cities
select * from CITY where COUNTRYCODE = "JPN"
--task 5 : Query a list of cities and states from the table STATION
select CITY, STATE from STATION
--task 6 : Query a list of CITY names from STATION for cities that have an even ID number. Avoid duplicates.
select distinct CITY from STATION where (ID%2)=0
--task 7 : Query the difference between total number of cities and number of unique cities present in table STATION.
select((select count(CITY) from STATION)-(select count(distinct(city)) from STATION))
/*task 8 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
(i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes 
first when ordered alphabetically.*/
SELECT CITY, LENGTH(CITY) AS LENGTH FROM STATION
ORDER BY LENGTH ASC, CITY
LIMIT 1;
SELECT CITY, LENGTH(CITY) AS LENGTH FROM STATION
ORDER BY LENGTH DESC, CITY
LIMIT 1;
--task 9 : Query the average population for all cities in CITY, rounded down to the nearest integer.
select floor(avg(POPULATION)) from CITY
/*task 10 : Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent)
and their respective average city populations (CITY.Population) rounded down to the nearest integer.*/
select COUNTRY.CONTINENT, floor(avg(CITY.POPULATION)) 
from CITY join COUNTRY on COUNTRY.CODE = CITY.COUNTRYCODE 
group by COUNTRY.CONTINENT;