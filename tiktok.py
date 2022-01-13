from TikTokApi import TikTokApi as tiktok
# import json
from helpers import process_results
import pandas as pd
import sys


def get_data(hashtag):
    # Set up instance
    api = tiktok.get_instance(use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)
    # print(trending)
    # Try the process_results functions definde in the helper module
    processed_resuts = process_results(data=trending)
    # Export processed data to a csv file
    df_results = pd.DataFrame.from_dict(processed_resuts, orient='index')
    print(df_results.head())
    df_results.to_csv("tiktokdata.csv", index=False)

    # Export processed data to json
    # with open("export.json", 'w') as f:
    #     json.dump(processed_resuts, f, indent=4)


if __name__ == '__main__':
    print(sys.argv[1])
    get_data(hashtag=sys.argv[1])
    print("Fininshed")
