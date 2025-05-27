def run_dfa(states, alphabet, transition, start_state, accept_states, input_str):
    current = start_state
    for symbol in input_str:
        if (current, symbol) not in transition:
            return "Rejected (invalid transition)"
        current = transition[(current, symbol)]
    return "Accepted" if current in accept_states else "Rejected"
