def create_future_failure_label(df,horizon=5):
    df["future_failure"]=0
    for i in range(len(df)):
        future_window=df["failed"].iloc[i+1:i+horizon+1]
        if future_window.max()==1:
            df.loc[i,"future_failure"]=1
    
    return df