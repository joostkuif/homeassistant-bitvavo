import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

class BitvavoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Bitvavo integration."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step where the user configures the integration."""
        errors = {}

        if user_input is not None:
            # Validation logic (optional)
            if not user_input["apikey"] or not user_input["apisecret"]:
                errors["base"] = "apikey_or_secret_missing"
            else:
                # If validation is passed, create an entry with the user input
                return self.async_create_entry(
                    title=user_input["name"],
                    data=user_input,
                )

        # Create form schema to ask for name, API key, and API secret
        data_schema = vol.Schema({
            vol.Required("name", default="Bitvavo Total value"): str,  # Default name
            vol.Required("apikey"): str,  # Required API key
            vol.Required("apisecret"): str,  # Required API secret
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return BitvavoOptionsFlow(config_entry)

class BitvavoOptionsFlow(config_entries.OptionsFlow):
    """Handle options for Bitvavo."""

    def __init__(self, config_entry):
        """Initialize the options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle the option form."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title=self.config_entry.data["name"],
                data=user_input,
            )

        # Form for options, allowing updates to the API key/secret if needed
        options_schema = vol.Schema({
            vol.Optional("name", default=self.config_entry.data["name"]): str,
            vol.Optional("apikey", default=self.config_entry.data["apikey"]): str,
            vol.Optional("apisecret", default=self.config_entry.data["apisecret"]): str,
        })

        return self.async_show_form(
            step_id="user", data_schema=options_schema, errors=errors
        )
