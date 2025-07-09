from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker
import pandas as pd
Base = declarative_base()

engine = create_engine("mysql+pymysql://root:cop2805@localhost:3306/seminar_project")

class WaitTime(Base):
    __tablename__ = "Wait_Times"

    id = Column("ID",Integer,primary_key=True)
    theme_park = Column("Theme Park", String)
    land = Column("Land",String)
    attraction_name = Column("Attraction",String)
    is_open = Column("Is Open", Boolean)
    wait_time = Column("Wait Time", Integer)
    update_time = Column("updated",DateTime)

    def __init__(self,id,theme_park,land,ride_name,is_open,wait_time,updated):
        self.id = id
        self.theme_park = theme_park
        self.land = land
        self.ride_name = ride_name
        self.is_open = is_open
        self.wait_time = wait_time
        self.updated = updated

    def data_to_mysql(data,table_name):
        data.to_sql(table_name,engine,if_exists='append',index=False)

