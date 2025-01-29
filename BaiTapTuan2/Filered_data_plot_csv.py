import os
import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn đến thư mục chứa các tệp CSV
directory = r'C:\Users\My-PC\Documents\IOT\dataset\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\Filtered_data'

# Đọc dữ liệu từ tệp s01_ex01_s02.csv
csv_file = 's01_ex01_s02.csv'
csv_file_path = os.path.join(directory, csv_file)

# Đọc tệp CSV
data = pd.read_csv(csv_file_path, header=None)

# Hiển thị dữ liệu của tệp CSV
print(f"Hiển thị dữ liệu từ tệp: {csv_file}")
print(data.head())  # Hiển thị 5 dòng đầu tiên của dữ liệu

# Lấy dữ liệu từ các kênh P4, Cz, F8, T7 (các cột tương ứng)
channels = [1, 2, 3, 4]
colors = ['b', 'g', 'r', 'c']  # Màu sắc cho từng kênh

# Vẽ tín hiệu cho các kênh
plt.figure(figsize=(12, 6))
for idx, (channel, color) in enumerate(zip(channels, colors)):
    plt.subplot(len(channels), 1, idx+1)
    plt.plot(data.iloc[:, channel], color=color)  # Vẽ tín hiệu cho từng kênh
    plt.title(f"Tín hiệu từ kênh: {csv_file.split('.')[0]} - {['P4', 'Cz', 'F8', 'T7'][idx]}")
    plt.xlabel('Thời gian')
    plt.ylabel('Amplitude')

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.suptitle(f"Bản ghi: {csv_file}", fontsize=16)
plt.show()  # Hiển thị đồ thị
