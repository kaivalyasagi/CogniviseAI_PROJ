from collections import defaultdict, Counter


def cognitive_profile(sessions):

    user_sessions = defaultdict(list)

    for s in sessions:
        user_sessions[s["user_id"]].append(s)

    profiles = {}

    for user, records in user_sessions.items():

        scores = [r["score"] for r in records]
        thinking_patterns = [r["thinking_pattern"] for r in records]
        confusions = [r["confusion_type"] for r in records]

        avg_score = round(sum(scores) / len(scores), 2)

        dominant_thinking = Counter(thinking_patterns).most_common(1)[0][0]
        common_confusion = Counter(confusions).most_common(1)[0][0]

        profiles[user] = {
            "average_score": avg_score,
            "dominant_thinking": dominant_thinking,
            "common_confusion": common_confusion
        }

    return profiles
