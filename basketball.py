class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.age = player_data['age']
        self.position = player_data['position']
        self.team = player_data['team']

    def display_player(self):
        keys = vars(self)
        print(keys)

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_player = cls(player)
            new_team.append(new_player)
        return new_team

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

new_team = []

for player in players:
    new_team.append(Player(player))

print(new_team)
for player in new_team:
    player.display_player()

print(Player.get_team(players))
