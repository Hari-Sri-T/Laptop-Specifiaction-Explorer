
use MySqlProject;

CREATE TABLE Laptop (
    laptop_id INT PRIMARY KEY AUTO_INCREMENT,
    model VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    rating INT,
    primary_storage_type VARCHAR(50),
    primary_storage_capacity INT,
    secondary_storage_type VARCHAR(50),
    secondary_storage_capacity INT,
    touch_screen BOOLEAN,
    display_size DECIMAL(5, 2),
    resolution_width INT,
    resolution_height INT,
    os VARCHAR(100),
    year_warranty INT,
    brand_id INT,
    gpu_id INT,
    category_id INT,
    processor_id INT,
    FOREIGN KEY (brand_id) REFERENCES Brand(brand_id),
    FOREIGN KEY (gpu_id) REFERENCES GPU(gpu_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    FOREIGN KEY (processor_id) REFERENCES Processor(processor_id)
);

CREATE TABLE Brand (
    brand_id INT PRIMARY KEY AUTO_INCREMENT,
    brand_name VARCHAR(100) NOT NULL
);

CREATE TABLE Processor (
    processor_id INT PRIMARY KEY AUTO_INCREMENT,
    processor_name VARCHAR(255) NOT NULL,
    processor_tier VARCHAR(50),
    no_core INT,
    no_threads INT
);

CREATE TABLE GPU (
    gpu_id INT PRIMARY KEY AUTO_INCREMENT,
    gpu_brand VARCHAR(100),
    gpu_type VARCHAR(100)
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE StagingLaptops (
    index_ int primary key,
    brand VARCHAR(255),
    model VARCHAR(255),
    price DECIMAL(10, 2),
    rating INT,
    processor_brand VARCHAR(255),
    processor_tier VARCHAR(255),
    num_cores INT,
    num_threads INT,
    ram_memory INT,
    primary_storage_type VARCHAR(50),
    primary_storage_capacity INT,
    secondary_storage_type VARCHAR(50),
    secondary_storage_capacity INT,
    gpu_brand VARCHAR(255),
    gpu_type VARCHAR(50),
    is_touch_screen BOOLEAN,
    display_size DECIMAL(4, 2),
    resolution_width INT,
    resolution_height INT,
    os VARCHAR(50),
    year_of_warranty INT
);

LOAD DATA INFILE " " -- put the file path here to the csv file
INTO TABLE StagingLaptops
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(index_, brand, model, price, rating, processor_brand, processor_tier, num_cores, num_threads, ram_memory, primary_storage_type, primary_storage_capacity, secondary_storage_type, secondary_storage_capacity, gpu_brand, gpu_type, is_touch_screen, display_size, resolution_width, resolution_height, os, year_of_warranty);


select * from staginglaptops;
INSERT INTO Brand (brand_name)
SELECT DISTINCT brand
FROM staginglaptops;

INSERT INTO Processor (processor_name, processor_tier, no_core, no_threads)
SELECT DISTINCT processor_brand, processor_tier, num_cores, num_threads
FROM staginglaptops;

INSERT INTO GPU (gpu_brand, gpu_type)
SELECT DISTINCT gpu_brand, gpu_type
FROM staginglaptops;

INSERT INTO Category (category_name)
SELECT DISTINCT primary_storage_type AS category_name
FROM staginglaptops;

INSERT INTO Laptop (model, price, rating, primary_storage_type, primary_storage_capacity, secondary_storage_type, secondary_storage_capacity, touch_screen, display_size, resolution_width, resolution_height, os, year_warranty, brand_id, gpu_id, category_id, processor_id)
SELECT 
    Model, 
    Price, 
    Rating, 
    primary_storage_type, 
    primary_storage_capacity, 
    secondary_storage_type, 
    secondary_storage_capacity, 
    is_touch_screen, 
    display_size, 
    resolution_width, 
    resolution_height, 
    OS, 
    year_of_warranty, 
    (SELECT brand_id FROM Brand WHERE brand_name = staginglaptops.brand LIMIT 1) AS brand_id,
    (SELECT gpu_id FROM GPU WHERE gpu_brand = staginglaptops.gpu_brand AND gpu_type = staginglaptops.gpu_type LIMIT 1) AS gpu_id,
    (SELECT category_id FROM Category WHERE category_name = primary_storage_type LIMIT 1) AS category_id,
    (SELECT processor_id FROM Processor WHERE processor_name = staginglaptops.processor_brand AND processor_tier = staginglaptops.processor_tier LIMIT 1) AS processor_id
FROM staginglaptops;



select * from laptop;
select * from brand;
select * from gpu;
select * from category;
select * from processor;


-- Count of Laptops by Brand
SELECT b.brand_name, COUNT(l.laptop_id) AS laptop_count
FROM Brand b
LEFT JOIN Laptop l ON b.brand_id = l.brand_id
GROUP BY b.brand_id;

-- total count of laptops
select count(laptop_id) from laptop;

-- Average Rating of Laptops by Brand
SELECT b.brand_name, round(AVG(l.rating),1) AS average_rating
FROM Brand b
JOIN Laptop l ON b.brand_id = l.brand_id
GROUP BY b.brand_id;

-- Laptops with Higher than Average Price
SELECT model, price
FROM Laptop
WHERE price > (SELECT AVG(price) FROM Laptop)
order by price desc;

-- Laptops with lower than Average Price
SELECT model, price
FROM Laptop
WHERE price < (SELECT AVG(price) FROM Laptop)
order by price asc;

-- Laptops with lower than Average Price but above average rating
SELECT model, price, rating
FROM Laptop
WHERE price < (SELECT AVG(price) FROM Laptop)
  AND rating > (SELECT AVG(rating) FROM Laptop)
ORDER BY rating desc;


