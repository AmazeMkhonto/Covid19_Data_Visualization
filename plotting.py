import json
import matplotlib.pyplot as plt
from datetime import datetime


def load_covid_data(filename):
    """
    Loads COVID-19 data from a JSON file.

    Args:
        filename: The path to the JSON file containing the data.

    Returns:
        A dictionary containing lists of dates, confirmed cases, deaths, and recovered cases.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return process_data(data)


def process_data(data):
    """
    Processes the loaded JSON data and extracts relevant information.

    Args:
        data: A dictionary containing COVID-19 data.

    Returns:
        A dictionary containing lists of dates, confirmed cases, deaths, and recovered cases.
    """
    dates = []
    confirmed_cases = []
    deaths = []
    recovered = []
    for entry in data:
        dates.append(datetime.strptime(entry['Date'], '%Y/%m/%d'))
        confirmed_cases.append(convert_to_int(entry['Total Confirmed Cases']))
        deaths.append(convert_to_int(entry['Total Deaths']))
        recovered.append(convert_to_int(entry['Total Recovered']))
    return {
        "dates": dates,
        "confirmed_cases": confirmed_cases,
        "deaths": deaths,
        "recovered": recovered
    }


def convert_to_int(value):
    """
    Attempts to convert a value to an integer, returns the original value on error.

    Args:
        value: The value to be converted.

    Returns:
        The integer value if successful, otherwise the original value.
    """
    if isinstance(value, str):
        try:
            return int(value.replace(" ", ""))  # Remove space before conversion (for strings)
        except ValueError:
            return value
    else:
        return value


def plot_covid_data(data):
    """
    Generates a plot showing the trends in confirmed cases, deaths, and recovered cases.

    Args:
        data: A dictionary containing lists of dates, confirmed cases, deaths, and recovered cases.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["dates"], data["confirmed_cases"], label='Total Confirmed Cases', color='blue')
    plt.plot(data["dates"], data["deaths"], label='Total Deaths', color='red')
    plt.plot(data["dates"], data["recovered"], label='Total Recovered', color='green')

    # Formatting
    plt.title('COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.show()


# Main program
if __name__ == '__main__':
    covid_data = load_covid_data("covid.json") 
    plot_covid_data(covid_data)