import random
import base64
from datetime import datetime, UTC
from math import sqrt


class Agent:
    def __init__(self, states, attributes, actions, model=None):
        self.states = states
        self.attributes = attributes
        self.actions = actions
        self.model = model

    def prompt(self, current_environment):
        if self.model is None:
            return self._fall_back(current_environment)
        return self._model_response(current_environment)

    def _model_response(self, current_environment):
        pass

    def _fall_back(self, current_environment):
        pass


class Environment:
    def __init__(self, boundaries, elements, agents: list[Agent]):
        self.boundaries: dict = boundaries
        self.elements: list = elements
        self.agents: dict = {}
        for agent in agents:
            self.add_agent(agent)

    def update(self, agent, agent_response):
        pass

    def get_display_representation(self):
        pass

    def add_agent(self, agent: Agent = None):
        if agent is not None:
            agent.attributes["id"] = base64.b64encode(str(datetime.now(tz=UTC).timestamp()).encode()).decode()
            self.agents.update({agent.attributes["id"]: agent})
            return

        agent_id = base64.b64encode(str(datetime.now(tz=UTC).timestamp()).encode()).decode()
        orient_comp = random.random()
        attributes = {
            "id": base64.b64encode(str(datetime.now(tz=UTC).timestamp()).encode()).decode(),
            "color": "red",
            "position": {
                "x": self.boundaries["right"]*random.random()+self.boundaries["left"],
                "y": self.boundaries["bottom"]*random.random()+self.boundaries["top"]
            },
            "orientation": {
                "x": orient_comp,
                "y": sqrt(1 - orient_comp*orient_comp)
            }
        }

        self.agents.update({agent_id: Agent({}, attributes, {})})





