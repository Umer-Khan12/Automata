# Umer Khan 04/29/2020
"""
An implementation of a Deterministic Finite Automaton
"""
import DFAState as state

# States created from DFAState.create()
q0 = state.create("q0")
q1 = state.create("q1", True)
# The current state (Starts at initial state)
currentState = q0
# The set of transitions implemented as a dictionairy with
# the key being a tuple (state, letter) and the value being the next state
# if there is no next state then we will represent it by None (Note: every null transition must be added here)
transitions = {(q0, "0"):q1,
               (q0, "1"):q0,
               (q1, "0"):q0,
               (q1, "1"):q1
               }

# The word we will run through the DFA
word = "0111001010"

# Use the DFA to check the word in worst-case O(n) time where n is the length of the word
for letter in word:
    # If there is no transition on a current letter then the machine crashes
    if transitions[(currentState, letter)] is None:
        break
    # Else switch to the new state
    else:
        currentState = transitions[(currentState, letter)]

# If it ends in a final state then accept, otherwise reject
if state.isFinal(currentState):
    print("The word: " + word + " was accepted")
else:
    print("The word: " + word + " was rejected")
