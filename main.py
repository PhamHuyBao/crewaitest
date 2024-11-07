import os
from crewai import Crew
import tasks
import agents

# 0. Setup environment
from dotenv import load_dotenv
load_dotenv()

def main():
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY") # type: ignore

    job_application_crew = Crew(
        agents=[agents.researcher,
                agents.profiler,
                agents.resume_strategist,
                agents.interview_preparer],

        tasks=[tasks.research_task,
            tasks.profile_task,
            tasks.resume_strategy_task,
            tasks.interview_preparation_task],

        verbose=True
    )

    job_application_inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/PhamHuyBao',
        'personal_writeup': """Detail-oriented software developer with 1.5 year of experience specializing in JavaScript technologies. Skilled in building robust web applications using front-end technologies like JavaScript, React. I really want to sharpen my skill in frontend development and willing to learning any thing to produce better UI."""
    }

    result = job_application_crew.kickoff(inputs=job_application_inputs)

if __name__ == "__main__":
    main()