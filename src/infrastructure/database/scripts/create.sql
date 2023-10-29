create database duber_db;

delete schema public cascade;
create schema public;

-- create schema duber;
--
-- create table duber.accounts (
-- 	account_id uuid,
-- 	name text,
-- 	email text,
-- 	cpf text,
-- 	car_plate text,
-- 	is_passenger boolean,
-- 	is_driver boolean,
-- 	date timestamp,
-- 	is_verified boolean,
-- 	verification_code uuid
-- );
--
-- create table duber.rides (
-- 	ride_id uuid,
-- 	passenger_id uuid,
-- 	driver_id uuid,
-- 	status text,
-- 	fare numeric,
-- 	distance numeric,
-- 	from_lat numeric,
-- 	from_long numeric,
-- 	to_lat numeric,
-- 	to_long numeric,
-- 	date timestamp
-- );