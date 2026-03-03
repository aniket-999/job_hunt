import asyncio
import uuid
import sys
from pathlib import Path

# Add parent directory to path so imports work
sys.path.insert(0, str(Path(__file__).parent.parent))

from job_assistant.core.database import AsyncSessionLocal
from job_assistant.core.model import Job, Resume, Application
from resume.resume_builder import build_resume
from resume.latex_compiler import compile_latex

async def run():
    async with AsyncSessionLocal() as session:

        job = Job(
            company="Atlassian",
            role="Backend Engineer",
            location="Bangalore",
            job_url="https://example.com/job1"
        )

        session.add(job)
        await session.commit()
        await session.refresh(job)

        context = {
            "name": "Your Name",
            "email": "you@email.com"
        }

        latex_source = build_resume(context)
        pdf_path = compile_latex(str(job.id), latex_source)

        resume = Resume(
            job_id=job.id,
            latex_source=latex_source,
            pdf_path=pdf_path
        )

        session.add(resume)
        await session.commit()
        await session.refresh(resume)

        application = Application(
            job_id=job.id,
            resume_id=resume.id
        )

        session.add(application)
        await session.commit()

        print("Pipeline successful!")

asyncio.run(run())