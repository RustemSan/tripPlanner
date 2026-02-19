🌍 AI Autonomous Travel Concierge
Multi-Agent Orchestration with CrewAI, Llama 3.1 & FastAPI
This project is an advanced Agentic AI system that automates the end-to-end travel planning process. It utilizes a team of specialized AI agents that reason, collaborate, and use real-world tools (Search, Calculator) to deliver verified, high-precision 7-day itineraries.

🧠 System Architecture & ML Logic
The core of the system is a Sequential Multi-Agent Workflow. Unlike static chatbots, this architecture breaks down complex requests into sub-tasks, ensuring each stage is handled by a specialized expert agent to maintain context and accuracy.

🤖 The Agentic Crew
City Selection Expert: Analyzes climate data, flight availability from the origin, and traveler interests to select the optimal destination.

Local Tour Guide: A "Knowledge Retrieval" specialist that performs deep-web research to find hidden gems, local customs, and real-time events.

Expert Travel Agent: The "Executive Agent" that synthesizes all gathered data into a structured, budget-aware Markdown itinerary.

🛠️ Tool Grounding & Retrieval
Agents are equipped with autonomous tools to "ground" their responses in real-world data:

Search Tool: Custom integration with Serper API for real-time Google Search indexing.

Calculator Tool: A Python-based validator that allows agents to perform precise arithmetic for budget breakdowns, eliminating LLM math hallucinations.

🛡️ ML Engineering: Taming Hallucinations
A significant part of the development was focused on AI Reliability and ensuring consistent agent behavior.

Structural Hallucinations: Large models (like Llama 70B) occasionally hallucinate non-standard tool-calling tags (e.g., <function>). To mitigate this, the system utilizes Llama 3.1 8B-Instant for tool-heavy tasks due to its superior instruction-following in JSON schemas.

Content Quality (Anti-Lazy): To prevent superficial responses, specific Task Constraints were engineered into the prompts, mandating minimum word counts and actual verified names for hotels and restaurants.

Data Grounding: Agents are restricted from finalizing budget or logistical tasks without a mandatory Internet Search step, ensuring every price and flight cost is backed by real data.

🚥 Optimization & Infrastructure
Rate-Limit Management: To operate within Groq API constraints (6,000 TPM), the agents implement Request Throttling using max_rpm=1.

Connection Resilience: The Nginx and FastAPI layers are configured with a 300s timeout to support long-polling during intensive deep-research cycles.

Microservices Architecture: The entire stack—Frontend (React), Backend (FastAPI), and Nginx—is containerized via Docker Compose for seamless deployment and environment parity.

🛠 Technical Stack
AI Orchestration: CrewAI

Inference Engine: Groq (Llama 3.1 8B-Instant)

Backend: FastAPI (Asynchronous Python 3.12-slim)

Frontend: React + Vite

Infrastructure: Docker, Nginx

🚀 Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/RustemSan/tripPlanner.git
cd tripPlanner
Configure Environment:
Create a .env file in the root directory:

Fragment of code: 

GROQ_API_KEY=your_groq_api_key

SERPER_API_KEY=your_serper_api_key

Run with Docker:

Bash
docker-compose up --build
Access the Application:

Frontend: http://localhost:3000

API Docs (Swagger): http://localhost:8000/docs