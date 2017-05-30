"""empty message

Revision ID: 9b1a6cbc314d
Revises: 
Create Date: 2017-05-30 02:27:36.922958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b1a6cbc314d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('face_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upload_ip', sa.String(length=15), nullable=True),
    sa.Column('upload_time', sa.DateTime(), nullable=True),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('format', sa.String(length=5), nullable=True),
    sa.Column('face_box_x', sa.Float(), nullable=True),
    sa.Column('face_box_y', sa.Float(), nullable=True),
    sa.Column('face_box_w', sa.Float(), nullable=True),
    sa.Column('face_box_h', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('analysis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=15), nullable=True),
    sa.Column('user_grade', sa.Integer(), nullable=True),
    sa.Column('grade_1', sa.Float(), nullable=True),
    sa.Column('grade_2', sa.Float(), nullable=True),
    sa.Column('grade_3', sa.Float(), nullable=True),
    sa.Column('grade_4', sa.Float(), nullable=True),
    sa.Column('model_id', sa.String(length=15), nullable=True),
    sa.Column('face_image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['face_image_id'], ['face_image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analysis')
    op.drop_table('face_image')
    # ### end Alembic commands ###