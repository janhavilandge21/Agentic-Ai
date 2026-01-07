
---

# 🚀 End-to-End Agentic AI with LLMOps

An **end-to-end Agentic AI system** built using **LangGraph**, **Groq LLM**, and **FastAPI**, demonstrating modern **LLMOps-ready agent orchestration**, tool calling, and production-grade API design.

---

## 📌 Project Overview

This project implements an **Agentic AI workflow** where an LLM can:

* Understand user queries
* Decide when to use external tools
* Call tools autonomously
* Reason over tool outputs
* Produce a final, structured response

The system is designed with **LLMOps best practices**, making it suitable for **real-world AI applications** rather than toy demos.

---

## 🧠 Key Features

* 🤖 **Agentic AI Architecture** (LLM decides actions)
* 🔁 **Multi-step reasoning loop (Agent → Tools → Agent)**
* 🧩 **Dynamic tool invocation**
* ⚡ **Groq LLM integration (low latency)**
* 🌐 **FastAPI backend**
* 📊 **Mermaid graph visualization of agent workflow**
* 🧪 **Production-ready, extensible design**

---

## 🛠️ Tools Integrated

The agent can automatically use the following tools based on the user query:

* 🌦️ Weather Information Tool
* 📍 Place Search Tool
* 💰 Expense Calculator Tool
* 💱 Currency Conversion Tool

---

## 🏗️ Architecture Flow

```
User Query
   ↓
FastAPI API
   ↓
LangGraph Agent
   ↓
LLM (Groq)
   ↓
Tool Decision
   ↓
Tool Execution (Weather / Places / Calculator / Currency)
   ↓
LLM Reasoning
   ↓
Final Response
```

---

## 🧩 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **LangGraph**
* **LangChain**
* **Groq LLM**
* **Pydantic**
* **Uvicorn**

---

## 📁 Project Structure

```
AI_TRIP_PLANNER/
│
├── agent/
│   └── agentic_workflow.py
│
├── tools/
│   ├── weather_info_tool.py
│   ├── place_search_tool.py
│   ├── expense_calculator_tool.py
│   └── currency_conversion_tool.py
│
├── prompt_library/
│   └── prompt.py
│
├── utils/
│   └── model_loader.py
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---



---

## 🧪 API Usage

### Swagger UI

Open in browser:

```
http://127.0.0.1:8000/docs
```

### Sample Request

```json
{
  "question": "Plan a 3-day trip to Goa and estimate budget in INR"
}
```

### Sample Response

```json
{
  "answer": "Here is a detailed 3-day Goa itinerary along with an estimated budget..."
}
```

---

## 🖥️ Optional: Streamlit UI

If you want a UI:

```bash
streamlit run streamlit_app.py
```

Opens at:

```
http://localhost:8501
```

---

## 🧠 LLMOps Considerations

* Designed for **extensibility**
* Supports **tool addition without changing core logic**
* Clear separation of concerns (LLM, tools, orchestration)
* Debuggable agent flow via graph visualization
* Ready for logging, tracing, and evaluation layers

---

## 🎯 Use Cases

* AI Travel Assistants
* Autonomous Research Agents
* Enterprise Knowledge Assistants
* Tool-augmented Chatbots
* LLMOps & Agentic AI demos

---



---

## 🔮 Future Enhancements

* 🔄 Conversation memory
* 📡 Streaming responses
* 🧪 Evaluation & hallucination detection
* 🐳 Docker deployment
* 📊 Observability & tracing

---


Just say **NEXT** 🚀

