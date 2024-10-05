# homeassistant-bitvavo

## What it is
A small Homeassistant Custom Integration featuring a sensor tracking the total value (in EUR) of your bitvavo wallet.

## Why did i build it
Another side project. I just wanted to learn some basic Python programming as the market is demanding this language more and more recently. First i programmed the api calls in a cli. Then i thought why not make it available in Homeassistant? And here we are. :-)

This integration polls the bitvavo every 30 seconds with only 2 requests. I might make the interval period configurable in a future release.

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=joostkuif&repository=homeassistant-bitvavo&category=Integration)

This integration can be installed using HACS.
To do it search for `homeassistant-bitvavo` in *Integrations* section.

### Manual

To install this integration manually you have to download [*bitvavo.zip*](https://github.com/joostkuif/homeassistant-bitvavo/archive/refs/tags/v1.0.0.zip) and extract its contents to `config/custom_components/bitvavo` directory:
```bash
mkdir -p custom_components/bitvavo
cd custom_components/bitvavo
wget https://github.com/joostkuif/homeassistant-bitvavo/archive/refs/tags/v1.0.0.zip
unzip v1.0.0.zip
rm v1.0.0.zip
```

## Configuration

### 1) Create an API key
In your Bitvavo account, you have to generate an API key and corresponding secret. The most important part is that
<b>YOU ONLY GIVE IT READ RIGHTS</b>.
I am not responsible for your keys if something or someone (gets their hands on them and) starts trading or does withdraw coins with your key.

The generated API key and secret should be saved for later use when you install and configure this Custom Integration.

### 2) Using UI in Homeassistant to configure the API key and secret

Use the button below:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=bitvavo)

#### Or do it Manually:

From the Home Assistant front page go to **Configuration** and then select **Integrations** from the list.

Use the "plus" button in the bottom right to add a new integration called **Bitvavo**.

The success dialog will appear or an error will be displayed in the popup.

