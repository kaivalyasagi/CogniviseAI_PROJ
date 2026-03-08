from collections import defaultdict


def error_percentage(sessions):

    error_counts = defaultdict(int)
    total = len(sessions)

    for s in sessions:
        error_counts[s["confusion_type"]] += 1

    percentages = {}

    for error, count in error_counts.items():
        percentages[error] = round((count / total) * 100, 2)

    return percentages
