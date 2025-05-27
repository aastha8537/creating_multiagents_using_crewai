from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


blog_researcher=Agent(
    role ="blog researcher from yt videos",
    goal="get the relevent video content from topic {topic} from yt channel",
    verbose=True,
    memory=True,
    backstory="Expert in understanding videos in AI Data science, Machine Learning and GENAI providing Suggesstion.",
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)
blog_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the videos{topic} from yt channel",
    verbose=True,
    memory=True,
    backstory="with a flair for simplifying complex topics,you craft engaging narratives that capativate and educate,bringing new discoveries to light in an accesible manners.",
    tools=[yt_tool],
     llm=llm,
    allow_delegation=False
)