import os
from crewai import Agent, LLM
from textwrap import dedent

from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

from dotenv import load_dotenv
load_dotenv()


"""
Creating Agents Cheat Sheet:

Think like a boss. Work backwards from the goal and think which employee you need to hire to get the job done.

Define the Captain of the crew who orient the other agents towards the goal.

Define which experts the captain needs to communicate with and delegate tasks to. Build a top down structure of the crew.

Goal:

Captain/Manager/Boss:


Employees/Experts to hire:

Notes:

Agents should be results driven and have a clear goal in mind

Role is their job title

Goals should actionable

Backstory should be their resume
"""


class TravelAgents:
    def __init__(self):
        self.groq_llm = LLM(
            model="groq/llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("Expert in travel planning and logistics."),
            goal=dedent("Create a 7-day itinerary with detailed per-day plans."),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            verbose=True,
            llm=self.groq_llm,
            allow_delegation=False,
            max_rpm=1 
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("Expert at picking ideal destinations."),
            goal=dedent("Select the best cities for travel."),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.groq_llm,
            allow_delegation=False,
            max_rpm=1 

        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("Local guide with deep city knowledge."),
            goal=dedent("Provide the BEST insights about the selected city."),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.groq_llm,
            allow_delegation=False,
            max_rpm=1 

        )