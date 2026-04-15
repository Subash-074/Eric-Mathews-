#Privileges: 
class User:
      def __init__(self, login_attempts):
            self.login_attempts=login_attempts

      def increment_login_attempt(self):
            self.login_attempts+=1
            print(f'Number of attempts to login till now is {self.login_attempts}')

      def reset_login_attempts(self):
            self.login_attempts=0
            print(f'The number of login attepmt is reset to {self.login_attempts}')


class Privileges():
      def __init__(self):
            self.previlages=['can add user', 'can del user ', 'can access user']

      def show_previlages(self):
            print('Admin Previlages')
            for previlage in self.previlages:
                  print(f'{previlage}')


class Admin(User):
      def __init__(self, login_attempts):
            super().__init__(login_attempts)
            self.previlages = Privileges()


request = Admin(1)
request.increment_login_attempt()
request.reset_login_attempts()
request.previlages.show_previlages()
