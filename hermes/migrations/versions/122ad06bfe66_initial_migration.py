"""empty message

Revision ID: 122ad06bfe66
Revises: c2f6d3e11658
Create Date: 2021-01-21 22:40:01.356804

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

from hermes.models import Status


# revision identifiers, used by Alembic.
revision = "122ad06bfe66"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hermes_messagequeue",
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.Column(
            "uuid", sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False
        ),
        sa.Column("scheduled_to", sa.DateTime(), nullable=False),
        sa.Column("sender", sa.String(length=100), nullable=False),
        sa.Column("recipient", sa.String(length=100), nullable=False),
        sa.Column("content", sa.Text(), nullable=True),
        sa.Column(
            "status", sqlalchemy_utils.types.choice.ChoiceType(Status), nullable=False
        ),
        sa.Column("status_message", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_table(
        "hermes_messagequeuehistory",
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("updated", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "message_uuid",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            nullable=True,
        ),
        sa.Column("scheduled_to", sa.DateTime(), nullable=False),
        sa.Column("sender", sa.String(length=100), nullable=False),
        sa.Column("recipient", sa.String(length=100), nullable=False),
        sa.Column("content", sa.Text(), nullable=True),
        sa.Column(
            "status", sqlalchemy_utils.types.choice.ChoiceType(Status), nullable=False
        ),
        sa.Column("status_message", sa.String(length=200), nullable=True),
        sa.ForeignKeyConstraint(
            ["message_uuid"],
            ["hermes_messagequeue.uuid"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("hermes_messagequeuehistory")
    op.drop_table("hermes_messagequeue")
    # ### end Alembic commands ###
