#!/usr/bin/env python
import sys
from my_mas.crew import MyMasCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'career_preferences': 'Remote Software Development',
        'target_industries': ['Technology', 'FinTech', 'Healthcare IT'],
        'key_requirements': ['Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack']
    }
    MyMasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'career_preferences': 'Remote Software Development',
        'target_industries': ['Technology', 'FinTech', 'Healthcare IT'],
        'key_requirements': ['Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack']
    }
    try:
        MyMasCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMasCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'career_preferences': 'Remote Software Development',
        'target_industries': ['Technology', 'FinTech', 'Healthcare IT'],
        'key_requirements': ['Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack']
    }
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
