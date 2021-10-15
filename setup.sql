CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT DEFAULT NULL,
    active BOOLEAN DEFAULT 1);


CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate VARCHAR(10) NOT NULL,
    v_type  VARCHAR(45) NOT NULL,
    color VARCHAR(45) NOT NULL,
    parking_spot_no INTEGER,
    description TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id)
);