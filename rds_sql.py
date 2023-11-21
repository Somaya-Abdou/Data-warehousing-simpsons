drop_award= """Drop table if exists award"""
drop_credit = """Drop table if exists credit"""
drop_episode = """Drop table if exists episode"""
drop_keyword = """Drop table if exists keyword"""
drop_person = """Drop table if exists person"""
drop_vote = """Drop table if exists vote"""

create_table_person = """Create table if not exists person(
                                                                    name varchar primary key,
                                                                    birth_date varchar,
                                                                    birth_name varchar,
                                                                    birth_place varchar,
                                                                    birth_region varchar,
                                                                    birth_country varchar,
                                                                    height_meters float,
                                                                    nickname varchar                                                                   
                                                                    )"""
create_table_award = """Create table if not exists award (
                                                                  award_id int primary key,
                                                                  organization text,
                                                                  year int,
                                                                  award_category text,
                                                                  award varchar,
                                                                  person varchar,
                                                                  role text,
                                                                  episode_id varchar(12),
                                                                  season text,
                                                                  song text,
                                                                  result text
                                                                  )"""
create_table_episode = """Create table if not exists episode(
                                                                     episode_id varchar primary key,
                                                                     season int,
                                                                     episode int,
                                                                     number_in_series int,
                                                                     title text,
                                                                     summary text,
                                                                     air_date date,
                                                                     episode_image text,
                                                                     rating float,
                                                                     votes int
                                                                     ) """
create_table_credit = """Create table if not exists credit (
                                                                episode_id varchar,
                                                                category text,
                                                                person text,
                                                                role text,
                                                                credited text,
                                                                CONSTRAINT fk_episode_id
                                                                  FOREIGN KEY(episode_id) 
                                                                  REFERENCES episode(episode_id)
                                                                  ON DELETE CASCADE
                                                                ) """

create_table_keyword = """Create table if not exists keyword(
                                                                     episode_id varchar,
                                                                     keyword text,
                                                                     CONSTRAINT fk_episode_id
                                                                       FOREIGN KEY(episode_id) 
                                                                       REFERENCES episode(episode_id)
                                                                       ON DELETE CASCADE 
                                                                     )"""
create_table_vote = """Create table vote(
                                                 episode_id varchar,
                                                 stars int,
                                                 votes int,
                                                 percent float,
                                                 CONSTRAINT fk_episode_id3
                                                    FOREIGN KEY(episode_id) 
                                                    REFERENCES episode(episode_id)
                                                    ON DELETE CASCADE
)"""

insert_into_person = """Insert into person(name ,birth_date ,birth_name ,birth_place ,birth_region ,
                                           birth_country ,height_meters ,nickname )
                                           values(%s,%s,%s,%s,%s,%s,%s,%s)"""
insert_into_award = """Insert into award (award_id ,organization ,year ,award_category ,
                                          award ,person ,role ,episode_id ,season ,song ,result)
                                          values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                                   ON CONFLICT (award_id) DO NOTHING """
insert_into_episode = """Insert into episode (episode_id ,season ,episode ,number_in_series ,
                                              title ,summary ,air_date ,episode_image ,rating ,votes)
                                              values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
insert_into_credit = """Insert into credit (episode_id ,category ,person ,role ,credited)
                                            values (%s,%s,%s,%s,%s) """
insert_into_keyword = """Insert into keyword(episode_id , keyword)
                                             values(%s,%s)"""

insert_into_vote = """Insert into vote(episode_id ,stars ,votes ,percent)
                                      values(%s,%s,%s,%s)"""  

drop_tables = [drop_award,drop_credit,drop_keyword,drop_person,drop_vote,drop_episode] 

create_tables = [create_table_person,create_table_award,create_table_episode,create_table_credit,\
                 create_table_keyword,create_table_vote]   
   
insert_into_tables = [insert_into_person,insert_into_award,insert_into_episode,insert_into_credit,\
                      insert_into_keyword,insert_into_vote]                                                      