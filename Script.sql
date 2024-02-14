
create table if not exists Genre(
id serial primary key,
name varchar(40) not null
);

create table if not exists Artist(
id serial primary key,
name varchar(25) not null,
genre_id integer references Genre(id));

create table if not exists Albums(
id serial primary key,
name varchar(30) not null,
released date
);

create table if not exists Songs(
id serial primary key,
name varchar(40) NOT NULL,
duration integer
);

create table if not exists Collection(
id serial primary key,
name varchar(35) not null,
released date
);

create table if not exists ArtistGenres(
id serial primary key,
artist_id integer references Artist(id),
genre_id integer references Genre(id)
);

create table if not exists AlbumsArtists(
id serial primary key,
albums_id integer references Albums(id),
artist_id integer references Artist(id)
);