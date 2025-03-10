def get_max(max_time, track_list, track_count, start_index=0, current_duration=0):
    optimal = current_duration

    for i in range(start_index, track_count):
        new_duration = current_duration + track_list[i]
        if new_duration <= max_time:
            best_attempt = get_max(max_time, track_list, track_count, i + 1, new_duration)
            if best_attempt == max_time:
                return best_attempt
            if best_attempt > optimal:
                optimal = best_attempt

    return optimal




while True:
    try:
        input_line = input().strip()
        if not input_line:
            break

        values = list(map(int, input_line.split()))
        max_time, num_tracks, track_durations = values[0], values[1], values[2:]

        max_recorded = get_max(max_time, track_durations, num_tracks)
        print(f"sum:{max_recorded}")

    except EOFError:
        break

