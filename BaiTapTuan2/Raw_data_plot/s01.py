import wfdb
import matplotlib.pyplot as plt
import os

# Đường dẫn đến bản ghi
data_path = r'C:\Users\My-PC\Documents\IOT\dataset\auditory-evoked-potential-eeg-biometric-dataset-1.0.0\WFDB_Files\Raw_data'

# Danh sách các bản ghi cần đọc
record_names = [
    "s01_ex01_s02", "s01_ex01_s03", "s01_ex02_s01", "s01_ex02_s02", "s01_ex02_s03",
    "s01_ex05", "s01_ex06", "s01_ex07", "s01_ex08", "s01_ex09", "s01_ex10"
]

# Danh sách màu sắc cho từng kênh
colors = ['b', 'g', 'r', 'c']  # Màu xanh dương, xanh lá, đỏ, cyan

# Lặp qua tất cả các bản ghi
for record_name in record_names:
    record_path = os.path.join(data_path, record_name)

    try:
        # Đọc bản ghi
        record = wfdb.rdrecord(record_path)

        # Lấy tín hiệu từ các kênh P4, Cz, F8, T7 
        channels = [0, 1, 2, 3]  
        # Vẽ tín hiệu
        plt.figure(figsize=(12, 6))
        for idx, (channel, color) in enumerate(zip(channels, colors)):
            plt.subplot(len(channels), 1, idx+1)
            plt.plot(record.p_signal[:, channel], color=color)
            plt.title(f"Tín hiệu từ kênh: {record.sig_name[channel]}")
            plt.xlabel('Thời gian')
            plt.ylabel('Amplitude')

        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.suptitle(f"Bản ghi: {record_name}", fontsize=16)
        plt.show()

    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file {record_name}.dat hoặc {record_name}.hea")
    except Exception as e:
        print(f"⚠️ Lỗi khi đọc {record_name}: {e}")
