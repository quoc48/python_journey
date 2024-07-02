from city_function import get_formatted_city

def test_city_country():
    city = get_formatted_city('santiago', 'chile')
    assert city == 'santiago, chile'

def test_city_country_population():
    city = get_formatted_city('santiago', 'chile', 10)
    assert city == 'santiago, chile - population 10'