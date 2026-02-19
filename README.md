🌍 AI Travel & Lifestyle Concierge
Autonomous Multi-Agent System for Intelligent Trip Planning
This project is a high-performance, full-stack application designed to automate complex travel planning. Using an Agentic AI approach, it orchestrates multiple specialized agents that research, calculate, and synthesize data from the real web to create comprehensive 7-day itineraries.

🧠 System Architecture & AI Logic
The core of the system is built on a Sequential Multi-Agent Workflow using the CrewAI framework. Unlike simple chatbots, these agents perform task decomposition and use external tools to "ground" their answers in reality.

🤖 The Agentic Crew
City Selection Expert: Analyzes climate, flight costs, and user interests to pick the best destination.

Local Tour Guide: A specialized "researcher" that finds hidden gems, local customs, and real-time events.

Expert Travel Agent: The "synthesizer" that compiles all data into a detailed, budget-aware Markdown plan.

🛠 Tools & Integration
Search Tool: Custom integration with Serper API (Google Search).

Calculation Tool: Python-based mathematical validator for budget estimations.

Inference Engine: Groq (Llama 3.1 8B & 3.3 70B) for low-latency reasoning.

🚀 Technical Stack
AI Orchestration: CrewAI

LLMs: Llama 3.1 8B-Instant & Llama 3.3 70B

Backend: FastAPI (Python) - Asynchronous request handling

Frontend: React + Vite (Modern UI with Markdown rendering)

DevOps: Docker & Docker Compose

Proxy/Web Server: Nginx (Configured for long-running AI sessions)

🛡️ Engineering Challenges & "The Battle with Hallucinations"
A significant part of the development was focused on AI Safety and Reliability.

1. Taming Structural Hallucinations
Problem: Larger models like Llama 70B sometimes hallucinated custom XML-like tags (e.g., <function>) instead of standard JSON tool-calls.

Solution: Implemented strict Few-Shot Prompting and switched to the more "disciplined" 8B-Instant model for tool-heavy tasks to ensure 100% stable execution.

2. Preventing "Lazy" Responses
Problem: Smaller models tended to "cut corners," providing brief summaries instead of detailed 7-day plans.

Solution: Engineered specific Task Constraints in the prompts, mandating minimum word counts and specific data points (links, prices) for each day.

3. Data Grounding (The Factual Layer)
Problem: Models often "guessed" prices (e.g., $30 hotels in central Paris).

Solution: Enforced a Mandatory Internet Search step. Agents cannot proceed without providing a real URL or a verified search snippet from the Serper API.

🚥 Performance Optimization & DevOps
Rate-Limit Management: To handle Groq's free-tier limits (6,000 TPM), I engineered a synchronization layer using max_rpm=1. This forces "thoughtful" sequential execution.

Connection Resilience: Configured Nginx and FastAPI to support long-polling connections with a 300s timeout, preventing breaks during intensive research cycles.

Containerization: The entire environment (Frontend, Backend, Nginx) is orchestrated via Docker Compose for one-click deployment.

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
Environment Variables:
Create a .env file in the root directory:

Фрагмент кода
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key
Run with Docker:

Bash
docker-compose up --build
Access the App:
Frontend: http://localhost:3000
API Docs: http://localhost:8000/docs

📈 Future Roadmap
Implement Hierarchical Process with a "Manager Agent" for more complex, non-linear tasks.

Integrate Azure OpenAI for enterprise-grade scalability.

Add LLM-as-a-Judge to automatically evaluate the quality of the generated itineraries.

Developed as part of a Data Science portfolio at CTU Prague (ČVUT).