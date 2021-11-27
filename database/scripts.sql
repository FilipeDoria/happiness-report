--a) What was the happiest country each year (year, country)?
SELECT survey_yr, country, ROUND(score,2)
FROM happiness
WHERE _rank = 1
ORDER BY survey_yr ASC;

--b) What was the average happiness each year (year, happiness)?
SELECT survey_yr, ROUND(AVG(score),2)
FROM happiness
GROUP BY survey_yr
ORDER BY survey_yr ASC;

--c) In which position was Portugal in the happiness index each year (year, position)?
SELECT survey_yr, country, _rank, ROUND(score,2)
FROM happiness
WHERE country = 'Portugal'
ORDER BY survey_yr ASC;

--d) What is the average happiness of the 10 countries with the higher GDP in each year
--(year, happiness)?
SELECT survey_yr, ROUND(AVG(score),2) happiness
FROM (
     (SELECT survey_yr, gdp, country, score
      FROM happiness
      WHERE survey_yr = 15
      ORDER BY gdp DESC
      LIMIT 10)
     UNION
     (SELECT survey_yr, gdp, country, score
      FROM happiness
      WHERE survey_yr = 16
      ORDER BY gdp DESC
      LIMIT 10)
     UNION
     (SELECT survey_yr, gdp, country, score
      FROM happiness
      WHERE survey_yr = 17
      ORDER BY gdp DESC
      LIMIT 10)
     UNION
     (SELECT survey_yr, gdp, country, score
      FROM happiness
      WHERE survey_yr = 18
      ORDER BY gdp DESC
      LIMIT 10)
     UNION
     (SELECT survey_yr, gdp, country, score
      FROM happiness
      WHERE survey_yr = 19
      ORDER BY gdp DESC
      LIMIT 10)
     ) as "yearly"
GROUP BY survey_yr
ORDER BY survey_yr ASC;

--What about the lower GDP?
SELECT survey_yr, ROUND(AVG(score),2) happiness
FROM (
         (SELECT survey_yr, gdp, country, score
          FROM happiness
          WHERE survey_yr = 15
          ORDER BY gdp ASC
          LIMIT 10)
         UNION
         (SELECT survey_yr, gdp, country, score
          FROM happiness
          WHERE survey_yr = 16
          ORDER BY gdp ASC
          LIMIT 10)
         UNION
         (SELECT survey_yr, gdp, country, score
          FROM happiness
          WHERE survey_yr = 17
          ORDER BY gdp ASC
          LIMIT 10)
         UNION
         (SELECT survey_yr, gdp, country, score
          FROM happiness
          WHERE survey_yr = 18
          ORDER BY gdp ASC
          LIMIT 10)
         UNION
         (SELECT survey_yr, gdp, country, score
          FROM happiness
          WHERE survey_yr = 19
          ORDER BY gdp ASC
          LIMIT 10)
     ) as "yearly"
GROUP BY survey_yr
ORDER BY survey_yr ASC;

--e) What are the three countries with a greater improvement in the happiness index
-- during the years (notice that we can have more years than those in the dataset)
-- present in the database (country, improvement)?
SELECT country_name, hp1,year1,hp2, year2, hp2-hp1 as dev_index
FROM
(select country_name, happiness_score as hp1, year as year1
    from score  where year=2015
) As Tab1
 INNER JOIN
(select country_name, happiness_score as hp2,year as year2
    from score  where year=2019
) As Tab2
USING(country_name)
order by dev_index desc
limit 3


--experiments for e)
SELECT MIN(survey_yr), MAX(survey_yr)
FROM (
SELECT DISTINCT survey_yr
FROM happiness ) as years

SELECT

SELECT *
FROM happiness
ORDER BY country ASC, survey_yr ASC


SELECT survey_yr, country, score max_score
FROM happiness
WHERE survey_yr = (
    SELECT MAX(survey_yr) as survey_yr
    FROM (
        SELECT DISTINCT survey_yr
        FROM happiness
        ) as years
    )
UNION
SELECT survey_yr, country, score min_score
FROM happiness
WHERE survey_yr = (
    SELECT MIN(survey_yr) as survey_yr
    FROM (
             SELECT DISTINCT survey_yr
             FROM happiness
         ) as years
)

SELECT country, ROUND(MAX(score)-MIN(score),3) improvment
FROM happiness
GROUP BY country
ORDER BY country ASC

-- What about those that had the larger regression in the index?

-- Extra points: Think of other interesting questions to ask!