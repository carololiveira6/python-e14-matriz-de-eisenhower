def verify_missing_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in required_keys if key not in data_keys]


def verify_required_key(data: dict, required_keys: list) -> list:
    data_keys = data.keys()

    return [key for key in data_keys if key not in required_keys]


def verify_value_option(data: dict, value_options: list) -> list:

    importance = data["importance"]
    urgency = data["urgency"]

    if importance in value_options and urgency in value_options:
        return True

    return False