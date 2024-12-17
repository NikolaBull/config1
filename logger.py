import csv
from datetime import datetime

class Logger:
    def __init__(self, log_path, user):
        self.log_path = log_path
        self.user = user

    def log(self, action):
        with open(self.log_path, 'a', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([datetime.now().isoformat(), self.user, action])
