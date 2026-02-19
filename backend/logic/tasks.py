# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


"""
Creating Tasks Cheat Sheet
Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.

Break down the outcome into actionable tasks, assigning each task to the appropriate agent.

Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:

Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:

Identify the Desired Outcome: Define what success looks like for your project.

Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.

Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

Task Description Template
Use this template as a guide to define each task in your CrewAI application. This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of the project.

Template:

Python
def [task_name](self, agent, [parameters]):
    return Task(description=dedent(f'''
        **Task**: [Provide a concise name or summary of the task.]
        **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected deliverables.]

        **Parameters**:
        - [Parameter 1]: [Description]
        - [Parameter 2]: [Description]
        ... [Add more parameters as needed.]

        **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or specific constraints.]
    '''), agent=agent)
"""
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Develop a 7-Day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, and 
                a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, and 
                actual restaurants to go to.
                
                CRITICAL: YOU ONLY HAVE ACCESS TO THE 'search_internet' AND 'calculate' TOOLS. DO NOT INVENT OTHER TOOLS.

                IMPORTANT: Your final answer must contain ONLY the Markdown itinerary. Do not include search queries, 
                tool tags, or internal thoughts.
                
                **Parameters**:
                - City: {city}
                - Trip Date: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {self.__tip_section()}
            """),
            expected_output="A complete 7-day travel itinerary in Markdown format with daily schedules and budget breakdown.",
            agent=agent,
            tools=[SearchTools.search_internet, CalculatorTools.calculate] 
        )

    def identify_city(self, agent, origin, cities, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Identify the Best City for the Trip
                **Description**: Analyze and select the best city for the trip based on specific criteria 
                such as weather patterns, seasonal events, and travel costs. Your final answer 
                must be a detailed report on the chosen city, including actual flight costs, weather 
                forecast, and attractions.
                
                CRITICAL: YOU ONLY HAVE ACCESS TO THE 'search_internet' TOOL. USE IT TO FIND THE WEATHER AND FLIGHTS. DO NOT INVENT OTHER TOOLS.

                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Interests: {interests}
                - Travel Date: {travel_dates}

                **Note**: {self.__tip_section()}
            """),
            expected_output="Detailed report on the chosen city including weather and flight costs.",
            agent=agent,
            tools=[SearchTools.search_internet]
        )
    
    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(f"""
                **Task**: Gather In-depth City Guide Information
                **Description**: Compile an in-depth guide for the selected city, gathering information about key 
                attractions, local customs, special events, and daily activity recommendations.
                
                CRITICAL: YOU ONLY HAVE ACCESS TO THE 'search_internet' TOOL. DO NOT INVENT OTHER TOOLS.

                **Parameters**:
                - Cities: {city}
                - Interests: {interests}
                - Travel Date: {travel_dates}

                **Note**: {self.__tip_section()}
            """),
            expected_output="Comprehensive city guide with hidden gems, attractions, and average daily costs.",
            agent=agent,
            tools=[SearchTools.search_internet]
        )