import json
import os
from analytics_engine.scoring_engine import calculate_score
from analytics_engine.topic_analysis import topic_statistics, average_scores
from analytics_engine.thinking_patterns import thinking_distribution
from analytics_engine.error_analysis import error_percentage
from analytics_engine.trend_analysis import learning_trend
from analytics_engine.cognitive_profile import cognitive_profile

DATA_FILE = "data/sessions.json"

def load_sessions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        sessions = json.load(f)
    for s in sessions:
        first   = s.get("first_attempt", 0)
        final   = s.get("final_attempt", 0)
        correct = s.get("correct_answer", 100)
        s["score"] = calculate_score(first, final, correct)
    return sessions

def analytics_summary():
    sessions = load_sessions()
    if not sessions:
        return {
            "topic_statistics": {},
            "average_scores": {},
            "thinking_patterns": {},
            "error_percentages": {},
            "learning_trends": {},
            "cognitive_profiles": {}
        }
    return {
        "topic_statistics":  topic_statistics(sessions),
        "average_scores":    average_scores(sessions),
        "thinking_patterns": thinking_distribution(sessions),
        "error_percentages": error_percentage(sessions),
        "learning_trends":   learning_trend(sessions),
        "cognitive_profiles": cognitive_profile(sessions)
    }
