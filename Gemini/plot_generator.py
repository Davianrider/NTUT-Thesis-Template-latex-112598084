import matplotlib.pyplot as plt
import numpy as np

# --- Data from your file ---
nodes = [11, 21, 31]
labels = ['11 Nodes', '21 Nodes', '31 Nodes']

# Average HopsToSink
avg_hops_native = [2.699, 3.524, 4.673]
avg_hops_modified = [2.009, 2.923, 3.561]

# Maximum HopsToSink
max_hops_native = [4.8, 6.5, 8.2]
max_hops_modified = [3.8, 5.7, 6.7]

# --- Configure font for Chinese characters ---
try:
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
except:
    plt.rcParams['font.sans-serif'] = ['sans-serif']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(len(labels))
width = 0.35

# --- Plot 1: Average HopsToSink ---
fig1, ax1 = plt.subplots(figsize=(8, 6))
rects1_avg = ax1.bar(x - width/2, avg_hops_native, width, label='Original FruityMesh')
rects2_avg = ax1.bar(x + width/2, avg_hops_modified, width, label='Modified (with hopsToSink)')

ax1.set_ylabel('Hops')
ax1.set_title('Average HopsToSink Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()
ax1.bar_label(rects1_avg, padding=3)
ax1.bar_label(rects2_avg, padding=3)
fig1.tight_layout()
plt.savefig(r'C:\Users\Davian\Downloads\Avg_hops_comparison.png')

# --- Plot 2: Maximum HopsToSink ---
fig2, ax2 = plt.subplots(figsize=(8, 6))
rects1_max = ax2.bar(x - width/2, max_hops_native, width, label='Original FruityMesh')
rects2_max = ax2.bar(x + width/2, max_hops_modified, width, label='Modified (with hopsToSink)')

ax2.set_ylabel('Hops')
ax2.set_title('Maximum HopsToSink Comparison')
ax2.set_xticks(x)
ax2.set_xticklabels(labels)
ax2.legend()
ax2.bar_label(rects1_max, padding=3)
ax2.bar_label(rects2_max, padding=3)
fig2.tight_layout()
plt.savefig(r'C:\Users\Davian\Downloads\Max_hops_comparison.png')