#login attempts:
class User:
      def __init__(self, login_attempts):
            self.login_attempts=login_attempts
      def increment_login_attempt(self):
            self.login_attempts+=1
            print(f'Number of attempts to login till now is {self.login_attempts}')
      def reset_login_attempts(self):
            self.login_attempts=0
            print(f'The number of login attepmt is reset to {self.login_attempts}')
      
hello=User(1)
hello.increment_login_attempt()
hello.reset_login_attempts()