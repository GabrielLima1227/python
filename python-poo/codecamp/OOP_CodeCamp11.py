# Abstraction 
# Reduce Complexity by hiding Unnecessary details

class EmailService:
    def _connect(self) -> None:
        print("Connecting to email server")

    def _authenticate(self) -> None:
        print("Authenticating...")

    def send_email(self) -> None:
        self._connect()
        self._authenticate()
        print("Sending email...")
        self._disconnect()

    def _disconnect(self) -> None:
        print("Diconnecting from email server...")

email01 = EmailService()
email01.send_email()