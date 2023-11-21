drop_table_fact = "Drop table if exists fact"
drop_table_dimention_person = "Drop table if exists person_dimension"
drop_table_dimension_episode = "Drop table if exists episode_dimension"
drop_table_dimension_award = "Drop table if exists award_dimension"

create_fact_table = """ Create table fact (
                                           episode_id varchar,
                                           name varchar
                                           ) diststyle all  """
create_dimention_person = """Create table person_dimension (
                                                           name varchar sortkey,
                                                           birth_date varchar,
                                                           birth_name varchar,
                                                           birth_place varchar,
                                                           birth_region varchar,
                                                           birth_country varchar,
                                                           height_meters varchar,
                                                           nickname varchar,
                                                           episode_id varchar,
                                                           category text,
                                                           person text,
                                                           role text,
                                                           credited text 
                                                           )diststyle even """
create_dimension_episode = """Create table episode_dimension (
                                                               episode_id varchar sortkey,
                                                               season int,
                                                               episode int,
                                                               number_in_series int,
                                                               title text,
                                                               summary text,
                                                               air_date date,
                                                               episode_image text,
                                                               rating float,
                                                               votes int,
                                                               keyword text
                                                              ) diststyle even"""
create_dimension_award = """Create table award_dimension (
                                                         award_id int ,
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
                                                         )diststyle even"""

insert_into_fact = """Insert into fact (episode_id,name) 
                                  Select e.episode_id as episode_id , p.name as name
                                  From episode e join award a ON a.episode_id = a.episode_id
                                  join person p on p.name = a.person 
                   """
insert_into_dimension_person = """Insert into person_dimension (name ,birth_date ,birth_name ,birth_place ,birth_region,
                                                                birth_country ,height_meters ,nickname ,episode_id ,
                                                                category ,person ,role ,credited)
                                              select  p.name as name ,p.birth_date as birth_date,p.birth_name as birth_name ,
                                                      p.birth_place as birth_place, p.birth_region as birth_region ,
                                                      p.birth_country as birth_country, p.height_meters as height_meters,
                                                      p.nickname as nickname, c.episode_id as episode_id ,c.category as category ,
                                                      c.person as person ,c.role as role ,c.credited as credited       
                                              From person p join credit c ON p.name = c.person            
                               """
insert_into_dimension_episode = """Insert into episode_dimension (episode_id ,season , episode ,number_in_series ,
                                                                  title ,summary ,air_date ,episode_image ,rating ,
                                                                  votes ,keyword )
                                               select  k.episode_id as episode_id ,e.season as season,e.episode as episode ,
                                                       e.number_in_series as number_in_series,e.title as title,
                                                       e.summary as summary,e.air_date as air_date ,
                                                       e.episode_image as episode_image,e.rating as rating ,
                                                       e.votes as votes ,k.keyword as keyword  
                                               From episode e full join keyword k on e.episode_id = k.episode_id
                                """
insert_into_dimension_award = """Insert into award_dimension(award_id ,organization ,year ,award_category ,
                                                             award ,person ,role ,episode_id ,season ,song ,result)
                                             select award_id ,organization ,year ,award_category ,award ,person ,
                                                    role ,episode_id ,season ,song ,result
                                             From award       
                               """

tables = ['fact','person_dimension','episode_dimension','award_dimension']
create_tables = [create_fact_table,create_dimention_person,create_dimension_episode,create_dimension_award]
insert_into_tables = [insert_into_fact,insert_into_dimension_person,insert_into_dimension_episode,\
                      insert_into_dimension_award]
drop_tables = [drop_table_fact,drop_table_dimention_person ,drop_table_dimension_episode,drop_table_dimension_award ]