def determine_aqi_category(pm25):
    if pm25 <= 12.0:
        return "Good"
    elif pm25 <= 35.4:
        return "Moderate"
    elif pm25 <= 55.4:
        return "Unhealthy for Sensitive Groups"
    elif pm25 <= 150.4:
        return "Unhealthy"
    elif pm25 <= 250.4:
        return "Very Unhealthy"
    else:
        return "Hazardous"

if __name__ == "__main__":
    # Interaction example
    pm25 = float(input("PM2.5: "))
    aqi_category = determine_aqi_category(pm25)
    print("AQI: {}".format(aqi_category))
