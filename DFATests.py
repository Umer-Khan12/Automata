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

# DFA for L = {w | w in {0, 1}*, 001 is a substring of w}
q0 = state.create("q0")
q1 = state.create("q1")
q2 = state.create("q2")
q3 = state.create("q3", True)
transitions = {(q0, "1"):q0,
               (q0, "0"):q1,
               (q1, "1"):q0,
               (q1, "0"):q2,
               (q2, "0"):q2,
               (q2, "1"):q3,
               (q3, "0"):q3,
               (q3, "1"):q3}
if DFA.run(q0, transitions, "0") is True:
    print("Error in second DFA: w = 0 should have returned False but it did not.")
if DFA.run(q0, transitions, "001") is not True:
    print("Error in second DFA: w = 001 should have returned True but it did not.")
if DFA.run(q0, transitions, "11001011") is not True:
    print("Error in second DFA: w = 11001011 should have returned True but it did not.")
if DFA.run(q0, transitions, "001101101110") is not True:
    print("Error in second DFA: w = 001101101110 should have returned True but it did not.")

# DFA for L = {w | w in {a, b}*, odd number of a's, even number of b's}
q0 = state.create("q0")
q1 = state.create("q1", True)
q2 = state.create("q2")
q3 = state.create("q3")
transitions = {(q0, "a"):q1,
               (q0, "b"):q3,
               (q1, "a"):q0,
               (q1, "b"):q2,
               (q2, "a"):q3,
               (q2, "b"):q1,
               (q3, "a"):q2,
               (q3, "b"):q0}
if DFA.run(q0, transitions, "aabaa") is True:
    print("Error in third DFA: w = aabaa should have returned False but it did not.")
if DFA.run(q0, transitions, "aabb") is True:
    print("Error in third DFA: w = aaabb should have returned False but it did not.")
if DFA.run(q0, transitions, "aabbbab") is not True:
    print("Error in third DFA: w = aabbbab should have returned True but it did not.")
if DFA.run(q0, transitions, "a") is not True:
    print("Error in third DFA: w = a should have returned True but it did not.")

print("Testing finished.")