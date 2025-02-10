from fastapi import FastAPI
from Core.models.agent_models import AgentConfig
from Core.agents.base_agent import BaseAgent

app = FastAPI()

@app.post("/create_agent")
async def create_agent(config: AgentConfig):
    agent = BaseAgent(config)
    return {"message": "Agente creado exitosamente", "agent_name": agent.config.name}
