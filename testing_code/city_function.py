def get_formatted_city(city, country, population=None):
    """Generate a neatly formatted full city name."""
    if population is not None:
        city = f"{city}, {country} - population {population}"
    else:
        city = f"{city}, {country}"
    return city