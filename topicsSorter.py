import pandas as pd
import random

def sortTopics():
    df = pd.read_csv("project.csv")
    print(type(df))
    #df['count'] = df.groupby('Tema')['Tema'].transform(pd.Series.value_counts)

    df.sort_values('Tema', inplace=True, ascending=False)
    print(df)
    
    groups = [df for _, df in df.groupby('Tema')]
    random.shuffle(groups)

    groups = pd.concat(groups).reset_index(drop=True)
        
    groups.to_csv('project.csv')
    print('sortirao sam project.csv')
    print(groups)
    
#sortTopics()