REATE TABLE "age_rating" (
  "id" SERIAL CONSTRAINT "pk_age_rating" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "min_age" INTEGER
);

CREATE TABLE "customer" (
  "id" SERIAL CONSTRAINT "pk_customer" PRIMARY KEY,
  "fisrt_name" TEXT NOT NULL,
  "last_name" TEXT NOT NULL,
  "email" TEXT NOT NULL,
  "address" TEXT NOT NULL,
  "phone" TEXT NOT NULL,
  "family" BOOLEAN,
  "blacklisted" BOOLEAN
);

CREATE TABLE "genre" (
  "genre_id" SERIAL CONSTRAINT "pk_genre" PRIMARY KEY,
  "name" TEXT NOT NULL,
  "desccription" TEXT NOT NULL
);

CREATE TABLE "movie" (
  "id" SERIAL CONSTRAINT "pk_movie" PRIMARY KEY,
  "genre" INTEGER NOT NULL,
  "age__rating" INTEGER NOT NULL,
  "name" TEXT NOT NULL,
  "length" INTEGER,
  "producer" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "poster" TEXT NOT NULL,
  "year" DATE NOT NULL
);

CREATE INDEX "idx_movie__age__rating" ON "movie" ("age__rating");

CREATE INDEX "idx_movie__genre" ON "movie" ("genre");

ALTER TABLE "movie" ADD CONSTRAINT "fk_movie__age__rating" FOREIGN KEY ("age__rating") REFERENCES "age_rating" ("id");

ALTER TABLE "movie" ADD CONSTRAINT "fk_movie__genre" FOREIGN KEY ("genre") REFERENCES "genre" ("genre_id");

CREATE TABLE "shelve" (
  "id" SERIAL CONSTRAINT "pk_shelve" PRIMARY KEY,
  "rack" INTEGER,
  "max_capacity" INTEGER
);

CREATE TABLE "dvd" (
  "id" SERIAL CONSTRAINT "pk_dvd" PRIMARY KEY,
  "movie" INTEGER NOT NULL,
  "shelve" INTEGER NOT NULL
);

CREATE INDEX "idx_dvd__movie" ON "dvd" ("movie");

CREATE INDEX "idx_dvd__shelve" ON "dvd" ("shelve");

ALTER TABLE "dvd" ADD CONSTRAINT "fk_dvd__movie" FOREIGN KEY ("movie") REFERENCES "movie" ("id");

ALTER TABLE "dvd" ADD CONSTRAINT "fk_dvd__shelve" FOREIGN KEY ("shelve") REFERENCES "shelve" ("id");

CREATE TABLE "customer_dvds" (
  "customer" INTEGER NOT NULL,
  "dvd" INTEGER NOT NULL,
  CONSTRAINT "pk_customer_dvds" PRIMARY KEY ("customer", "dvd")
);

CREATE INDEX "idx_customer_dvds" ON "customer_dvds" ("dvd");

ALTER TABLE "customer_dvds" ADD CONSTRAINT "fk_customer_dvds__customer" FOREIGN KEY ("customer") REFERENCES "customer" ("id");

ALTER TABLE "customer_dvds" ADD CONSTRAINT "fk_customer_dvds__dvd" FOREIGN KEY ("dvd") REFERENCES "dvd" ("id")

