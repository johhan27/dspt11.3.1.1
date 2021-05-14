from mylambdata.helper_functions import LambDataframe
import pandas as pd
from mymodule import user

#print (user.admin)
lambdataframe = LambDataframe([["a",1,float("NaN")],
                     ["b",2,float("NaN")],
                     [3,3,float("NaN")],
                     [4,4,float("NaN")]])

#print (test, null_count(test))

#tuple = train_test_split(df, frac=0.2)
#print (tuple[0], tuple[1])]

#lambdataframe = LambDataframe(df)
print (lambdataframe.randomize(seed=200))
print (lambdataframe)


