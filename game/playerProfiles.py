import csv
import os
from datetime import datetime

class PlayerProfiles:
    def __init__(self):
        self.file = "profiles.csv"
        self.createCSV()

    # create the csvfile to store player profiles
    def createCSV(self):
        if not os.path.exists(self.file):
            with open(self.file, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Name', 'Score', 'High Score', 'Date'])

    # save the player name, score, and highscore to the csv
    def save_score(self, name, score, highscore):
        # list to keep track of existing players
        player_info = []
        found = False
        # read csv, check if player already made a profile
        try:
            with open(self.file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['Name'] == name:
                        row['Score'] = score
                        row['High Score'] = highscore
                        row['Date'] = datetime.now()
                        found = True
                    player_info.append(row)
        except FileNotFoundError:
            pass
        
        if not found:
            player_info.append({'Name': name, 'Score': score, 'High Score': highscore, 'Date': datetime.now()})

        with open(self.file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Score', 'High Score', 'Date'])
            writer.writeheader()
            writer.writerows(player_info)

    # check csv for high score of give player name
    def get_high_score(self, name):
        try: 
            with open(self.file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                high_score = 0
                for row in reader:
                    score = int(row['High Score'])
                    if score > high_score:
                        high_score = score
                return high_score
        except FileNotFoundError:
            return 0
        
    