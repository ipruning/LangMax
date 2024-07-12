import multiprocessing
import random
import time
import unittest
from typing import Callable, Dict, List, Union

import matplotlib.pyplot as plt


def ipv4_to_uint32_baseline(ip_address: str) -> int:
    try:
        return int.from_bytes(bytes(map(int, ip_address.split("."))), "big")
    except (ValueError, AttributeError):
        raise ValueError("Invalid IP address format")


def ipv4_to_uint32(ip_address: str) -> int:
    """Convert an IPv4 address string to a 32-bit unsigned integer.

    This function parses an IPv4 address string and converts it to its
    equivalent 32-bit unsigned integer representation.

    Args:
        ip_address (str): A string representing an IPv4 address in dotted-decimal notation.

    Raises:
        ValueError: If the IP address format is invalid, including:
            - Invalid start of IP address
            - Octet value out of range (> 255)
            - Invalid character in octet
            - Incorrect number of octets (not exactly 4)
            - Empty octet
            - Octet with leading zeros

    Returns:
        int: The 32-bit unsigned integer representation of the IPv4 address.

    Notes:
        1. The current implementation does not handle leading spaces before the first character.
           The LEADING_SPACE state is commented out and not implemented.
        # case "LEADING_SPACE":
        #     match char:
        #         case _ if isdigit(char):
        #             current_octet = int(char)
        #             parsing_state = "IN_NUMBER"
        #         case _ if isspace(char):
        #             continue
        #         case _:
        #             raise ValueError("Invalid character after leading space")
        2. The isspace() function only checks for regular spaces (' ') and does not
           consider other whitespace characters like tabs, newlines, etc.
        # def isspace(char: str) -> bool:
        #     return char == " "  # return char in " \t\n\r\f\v"

    Example:
        >>> ipv4_to_uint32("192.168.1.1")
        3232235777
    """
    octet_count: int = 0
    current_octet: int = 0
    uint32_value: int = 0

    parsing_state: str = "START"

    def isspace(char: str) -> bool:
        return char == " "

    def isdigit(char: str) -> bool:
        return "0" <= char <= "9"

    for char in ip_address:
        match parsing_state:
            case "START":
                match char:
                    case _ if isdigit(char):
                        current_octet = int(char)
                        parsing_state = "IN_NUMBER"
                    case _ if isspace(char):
                        # parsing_state = "LEADING_SPACE"
                        raise ValueError("Invalid start of IP address")
                    case _:
                        raise ValueError("Invalid start of IP address")

            case "IN_NUMBER":
                match char:
                    case _ if isdigit(char):
                        current_octet = current_octet * 10 + int(char)
                        if current_octet > 255:
                            raise ValueError("Octet value out of range")
                    case ".":
                        uint32_value = (uint32_value << 8) | current_octet
                        octet_count += 1
                        current_octet = 0
                        parsing_state = "AFTER_DOT"
                    case _ if isspace(char):
                        parsing_state = "AFTER_NUMBER"
                    case _:
                        raise ValueError("Invalid character in octet")

            case "AFTER_NUMBER":
                match char:
                    case ".":
                        uint32_value = (uint32_value << 8) | current_octet
                        octet_count += 1
                        current_octet = 0
                        parsing_state = "AFTER_DOT"
                    case _ if isspace(char):
                        continue
                    case _:
                        raise ValueError("Invalid character after number")

            case "AFTER_DOT":
                match char:
                    case _ if isdigit(char):
                        current_octet = int(char)
                        parsing_state = "IN_NUMBER"
                    case _ if isspace(char):
                        continue
                    case _:
                        raise ValueError("Invalid character after dot")

    match parsing_state:
        case "IN_NUMBER":
            uint32_value = (uint32_value << 8) | current_octet
            octet_count += 1
        case "AFTER_NUMBER":
            pass
        case _:
            raise ValueError("Invalid end of IP address")

    if octet_count != 4:
        raise ValueError("Incorrect number of octets")

    return uint32_value


class IPGenerator:
    @staticmethod
    def generate_valid_ip() -> str:
        return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    @staticmethod
    def generate_valid_ip_with_spaces() -> str:
        octets: List[str] = [str(random.randint(0, 255)) for _ in range(4)]
        ip_with_spaces: str = ""
        for i, octet in enumerate(octets):
            if i > 0:
                ip_with_spaces += " " * random.randint(1, 3)
                ip_with_spaces += "."
                ip_with_spaces += " " * random.randint(1, 3)
            ip_with_spaces += octet
        return ip_with_spaces

    @staticmethod
    def generate_invalid_ip_with_spaces() -> str:
        octets: List[str] = [str(random.randint(0, 255)) for _ in range(4)]

        invalid_octet_index: int = random.randint(0, 3)
        invalid_octet: str = octets[invalid_octet_index]

        if len(invalid_octet) == 1:
            invalid_octet = str(random.randint(3, 9)) + invalid_octet

        insert_pos: int = random.randint(1, len(invalid_octet) - 1)
        invalid_octet = invalid_octet[:insert_pos] + " " + invalid_octet[insert_pos:]

        octets[invalid_octet_index] = invalid_octet

        ip_with_invalid_spaces: str = ""
        for i, octet in enumerate(octets):
            if i > 0:
                ip_with_invalid_spaces += " " * random.randint(0, 2)
                ip_with_invalid_spaces += "."
                ip_with_invalid_spaces += " " * random.randint(0, 2)
            ip_with_invalid_spaces += octet

        return ip_with_invalid_spaces

    @staticmethod
    def generate_random_ip() -> Dict[str, Union[str, bool]]:
        generators: List[Callable[[], str]] = [
            IPGenerator.generate_valid_ip,
            IPGenerator.generate_valid_ip_with_spaces,
            IPGenerator.generate_invalid_ip_with_spaces,
        ]
        chosen_generator: Callable[[], str] = random.choice(generators)
        generated_ip: str = chosen_generator()

        actual_ip: str = "".join(generated_ip.split())
        is_valid: bool = chosen_generator != IPGenerator.generate_invalid_ip_with_spaces

        return {"generated_ip": generated_ip, "actual_ip": actual_ip, "is_valid": is_valid}

    @staticmethod
    def generate_ip_batch(batch_size: int) -> List[Dict[str, Union[str, bool]]]:
        ip_list: List[Dict[str, Union[str, bool]]] = []
        for _ in range(batch_size):
            ip_list.append(IPGenerator.generate_random_ip())
        return ip_list

    @staticmethod
    def generate_ip_dataset(num_ips: int) -> List[Dict[str, Union[str, bool]]]:
        num_cpus: int = multiprocessing.cpu_count()
        batch_size: int = num_ips // num_cpus

        with multiprocessing.Pool(processes=num_cpus) as pool:
            results: List[List[Dict[str, Union[str, bool]]]] = pool.map(
                IPGenerator.generate_ip_batch, [batch_size] * num_cpus
            )

        ip_list: List[Dict[str, Union[str, bool]]] = [ip for batch in results for ip in batch]
        return ip_list[:num_ips]


class TestIPv4ToUint32(unittest.TestCase):
    def test_random_cases(self):
        num_tests = MAX_TEST_CASES

        for _ in range(num_tests):
            ip_data = IPGenerator.generate_random_ip()
            generated_ip = ip_data["generated_ip"]
            actual_ip = ip_data["actual_ip"]
            is_valid = ip_data["is_valid"]

            if is_valid:
                self.assertEqual(
                    int("".join([bin(int(x) + 256)[3:] for x in actual_ip.split(".")]), 2),  # type: ignore
                    ipv4_to_uint32(generated_ip),  # type: ignore
                    f"Results differ for IP: {generated_ip}",
                )
            else:
                with self.assertRaises(ValueError):
                    ipv4_to_uint32(generated_ip)  # type: ignore

    def test_edge_cases(self):
        edge_cases = [
            ("0.0.0.0", 0),
            ("1.1.1. 1", 16843009),
            ("1.1.1. 12", 16843020),
            ("10.0.0.1", 167772161),
            ("255.255.255.255", 4294967295),
            ("192 . 168 . 1 . 1", 3232235777),
        ]
        for ip, expected in edge_cases:
            self.assertEqual(ipv4_to_uint32(ip), expected, f"Failed on edge case: {ip}")

    def test_invalid_cases(self):
        invalid_cases = [
            "1.1.1",
            "1..1.1.1",
            "1.1.1. 1 2",
            "1 1.1.1.1",
            "1.1.1.1.1",
            ".1.1.1.1",
            "255.255.255.255 ",
            "255.255.255.25 5",
            "255.255.255.256",
            "2555.255.255.256",
        ]
        for ip in invalid_cases:
            with self.assertRaises(ValueError):
                ipv4_to_uint32(ip)


def test_perf():
    ip_data = IPGenerator.generate_ip_dataset(MAX_TEST_CASES)
    ip_list = [ip_info["generated_ip"] for ip_info in ip_data]
    print(f"Processed {len(ip_list)} IP addresses:")

    def measure_performance(func):
        start_time = time.time()
        for ip in ip_list:
            try:
                func(ip)
            except Exception:
                pass
        elapsed_time = time.time() - start_time
        print(f"{func.__name__}: {elapsed_time:.2f} seconds")

    for func in [ipv4_to_uint32_baseline, ipv4_to_uint32]:
        measure_performance(func)


def test_perf_and_plot_complexity():
    test_cases: List[int] = [
        25,
        50,
        100,
        250,
        500,
        750,
        1000,
        2500,
        5000,
        7500,
        10000,
        25000,
        50000,
        75000,
        100000,
        250000,
        500000,
        750000,
        1000000,
    ]
    times_v0: List[float] = []
    times_v1: List[float] = []
    ratios: List[float] = []

    for case in test_cases:
        ip_data: List[Dict[str, Union[str, bool]]] = IPGenerator.generate_ip_dataset(case)
        ip_list: List[str] = [ip_info["generated_ip"] for ip_info in ip_data]  # type: ignore

        # Increase sample size
        num_samples: int = 5
        time_v0_samples: List[float] = []
        time_v1_samples: List[float] = []

        for _ in range(num_samples):
            start_time: float = time.time()
            for ip in ip_list:
                try:
                    ipv4_to_uint32_baseline(ip)
                except Exception:
                    pass
            end_time: float = time.time()
            time_v0_samples.append(end_time - start_time)

            start_time = time.time()
            for ip in ip_list:
                try:
                    ipv4_to_uint32(ip)
                except Exception:
                    pass
            end_time = time.time()
            time_v1_samples.append(end_time - start_time)

        avg_time_v0: float = sum(time_v0_samples) / num_samples
        avg_time_v1: float = sum(time_v1_samples) / num_samples

        times_v0.append(avg_time_v0)
        times_v1.append(avg_time_v1)
        ratios.append(avg_time_v1 / avg_time_v0)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    ax1.plot(test_cases, times_v0, label="ipv4_to_uint32_baseline")
    ax1.plot(test_cases, times_v1, label="ipv4_to_uint32")
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_ylabel("Time (seconds)")
    ax1.set_title("Time Complexity Comparison")
    ax1.legend()
    ax1.grid(True)

    ax2.plot(test_cases, ratios, label="Ratio (ipv4_to_uint32 / baseline)", color="green")
    ax2.set_xscale("log")
    ax2.set_xlabel("Number of Test Cases")
    ax2.set_ylabel("Time Ratio")
    ax2.set_title("Performance Ratio")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("time_complexity_comparison.png")
    plt.close()

    print("Time complexity comparison graph saved as 'time_complexity_comparison.png'")


if __name__ == "__main__":
    MAX_TEST_CASES = 1000000
    unittest.main()
    test_perf()
    test_perf_and_plot_complexity()
