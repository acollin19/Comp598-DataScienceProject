'''

python3 filter.py -i <json file> -o <text tsv>
'''
import argparse
import csv
import json
def get_input():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', required=True)
    parser.add_argument('-o', required=True)
    args=parser.parse_args()

    input=args.i
    output=args.o
    root=None
    with open (input) as f:
        root = json.load(f)

    return root,output

def main():
    i,o=get_input()

    #print(type(i))  
    with open(o, "a") as out_file:
        tsv_writter = csv.writer(out_file, delimiter='\t')
        tsv_writter.writerow(['title', 'topic','code'])
        
        for post in i:
            t = post["text"]
            tsv_writter.writerow([t])
    #tsv_writter.writerow(t)





if __name__ == '__main__':
    main()
        



