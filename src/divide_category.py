'''
script that divides tweets by category

python3 divide_category.py -i a.tsv -c category_symbol -o tweet_category_file.txt
'''
import argparse
import pandas as pd
import csv

def get_input():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-c', '--category')
    parser.add_argument('-o', '--output')
    args=parser.parse_args()

    input=args.input
    output=args.output
    category=args.category

    return input,output,category

def main():
    i,o,c=get_input()
    f = open(i, encoding = "ISO-8859-1")
    df = pd.read_csv(f, sep='\t')

    #loop through the tweets and add only the ones in the specified category
    with open(o, "w") as out_file:
        tsv_writter = csv.writer(out_file, delimiter='\t')
        tsv_writter.writerow(['title', 'topic','code'])
        for index, row in df.iterrows():
            if str(row['topic']) in c:
                tsv_writter.writerow([row['title'], row['topic'], row['code']])
                #out_file.write(row["title"])
                #out_file.write("\n")


if __name__ == '__main__':
    main()
        




