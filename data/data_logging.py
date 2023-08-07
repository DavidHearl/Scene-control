import psutil
import time
import pynvml
import json
import matplotlib.pyplot as plt

def get_cpu_utilization():
    return psutil.cpu_percent(interval=1, percpu=True)

def get_cpu_clock_speed():
    cpufreq = psutil.cpu_freq()
    return cpufreq.current

def get_ram_usage():
    memory = psutil.virtual_memory()
    ram_used = round(memory.used / 1024**3, 2)  # Convert to GB
    ram_total = round(memory.total / 1024**3, 2)  # Convert to GB
    return ram_used, ram_total

def get_gpu_usage():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    gpu_usages = []
    gpu_vram_usages = []

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_usages.append(util.gpu)

        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        gpu_vram_usages.append(mem_info.used / 1024**2)  # Convert to MB

    pynvml.nvmlShutdown()

    return gpu_usages, gpu_vram_usages


data_list = []

# Run the loop for 60 seconds
for _ in range(60):
    data = {}
    # Get CPU utilization
    cpu_utilization = get_cpu_utilization()
    average_cpu_utilization = sum(cpu_utilization) / len(cpu_utilization)
    data['Average CPU Utilization'] = round(average_cpu_utilization, 2)
    for i, utilization in enumerate(cpu_utilization):
        data[f'Core {i} Utilization'] = round(utilization, 2)

    # Get RAM usage
    ram_used, ram_total = get_ram_usage()
    data['RAM Usage'] = round(ram_used, 2)
    data['Total RAM'] = round(ram_total, 2)

    # Get GPU usage
    gpu_usages, gpu_vram_usages = get_gpu_usage()
    for i, usage in enumerate(gpu_usages):
        data[f'GPU {i} Usage'] = round(usage, 2)
        data[f'GPU {i} VRAM Usage'] = round(gpu_vram_usages[i], 2)

    # Append the data to the data_list
    data_list.append(data)

    # Wait for 1 second before the next iteration
    time.sleep(1)

# Save the data_list to a JSON file
file_path = 'data/logs/log_history/system_utilisation.json'
with open(file_path, 'w') as f:
    json.dump(data_list, f, indent=2)

print('Data collection completed. Data saved to', file_path)

# Extract the data for plotting
time_points = list(range(1, 61))  # Time points for x-axis
cpu_utilization_data = [d['Average CPU Utilization'] for d in data_list]
ram_usage_data = [d['RAM Usage'] for d in data_list]
gpu_usage_data = [d['GPU 0 Usage'] for d in data_list]  # Assuming there's only one GPU

# Plot CPU utilization
plt.figure(figsize=(10, 6))
plt.plot(time_points, cpu_utilization_data, label='CPU Utilization', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Utilization (%)')
plt.title('CPU Utilization Over Time')
plt.grid(True)
plt.legend()
plt.savefig('data/logs/cpu_usage/cpu_utilization.png')
# plt.show()

# Plot RAM usage
plt.figure(figsize=(10, 6))
plt.plot(time_points, ram_usage_data, label='RAM Usage', marker='o', color='orange')
plt.xlabel('Time (seconds)')
plt.ylabel('RAM Usage (GB)')
plt.title('RAM Usage Over Time')
plt.grid(True)
plt.legend()
plt.savefig('data/logs/ram_usage/ram_usage.png')
# plt.show()

# Plot GPU usage
plt.figure(figsize=(10, 6))
plt.plot(time_points, gpu_usage_data, label='GPU Usage', marker='o', color='green')
plt.xlabel('Time (seconds)')
plt.ylabel('GPU Usage (%)')
plt.title('GPU Usage Over Time')
plt.grid(True)
plt.legend()
plt.savefig('data/logs/gpu_usage/gpu_usage.png')
# plt.show()
