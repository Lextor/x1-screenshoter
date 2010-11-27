ALTER TABLE `screenshot_screenshotfile` MODIFY COLUMN `unique_hash` varchar(16) NOT NULL UNIQUE;


BEGIN;CREATE TABLE `news_news` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(100) NOT NULL,
    `slug` varchar(50) NOT NULL,
    `chortext` longtext NOT NULL,
    `text` longtext NOT NULL,
    `publisher_id` integer NOT NULL,
    `published` bool NOT NULL,
    `date_published` date NOT NULL
)
;
ALTER TABLE `news_news` ADD CONSTRAINT `publisher_id_refs_id_6d930764` FOREIGN KEY (`publisher_id`) REFERENCES `auth_user` (`id`);COMMIT;