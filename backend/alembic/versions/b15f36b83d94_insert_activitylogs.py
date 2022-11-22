"""insert ActivityLogs

Revision ID: b15f36b83d94
Revises: 8fd8039afd96
Create Date: 2022-11-22 01:38:27.035317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15f36b83d94'
down_revision = '8fd8039afd96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for idx in range(0,1000000):
        op.execute(f"""INSERT INTO activity_logs("user_id", "post_id", "timestamp", interaction_type)
            values (
                (select ceil(RANDOM()*(select count(*) from users)::integer)),
                (select ceil(RANDOM()*(select count(*) from posts)::integer)),
                (select CAST( NOW() - INTERVAL '10 year' * RANDOM() AS TIMESTAMP)),
                (select (enum_range(null::interactiontype))[ceil(random()*2)])
                )""")


def downgrade() -> None:
    meta = sa.MetaData(bind=op.get_bind())
    users_tbl = sa.Table('alctivity_logs', meta)
    users_tbl.delete()
