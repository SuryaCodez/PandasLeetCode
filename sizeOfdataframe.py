import pandas as pd
def getDataframeSize(players:pd.DataFrame)-> List:
    return [players.shape[0], players.shape[1]]
#time complexity: 461ms
#space complexity: 58.93 MB
