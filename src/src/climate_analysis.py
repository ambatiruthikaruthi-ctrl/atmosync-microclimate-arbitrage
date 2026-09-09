import pandas as pd
import numpy as np


def load_data(file_path):
    """Load climate data from CSV."""
    return pd.read_csv(file_path)


def calculate_location_summary(data):
    """Calculate average climate conditions for each location."""

    summary = data.groupby("location").agg(
        average_temperature_c=("temperature_c", "mean"),
        average_humidity_percent=("humidity_percent", "mean"),
        total_rainfall_mm=("rainfall_mm", "sum"),
        average_wind_speed_kmh=("wind_speed_kmh", "mean")
    ).reset_index()

    return summary


def calculate_temperature_difference(data):
    """Calculate temperature differences between locations."""

    temperature = data.groupby("location")["temperature_c"].mean()

    difference = temperature.max() - temperature.min()

    return difference


def detect_temperature_anomalies(data, threshold=2):
    """
    Detect temperature anomalies using standard deviation.
    """

    mean_temperature = data["temperature_c"].mean()
    std_temperature = data["temperature_c"].std()

    upper_limit = mean_temperature + threshold * std_temperature
    lower_limit = mean_temperature - threshold * std_temperature

    anomalies = data[
        (data["temperature_c"] > upper_limit) |
        (data["temperature_c"] < lower_limit)
    ].copy()

    return anomalies


def generate_climate_report(data):
    """Generate a basic AtmoSync climate report."""

    summary = calculate_location_summary(data)
    temperature_difference = calculate_temperature_difference(data)
    anomalies = detect_temperature_anomalies(data)

    report = {
        "location_summary": summary,
        "temperature_difference": temperature_difference,
        "temperature_anomalies": anomalies
    }

    return report


if __name__ == "__main__":

    file_path = "../data/raw/climate_data.csv"

    data = load_data(file_path)

    report = generate_climate_report(data)

    print("\n=== AtmoSync Climate Analysis ===\n")

    print("Location Summary:")
    print(report["location_summary"])

    print(
        f"\nTemperature difference between locations: "
        f"{report['temperature_difference']:.2f} °C"
    )

    print("\nTemperature Anomalies:")
    print(report["temperature_anomalies"])
