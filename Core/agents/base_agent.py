from abc import ABC, abstractmethod
from Core.models.agent_models import AgentConfig
from Core.knowledge.knowledge_base import KnowledgeBase

class BaseAgent(ABC):
    def __init__(self, config: AgentConfig):
        self.config = config
        self.knowledge_base = KnowledgeBase()
        self._init_chain()

    @abstractmethod
    def _init_chain(self):
        """Inicializar cadena de procesamiento con LangChain"""
        pass
