"""insert data data

Revision ID: 744caedc8a7e
Revises: 7bb15d8550e2
Create Date: 2022-11-22 00:01:10.692023

"""
import os
import hashlib
import base64

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '744caedc8a7e'
down_revision = '7bb15d8550e2'
branch_labels = None
depends_on = None

GENERIC_PASSWORD = 'sonar1234'


def upgrade() -> None:
    meta = sa.MetaData(bind=op.get_bind())
    users_tbl = sa.Table('users', meta)
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', GENERIC_PASSWORD.encode('utf-8'), salt, 100000) 
    encodedSalt = base64.b64encode(salt)
    encodedKey = base64.b64encode(key)
    
    for x in range(1,1001):
        op.execute(f"INSERT INTO users (id,username,password,salt) VALUES ({x},'user{x}','{encodedKey.decode('utf-8')}','{encodedSalt.decode('utf-8')}')")

def downgrade() -> None:
    meta = sa.MetaData(bind=op.get_bind())
    users_tbl = sa.Table('users', meta)
    users_tbl.delete()
