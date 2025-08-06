import matplotlib.pyplot as plt

# Data extracted from the file
packets = [125, 150, 175, 200, 250, 300, 600, 1200]
retransmission_rate = [0.4582, 0.992, 1.42, 1.03, 2.5, 1.9, 1.45, 2.89]
avg_delay = [153.9, 188.4, 183.2, 154, 212.2, 190.4, 193.1, 220.3]
pdr = [100, 100, 100, 100, 100, 100, 100, 100]

# Generate a list of strings for x-axis labels
x_labels = [str(p) for p in packets]
# Create an evenly spaced x-axis
x_ticks = range(len(packets))

# Create and save the Delay Time plot
plt.figure()
plt.plot(x_ticks, avg_delay, marker='o')
plt.title('Delay Time vs. Packets Sent')
plt.xlabel('Packets Sent per Node')
plt.ylabel('Average Delay (ms)')
plt.xticks(x_ticks, x_labels) # Set evenly spaced ticks with custom labels
plt.grid(True)
plt.savefig('C:/Users/Davian/Downloads/delay_time_trend.png')
plt.close()

# Create and save the PDR plot
plt.figure()
plt.plot(x_ticks, pdr, marker='o')
plt.title('PDR vs. Packets Sent')
plt.xlabel('Packets Sent per Node')
plt.ylabel('PDR (%)')
plt.xticks(x_ticks, x_labels) # Set evenly spaced ticks with custom labels
plt.ylim(90, 101)  # Adjust y-axis to 90-101%
plt.grid(True)
plt.savefig('C:/Users/Davian/Downloads/pdr_trend.png')
plt.close()

# Create and save the Retransmission Rate plot
plt.figure()
plt.plot(x_ticks, retransmission_rate, marker='o')
plt.title('Retransmission Rate vs. Packets Sent')
plt.xlabel('Packets Sent per Node')
plt.ylabel('Retransmission Rate (%)')
plt.xticks(x_ticks, x_labels) # Set evenly spaced ticks with custom labels
plt.grid(True)
plt.savefig('C:/Users/Davian/Downloads/retransmission_rate_trend.png')
plt.close()

print("Plots saved to C:/Users/Davian/Downloads/")