from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, String

engine = create_engine("postgresql://postgres:Jeganchaela1011@localhost:5432/accounts")
meta = MetaData()


accounts = Table(
   'accounts', meta, 
   Column('username', String, primary_key = True), 
   Column('password', String),
   Column('email',String),
)
meta.create_all(engine)


