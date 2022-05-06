CREATE TABLE user_states(
    username VARCHAR(15) NOT NULL, -- twitter user associated 
    evolution int NOT NULL DEFAULT 0, -- index of filepath in a string[] handled by server application
    
    last_interaction DATE DEFAULT GETDATE(), -- date the user last interacted directly with the bot
    CONSTANT creation_date DATE DEFAULT GETDATE(), -- date user entered into database

    fav_food VARCHAR(20) DEFUALT 'cheese', -- bot fav food for later image recog
    hated_food VARCHAR(20) DEFUALT 'sand',    -- least favorite of above

    persistent_sentiment DOUBLE NOT NULL DEFAULT 0.5, -- saved sentiment state of bot, averaged over past K interactions [0,1] 1 is happiest
    hunger DOUBLE NOT NULL DEFAULT 0.0, -- scale [0, 1] of hunger. 1 is most hungry. 0 is just fed
    playfulness DOUBLE NOT NULL DEFAULT 0.5, -- how much the bot wants the user to interact with it 

    interactions_counter INT NOT NULL DEFAULT 1,
    
    CONSTRAINT user_states_pk PRIMARY KEY (username), -- twitter @s are all unique. sufficient PK. surrogate not chosen as only single table in database ; repetition not an issue
    CONSTRAINT CHECK 0.0 <= hunger AND hunger <= 1.0, -- enforce range
    CONSTRAINT CHECK 0.0 <= playfulness AND playfulness <= 1.0, -- enforce range
    CONSTRAINT CHECK 0.0 <= persistent_sentiment AND persistent_sentiment <= 1.0, -- enforce range

);

INSERT INTO user_states( username, evolution, fav_food, hated_food, persistent_sentiment, hunger, playfulness)
    VALUES ('rawbarobx', 1, 'steak', 'rock', 0.99, 0.85, 0.2);
#