

DROP DATABASE IF EXISTS LIBRARY_MANAGEMENT;
CREATE DATABASE LIBRARY_MANAGEMENT;

CREATE TABLE EMPLOYEE (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(250) NOT NULL,
    email       VARCHAR(250) NOT NULL UNIQUE,
    password    VARCHAR(75) NOT NULL,
    active      BOOLEAN NOT NULL DEFAULT TRUE,
    created_on  DATE DEFAULT NOW()
);


CREATE TABLE STUDENT (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(250) NOT NULL,
    email       VARCHAR(250) NOT NULL UNIQUE,
    reg_no      VARCHAR(75) NOT NULL,
    active      BOOLEAN NOT NULL DEFAULT TRUE,
    created_on  DATE DEFAULT NOW(),
    created_by  INTEGER REFERENCES EMPLOYEE
);

CREATE TABLE BOOKS (
    id                  SERIAL PRIMARY KEY,
    title               VARCHAR(250) NOT NULL,
    author              VARCHAR(250) NOT NULL UNIQUE,
    total_copies        INTEGER NOT NULL,
    available_copies    INTEGER NOT NULL,
    bought_on           DATE DEFAULT NOW(),
    created_by          INTEGER REFERENCES EMPLOYEE NOT NULL
);

CREATE TABLE BORROWEDBOOKS (
    student_id          INTEGER NOT NULL,
    book_id             INTEGER NOT NULL,
    issued_date         DATE DEFAULT NOW(),
    return_date         DATE,
    due_date            DATE,
    emp_id              INTEGER REFERENCES EMPLOYEE NOT NULL
);