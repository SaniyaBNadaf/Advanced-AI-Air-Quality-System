def health_risk_analysis(aqi):
    if aqi <= 50:
        return "LOW", "Air quality is good. No health risk."
    elif aqi <= 100:
        return "MODERATE", "Sensitive people may feel discomfort."
    elif aqi <= 150:
        return "HIGH", "Breathing issues possible. Reduce outdoor activity."
    elif aqi <= 200:
        return "VERY HIGH", "Health effects for everyone."
    else:
        return "SEVERE", "Emergency condition. Stay indoors."

aqi_value = int(input("Enter AQI value: "))
risk, explanation = health_risk_analysis(aqi_value)

print("\n🧠 AI Health Risk Meter")
print("AQI:", aqi_value)
print("Risk Level:", risk)
print("AI Explanation:", explanation)
