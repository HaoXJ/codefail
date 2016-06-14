#!/usr/bin/env  python3
import pandas as pd
import sys

def test_df_ranks(f):
    df = pd.read_hdf(f, key="bad_series")
    #df = df.T
    #df.to_hdf(f,key="t")
    print (df.shape)
    print (type(df))
    print (df)
    #s=df.non_current_asset_to_total_asset
    #print (s)
    #df.rank()
    df.rank(ascending=False)



if __name__=="__main__":
    test_df_ranks(sys.argv[1])







