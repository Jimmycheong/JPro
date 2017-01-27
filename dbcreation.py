from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm	import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#===##===##===##===##===##===##===#
#MODELS TABLE  
#===##===##===##===##===##===##===#

class Models(Base):
	__tablename__ = 'models'

	id = Column(Integer, primary_key = True)
	name = Column(String(10), nullable = False)
	parts = Column(String(200))

#===##===##===##===##===##===##===#
#PARTS TABLE  
#===##===##===##===##===##===##===#

class Parts(Base):
	__tablename__ = 'Parts'

	id = Column(Integer, primary_key = True)
	name = Column(String(10))
	models = Column(String(80))
	processes = Column(String(80))

#===##===##===##===##===##===##===#
#PROCESSES TABLE  
#===##===##===##===##===##===##===#

class Processes(Base):
	__tablename__ = 'processes'

	id = Column(Integer, primary_key = True)
	name = Column(String(10))
	dictionary = {} 

#===##===##===##===##===##===##===#
#DATABASE BUILDER  
#===##===##===##===##===##===##===#

engine = create_engine('sqlite:///complete.db')
Base.metadata.create_all(engine) 