"""added currency

Revision ID: 06a006f6fb8f
Revises: b3d3b8a4dd6e
Create Date: 2023-01-30 11:52:20.432070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06a006f6fb8f'
down_revision = 'b3d3b8a4dd6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_countries')
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country_currency', sa.String(), nullable=True))
        batch_op.drop_column('description')
        batch_op.drop_column('best_hotels')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('best_hotels', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('country_currency')

    op.create_table('_alembic_tmp_countries',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('country_currency', sa.VARCHAR(), nullable=False),
    sa.Column('country_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('capital_name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('official_language', sa.VARCHAR(length=50), nullable=False),
    sa.Column('filename', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
