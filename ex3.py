import pandas as pd
def disassembly_data(df,classes):
    filtered = df[(df['class'].isin(classes))]

    # df_80_percent = filtered.sample(frac=0.80)
    df_80_percent = filtered.head(int(filtered.shape[0]*0.8))
    df_20_percent=filtered.tail(int(filtered.shape[0]*0.2))
    # df_20_percent = filtered.drop(df_80_percent.index)
    classification = df_20_percent['class']
    df_20_percent.drop('class', inplace=True, axis=1)
    # print(df_80_percent)
    return(df_80_percent,df_20_percent,classification)
