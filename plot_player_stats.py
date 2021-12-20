from nba_api.stats.endpoints import commonplayerinfo
import matplotlib
import matplotlib.pyplot as plt

def main():
    # データを取得
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)

    # DataFrameオブジェクトに変換
    pd = player_info.player_headline_stats.get_data_frame()

    # 各項目を取得
    pts   = pd['PTS'][0]
    ast   = pd['AST'][0]
    reb   = pd['REB'][0]
    name  = pd['PLAYER_NAME'][0]
    frame = pd['TimeFrame'][0]

    # matplotの設定
    left   = [1, 2, 3]
    label  = ['PTS', 'AST', 'REB']
    height = [pts, ast, reb]
    fig    = plt.figure('NBA STATS')

    plt.bar(left,height, tick_label=label, align='center')
    plt.title(name + ' (' + frame + ')')
    for x, y in zip(left, height):
        plt.text(x, y, y, ha='center', va='bottom')
    plt.show()

if __name__ == '__main__':
    main()
