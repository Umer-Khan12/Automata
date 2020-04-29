# Umer Khan 04/29/2020
"""
An implementation of a Deterministic Finite Automaton
"""
import DFAState as state

# States created from DFAState.create()
q0 = state.create("q0")
q1 = state.create("q1", True)
# The input alphabet
alphabet = ["0", "1"]
# The initial state
initialState = "q0"
# The set of transitions implemented as a dictionairy with
# the key being a tuple (state, letter) and the value being the next state
# if there is no next state then we will represent it by None
transitions = {(q0, "0"):q1,
               (q0, "1"):q0,
               (q1, "0"):q0,
               (q1, "1"):q1
               }

