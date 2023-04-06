event_time_seconds = int(input())
hours, remainder = divmod(event_time_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{hours}h {minutes}m {seconds}s")
