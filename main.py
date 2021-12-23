from nba_api.stats.endpoints import commonplayerinfo
import matplotlib
import matplotlib.pyplot as plt

class my_nba:
    ID_LEBRON  = 2544
    ID_IVERSON = 947
    ID_ZION    = 1629627
    NB_DRAFT   = 59

    def __init__(self):
        self.pd      = None
        self.index   = []
        self.score   = []
        self.players = []

    def get_info(self, id):
        """
        選手情報を取得
        """
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=id)
        self.pd = player_info.player_headline_stats.get_data_frame()

    def get_players_info(self, start, end):
        """
        指定された範囲の選手情報をインスタンス変数に追加していく
        """
        index = 1
        for i in range(start, end):
            try:
                self.get_info(i)
            except:
                continue
            try:
                pts   = self.pd['PTS'][0]
                ast   = self.pd['AST'][0]
                reb   = self.pd['REB'][0]
                name  = self.pd['PLAYER_NAME'][0]
            except IndexError:
                continue
            self.players.insert(0,name)
            self.index.append(index)
            index += 1
            score = (pts + ast + reb)
            self.score.insert(0,score)

    def plot_bar_graph(self, year):
        """
        横棒グラフを表示する
        """
        plt.barh(self.index, self.score, align="center")
        plt.yticks(self.index, self.players)
        plt.title(str(year) + " Draft Players Score")
        plt.show()

def main():
    print("Please wait...")
    nba = my_nba()
    nba.get_players_info(nba.ID_IVERSON, (nba.ID_IVERSON + nba.NB_DRAFT))
    nba.plot_bar_graph(1996)

if __name__ == '__main__':
    main()
