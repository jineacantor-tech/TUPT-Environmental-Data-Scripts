# ==========================================
# Air Quality Index (AQI) Checker for Taguig
# Author: Regine Sophia Cantor (TUPT)
# ==========================================

def evaluate_air_quality():
    try:
        # Allows live keyboard input instead of a static value
        aqi_level = float(input("Enter current Taguig AQI Level: "))
        
        print(f"\nEvaluating air data parameters... [AQI: {aqi_level}]")
        
        if aqi_level <= 50:
            print("🟢 Status: Good. Air quality is safe. Perfect day for field research!")
        elif 51 <= aqi_level <= 100:
            print("🟡 Status: Moderate. Acceptable air quality for the community.")
        elif 101 <= aqi_level <= 150:
            print("🟠 Warning: Unhealthy for Sensitive Groups. Wear a protective mask.")
        else:
            print("🔴 Alert: Hazardous conditions detected! Restrict outdoor operations.")
            
    except ValueError:
        print("❌ Invalid entry. Please input a numerical value.")

if __name__ == "__main__":
    evaluate_air_quality()

