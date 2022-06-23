from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost/prueba_tecnica")

meta = MetaData()

conn = engine.connect()