from http import HTTPStatus


class InvalidOptionError(Exception):
    def __init__(self, importance, urgency, value_list: list) -> None:
        self.message = (
            {
                "error": {
                    "valid options": {"importance": value_list, "urgency": value_list},
                    "recieved options": {
                        "importance": importance,
                        "urgency": urgency,
                    },
                }
            },
            HTTPStatus.BAD_REQUEST,
        )

        super().__init__(self.message)
