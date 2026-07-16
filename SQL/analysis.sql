SELECT COUNT(*) AS total_records
FROM crypto_prices;

SELECT MAX(price) AS highest_price
FROM crypto_prices;

SELECT MIN(price) AS lowest_price
FROM crypto_prices;

SELECT AVG(price) AS average_price
FROM crypto_prices;

SELECT *
FROM crypto_prices
LIMIT 10;