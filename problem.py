
class Competitor:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

def calculate_competitor_score(competitor):
    return competitor.chickenwings * 5 + competitor.hamburgers * 3 + competitor.hotdogs * 2

def generate_competition_scoreboard(competitors):
    scoreboard = []
    for competitor in competitors:
        score = calculate_competitor_score(competitor)
        scoreboard.append({'name': competitor.name, 'score': score})
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard

# Test cases
competitors = [
    Competitor("Habanero Hillary", 5, 17, 11),
    Competitor("Big Bob", 20, 4, 11)
]

scoreboard = generate_competition_scoreboard(competitors)
print(scoreboard)



# example 2
competitors = [
    Competitor("Habanero Hillary", 50, 34, 51),
    Competitor("Big Bob", 24, 14, 90)
]

scoreboard = generate_competition_scoreboard(competitors)
print(scoreboard)