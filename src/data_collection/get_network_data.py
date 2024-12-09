import requests
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='/tmp/network_data_collection.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

ROUTER_API_URL = os.environ.get("ROUTER_API_URL")   # e.g. http://192.168.1.1/api
API_KEY = os.environ.get("ROUTER_API_KEY")

def fetch_device_data():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{ROUTER_API_URL}/devices", headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    try:
        data = fetch_device_data()
        # Process data as needed. For now, just log and store as JSON in a temporary file
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        output_file = f"/tmp/device_data_{timestamp}.json"
        with open(output_file, "w") as f:
            f.write(str(data))
        logging.info("Data successfully fetched and stored: %s", output_file)
    except requests.exceptions.RequestException as e:
        logging.error("Error fetching data: %s", e)
        raise

if __name__ == "__main__":
    main()
