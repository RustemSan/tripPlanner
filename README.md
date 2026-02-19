# 🌍 AI Autonomous Travel Concierge
### *Autonomous Multi-Agent System for Intelligent Trip Planning*

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-05998b?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ed?style=for-the-badge&logo=docker)
![CrewAI](https://img.shields.io/badge/Orchestration-CrewAI-red?style=for-the-badge)

An advanced **Agentic AI** solution that automates the end-to-end travel planning process. Unlike standard RAG systems, this project utilizes a team of specialized AI agents that reason, collaborate, and execute Python-based tools to deliver high-precision itineraries.

---

## 🧠 System Architecture

The system utilizes a **Sequential Multi-Agent Workflow**. This ensures a clear chain of thought (Reasoning Chain) where data flows logically from research to final synthesis.


### 🤖 The Agentic Crew
* **City Selection Expert**: Analyzes climate data, flight costs, and traveler interests to select the optimal destination.
* **Local Tour Guide**: A research-heavy agent that finds "hidden gems" and local customs via real-time web search.
* **Expert Travel Agent**: The "Executive Agent" responsible for the final synthesis into a structured Markdown itinerary.

---

## 🛠️ ML Engineering & Logic

### ⚔️ Taming the AI (Hallucination Mitigation)
A core focus of this project was ensuring **AI Reliability**. We implemented several layers of defense against common LLM failures:

| Challenge | Mitigation Strategy | Implementation |
| :--- | :--- | :--- |
| **Structural Hallucinations** | Instruction Following Optimization | Pivoted to **Llama 3.1 8B-Instant** for tool-heavy tasks to ensure 100% stable JSON schema execution. |
| **Content Quality** | Detailed Prompt Constraints | Mandated **minimum word counts** and specific data points (URLs/Prices) in task descriptions. |
| **Factual Accuracy** | **Data Grounding** | Restricted agents from finishing tasks without an **Internet Search** step to verify real-world prices. |

### 🚥 Performance & Infrastructure
* **Rate-Limit Management**: Engineered a synchronization layer using `max_rpm=1` to handle the 6,000 TPM limits of the Groq API.
* **Connection Resilience**: Configured **Nginx** and **FastAPI** to support long-polling with a **300s timeout**, allowing deep-research cycles to complete without interruption.
* **Tool-Calling**: Developed custom Python tools for **Mathematical Validation** (`CalculatorTools`) to prevent LLM arithmetic errors in budget breakdowns.

---

## 🚀 Technical Stack

* **AI Engine**: [CrewAI](https://www.crewai.com/) (Orchestration)
* **Models**: Llama 3.1 8B-Instant (Inference via Groq)
* **Backend**: FastAPI (Python 3.12-slim)
* **Tools**: Serper API (Google Search), Custom Python Calculator
* **DevOps**: Docker, Docker Compose, Nginx

---

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/RustemSan/tripPlanner.git](https://github.com/RustemSan/tripPlanner.git)
    cd tripPlanner
    ```

2.  **Configure Credentials**
    Create a `.env` file in the root directory:
    ```env
    SERPER_API_KEY=your_key_here
    GROQ_API_KEY=your_key_here
    ```

3.  **Deploy with Docker**
    ```bash
    docker-compose up --build
    ```

---

## 📈 Future Roadmap
* **Hierarchical Orchestration**: Implementing a "Manager Agent" to handle non-linear task delegation.
* **Azure Integration**: Transitioning to Azure OpenAI services for enterprise-grade scalability.
* **LLM-as-a-Judge**: Integrating a secondary model to automatically grade the quality and safety of generated itineraries.

---
*Developed by Rustem Sandibekov — Exploring the frontiers of Agentic AI.*