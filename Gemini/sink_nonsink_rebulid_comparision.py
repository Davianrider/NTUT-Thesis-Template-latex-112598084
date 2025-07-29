import matplotlib.pyplot as plt
import numpy as np
import os

# 設定字體以正確顯示中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 圖片中的數據
labels = ['11點', '21點', '31點']
sink_means = [15.09, 21.72, 25.82]
sink_std = [4.78, 4.96, 4.31]
non_sink_means = [10.93, 11.52, 11.96]
non_sink_std = [2.9, 2.1, 1.89]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots(figsize=(10, 7))

# 繪製 Sink 節點的長條圖和誤差線
rects1 = ax.bar(x - width/2, sink_means, width, label='Sink節點斷線連回', yerr=sink_std,
   capsize=5, color='royalblue')
# 繪製非 Sink 節點的長條圖和誤差線
rects2 = ax.bar(x + width/2, non_sink_means, width, label='非Sink節點斷線連回',
   yerr=non_sink_std, capsize=5, color='lightcoral')
# 定義偏移量
mean_y_offset = 0.5  # 平均值標籤向上偏移量
mean_x_offset = 0.1 # 平均值標籤向右偏移量
std_y_offset = 0.5   # 標準差標籤向上偏移量

# 添加平均秒數的標籤 (手動放置，偏右)
for i, rect in enumerate(rects1):
    ax.text(rect.get_x() + rect.get_width()/2 + mean_x_offset, # X 軸位置：長條中心 + 向右偏移
            rect.get_height() + mean_y_offset, # Y 軸位置：長條高度 + 向上偏移
            f'{sink_means[i]:.2f}', # 顯示平均值，保留兩位小數
            ha='center', va='bottom', fontsize=9, color='black')

for i, rect in enumerate(rects2):
    ax.text(rect.get_x() + rect.get_width()/2 + mean_x_offset, # X 軸位置：長條中心 + 向右偏移
            rect.get_height() + mean_y_offset, # Y 軸位置：長條高度 + 向上偏移
            f'{non_sink_means[i]:.2f}', # 顯示平均值，保留兩位小數
            ha='center', va='bottom', fontsize=9, color='black')

# 添加標準差的數值標籤 (顯示在誤差線上方)
for i, rect in enumerate(rects1):
    # 計算文字的垂直位置：長條高度 (平均值) + 標準差 + 向上偏移
    y_pos = rect.get_height() + sink_std[i] + std_y_offset
    ax.text(rect.get_x() + rect.get_width()/2, y_pos, # X 軸位置：長條中心
            f'±{sink_std[i]:.2f}', # 顯示標準差，保留兩位小數，帶 ± 符號
            ha='center', va='bottom', fontsize=9, color='black')

for i, rect in enumerate(rects2):
    # 計算文字的垂直位置：長條高度 (平均值) + 標準差 + 向上偏移
    y_pos = rect.get_height() + non_sink_std[i] + std_y_offset
    ax.text(rect.get_x() + rect.get_width()/2, y_pos, # X 軸位置：長條中心
            f'±{non_sink_std[i]:.2f}', # 顯示標準差，保留兩位小數，帶 ± 符號
            ha='center', va='bottom', fontsize=9, color='black')

# 添加標籤、標題和坐標軸刻度的文字
ax.set_ylabel('Mesh完成時間 (秒)')
ax.set_xlabel('節點數量')
ax.set_title('不同節點數量下Sink與非Sink節點斷線重連時間比較')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
fig.tight_layout()

# 儲存圖表為圖片檔案
plt.savefig('bar_chart_custom_labels.png')

print('長條圖已成功儲存至 bar_chart_custom_labels.png')