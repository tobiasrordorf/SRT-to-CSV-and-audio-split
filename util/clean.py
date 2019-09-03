import string
import pandas as pd


def clean_unwanted_characters(final_csv_path):

    df_ds_final = pd.read_csv('./merged_csv/'+final_csv_path)

    df_ds_final['transcript'] = df_ds_final['transcript'].replace('<font color=#91FFFF>', '', regex=True)
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('<font color=#72FD59>', '', regex=True)
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('<font color=#E8E858>', '', regex=True)
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('<font color=#FFFFFF>', '', regex=True)
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('</font>', '', regex=True)





    #Characters to be removed
    punct = str(['.!"#$%&\'()*+,-/:;<–=>?@[\\]^_°`{}~ ̀ ̆ ̃ ́'])
    transtab = str.maketrans(dict.fromkeys(punct, ' '))
    df_ds_final = df_ds_final.dropna()

    df_ds_final['transcript'] = '£'.join(df_ds_final['transcript'].tolist()).translate(transtab).split('£')

    df_ds_final['transcript'] = df_ds_final['transcript'].str.lower()
    df_ds_final['transcript'] = df_ds_final['transcript'].replace('\s+', ' ', regex=True)
    df_ds_final['transcript'] = df_ds_final['transcript'].str.strip()

    #Save cleaned files
    final_path = final_csv_path[:-4]
    print('Length of ds_final: {}'.format(len(df_ds_final)))
    df_ds_final.to_csv('./merged_csv/'+final_path + '_cleaned.csv', header=True, index=False, encoding='utf-8-sig')

    print('Final Files cleaned of unwanted characters')
