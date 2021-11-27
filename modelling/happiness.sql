-- SQL Modelling https://app.quickdatabasediagrams.com/#/

CREATE TABLE "Country" (
    "country_name" text   NOT NULL,
    "region" text   NOT NULL,
    "population" int   NOT NULL,
    "area" int   NOT NULL,
    "infant_mortality" int   NOT NULL,
    "literacy" int   NOT NULL,
    CONSTRAINT "pk_Country" PRIMARY KEY (
        "country_name"
     )
);

CREATE TABLE "Score" (
    "country_name" text   NOT NULL,
    "GDP" money   NOT NULL,
    "happiness_score" int   NOT NULL,
    "year" SMALLINT   NOT NULL,
    UNIQUE (country_name, year)
);

ALTER TABLE "Score" ADD CONSTRAINT "fk_Score_country_name" FOREIGN KEY("country_name")
REFERENCES "Country" ("country_name");
