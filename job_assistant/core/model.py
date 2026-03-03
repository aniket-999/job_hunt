import uuid
from sqlalchemy import Column, String, Float, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company = Column(String(200), nullable=False)
    role = Column(String(200), nullable=False)
    location = Column(String(200))
    jd_text = Column(Text)
    job_url = Column(Text, unique=True, nullable=False)
    experience_required = Column(Float)
    estimated_ctc = Column(Float)
    match_score = Column(Float)
    selected = Column(Boolean, default=False)

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"))
    latex_source = Column(Text, nullable=False)
    pdf_path = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Application(Base):
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"))
    resume_id = Column(UUID(as_uuid=True), ForeignKey("resumes.id"))
    stage = Column(String(50), default="pending")
    notes = Column(Text)