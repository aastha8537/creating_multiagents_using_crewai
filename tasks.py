from crewai import Task
from tools import yt_tool 
from agents import blog_researcher,blog_writer

research_task=Task(
    description=(
        "identify the video{topic}"
        "get detailed information about the video from the channel."
    ),
    expected_output="A comprehensive 3 paragraph long report based on the {topic}of video content",
    tools=[yt_tool],
    agent=blog_researcher
)
writer_task=Task(
    description=(
        "get the information from the youtube channel on the topic{topic}"
    ),
    expected_output="summarize the information from the youtube channel video on the topic{topic} and create the content for the blog.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)
