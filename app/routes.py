from flask import Blueprint, render_template, request
from app.logic import tes_dfa, regex_to_nfa, minimization_dfa, tes_equivalen

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dfa', methods=['GET', 'POST'])
def dfa():
    result = ''
    if request.method == 'POST':
        states = request.form['states'].split(',')
        alphabet = request.form['alphabet'].split(',')
        start = request.form['start']
        accept = request.form['accept'].split(',')
        trans_raw = request.form['transitions'].split(',')
        input_str = request.form['input']

        transitions = {}
        for tr in trans_raw:
            src, sym, dst = tr.strip().split(':')
            transitions[(src, sym)] = dst

        result = tes_dfa.run_dfa(states, alphabet, transitions, start, accept, input_str)
    
    return render_template('tes_dfa.html', result=result)

