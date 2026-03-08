from collections import defaultdict


def topic_statistics(sessions):

    topic_counts = defaultdict(int)

    for s in sessions:
        topic_counts[s["topic"]] += 1

    return dict(topic_counts)


def average_scores(sessions):

    topic_scores = defaultdict(list)

    for s in sessions:
        topic_scores[s["topic"]].append(s["score"])

    avg_scores = {}

    for topic, scores in topic_scores.items():
        avg_scores[topic] = round(sum(scores) / len(scores), 2)

    return avg_scores
