import argparse
import pandas as pd 
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument('--InputFilePath', type = str, required = True)   ### '/Users/junesong/Downloads/Chase_Bank'
parser.add_argument('--OutputFilePath', type = str, required = True)   ### '/Users/junesong/Downloads/Chase_Bank_output'
parser.add_argument('--Keyword', type = str, required = True)  ### 'STRIPE'

args = parser.parse_args()

def bk_keyword_ChaseBankStatement(input_file_path, output_file_path, keyword):
    for file in os.listdir(input_file_path):
        data = pd.read_csv(os.path.join(input_file_path, file))
        data['DESCRIPTION_delim'] = data['DESCRIPTION'].apply(lambda x: re.split('[: ]', x))
        output_data = data.loc[data['DESCRIPTION_delim'].apply(lambda x: keyword in x), 
                               ['DATE', 'DESCRIPTION', 'RECEIVED']]
        output_data.to_csv(os.path.join(output_file_path, file), index = False)

bk_keyword_ChaseBankStatement(args.InputFilePath, args.OutputFilePath, args.Keyword)