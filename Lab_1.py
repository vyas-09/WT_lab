import pandas as pd
def makeDataFrame(filename):
    data = pd.read_csv(filename)
    df=pd.DataFrame(data)
    return(data)
makeDataFrame("C:/Users/vedav/Downloads/Telegram Desktop/statemappings.csv")
#def parsename(fromstring):
 #   s1=fromstring.fid(':')+1'