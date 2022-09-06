#find number if tweets in each category
import json
import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    positive={'Actors':127,'Box Office':105,'Ratings':195,'Comparisons':69,'Fan':53,'Other':77}
    negative={'Actors':18,'Box Office':34,'Ratings':71,'Comparions':16,'Fan':6,'Other':68}
    neutral={'Actors':4,'Box Office':0,'Ratings':46,'Comparisons':2,'Fan':37,'Other':49}
    
    x=list(positive.keys())
    y=list(positive.values())
    z=list(negative.values())
    w=list(neutral.values())
    
    
    fig=plt.figure(figsize=(10,5))
    p1=plt.bar(x,y, width=0.4, color='pink')
    p2=plt.bar(x,z, width=0.4, color='blue')
    p3=plt.bar(x,w, width=0.4, color='green')
    plt.xlabel("Categories")
    plt.ylabel("Number of Tweets")
    plt.title("The Distribution of Tweets Per Category")
    plt.legend((p1[0],p2[0],p3[0]),('Positive','Negative','Neutral'))
    plt.show()
    
    


if __name__ == "__main__":
    main()
    
    
    