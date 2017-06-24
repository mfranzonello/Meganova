'''Analyst work'''
from typing import List
from app.stella import org,physical

class Project:
    def __init__(self,name:str,customer:org.Customer,
                 portfolio:physical.Portfolio):
        self.name = name
        self.customer = customer
        self.portfolio = portfolio
        self.scenarios = {}

    def add_portfolio(portfolio:physical.Portfolio):
        self.portfolio = portfolio

    def add_scenario(self,scenario:physical.Scenario):
        self.scenarios[scenario.name] = scenario

class User:
    def __init__(self,name:str):
        self.name = name
        self.permissions = {}
        self.projects = {}

    def update_permissions(self,**permissions):
        self.permissions.update(permissions)

    def add_project(self,project:Project):
        self.projects[project.name] = project
    
    def get_project(self,project_name:str) -> Project:
        return self.projects[project_name]

    def remove_project(self,project_name:str):
        if project_name in self.projects:
            self.projects.pop(project_name)




