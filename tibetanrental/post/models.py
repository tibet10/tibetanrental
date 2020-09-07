
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..database import Base

metadata = Base.metadata

class Amenity(Base):
    __tablename__ = 'amenities'

    id = Column(Integer, primary_key=True, server_default=text("nextval('amenities_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    createDate = Column(DateTime(True), nullable=False)
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))