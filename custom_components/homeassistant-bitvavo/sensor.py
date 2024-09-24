from homeassistant.helpers.entity import Entity
from python_bitvavo_api.bitvavo import Bitvavo

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Bitvavo sensor platform."""
    name = config_entry.data["name"]
    apikey = config_entry.data["apikey"]
    apisecret = config_entry.data["apisecret"]

    # Initialize the Bitvavo client with user-supplied API key and secret
    bitvavo_client = Bitvavo({
        'APIKEY': apikey,
        'APISECRET': apisecret,
        'RESTURL': 'https://api.bitvavo.com/v2',
        'WSURL': 'wss://ws.bitvavo.com/v2'
    })

    # Create a unique ID based on the name, for example
    unique_id = f"bitvavo_{name.replace(' ', '_').lower()}"

    async_add_entities([BitvavoPriceSensor(name, bitvavo_client, unique_id)])

class BitvavoPriceSensor(Entity):
    """Representation of a Bitvavo wallet sensor."""

    def __init__(self, name: str, client: Bitvavo, unique_id: str):
        """Initialize the sensor."""
        self._name = name
        self._client = client
        self._price = None
        self._unique_id = unique_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the current price of the bitvavo wallet."""
        return self._price

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement (EUR for Euro)."""
        return "EUR"

    @property
    def unique_id(self):
        """Return the unique ID for this sensor."""
        return self._unique_id

    @property
    def icon(self):
        """Return the icon for this sensor."""
        return "mdi:currency-eur"

    @property
    def entity_picture(self):
        """Return the picture for the sensor."""
        return "/local/bitvavo.png"  # 'local' refers to the www folder

    def update(self):
        """Fetch the latest price from Bitvavo API."""
        try:            
            prices = {}
            # Fetch the balance and prices of all coins
            balances = self._client.balance() # Fetch the balance of all your coins (this is where your API key and secret are used)
            tickers = self._client.tickerPrice() #Fetch the current price of all markets. (public data)
            print(f"tickers: {tickers}")

            # Cache the prices of all markets in a key/value array for faster lookups
            for item in tickers:
                print(item)
                if 'price' in item:
                    prices.update({item['market']: item['price']})

            total_balance = 0.0

            # Calculate the total balance in EUR by converting the balances to EUR and accumulating the values of each coin.
            for balance in balances:
                # Fetch the current price of the coin to convert to a common currency (EUR)
                symbol = f"{balance['symbol']}-EUR"
                if symbol == 'EUR-EUR':
                    current_price = 1.0
                else:
                    current_price = prices.get(symbol, {'price': 0.0})  # add the market to the list if it doesn't exist.

                # Calculate the total value of the coin
                coin_balance = float(balance['available'])

                #if there is a coin in order, accumulate the inOrder value as well
                if balance['inOrder']:
                    coin_balance += float(balance['inOrder'])

                total_value = coin_balance * float(current_price)

                # Accumulate the total balance
                total_balance += total_value

                print(f"{balance['symbol']} - Balance: {coin_balance} - Price: {current_price} - Value: {total_value}")

            print(f"\nTotal Balance in EUR: {total_balance}")
            self._price = round(float(total_balance), 2)
            
        except Exception as err:
            self._price = None
            print(f"Error fetching data from Bitvavo: {err}")
