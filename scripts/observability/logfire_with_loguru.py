import logfire
from loguru import logger

logger.configure(handlers=[logfire.loguru_handler()])
logger.info("Hello, {name}!", name="World")
