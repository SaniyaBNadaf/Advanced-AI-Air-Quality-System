def send_alert(aqi):
    if aqi > 200:
        print("🚨 EMERGENCY ALERT: Severe air pollution detected!")
    elif aqi > 100:
        print("⚠️ WARNING: Air quality is unhealthy.")
    else:
        print("✅ SAFE: Air quality is acceptable.")

aqi_input = int(input("Enter AQI for alert check: "))
send_alert(aqi_input)
