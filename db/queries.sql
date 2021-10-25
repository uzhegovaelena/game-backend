CREATE TABLE users
(
	user_id serial,
	email varchar (128) UNIQUE NOT NULL,

	CONSTRAINT PK_users_user_id PRIMARY KEY(user_id)
);

CREATE TABLE games
(
	game_id serial,
	game_name varchar (128) DEFAULT 'game1',
	user_id integer,
	start_game timestamp DEFAULT current_timestamp,

	CONSTRAINT PK_games_game_id PRIMARY KEY(game_id),
	CONSTRAINT FK_game_users FOREIGN KEY(user_id) REFERENCES users(user_id)
);
