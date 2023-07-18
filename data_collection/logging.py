import psutil
import time
import pynvml

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

def get_drive_info():
    drives = psutil.disk_partitions(all=True)
    drive_info = []

    for drive in drives:
        try:
            drive_usage = psutil.disk_usage(drive.mountpoint)
            drive_io_counters = psutil.disk_io_counters(perdisk=True).get(drive.device)
            
            if drive_io_counters is None:
                # Skip drives with no IO counters available
                continue
            
            drive_info.append({
                'device': drive.device,
                'mountpoint': drive.mountpoint,
                'usage': drive_usage.percent,
                'read_speed': drive_io_counters.read_bytes / 1024**2,  # Convert to MB
                'write_speed': drive_io_counters.write_bytes / 1024**2,  # Convert to MB
                'active_time': drive_io_counters.busy_time
            })
        except Exception as e:
            print(f"Error retrieving information for drive {drive.device}: {str(e)}")

    return drive_info

while True:
    # Get CPU utilization
    cpu_utilization = get_cpu_utilization()
    average_cpu_utilization = sum(cpu_utilization) / len(cpu_utilization)
    print('Average CPU Utilization: {:.2f}%'.format(average_cpu_utilization))
    for i, utilization in enumerate(cpu_utilization):
        print('Core', i, 'Utilization: {:.2f}%'.format(utilization))

    # Get CPU clock speed
    cpu_clock_speed = get_cpu_clock_speed()
    print('CPU Clock Speed: {:.2f} MHz'.format(cpu_clock_speed))

    # Get RAM usage
    ram_used, ram_total = get_ram_usage()
    print('RAM Usage: {:.2f}GB out of {:.2f}GB'.format(ram_used, ram_total))

    # Get GPU usage
    gpu_usages, gpu_vram_usages = get_gpu_usage()
    for i, usage in enumerate(gpu_usages):
        print('GPU', i, 'Usage: {:.2f}%'.format(usage))
        print('GPU', i, 'VRAM Usage: {:.2f}MB'.format(gpu_vram_usages[i]))

    # Get drive information
    drive_info = get_drive_info()
    for drive in drive_info:
        print('Drive:', drive['device'])
        print('Mount Point:', drive['mountpoint'])
        print('Usage:', drive['usage'], '%')
        print('Read Speed:', drive['read_speed'], 'MB/s')
        print('Write Speed:', drive['write_speed'], 'MB/s')
        print('Active Time:', drive['active_time'], 'seconds')

    print()  # Print an empty line for separation

    time.sleep(1)  # Wait for 1 second before the next iteration
