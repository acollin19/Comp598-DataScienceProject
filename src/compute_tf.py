'''
script that makes a JSON file with the category[word] = # word was used 

python3 compute_tf.py  -o output_words.json -f a.tsv
'''

import argparse
import pandas as pd
import json


def get_input():
    parser=argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--final')
    args=parser.parse_args()

    output=args.output
    total_file = args.final

    return output,total_file

def compile(d, stopwords):
    f = open(d, encoding = "ISO-8859-1")
    df = pd.read_csv(f, sep='\t')

    data ={}
    data["A"]={}
    data['B']={}
    data['C']={}
    data['F']={}
    data['R']={}
    data['O']={}
    ponctuations = ['(', ')', '[', ']', ',', '-', '.', '?', '!', ':', ';', '#', '&']

    for index, row in df.iterrows():
        category = row["topic"]
        if (category in data):
            s = row['title']
            #replace ponctuation with space 
            for p in ponctuations:
                if p in s:
                    s = s.replace(p, " ")
            slist = s.split()

            for word in slist:
                lword = word.lower()
                if ((lword.isalpha()) and (lword not in stopwords)):
                    #add word to pony 
                    if lword not in data[category]:
                        data[category][lword] = 1
                    else:
                        data[category][lword] +=1


    return data




    



def main():
    a_file = open("stopwords.txt", "r")
    lines = a_file. read()
    list_of_lists = lines. splitlines()
    stopwords = list_of_lists[6:]
    a_file.close()
    o,total_file = get_input()

    x = compile(total_file, stopwords)
    s = json.dumps(x, indent=4)
    with open(o, "w") as f:
        f.write(s)









if __name__ == '__main__':
    main()
        


