# Umer Khan 04/29/2020
"""
An implementation of a Deterministic Finite Automaton
"""
import DFAState as state

def run(initialState, transitions, w):
    """
    Runs a word through a DFA
    :param initialState: The initial state of the DFA
    :param transitions:
        The set of transitions of the DFA. Represented as a dictionairy with key:value pairs
        key: tuple (DFAState, character) and value: DFAState.
        each pair represents a transition from a state on a letter.
    :param w: the input word
    :return: returns true if the word accepts, false otherwise
    :analysis: Worst-case O(n) time complexity where n is the length of w
    """
    currentState = initialState
    for letter in w:
        # If there is no transition on a current letter then the machine crashes
        if transitions[(currentState, letter)] is None:
            break
        else:
            currentState = transitions[(currentState, letter)]

    # If the last state was a final state then accept, otherwise reject
    if state.isFinal(currentState):
        return True
    else:
        return False


