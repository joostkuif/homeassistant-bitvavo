from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "bitvavo"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Bitvavo integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Bitvavo from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload Bitvavo config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
