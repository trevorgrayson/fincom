from .usaa import *

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
