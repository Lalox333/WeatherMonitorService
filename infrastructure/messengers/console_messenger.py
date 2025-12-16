from core.protocols.messenger_protocol import MessengerProtocol


class ConsoleMessenger(MessengerProtocol):

    def send_message(self, message: str) -> None:
        print(message)
