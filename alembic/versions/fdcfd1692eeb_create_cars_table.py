"""create cars_table

Revision ID: fdcfd1692eeb
Revises: 
Create Date: 2024-04-25 10:55:59.837179

"""
from typing import Sequence

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdcfd1692eeb'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("cars",
                    sa.Column("id",sa.Integer, primary_key=True, autoincrement=True ),
                    sa.Column("vin", sa.Text, nullable=False), 
                    sa.Column("model", sa.Text, nullable=False), 
                    sa.Column("make",sa.Text, nullable=False ), 
                    sa.Column("engine", sa.Text, nullable=False), 
                    sa.Column("year", sa.Integer))
    
    op.create_table("dealerships",
                    sa.Column("id",sa.Integer, primary_key=True, autoincrement=True ),
                    sa.Column("name", sa.Text, nullable=False), 
                    sa.Column("address", sa.Text, nullable=False), 
                    sa.Column("phone_number",sa.Text, nullable=False ))
                    
    op.create_table("inventory",
                sa.Column("car_id", sa.Integer,sa.ForeignKey("cars.id"),  primary_key=True),
                sa.Column("dealer_id",sa.Integer, sa.ForeignKey("dealerships.id"), primary_key=True), 
                sa.Column("cost", sa.Float, nullable=False), 
                sa.Column("is_solid", sa.Boolean, nullable=False),
                sa.PrimaryKeyConstraint("car_id", "dealer_id"))

def downgrade() -> None:
    op.drop_table("cars")
    op.drop_table("dealerships")
    op.drop_table("inventory")