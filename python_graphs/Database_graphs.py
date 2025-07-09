import matplotlib.pyplot as plt
from sqlalchemy import Column,Integer,String,Sequence,Boolean,DateTime,create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import pandas as pd
import numpy as np

mysql = create_engine("mysql+pymysql://root:cop2805@localhost:3306/seminar_project")

Session = sessionmaker(bind=mysql)
session = Session()

Base = declarative_base()

class WaitTime(Base):
    __tablename__ = "Wait_Times"

    id = Column("ID",Integer,primary_key=True)
    theme_park = Column("Theme Park", String)
    land = Column("Land",String)
    attraction_name = Column("Attraction",String)
    is_open = Column("Is Open", Boolean)
    wait_time = Column("Wait Time", Integer)
    update_time = Column("updated",DateTime)

""" wait_time = session.query(WaitTime).filter(WaitTime.attraction_name.like('Guardians of the Galaxy: Cosmic Rewind')).all()
print(wait_time)

df = pd.DataFrame(wait_time)

 for index,row in df.iterrows():

  print(f"Name: {row['Attraction']} Wait time: {row['Wait Time']}")

for index in range(len(df)):
    print(f"Name: {df.loc[index, 'attraction_name']} Wait time: {df.loc[index, 'wait_time']}") """
  

query = """
SELECT *
FROM wait_times
WHERE Attraction = %s AND updated LIKE %s;
"""

""" AND updated LIKE %s """

attraction_name = "TRON Lightcycle / Run"
date = "2025-06-16%"

data = pd.read_sql(
    query,
    mysql,
    params=(attraction_name,date))

#print(data.head(90))

plt.figure(figsize=(12,4))
plt.subplots_adjust(
    wspace=0.3,  # Increase horizontal space
    hspace=0.5,  # Increase vertical space
    left=0.067,    # Increase left margin
    right=0.976,   # Keep right margin
    top=0.936,     # Keep top margin
    bottom=0.264   # Keep bottom margin
)
plt.grid(True)
x_lable = [f"{str(x)[10:19]}" for x in data['updated']]

x_positions = np.arange(len(x_lable))

plt.xticks(x_positions,x_lable,rotation=90)

plt.plot(data['updated'],data['Wait Time'])  
plt.title(f'{attraction_name} - {date[0:10]}')
plt.xlabel('Time of day')
plt.ylabel('Wait time')
plt.savefig(f'{attraction_name}{date[0:10]}.png',dpi=200,bbox_inches='tight')
plt.show()
