/*

INSTRUCTIONS: Execute these queries to create a new "salad database" and populate it with data.

DBMS: MySQL

SOURCE: https://github.com/gwu-business/salad-system-py/tree/master/database

*/


/* MIGRATE SALAD DATABASE (CREATE TABLES) */

DROP TABLE IF EXISTS `menu_items`;
CREATE TABLE `menu_items` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `category` varchar(255) NOT NULL,
    `title` varchar(255) NOT NULL,
    `calories` int(11) NOT NULL,
    `gluten_free` tinyint(1),
    `vegan_safe` tinyint(1),
    `description` text NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

/* POPULATE SALAD DATABASE WITH DATA */

INSERT INTO menu_items (`category`,`title`,`calories`,`gluten_free`,`vegan_safe`,`description`)
VALUES
  ('SeasonalSalad', 'KALE YEAH',  540, 0, 1,  'a kale-based salad.'),
  ('SignatureGrain', 'NEWTON',    720, 1, 0,  'quinoa + farro, organic arugula, tomatoes, raw corn, organic chickpeas, spicy broccoli, organic white cheddar, roasted chicken, pesto vinaigrette.')
;

SELECT * FROM menu_items;
