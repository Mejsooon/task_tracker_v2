CREATE DATABASE IF NOT EXISTS task_tracker
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE task_tracker;

CREATE TABLE users (
    id          VARCHAR(10)  PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL
);


CREATE TABLE tasks (
    id                    VARCHAR(10)  PRIMARY KEY,
    user_id               VARCHAR(10)  NOT NULL,
    difficulty            TINYINT      NOT NULL CHECK (difficulty_level BETWEEN 1 AND 10),
    description           TEXT         NOT NULL,
    additional_notes      TEXT
    status                ENUM('active','completed') NOT NULL DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


INSERT INTO users (id, name, username, password)
VALUES ('U001', 'Jan Kowalski', 'user1', 'pass123');