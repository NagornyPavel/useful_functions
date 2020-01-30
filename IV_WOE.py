import pandas as pd
import numpy as np
def WOE_IV(data,feature,target,bins=10,cont=False):
    df=data.copy()
    if cont:    
        try:
            df[feature+'_GROUP']=pd.qcut(df[feature], bins,duplicates='drop')
            lst=[]
            for i in df[feature+'_GROUP'].unique():
                lst.append([feature,                                                                          # feature
                            i,                                                                                # Value
                            df[df[feature+'_GROUP'] == i].count()[feature+'_GROUP'],                          # All
                            df[(df[feature+'_GROUP'] == i) & (df[target] == 1)].count()[feature+'_GROUP'],    # Good (think: Bad == 0)
                            df[(df[feature+'_GROUP'] == i) & (df[target] == 0)].count()[feature+'_GROUP']])   # Bad (think: Good == 1)
            result=pd.DataFrame(lst,columns=['Feature','Value','All','Good','Bad'])
            result['p_good']=result['Good']/result['Good'].sum()
            result['p_bad']=result['Bad']/result['Bad'].sum()
            result['WOE']=np.log(result['p_good']/result['p_bad'])
            result=result.replace({'WOE': {np.inf: 0, -np.inf: 0}})    
            result['IV']=(result['p_good']-result['p_bad'])*result['WOE']
            return result
        except:
            print ('Check missing values')
    else:
        try:
            lst=[]
            for i in df[feature].unique():
                lst.append([feature,                                                        # feature
                            i,                                                              # Value
                            df[df[feature] == i].count()[feature],                          # All
                            df[(df[feature] == i) & (df[target] == 1)].count()[feature],    # Good (think: Bad == 0)
                            df[(df[feature] == i) & (df[target] == 0)].count()[feature]])   # Bad (think: Good == 1)
            result=pd.DataFrame(lst,columns=['Feature','Value','All','Good','Bad'])
            result['p_good']=result['Good']/result['Good'].sum()
            result['p_bad']=result['Bad']/result['Bad'].sum()
            result['WOE']=np.log(result['p_good']/result['p_bad'])
            result=result.replace({'WOE': {np.inf: 0, -np.inf: 0}})    
            result['IV']=(result['p_good']-result['p_bad'])*result['WOE']
            return result
        except:
            print ('Check missing values')
