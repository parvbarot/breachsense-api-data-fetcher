# breachsense-api-data-fetcher

This is a Python script that retrieves data from the BreachSence API for a list of websites and saves the data to JSON files.

## Getting Started

### Prerequisites

To run this script, you will need:

- Python 3.x installed on your computer.
- The `requests` module installed. You can install it using pip:


- A license key for the BreachSence API. You can sign up for a free trial at [https://breachsense.io/](https://breachsense.io/).

### Usage

1. Clone or download this repository to your computer.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:


4. Follow the prompts to enter the website names (comma-separated), date (in YYYYMMDD format), and license key.
5. The script will retrieve data from the following endpoints for each website and save it to JSON files:

- combo
- creds
- darkweb
- radar
- sessions
- stealer

The JSON files will be saved in the same directory as the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This script was created using the [Requests](https://docs.python-requests.org/en/latest/) library and the [BreachSence API](https://breachsense.io/).
