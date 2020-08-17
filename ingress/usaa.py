import pandas
FILENAME = 'bk_download.csv'


class MLF:
    def execute(self):
        data = self.load()
        feats = self.features(*data)
        return feats[0]

    def console(self):
        pass


class USAAIngress(MLF):
    def load(self):
        return (pandas.read_csv('data/ingress/bk_download.csv'),)

    def features(self, df, *args):
        df['amount'] = df['amount'].apply(lambda amt: float(amt.replace('--', '')))
        df['month'] = df['date'].apply(lambda date: "{2}-{0}".format(*date.split('/')))
        return (df,)

def utility(df):
    df = df[
        df['category'] == 'Utilities'
    ]

        
if __name__ == '__main__':
    ing = USAAIngress()
    results = ing.execute()

    print(
        results.groupby(['month', 'category', 'memo']).sum()
    )

    print(
        results.groupby(['month']).sum().sum()
    )
    print(
        results.groupby(['month']).sum().count()
    )

