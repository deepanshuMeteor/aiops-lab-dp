import sys
def detect_anomalies(log_file):
    with open(log_file, 'r') as f:
        for line in f:
            if 'error' in line.lower() or 'exception' in line.lower():
                print(f"Anomaly Detected: {line.strip()}")
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python log_anomaly_detector.py <log_file_path>")
        sys.exit(1)
    detect_anomalies(sys.argv[1])
