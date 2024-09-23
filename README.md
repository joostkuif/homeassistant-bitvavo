# homeassistant-bitvavo

## What it is
A small Homeassistant Custom Integration featuring a sensor tracking the total value (in EUR) of your bitvavo wallet.

## Why did i build it
Another side project. I just wanted to learn some basic Python programming as the market is demanding this language more and more recently. First i programmed the api calls in a cli. Then i thought why not make it available in Homeassistant? And here we are. :-)

## Configuration
In your Bitvavo account, you have to generate a API key and corresponding secret. The most important part is that 
<b>YOU ONLY GIVE IT READ RIGHTS</b>. 
I am not responsible for your keys if someone (gets their hands on them and) starts trading or does withdraw coins with your key.

The generated API key and secret should be saved for later use when you install and configure this Custom Integration.