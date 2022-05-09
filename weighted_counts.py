import numpy as np
import pandas as pd

def weighted_value_counts(df_col,w):
    '''
    Count the occurrencies of each unique value in a data column of interest, weighting each observation by a given number

    INPUT
    df_col: pandas data column containing the values of interest
    w: array containing oen weight for each observation

    OUTPUT
    a pandas Series containing the weighted count of unique values in the data column of interest
    '''

    labels = [np.NaN]
    counts = [0]

    l_w = list(w)

    for o,obs in enumerate(df_col):

        #count
        w_count = l_w[o]

        if np.isnan(obs):
            #update count
            counts[0] += w_count
        else:
            #if new append label and count
            if not obs in labels:
                labels.append(obs)
                counts.append(w_count)
            else:
                #update count
                counts[labels.index(obs)] += w_count

    return pd.Series(counts, index=labels, name=df_col.name)


def weighted_country_value_counts(df_country_col1, df_col2,w):
    '''
    Count the occurrencies of each unique value in a data column of interest, weighting each observation by a given number,
    dividing the count by country.

    INPUT
    df_country_col1: pandas data colunb containing a country code for each observation
    df_col2: pandas data column containing the values of interest
    w: array containing oen weight for each observation

    OUTPUT
    a pandas Series containing the weighted count of unique values in the data column of interest diveded by country
    '''

    labels1 = [np.NaN]
    labels2 = [np.NaN]
    counts = [0]

    l_col2 = list(df_col2)
    l_w = list(w)

    for o1,obs1 in enumerate(df_country_col1):
        
        #col2
        obs2 = l_col2[o1]

        #count
        w_count = l_w[o1]

        if np.isnan(obs2):
            #update count
            counts[0] += w_count
        else:
            #if new append labels and count
            if (not obs1 in labels1) or (not obs2 in labels2) or not(obs2 in [labels2[i] for i in [i for i, x in enumerate(labels1) if x == obs1]]):
                labels1.append(obs1)
                labels2.append(obs2)
                counts.append(w_count)
            else:
                #if already in the count array find the location
                count_indx = list(set([i for i, x in enumerate(labels1) if x == obs1]).intersection([i for i, x in enumerate(labels2) if x == obs2]))
                #update count
                counts[count_indx[0]] += w_count

    return pd.Series(counts, index=[labels1,labels2])
