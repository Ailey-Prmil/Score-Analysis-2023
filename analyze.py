import pandas as pd
import numpy as np
from collections import Counter

# Question 1
khtn = pd.read_csv(".\dataset\diem_thi_khoi_khtn.csv")
khxh = pd.read_csv(".\dataset\diem_thi_khoi_khxh.csv")

diem_full = pd.read_csv(".\dataset\diem_thi.csv")
dropout = pd.read_csv(".\dataset\dropout.csv", header = None, index_col=False)
districts = pd.read_csv(".\dataset\district.csv", index_col=0)

dropout = dropout[0].astype(str)
diem_full['sbd'] = diem_full['sbd'].astype(str)

def thu_khoa(data, cac_mon =[]) :
    khoi = data[cac_mon]
    khoi.set_index("sbd", inplace = True)
    khoi["score"] = khoi.sum(axis=1)
    khoi.sort_values(by="score", ascending=False, inplace=True)
    return (khoi)

# Question 3
def q3(dropout, diem_full):
    location_code = np.where(dropout.str.len()==7, dropout.str[0], dropout.str[0:2])
    students_loc = np.where(diem_full['sbd'].str.len()==7, diem_full["sbd"].str[0], diem_full["sbd"].str[0:2])
    dropout_dict = Counter(location_code)
    full_dict = Counter(students_loc)

    for key, val in dropout_dict.items():
        loc = districts.loc[int(key),"LOCATION"]
        total_students = full_dict[key]
        drop_rate = (val/(total_students+val))*100
        print (f'- {loc} có số lượng học sinh bỏ thi là: {val}')
        print ('Tỷ lệ bỏ thi tương ứng của khu vực là: {}%'.format(round(drop_rate, 3)))

# Question 4
def q4(diem_full):
    count = dict(diem_full.value_counts("ma_ngoai_ngu"))
    avg_language = diem_full.groupby(["ma_ngoai_ngu"])["ngoai_ngu"].mean()
    for index, avg in avg_language.items():
        print (f"- {index} có số lượng đăng ký là: ***{count[index]}***")
        print (f"\t> Điểm TB học sinh đạt được: {avg}")

print (diem_full.value_counts("gdcd")[0.0])