<p align="center"><img src="https://user-images.githubusercontent.com/72194651/145438948-ed33b22f-fb8a-40e3-90fc-94d3bb594888.png" alt="Covid 19" height="200"/></p>
<h1 align="center">Covid 19 Vaccine Vaccination Data</h1>

Để crawl dữ liệu ta vào thư mục tiemchungcovidVN/**tiemchung1**

Sau đó, nhấn Shift + chuột phải chọn vào **Open powershell window here**

Nhập vào lệnh scrapy crawl bot_tiemchung1 -o <tên_file_csv>.csv

Dữ liệu được crawl về nằm ở thư mục tiemchungcovidVN/**tiemchung1**

**dulieutiemchung.csv**  là file chứa tất cả các dữ liệu về dữ liệu **chưa qua xử lý**

**dulieutiemchungdaxuly.csv**  là file chứa tất cả các dữ liệu về dữ liệu **đã xử lý**

Dữ liệu được xử lý thông qua file **suafile.py**

Thông tin dữ liệu:

- **stt**              - Số thứ tự các thành phố

- **thanhpho**         - Tên các thành phố

- **du_kien_phan_bo**  - Dự kiến KH phân bổ

- **phan_bo_thuc_te**  - Phân bổ thực tế

- **dan_so_du_dieu_kien_tiem** - Dân số >= 18 tuổi

- **so_lieu_da_tiem**  - Số liều đã tiêm

- **ty_le_du_kien_phan_bo_so_voi_dan_so** - Tỷ lệ dự kiến phân bổ theo kế hoạch/ dân số (>= 18 tuổi)

- **ty_le_da_phan_bo_thuc_te_so_voi_dan_so** - Tỷ lệ đã phân bổ/ dân số (>= 18 tuổi)

- **ty_le_dan_so_it_nhat_tiem_mot_mui** - Tỷ lệ đã tiêm ít nhất 1 mũi/ dân số (>= 18 tuổi)

- **ty_le_tiem_chung_tren_so_vacxin_phan_bo_thuc_te** - Tỷ lệ tiêm chủng/ Vắc xin phân bổ thực tế

- **ty_le_phan_bo_vacxin_so_voi_ca_nuoc**  - Tỷ lệ phân bổ vắc xin/Tổng số phân bổ cả nước
