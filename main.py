import json


def toArea(state,pseq1, widths, heights):
    pseq=[state,pseq1]
    x=[0]*len(state)
    y=[0]*len(state)
    fplus=[]
    fminus=[]
    for i in range(len(pseq[0])):
        fplus.append(pseq[0].index(i+1))
        fminus.append(pseq[1].index(i+1))
    for i in pseq[0]:
        i=i-1
        lis=[]
        for j in range(len(fminus)):
            if fplus[j] < fplus[i] and fminus[j] < fminus[i] and i!=j:
                try:
                    lis.append(x[j]+widths[j])
                except:
                    pass
        if len(lis)==0:
            x[i]=0
        else:
            x[i]=max(lis)        
    for i in pseq[1]:
        i=i-1
        lisy=[]
        for j in range(len(fplus)):
            if fplus[j] > fplus[i] and fminus[j] < fminus[i] and i!=j:
                try:
                    lisy.append(y[j]+heights[j])
                except:
                    pass

        if len(lisy)==0:
            y[i]=0
        else:
            y[i]=max(lisy)

    X=[]
    Y=[]
    for i in range(len(x)):
        X.append(x[i]+widths[i])
        Y.append(y[i]+heights[i])
    widthtot=max(X)
    heighttot=max(Y)
    area=widthtot*heighttot
    return area,x,y