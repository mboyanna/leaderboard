from pyhocon import ConfigFactory
from pyhocon.tool import HOCONConverter

class MyProcessor:
    def run(self, df):
        #return df.agg(['mean', 'min', 'max'])
        rConfigTree = ConfigFactory.parse_file('defaultLeaderboardResponse.conf').get("LeaderboardComprehensive")
        r = HOCONConverter.convert(rConfigTree, 'json')
        print(r)
        return r

