import statistics

#8 standard deviation
def value8std(df,col):
    dat=df[df[col].notnull()]
    rataan= dat[col].mean()
    std= statistics.stdev(dat[col])
    df[col+'_2']=np.where((df[col]> (rataan+ 8*std) ),(rataan+ 8*std),df[col])
    return df 
#6 standard deviation
def value6std(df,col):
    dat=df[df[col].notnull()]
    rataan= dat[col].mean()
    std= statistics.stdev(dat[col])
    df[col+'_2']=np.where((df[col]> (rataan+ 6*std) ),(rataan+ 6*std),df[col])
    return df 
#handling outlier
def handleoutlier(df,col):
    dat=df[df[col].notnull()]
    q1=dat[col].quantile(.25)
    q3=dat[col].quantile(.75)
    low= q1- (1.1*(q3-q1))
    df[col+'_1']=np.where((df[col]< low ),low,df[col])
    return df