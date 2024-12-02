import psutil
import platform
from datetime import datetime
import socket

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {cpu_usage}%"

def check_memory():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}% ({memory.used / (1024**3):.2f} GB used of {memory.total / (1024**3):.2f} GB)"

def check_disk():
    disk = psutil.disk_usage('/')
    return f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB used of {disk.total / (1024**3):.2f} GB)"

def check_network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return "Network: Connected"
    except OSError:
        return "Network: Disconnected"

def generate_report():
    system_info = platform.uname()
    report = f"""
    System Health Report - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    System: {system_info.system} {system_info.release} ({system_info.version})
    Node Name: {system_info.node}
    Processor: {system_info.processor}
    Machine: {system_info.machine}

    {check_cpu()}
    {check_memory()}
    {check_disk()}
    {check_network()}
    """

    # Save report to file
    with open("system_health_report.txt", "w") as file:
        file.write(report)

    return report

if __name__ == "__main__":
    print("Generating system health report...")
    print(generate_report())
    print("Report saved to system_health_report.txt")
