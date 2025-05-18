def read_alerts(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        alerts = []
        for line in lines[-20:]:  # last 20 alerts
            if line.strip():
                parts = line.split("]")
                timestamp = parts[0].replace("[", "").strip()
                msg = parts[1].strip() if len(parts) > 1 else "Alert"
                alerts.append({"timestamp": timestamp, "alert": msg})
        return alerts
    except Exception as e:
        return [{"timestamp": "ERROR", "alert": str(e)}]
