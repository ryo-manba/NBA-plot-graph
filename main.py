from nba_api.stats.endpoints import commonplayerinfo
import matplotlib
import matplotlib.pyplot as plt

class my_nba:
    def __init__(self):
        self.pd = None
        self.index = []
        self.players = []
        self.score = []

    def get_info(self, id):
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=id)
        self.pd = player_info.player_headline_stats.get_data_frame()

    def get_players_info(self, start, end):
        index = 1
        for i in range(start, end):
            try:
                self.get_info(i)
            except:
                continue
            try:
                ast   = self.pd['AST'][0]
                pts   = self.pd['PTS'][0]
                reb   = self.pd['REB'][0]
                name  = self.pd['PLAYER_NAME'][0]
            except IndexError:
                continue

            # Debug
            print(f'''name = {name},pts  = {pts}, ast  = {ast}, reb  = {reb}''')

            self.players.insert(0,name)
            self.index.append(index)
            index += 1
            score = (pts + ast + reb)
            self.score.insert(0,score)

    def plot_bar_graph(self, year):
        plt.barh(self.index, self.score, align="center")
        plt.yticks(self.index, self.players)
        plt.title(str(year) + " Draft Players Score")
        plt.show()

# 947 = Iverson, 2544 = Lebron, 1629627 = Zion
def main():
    print("Please wait...")
    nba = my_nba()
    nba.get_players_info(947, (947 + 58))
    nba.plot_bar_graph(1996)

if __name__ == '__main__':
    main()
