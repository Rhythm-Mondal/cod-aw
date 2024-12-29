class Environment:
    def __init__(self, boundaries, elements, agents):
        self.boundaries = boundaries
        self.elements = elements
        self.agents = agents

    def update(self, agent, agent_response):
        pass

    def get_display_representation(self):
        pass


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






