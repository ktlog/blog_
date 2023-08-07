"""deleted unique on username

Revision ID: 79cd163ecf50
Revises: 98e6a0307696
Create Date: 2023-01-15 18:53:55.962827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79cd163ecf50'
down_revision = '98e6a0307696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_username_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint('user_username_key', ['username'])

    # ### end Alembic commands ###