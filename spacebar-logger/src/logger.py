def log_occurrence(timestamp):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp}\n")