from sqlalchemy import Table, Column, Integer, String
from src.model.settings.metadata import metadata

# by default slqalchemy requires a schema/table mirroring the class name,
# in this case, it would be "user" (lowercase) as the table name,
# but we can change it by passing the table name as a parameter to the Table function   
user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(255), nullable=True),
    Column("age", Integer),
    Column("uf", String),

)