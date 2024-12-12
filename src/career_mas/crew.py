#!/usr/bin/env python
import os
import yaml
from pathlib import Path
from crewai import Agent, Task, Crew
from textwrap import dedent

class MyMasCrew:
    """
    Career exploration crew configuration and management.
    """
    
    def __init__(self):
        self.config_path = Path(__file__).parent / "config"
        self.agents_config = self._load_yaml("agents.yaml")
        self.tasks_config = self._load_yaml("tasks.yaml")
        
    def _load_yaml(self, filename):
        """Load YAML configuration file."""
        file_path = self.config_path / filename
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def _create_agents(self, inputs):
        """Create agents based on YAML configuration."""
        agents = {}
        
        for agent_name, config in self.agents_config.items():
            # Format the role with input variables
            role = config['role'].format(topic=inputs.get('career_preferences', ''))
            
            agents[agent_name] = Agent(
                role=role,
                goal=config['goal'].format(topic=inputs.get('career_preferences', '')),
                backstory=dedent(config['backstory']).strip(),
                verbose=True
            )
        
        return agents

    def _create_tasks(self, agents, inputs):
        """Create tasks based on YAML configuration."""
        tasks = []
        
        for task_name, config in self.tasks_config.items():
            # Format description with input variables
            description = config['description'].format(
                career_preferences=inputs.get('career_preferences', ''),
                target_industries=', '.join(inputs.get('target_industries', [])),
                key_requirements=', '.join(inputs.get('key_requirements', []))
            )
            
            tasks.append(
                Task(
                    description=description,
                    expected_output=config['expected_output'],
                    agent=agents[config['agent']]
                )
            )
        
        return tasks

    def crew(self):
        """Initialize the crew with default inputs."""
        default_inputs = {
            'career_preferences': 'Career Analysis',
            'target_industries': ['General'],
            'key_requirements': ['All']
        }
        
        # Create agents and tasks
        agents = self._create_agents(default_inputs)
        tasks = self._create_tasks(agents, default_inputs)
        
        # Create and return the crew
        return Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=True
        )

    def process(self, inputs):
        """
        Process career exploration with specific inputs.
        """
        # Create agents and tasks with provided inputs
        agents = self._create_agents(inputs)
        tasks = self._create_tasks(agents, inputs)
        
        # Create and return the crew
        return Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=True
        )
