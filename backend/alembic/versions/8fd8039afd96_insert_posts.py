"""insert posts

Revision ID: 8fd8039afd96
Revises: 744caedc8a7e
Create Date: 2022-11-22 00:53:20.312114

"""
from alembic import op
import sqlalchemy as sa

from faker import Faker
fake = Faker()

# revision identifiers, used by Alembic.
revision = '8fd8039afd96'
down_revision = '744caedc8a7e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    
    for x in range(1,1001):
        for post in range(1,21):
            date = fake.date_time_between(start_date='-10y', end_date='now')
            op.execute(f"""INSERT INTO posts (title, description, "imageSrc", created, owner_id) 
                        VALUES ('{fake.text()}','{fake.paragraph()}','https://picsum.photos/200', '{date}','{x}')""")

def downgrade() -> None:
    meta = sa.MetaData(bind=op.get_bind())
    users_tbl = sa.Table('posts', meta)
    users_tbl.delete()
