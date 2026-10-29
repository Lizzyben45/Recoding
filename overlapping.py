def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort()

    merged = [intervals[0]]

    for next_interval in intervals[1:]:
        current_interval = merged[-1]
        
        if next_interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            merged.append(next_interval)

    return merged

intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals))
