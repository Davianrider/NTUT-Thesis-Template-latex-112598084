
import matplotlib.pyplot as plt
import numpy as np
import os

# --- Data Setup ---
packets = [25, 50, 75, 100]
output_path = r'G:\其他電腦\我的筆記型電腦\研究所\霸昏論文資料'

# Data for Avg Packet Delay (ms)
delay_fruitymesh = [966.07, 1314.86, 1595.63, 1734.08]
delay_dost = [704.4, 848.2, 890.72, 978.05]
delay_ci = [175.4, 179.5, 184.7, 167.8]

# Data for Avg Retransmission Rate (%)
retrans_fruitymesh = [126, 113, 110.35, 111.22]
retrans_dost = [14.33, 15.09, 18.26, 18.95]
retrans_ci = [0.0727, 0.2544, 0.3151, 1.2545]

# Data for PDR (%)
pdr_fruitymesh = [99, 86.06, 75.23, 73.08]
pdr_dost = [100, 100, 100, 100]
pdr_ci = [100, 100, 100, 100] # PDR was 1, which is 100%

# --- Font Configuration for Chinese Characters ---
try:
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
except:
    plt.rcParams['font.sans-serif'] = ['sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# --- Create Output Directory if it doesn't exist ---
if not os.path.exists(output_path):
    os.makedirs(output_path)

# --- Plot 1: Avg Packet Delay ---
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(packets, delay_fruitymesh, marker='o', linestyle='-', label='FruityMesh')
ax1.plot(packets, delay_dost, marker='s', linestyle='--', label='DOST')
ax1.plot(packets, delay_ci, marker='^', linestyle='-.', label='層級式CI調整')
ax1.set_xlabel('發送封包數 (packet)')
ax1.set_ylabel('平均封包延遲 (ms)')
ax1.set_title('平均封包延遲比較')
ax1.set_xticks(packets)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)
fig1.tight_layout()
plt.savefig(os.path.join(output_path, 'Avg_Packet_Delay_Comparison.png'))
plt.close(fig1)

# --- Plot 2: Avg Retransmission Rate ---
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(packets, retrans_fruitymesh, marker='o', linestyle='-', label='FruityMesh')
ax2.plot(packets, retrans_dost, marker='s', linestyle='--', label='DOST')
ax2.plot(packets, retrans_ci, marker='^', linestyle='-.', label='層級式CI調整')
ax2.set_xlabel('發送封包數 (packet)')
ax2.set_ylabel('平均重傳率 (%)')
ax2.set_title('平均重傳率比較')
ax2.set_xticks(packets)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)
fig2.tight_layout()
plt.savefig(os.path.join(output_path, 'Avg_Retransmission_Rate_Comparison.png'))
plt.close(fig2)

# --- Plot 3: Packet Delivery Rate (PDR) ---
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.plot(packets, pdr_fruitymesh, marker='o', linestyle='-', label='FruityMesh')
ax3.plot(packets, pdr_dost, marker='s', linestyle='--', label='DOST')
ax3.plot(packets, pdr_ci, marker='^', linestyle='-.', label='層級式CI調整')
ax3.set_xlabel('發送封包數 (packet)')
ax3.set_ylabel('封包交付率 (%)')
ax3.set_title('封包交付率 (PDR) 比較')
ax3.set_xticks(packets)
ax3.set_ylim(min(pdr_fruitymesh) - 5, 101) # Adjust y-axis to better see the lines
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.6)
fig3.tight_layout()
plt.savefig(os.path.join(output_path, 'PDR_Comparison.png'))
plt.close(fig3)

print(f"圖表已成功儲存至 {output_path}")
