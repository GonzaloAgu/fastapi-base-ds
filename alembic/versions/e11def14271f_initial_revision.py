"""initial_revision

Revision ID: e11def14271f
Revises: 
Create Date: 2024-09-08 22:01:01.870901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e11def14271f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_mascotas_id', table_name='mascotas')
    op.drop_index('ix_mascotas_nombre', table_name='mascotas')
    op.drop_table('mascotas')
    op.drop_index('ix_personas_email', table_name='personas')
    op.drop_index('ix_personas_id', table_name='personas')
    op.drop_index('ix_personas_nombre', table_name='personas')
    op.drop_table('personas')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('fecha_creacion', sa.DATETIME(), nullable=False),
    sa.Column('fecha_modificacion', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_personas_nombre', 'personas', ['nombre'], unique=False)
    op.create_index('ix_personas_id', 'personas', ['id'], unique=False)
    op.create_index('ix_personas_email', 'personas', ['email'], unique=1)
    op.create_table('mascotas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(), nullable=False),
    sa.Column('tipo', sa.VARCHAR(), nullable=False),
    sa.Column('tutor_id', sa.INTEGER(), nullable=False),
    sa.Column('fecha_creacion', sa.DATETIME(), nullable=False),
    sa.Column('fecha_modificacion', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['tutor_id'], ['personas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_mascotas_nombre', 'mascotas', ['nombre'], unique=False)
    op.create_index('ix_mascotas_id', 'mascotas', ['id'], unique=False)
    # ### end Alembic commands ###
