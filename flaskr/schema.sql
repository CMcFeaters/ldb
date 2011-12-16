drop table if exists entries;
crate table entries(
	id integer primary key autoincrement,
	title string not null,
	text string not null
);