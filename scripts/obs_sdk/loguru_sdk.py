import random
import string

from loguru import logger

if __name__ == "__main__":
    # Test different log levels with random data
    logger.debug(f"Debug: Random number {random.randint(1, 100)}")
    logger.info(f"Info: Random string {''.join(random.choices(string.ascii_letters, k=10))}")
    logger.warning(f"Warning: Random float {random.uniform(0.1, 1.0):.2f}")
    logger.error(f"Error: Random choice {random.choice(['Apple', 'Banana', 'Cherry'])}")
    logger.critical(f"Critical: Random boolean {random.choice([True, False])}")

    # Test exception logging with context
    try:
        random_dict = {"a": 1, "b": 2, "c": 3}
        random_key = random.choice(list(random_dict.keys()) + ["d"])
        value = random_dict[random_key]
    except KeyError as e:
        logger.exception(f"KeyError occurred when accessing key '{e.args[0]}'")

    # Test structured logging with more context
    user_actions = ["login", "logout", "purchase", "view_profile", "update_settings"]
    logger.info("User action", action=random.choice(user_actions), user_id=random.randint(1000, 9999))

    # Test context manager with random request IDs
    with logger.contextualize(request_id=f"req-{''.join(random.choices(string.hexdigits, k=6))}"):
        logger.info("Processing request")
        if random.random() < 0.5:
            logger.error("An error occurred during request processing")
        else:
            logger.info("Request processed successfully")

    # Test log file creation and rotation with varied log messages
    for i in range(10):
        log_type = random.choice(["info", "warning", "error"])
        if log_type == "info":
            logger.info(f"Info log rotation: {i} - Random data: {random.randint(1, 1000)}")
        elif log_type == "warning":
            logger.warning(f"Warning log rotation: {i} - Random float: {random.uniform(0.1, 100.0):.2f}")
        else:
            logger.error(
                f"Error log rotation: {i} - Random string: {''.join(random.choices(string.ascii_letters, k=5))}"
            )

    print("Log tests with random data completed. Please check your log files and console output.")
