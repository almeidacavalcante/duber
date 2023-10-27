drop schema duber cascade;

create schema duber;

create table duber.account (
	account_id uuid,
	name text,
	email text,
	cpf text,
	car_plate text,
	is_passenger boolean,
	is_driver boolean,
	date timestamp,
	is_verified boolean,
	verification_code uuid
);

create table duber.ride (
	ride_id uuid,
	passenger_id uuid,
	driver_id uuid,
	status text,
	fare numeric,
	distance numeric,
	from_lat numeric,
	from_long numeric,
	to_lat numeric,
	to_long numeric,
	date timestamp
);