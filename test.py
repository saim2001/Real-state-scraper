import datetime
import re

def parse_address(address):
    # Regular expression pattern to match the postal code
    postal_code_pattern = r'\b[A-Za-z]\d[A-Za-z]\s*\d[A-Za-z]\d\b'

    # Regular expression pattern to match the city
    city_pattern = r'([^,]+),'

    # Regular expression pattern to match the state
    state_pattern = r',\s*([A-Za-z\s]+)'

    # Search for postal code
    postal_code_match = re.search(postal_code_pattern, address)
    postal_code = postal_code_match.group() if postal_code_match else None

    # Search for city
    city_match = re.search(city_pattern, address)
    city = city_match.group(1).strip() if city_match else None

    # Search for state
    state_match = re.search(state_pattern, address)
    state = state_match.group(1).strip() if state_match else None

    return city, state, postal_code


print(parse_address('#421 -170 SUMACH ST Toronto, Ontario M5A0C3'))
print(datetime.datetime.now().date())