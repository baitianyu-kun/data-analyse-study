import glob
import os
import pandas as pd
import json

# net_name为ours就是自己的net
net_name = 'fmr_origin'
base_path = f'D:\\GraduationProject\\AllExpResults\\XIDIAN\\modelnet40normals\\{net_name}_evaluate_all'
csv_save_path = f'./csvs/{net_name}'
isseen = 'unseen'
# data type: clean, noise, density...
for data_type in os.listdir(base_path):
    # zip或者其他文件不予处理
    if os.path.isdir(os.path.join(base_path,data_type)):
        evaluate_datas = sorted(glob.glob(os.path.join(base_path, data_type, isseen, "*", "*.json")), key=os.path.getmtime)
        df = pd.DataFrame(columns=('r_mse', 'r_mae', 't_mse', 't_mae', 'g_mse', 'residual_rotdeg', 'residual_transmag'))
        index = 0
        for data_path in evaluate_datas:
            f = open(data_path, "r")
            data = json.loads(f.read())
            df.loc[index] = data
            index += 1
        df.to_csv(os.path.join(csv_save_path, net_name + '_' + data_type + "_" + isseen + ".csv"), index=False, sep=',')
