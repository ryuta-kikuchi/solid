class UserManager:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, user_data):
        self.user_repository.save(user_data)

class EmailSender:
    def send_welcome_email(self, email_address):
        print(f"Sending welcome email to {email_address}")
