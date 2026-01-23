# app/operations/trip_tracking/model.py

import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base

class TripLocation(Base):
    __tablename__ = "trip_locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trip_id = Column(UUID(as_uuid=True), ForeignKey("trips.id"), nullable=False)
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
