from flask import Blueprint, render_template, request, jsonify
from .utils import project_future, analyze_behavior, backward_impact
from .ai_advisor import get_advice

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    future = project_future(data)
    behavior = analyze_behavior(data)
    past = backward_impact(data)
    advice = get_advice(data)
    return jsonify({
        "future": future,
        "behavior": behavior,
        "past": past,
        "advice": advice
    })
