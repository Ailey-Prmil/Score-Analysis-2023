import pandas as pd
import numpy as np


def missing_values(data, cols, file):
    # Check the number of missing values in each field
    for i in cols:
        print (f"COl: {i} have {pd.isna(data['{}'.format(i)]).sum()} missing values", file=file)

def drop_out(data):
   # Create file dropout.txt containing sbd not attending examination
   dropout_tag = data.isna().all(axis=1)
   with open("dropout.txt", "w") as drop_out:
    temp = data.loc[dropout_tag, :]
    dropout_sbd = temp.index.values
    for i in dropout_sbd:
        drop_out.write(f"{i}\n")

# Access dataset
data_path = ".\diem_thi.csv"
data = pd.read_csv(data_path, index_col=0)
loc_code = pd.read_csv("district_code.txt", sep=" - ", index_col=0, engine="python")

cols = data.columns.values

# drop missing values from df
data.dropna(how="all", inplace=True)


khxh_tag = data[['vat_li', 'hoa_hoc', 'sinh_hoc']].isna().all(axis=1)
khtn_tag = data[['lich_su', 'dia_li', 'gdcd']].isna().all(axis=1)

temp = data[['lich_su', 'dia_li', 'gdcd', 'vat_li', 'hoa_hoc', 'sinh_hoc']].isna().all(axis=1)


khxh_grp = data.loc[khxh_tag, :]
khtn_grp = data.loc[khtn_tag, :]

# delete students who dont participate both groups
khxh_grp.dropna(how="all", subset=['lich_su', 'dia_li', 'gdcd', 'vat_li', 'hoa_hoc', 'sinh_hoc'], inplace=True)
khtn_grp.dropna(how="all", subset=['lich_su', 'dia_li', 'gdcd', 'vat_li', 'hoa_hoc', 'sinh_hoc'], inplace=True)

# drop unnecessary columns
khtn_grp.drop(['lich_su', 'dia_li', 'gdcd'], axis=1, inplace=True)
khxh_grp.drop(['vat_li', 'hoa_hoc', 'sinh_hoc'], axis=1, inplace=True)


data.fillna(0, inplace=True)
khtn_grp.fillna(0, inplace=True)
khxh_grp.fillna(0, inplace=True)

loc_code.to_csv("district.csv")

# khtn_grp.to_csv("diem_thi_khoi_khtn.csv")
# khxh_grp.to_csv("diem_thi_khoi_khxh.csv")
# data.to_csv("diem_thi.csv")
languages = data.ma_ngoai_ngu.value_counts()




   






