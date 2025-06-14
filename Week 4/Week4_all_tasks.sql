/*task 1: Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u)
as both their first and last characters. Your result cannot contain duplicates.*/
select distinct CITY from STATION WHERE city RLIKE '^[aeiouAEIOU].*[aeiouAEIOU]$';

--task 2: Query the difference between the maximum and minimum populations in CITY.
select max(POPULATION)-min(POPULATION) from CITY;

--task 3: Calculate the Euclidean distance between two cities.
select round(sqrt(power(max(LAT_N) - min(LAT_N), 2) + power(max(LONG_W) - min(LONG_W), 2)), 4) FROM STATION;

--task 4: A median is defined as a number separating the higher half of a data set from the lower half.
--Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.
select ROUND(S1.LAT_N, 4) 
from STATION as S1 where (select ROUND(COUNT(S1.ID)/2) - 1 from STATION) = (select COUNT(S2.ID) from STATION AS S2 
where S2.LAT_N > S1.LAT_N); select cast(lat_n as decimal(10,4)) from
(select lat_n, row_number() over (order by lat_n desc) as rnum1 from station) t1
where rnum1 = (select case when max(rnum)%2=0 then max(rnum)/2
else max(rnum)/2+1 end from 
(select row_number() over (order by lat_n desc) as rnum from station) t)

--task 5 & 6: Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
SELECT CITY.NAME FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';

--task 7: The report
select case when Grade < 8 then null
else Students.Name
end as Name, Grades.Grade, Students.Marks from Students 
join Grades on Students.Marks between Grades.Min_Mark and Grades.Max_Mark
order by Grades.Grade desc,
case when Grades.Grade < 8 then Students.Marks
else Students.Name end; 

--task 8: Top Competitors
select Hackers.hacker_id, Hackers.name from Submissions as Submissions join Hackers
on Submissions.hacker_id = Hackers.hacker_id 
join Challenges on Submissions.challenge_id = Challenges.challenge_id
join Difficulty on Challenges.Difficulty_level = Difficulty.Difficulty_level
where Submissions.score = Difficulty.score 
group by Hackers.hacker_id, Hackers.name 
having count(*) > 1
order by count(*) desc, Hackers.hacker_id;

--task 9: Ollivander's Inventory
select w.id, p.age, w.coins_needed, w.power from Wands as w 
join Wands_Property as p
on w.code = p.code
where w.coins_needed = (select min(coins_needed) from Wands w2 inner join Wands_Property p2 
on w2.code = p2.code where p2.is_evil = 0 and p.age = p2.age and w.power = w2.power)
order by w.power desc, p.age desc;

--task 10: Contest Leaderboard
select m.hacker_id, h.name, sum(score) as total_score from
(select hacker_id, challenge_id, max(score) as score
from Submissions group by hacker_id, challenge_id) as m
join Hackers as h
on m.hacker_id = h.hacker_id
group by m.hacker_id, h.name
having total_score > 0
order by total_score desc, m.hacker_id;