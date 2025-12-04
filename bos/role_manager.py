"""
role_manager.py
Manages the role of the model within the conscious bridge.
"""

class RoleManager:
    def __init__(self):
        self.roles = {}

    def assign_role(self, entity, role):
        self.roles[entity] = role

    def get_role(self, entity):
        return self.roles.get(entity, "unknown")