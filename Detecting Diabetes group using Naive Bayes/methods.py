def catconsep(df):
    cat=[]
    con=[]
    for i in df.columns:
        if(df[i].dtype =='object'):
            cat.append(i)
        else:
            con.append(i)
    return cat, con


######


def replacer(df):
    cat1 , con1 = catconsep(df)
    for i in con1:
        x = df[i].mean()
        df[i]= df[i].fillna(x)
        
    for i in cat1:
        x = df[i].mode()
        df[i]= df[i].fillna(x)
        
############


def standardize(df):
    import pandas as pd
    cat, con = catconsep(df)
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    x1 = pd.DataFrame(ss.fit_transform(df[con]), columns = con)
    return x1

############


def preprocessing(df):
    cat, con = catconsep(df)
    x1 = standardize(df)
    import pandas as pd
    x2 = pd.get_dummies(df[cat])
    Xnew = x1.join(x2)
    return Xnew
 