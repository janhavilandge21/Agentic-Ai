from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from agent.agentic_workflow import GraphBuilder
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str


@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        # 1️⃣ Build graph (Groq only)
        graph_builder = GraphBuilder(model_provider="groq")
        react_app = graph_builder()   # or graph_builder.build_graph()

        # 2️⃣ (Optional) Save graph visualization
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        # 3️⃣ Correct message format
        inputs = {
            "messages": [
                HumanMessage(content=query.question)
            ]
        }

        # 4️⃣ Invoke graph
        output = react_app.invoke(inputs)

        # 5️⃣ Extract final AI response
        final_answer = output["messages"][-1].content

        return {"answer": final_answer}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
