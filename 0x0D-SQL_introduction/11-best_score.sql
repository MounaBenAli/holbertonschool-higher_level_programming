-- lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
-- Results should display both the score and the name (in this order)
SELECT score, name FROM second_table ORDER BY score DESC WHERE score >= 10;
