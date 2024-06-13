import base64

from decouple import config


def unwrap_env_var(name: str) -> str:
    value = config(name)
    if value is None:
        raise ValueError(f"{name} environment variable is not set")
    return str(value)


def encode_id_to_base64(loan_id: int) -> str:
    id_bytes = loan_id.to_bytes((loan_id.bit_length() + 7) // 8, "big")
    base64_bytes = base64.urlsafe_b64encode(id_bytes)
    base64_str = base64_bytes.decode("utf-8")
    return base64_str.rstrip("=")


def decode_base64_to_id(encoded_id: str) -> int:
    padding = "=" * (4 - len(encoded_id) % 4)
    encoded_id += padding
    id_bytes = base64.urlsafe_b64decode(encoded_id)
    loan = int.from_bytes(id_bytes, "big")
    return loan


#
#
# def calc_contract_percentage(amount: int, percent: int) -> int:
#     result = (percent.native * amount.native) // ap.UInt64(100)
#     return A4UInt64(result)


def calc_amount_plus_fee(amount: int) -> int:
    percentage = (5 * (amount * 10)) // 100
    return (percentage // 10) + amount
