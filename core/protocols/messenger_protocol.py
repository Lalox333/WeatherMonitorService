from typing import Protocol


class MessengerProtocol(Protocol):

    def send_message(self, message: str) -> None:
        ...