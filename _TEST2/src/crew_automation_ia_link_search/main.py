#!/usr/bin/env python
import sys
from crew_automation_ia_link_search.crew import CrewAutomationIaLinkSearchCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'figma_link': 'https://www.figma.com/proto/umpOYIEdIYYdpMAHx3iowG/Airbnb-UI-Kit---Yourte?node-id=365-704&p=f&t=VLkmDsSlbuGx4X1y-1&scaling=scale-down&content-scaling=fixed&page-id=365%3A703&starting-point-node-id=365%3A704'
    }
    try:
    CrewAutomationIaLinkSearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'figma_link': 'https://www.figma.com/proto/umpOYIEdIYYdpMAHx3iowG/Airbnb-UI-Kit---Yourte?node-id=365-704&p=f&t=VLkmDsSlbuGx4X1y-1&scaling=scale-down&content-scaling=fixed&page-id=365%3A703&starting-point-node-id=365%3A704'
    }
    try:
        CrewAutomationIaLinkSearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewAutomationIaLinkSearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'figma_link': 'https://www.figma.com/proto/umpOYIEdIYYdpMAHx3iowG/Airbnb-UI-Kit---Yourte?node-id=365-704&p=f&t=VLkmDsSlbuGx4X1y-1&scaling=scale-down&content-scaling=fixed&page-id=365%3A703&starting-point-node-id=365%3A704'
    }
    try:
        CrewAutomationIaLinkSearchCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
