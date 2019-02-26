"""add bio,profile_pic

Revision ID: 49f67f146a83
Revises: c38441f17589
Create Date: 2019-02-22 17:18:21.789156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49f67f146a83'
down_revision = 'c38441f17589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###
