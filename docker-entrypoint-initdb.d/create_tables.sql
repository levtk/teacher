CREATE TABLE IF NOT EXISTS "public"."instructors" (
    "id" uuid NOT NULL,
    "first_name" character varying NOT NULL,
    "second_name" character varying NOT NULL,
    "third_name" character varying,
    "fourth_name" character varying,
    "phone" character varying NOT NULL,
    "email" character varying NOT NULL,
    "whatsapp" character varying,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "country" integer NOT NULL,
    "subscription_plan" character varying NOT NULL,
    "created" date NOT NULL,
    "updated" timestamp NOT NULL,
    CONSTRAINT "instructors_id" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "instructors_email" ON "public"."instructors" USING btree ("email");


CREATE TABLE IF NOT EXISTS "public"."users" (
    "first_name" character varying NOT NULL,
    "second_name" character varying NOT NULL,
    "third_name" character varying,
    "fourth_name" character varying,
    "user_type" character varying NOT NULL,
    "email" character varying NOT NULL,
    "phone" character varying NOT NULL,
    "whatsapp" character varying,
    "instructor_name" character varying NOT NULL,
    "city" character varying NOT NULL,
    "state" character varying NOT NULL,
    "country" character varying NOT NULL,
    "post_code" character varying NOT NULL,
    "created" date NOT NULL,
    "updated" timestamp NOT NULL,
    "id" uuid NOT NULL,
    "instructor_id" uuid NOT NULL,
    CONSTRAINT "users_id" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "users_instructor_id" ON "public"."users" USING btree ("instructor_id");