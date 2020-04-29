# Umer Khan 04/29/2020
"""
An implementation of a DFA State
"""

def create(name, final=False):
    """
    Creates a new state for a DFA
    :param name: name of the state
    :param final: is it a final state? No by default
    :return: the state as a tuple
    """
    return (name, final)

def getName(state):
    """
    Returns the name of the given state
    :param state: the state we want the name of
    :return: the name of the state (string)
    """
    assert state is not None, "getName called with no state"
    return state[0]

def isFinal(state):
    """
    Is it a final state?
    :param state: the state we are checking
    :return: True if it is a final state, False otherwise
    """
    assert state is not None, "isFinal called with no state"
    return state[1]
