-- Check if the database 'hbnb_dev_db' exists
SELECT COUNT(*) INTO @db_exists
FROM information_schema.schemata
WHERE schema_name = 'hbnb_dev_db';

-- If 'hbnb_dev_db' doesn't exist, create it
IF @db_exists = 0 THEN
    CREATE DATABASE hbnb_dev_db;
    GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
END IF;

-- Check if the user 'hbnb_dev' exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE user = 'hbnb_dev';

-- If 'hbnb_dev' doesn't exist, create it and grant privileges
IF @user_exists = 0 THEN
    CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
    GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
    GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
    FLUSH PRIVILEGES;
END IF;
