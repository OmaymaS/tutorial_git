import pandas as pd

df=pd.read_csv("labeled_data_raw.csv")

df=df[(df['question01']==1) & (df['tag_name'].isin(['Gym']))]


for col in df.columns:
    if "id" in col : 
        df[col]=df[col].astype(str).apply(lambda x:x.replace(".0",''))
for col in df.columns:
    if "image" in col : 
        df[col]=df[col].astype(str).apply(lambda x:x.replace("https://imgcy.trivago.com/c_limit,d_dummy.jpeg,f_auto,h_470,q_auto,w_805/","https://d7k6g2b9ef.execute-api.eu-west-1.amazonaws.com/prod/w_800/"))

df['tag_name']=df['tag_name'].str.lower() +'_'+ df['tag_id'].astype(str)
df=df.rename(columns={'tag_name':'tag'})

no_dupls=df.drop_duplicates(subset=['tag','image_id'],keep='last')

no_dupls.to_csv('gym_image_imageid_tag.csv',columns=['image_id','image','tag'],index=False)
no_dupls.to_csv('filtered_data_justgym.csv',columns=['accommodation_id','image','image_id','tag','project_id','question01'],index=False)

#Duplicates to csv
#duplicate_data=df[(df.duplicated(['tag','image_id']))].sort_values(by="image_id")
#duplicate_data.to_csv('duplicated_rows.csv',index=False)
