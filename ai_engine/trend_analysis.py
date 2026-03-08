from collections import defaultdict


def learning_trend(sessions):

    user_scores = defaultdict(list)

    for s in sessions:
        user_scores[s["user_id"]].append((s["date"], s["score"]))

    trends = {}

    for user, records in user_scores.items():

        records.sort()
        scores = [r[1] for r in records]

        if len(scores) < 2:
            trends[user] = "insufficient data"
            continue

        if scores[-1] > scores[0]:
            trends[user] = "improving"
        elif scores[-1] < scores[0]:
            trends[user] = "declining"
        else:
            trends[user] = "stable"

    return trends
