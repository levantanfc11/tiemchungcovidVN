import os
import pandas as pd

path = os.getcwd() + "\\tiemchung1"
os.chdir(path)

df = pd.read_csv("dulieutiemchung.csv", encoding="utf-8")
df.columns = ["STT", "Tỉnh/Thành phố", "Dự kiến KH phân bổ", "Phân bổ thực tế", "Dân số >= 18 tuổi", "Số liều đã tiêm", "Tỷ lệ dự kiến phân bổ theo kế hoạch/ dân số (>= 18 tuổi)", "Tỷ lệ đã phân bổ/ dân số (>= 18 tuổi)", "Tỷ lệ đã tiêm ít nhất 1 mũi/ dân số (>= 18 tuổi)", "Tỷ lệ tiêm chủng/ Vắc xin phân bổ thực tế", "Tỷ lệ phân bổ vắc xin/Tổng số phân bổ cả nước"]
df.to_csv("dulieutiemchung.csv", index=False, encoding="utf-8")
