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

#question 7
mon_hoc = ["toan","ngu_van","ngoai_ngu"]
khoi_khtn = ["vat_li", "hoa_hoc", "sinh_hoc"]
khoi_khxh = ["lich_su", "dia_li", "gdcd"]
def find_med_avg(mon_hoc, data):
    for i in mon_hoc:
        avg_mon = data[i].mean()
        med_mon = data[i].median()
        print (f"Điểm trung bình học sinh đạt được trong môn {i}: {avg_mon}")
        print (f"Trung vị điểm đạt được của môn {i}: {med_mon}")

# Question 8
def max_score(mon_hoc, data):
    for i in mon_hoc:
        print (f"- Số lượng học sinh đạt điểm 10 môn {i}: {data.value_counts(i)[10.0]}")

# Questionn 9:
# Có 2170 thí sinh bỏ thi các toàn bộ môn trong khối nên ko xác định được thi khối nào
khoi_khtn_rot = (khtn[khoi_khtn+mon_hoc]<=1).any(axis=1).sum()
khoi_khxh_rot = (khxh[khoi_khxh+mon_hoc]<=1).any(axis=1).sum()
bo_thi_khoi = 2170 # tinh tu file report.txt
bo_thi_toan_bo = 4476

tong_thi_sinh = len(diem_full.index)+ bo_thi_toan_bo

rot_tot_nghiep = khoi_khtn_rot+khoi_khxh_rot+ bo_thi_khoi+ bo_thi_toan_bo
print (rot_tot_nghiep)
print ((rot_tot_nghiep/tong_thi_sinh)*100)

