import string
import pandas as pd


def clean_unwanted_characters(final_csv_path):

    df_ds_final = pd.read_csv('./merged_csv/'+final_csv_path)

    #Characters to be removed
    punct = str(['.!"#$%&\'()*+,-/:;<=>?@[\\]^_°`{}~ ̀ ̆ ̃ ́'])
    transtab = str.maketrans(dict.fromkeys(punct, ' '))
    df_ds_final = df_ds_final.dropna()

    df_ds_final['transcript'] = '£'.join(df_ds_final['transcript'].tolist()).translate(transtab).split('£')

    df_ds_final['transcript'] = df_ds_final['transcript'].str.lower()
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('  ', ' ', regex=True)
    #Save cleaned files
    final_path = final_csv_path[:-4]
    df_ds_final.to_csv('./merged_csv/'+final_path + '_cleaned.csv', header=True, index=False, encoding='utf-8-sig')

    print('Final Files cleaned of unwanted characters')
