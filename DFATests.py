# Umer Khan 04/29/2020
"""
Test cases for DFA implementation in DFA.py
"""

import DFA as DFA
import DFAState as state

# DFA for L = {w | w in {0, 1}*, w contains an odd number of 0's}
q0 = state.create("q0")
q1 = state.create("q1", True)
transitions = {(q0, "1"):q0,
               (q0, "0"):q1,
               (q1, "1"):q1,
               (q1, "0"):q0}
if DFA.run(q0, transitions, "010101100001") is not True:
    print("Error in first DFA: w = 010101100001 should have returned True but it did not.")
if DFA.run(q0, transitions, "00") is True:
    print("Error in first DFA: w = 00 should have returned False but it did not.")
if DFA.run(q0, transitions, "11111") is True:
    print("Error in first DFA: w = 11111 should have returned False but it did not.")
if DFA.run(q0, transitions, "0") is not True:
    print("Error in first DFA: w = 0 should have returned True but it did not.")

print("Testing finished.")