import logging
from typing import Any, Dict, Optional
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
# from homeassistant.const import CONF_NECO, CONF_NECO1
from homeassistant.helpers.selector import TemplateSelector
from homeassistant.helpers.template import Template, TemplateError

from .const import DOMAIN, ADDITIONAL_EXPORT_ELECTRICITY, ADDITIONAL_IMPORT_ELECTRICITY

logger = logging.getLogger(__name__)
