'''
script that computes the 10 highest tf idf words for each category 

python3 analysis.py -c output_words.json -o result.json
'''

import json 
import argparse 
import os 
import math

#parse the args
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--counts')
parser.add_argument('-o', '--output')
args = parser.parse_args()

def compute(dialogs, num_words):
    categories = ["A", "B", "C", "F", "R", "O"]

    dictwords = {}
    dictwords["A"]={}
    dictwords['B']={}
    dictwords['C']={}
    dictwords['F']={}
    dictwords['R']={}
    dictwords['O']={}

    for cat in categories:
        numcategories = 6
        words = dialogs[cat]

        for word in words:
            this_cat_used = dialogs[cat][word]

            cat_used = 0
            for c in categories:
                if word in dialogs[c]:
                    cat_used +=1
            
            #calculate tdidf
            tf = this_cat_used
            idf = math.log((numcategories/cat_used))
            tfidf = tf * idf 

            #add tdidf to global dict 
            dictwords[cat][word] = tfidf
    
    #sort the dict and grab only the highest 10 
    for cc in categories:
        if (num_words > 0):
            sorted_tf_idf_scores = sorted((dictwords[cc]).items(), key=lambda x: x[1], reverse=True)
            dictwords[cc] = [x[0] for x in sorted_tf_idf_scores[:num_words]]

    return dictwords


def main():
    num_words = 10

    f = open(args.counts,)
    dialogs = json.load(f)

    x = compute(dialogs, num_words)

    #write to json file
    output = json.dumps(x, indent=1)
    with open(args.output, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()

