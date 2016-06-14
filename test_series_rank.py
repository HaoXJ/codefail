#!/usr/bin/env  python



import pandas as pd
import numpy as np
import sys

def test(csv):
    m=pd.read_csv(csv,names=["orderbook","price"])
    m.set_index("orderbook", inplace=True)
    a=m.price
    print (a)
    print (a.shape)
    print (type(a))
    b= a.rank(ascending=False)
    a.to_csv("dddd")
    print (b.shape)



if __name__=="__main__":
    test(sys.argv[1])
    



