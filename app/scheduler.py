import os
import random
import datetime
from github import Github
from config import CONFIG

class CommitScheduler:
    def __init__(self, pattern):
        self.pattern = pattern
        self.github = Github(CONFIG['github_token'])
        self.repo = self.github.get_repo(CONFIG['repo_name'])
    
    def commit_once_a_day(self):
        for x in range(52):
            for y in range(7):
                if self.pattern[y][x] == 1:
                    self.commit_on_date(self.get_date_for_pixel(x, y))
    
    def commit_multiple_times_a_day(self, times):
        for x in range(52):
            for y in range(7):
                if self.pattern[y][x] == 1:
                    for _ in range(times):
                        self.commit_on_date(self.get_date_for_pixel(x, y))
    
    def commit_randomly(self):
        for x in range(52):
            for y in range(7):
                if self.pattern[y][x] == 1:
                    times = random.randint(1, 5)
                    for _ in range(times):
                        self.commit_on_date(self.get_date_for_pixel(x, y))
    
    def get_date_for_pixel(self, x, y):
        start_date = datetime.date(datetime.datetime.now().year - 1, 1, 1)
        delta_days = x * 7 + y
        return start_date + datetime.timedelta(days=delta_days)
    
    def commit_on_date(self, date):
        os.system(f"git commit --allow-empty -m 'Commit on {date}' --date '{date}'")
        self.repo.update_file("README.md", "Update README", "New content", self.repo.get_contents("README.md").sha, branch="main")

# Example usage:
# pattern = [[0, 1, 0, 0, 1, 0, 0] for _ in range(52)]  # Sample pattern
# scheduler = CommitScheduler(pattern)
# scheduler.commit_once_a_day()
