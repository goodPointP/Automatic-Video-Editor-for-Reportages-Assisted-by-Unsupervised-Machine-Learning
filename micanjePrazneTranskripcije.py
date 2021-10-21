def makniRedovePrazneTranskripcije():
    import pandas as pd

    projectDf = pd.read_csv('project.csv', header = 0)

    for index, row in projectDf.iterrows():
        if isinstance(row['Transkripcija'], float):
            projectDf = projectDf.drop(index, axis = 0)

    projectDf.to_csv('project.csv', index = False)      
    return 'ocistio sam project.csv od redova bez transkripcije'
