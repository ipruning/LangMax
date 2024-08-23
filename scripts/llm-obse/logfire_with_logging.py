from logging import basicConfig, getLogger

import logfire

logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])

logger = getLogger(__name__)
logger.error("Hello %s!", "Fred")
