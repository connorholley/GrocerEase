CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE ingredient_categories (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY
);

CREATE TYPE UNIT_TYPE AS ENUM (
    'gram',
    'milliliter'
);

CREATE TABLE pantry_items (
    id SERIAL PRIMARY KEY,
    ingredient_id INT REFERENCES ingredients(id),
    amount INT,
    unit UNIT_TYPE
);

CREATE TABLE ingredient_category_relationships (
    ingredient_id INT,
    ingredient_category_id INT,
    PRIMARY KEY (ingredient_id, ingredient_category_id)
);

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    instructions TEXT[],
    description TEXT
);

CREATE TABLE recipe_ingredient_relationships (
    recipe_id INT,
    ingredient_id INT,
    PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE user_recipe_relationships (
    user_id INT,
    recipe_id INT,
    PRIMARY KEY (user_id, recipe_id)
);
