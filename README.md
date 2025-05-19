# Intrusion Detection Tool by TechTitans

A cybersecurity project designed for the HACKTHON 2025 competition. This tool simulates network-based attacks, detects suspicious traffic, and logs alerts using Snort IDS and a Flask-based dashboard.

## Team
**TechTitans**  
University Project – 2025

## Description
This project focuses on:
- Simulating MITM and DNS spoofing attacks
- Detecting intrusions using Snort IDS
- Logging traffic and alerts
- Visualizing data using a lightweight Flask web dashboard

## Technologies Used
- **Kali Linux**
- **Snort** (Intrusion Detection System)
- **Flask** (Python web framework)
- **Python 3**

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Intrusion-Detection-Tool-by-TechTitans.git
cd Intrusion-Detection-Tool-by-TechTitans
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*Or manually install:*
```bash
pip install flask
```

### 3. Install Snort
```bash
sudo apt update
sudo apt install snort
```

### 4. Configure Snort
- Add custom rules in `/etc/snort/rules/local.rules`
- Restart Snort service:
```bash
sudo systemctl restart snort
```

---

## Running the Tool

### 1. Start the Flask App
```bash
python3 app.py
```

### 2. Monitor Alerts in Real-Time
```bash
tail -f /var/log/snort/alert
```

---

## Project Structure
```
Intrusion-Detection-Tool/
├── app.py                # Flask dashboard
├── templates/            # HTML files
├── static/               # CSS/JS (if used)
├── snort-config/         # Custom rules and setup
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## Future Enhancements
- Real-time alert notification via email or SMS
- Graph-based traffic analysis
- Integration with machine learning for anomaly detection

---

## License
MIT License

## Contact
**Team TechTitans**  
Email: techtitanscybersec@gmail.com  
GitHub: [github.com/TechTitans](https://github.com/TechTitans)
