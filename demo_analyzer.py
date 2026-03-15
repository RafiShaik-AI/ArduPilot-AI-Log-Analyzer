import time

# A "Mock" database of flight logs for the demo
flight_data = [
    {"time": "10:00", "alt": 10, "vibe": 12, "msg": "GPS OK"},
    {"time": "10:01", "alt": 15, "vibe": 45, "msg": "VIBRATION WARNING"},
    {"time": "10:02", "alt": 5, "vibe": 20, "msg": "EKF VARIANCE ERROR"},
    {"time": "10:03", "alt": 0, "vibe": 10, "msg": "CRASH DETECTED"}
]

def ai_diagnosis_engine(logs):
    print("🤖 AI LOG ANALYZER STARTING...")
    time.sleep(1)
    
    for log in logs:
        print(f"[{log['time']}] Checking Altitude: {log['alt']}m | Vibe: {log['vibe']}")
        
        # This is where your AI logic "lives"
        if log['vibe'] > 40:
            print("   ⚠️ DIAGNOSIS: High mechanical vibration! Check propeller balance.")
        
        if "EKF" in log['msg']:
            print("   🚨 DIAGNOSIS: Compass/GPS interference. Possible magnetic shielding issue.")
            
        if "CRASH" in log['msg']:
            print("   🏁 SUMMARY: Flight ended in crash. Primary cause: Sensor inconsistency.")

if __name__ == "__main__":
    ai_diagnosis_engine(flight_data)