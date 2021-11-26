from nba_api.stats.endpoints import commonplayerinfo
import matplotlib
import matplotlib.pyplot as plt

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

pd = player_info.player_headline_stats.get_data_frame()

def main():
    for index, rows in pd.iterrows():
        pts = rows['PTS']
        ast = rows['AST']
        reb = rows['REB']
        name = rows['PLAYER_NAME']
        frame = rows['TimeFrame']
    #    pie = rows['PIE']

    label = ["PTS", "AST", "REB"]
    print(name, pts, ast, reb)
    left = [1, 2, 3]
    height = [pts, ast, reb]
    fig = plt.figure("NBA Stats")
    plt.bar(left,height, tick_label=label, align="center")
    plt.title(name + " (" + frame + ")")
    plt.show()

if __name__ == '__main__':
    main()
