
-- Query 1
SELECT * FROM passengers
WHERE Age > 40;

-- Query 2
SELECT Sex, COUNT(*) AS Total
FROM passengers
GROUP BY Sex;

-- Query 3
SELECT Pclass, AVG(Fare) AS AvgFare
FROM passengers
GROUP BY Pclass
HAVING AvgFare > 30;

-- Query 4
SELECT Name, Fare
FROM passengers
ORDER BY Fare DESC
LIMIT 10;

-- Query 5
SELECT *
FROM passengers
WHERE Sex='female'
AND Survived=1;

-- Query 6
SELECT *
FROM passengers
WHERE Age BETWEEN 20 AND 30;
