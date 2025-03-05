from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SeleniumScrapingTool
from crewai_tools import WebsiteSearchTool

@CrewBase
class CrewAutomationIaLinkSearchCrew():
    """CrewAutomationIaLinkSearch crew"""

    @agent
    def figma_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['figma_extractor'],
            tools=[SeleniumScrapingTool()],
        )

    @agent
    def content_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['content_parser'],
            tools=[],
        )

    @agent
    def post_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['post_creator'],
            tools=[],
        )

    @agent
    def audience_searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['audience_searcher'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def outreach_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['outreach_coordinator'],
            tools=[],
        )


    @task
    def extract_figma_data(self) -> Task:
        return Task(
            config=self.tasks_config['extract_figma_data'],
            tools=[SeleniumScrapingTool()],
        )

    @task
    def parse_figma_content(self) -> Task:
        return Task(
            config=self.tasks_config['parse_figma_content'],
            tools=[],
        )

    @task
    def create_social_media_post(self) -> Task:
        return Task(
            config=self.tasks_config['create_social_media_post'],
            tools=[],
        )

    @task
    def search_french_audience(self) -> Task:
        return Task(
            config=self.tasks_config['search_french_audience'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def distribute_post(self) -> Task:
        return Task(
            config=self.tasks_config['distribute_post'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CrewAutomationIaLinkSearch crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
