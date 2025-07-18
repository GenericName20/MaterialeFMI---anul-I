nfa = {
    "states": {"q0", "q1", "q2"},
    "alphabet": {"a", "b"},
    "transitions": {
        "q0": {
            "a": {"q0", "q1"},
            "b": {"q0"}
        },
        "q1": {
            "b": {"q2"}
        },
        "q2": {}
    },
    "start": "q0",
    "accept": {"q2"}
}

def convert_nfa_to_dfa(nfa_config):
    alphabet = nfa_config["alphabet"]
    transitions = nfa_config["transitions"]
    start = nfa_config["start"]
    accept = nfa_config["accept"]

    dfa_start = frozenset([start])

    dfa_states = []
    dfa_transitions = {}
    dfa_accept = set()

    unprocessed = [dfa_start]
    while unprocessed:
        current = unprocessed.pop(0)
        if current not in dfa_states:
            dfa_states.append(current)

        if any(state in accept for state in current):
            dfa_accept.add(current)

        for symbol in alphabet:
            next_state = set()
            # For each NFA state in the current DFA state, get transitions on the symbol.
            for state in current:
                # If the state has a transition on this symbol, add the resulting states.
                if symbol in transitions.get(state, {}):
                    next_state.update(transitions[state][symbol])
            # Convert to frozenset to use as a DFA state.
            next_state = frozenset(next_state)
            if not next_state:
                continue  # No transitions on this symbol.
            # Record the DFA transition.
            dfa_transitions.setdefault(current, {})[symbol] = next_state
            # If the next state hasn't been processed yet, add it to the queue.
            if next_state not in dfa_states and next_state not in unprocessed:
                unprocessed.append(next_state)
    dfa = {
        "states": dfa_states,
        "alphabet": alphabet,
        "transitions": dfa_transitions,
        "start": dfa_start,
        "accept": dfa_accept
    }
    return dfa


dfa = convert_nfa_to_dfa(nfa)

# Print out the DFA components.
print("DFA States:")
for state in dfa["states"]:
    print(" ", state)

print("\nDFA Alphabet:")
print(" ", dfa["alphabet"])

print("\nDFA Start State:")
print(" ", dfa["start"])

print("\nDFA Accept States:")
for state in dfa["accept"]:
    print(" ", state)

print("\nDFA Transitions:")
for state, trans in dfa["transitions"].items():
    for symbol, next_state in trans.items():
        print(f"  {state} -- {symbol} --> {next_state}")