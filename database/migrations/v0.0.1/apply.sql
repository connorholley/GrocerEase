CREATE TABLE user (
	   id SERIAL PRIMARY KEY
	   , 
);

CREATE TYPE UNIT_TYPE AS ENUM (
	   'gram'
	   , 'milliliter'
);

CREATE TABLE pantry_item (
	   id SERIAL PRIMARY KEY
	   , ingredient_id int FOREIGN KEY ingredient(id)
	   , amount INT
	   , unit UNIT_TYPE
);

CREATE TABLE ingredient (
	   id SERIAL PRIMARY KEY
	   , name TEXT
);

CREATE TABLE ingredient_category_relationship (
	   ingredient_id INT
	   , ingredient_category_id INT
	   PRIMARY KEY (ingredient_id, ingredient_category_id)
);

CREATE TABLE ingredient_category (
	   id SERIAL PRIMARY KEY
	   , name TEXT
);

CREATE TABLE recipe (
	   id SERIAL PRIMARY KEY
	   , name TEXT
	   , instructions TEXT[]
	   , description TEXT
);

CREATE TABLE recipe_ingredient_relationship (
	   recipe_id int
	   , ingredient_id int
	   , PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE user_recipe_relationship (
	   user_id int
	   , recipe_id int
	   , PRIMARY KEY (user_id, recipe_id)
);


