# class ConsoleLogManager:
#     _instance = None
#
#   def __new__(cls,*args,**kwargs):
#       if cls._instance is None:
#           cls._instance = super(ConsoleLogManager, cls).__new__(cls)
#       return cls._instance
#
#
#
#
# # Usage:
# log_manager1 = ConsoleLogManager()
# log_manager1.error_log = 'Error'
# log_manager2 = ConsoleLogManager()
# print(log_manager2.error_log)
#
# # Trying to create another instance will throw an error.
# # Uncommenting next line will throw an error.
# # another_log_manager = ConsoleLogManager()

# class ConsoleLogManager:
#     _instance = None
#
#     @staticmethod
#     def getInstance():
#         if ConsoleLogManager._instance is None:
#             ConsoleLogManager()
#         return ConsoleLogManager._instance
#
#     def __init__(self):
#         if ConsoleLogManager._instance is not None:
#             raise Exception("Only one instance of ConsoleLogManager!")
#         else:
#             ConsoleLogManager._instance = self
#
#     @staticmethod
#     def log(self, message):
#         print(f'Log entry: {message}')
#
#
# # Usage:
# log_manager = ConsoleLogManager.getInstance()
# log_manager.log("Singleton pattern in action!")
#
# # Trying to create another instance will throw an error.
# # Uncommenting next line will throw an error.
# # another_log_manager = ConsoleLogManager()


# Practical Example of Pattern Creation and Use in Python
class MorningGreeting:
    def greet(self):
        print('Good morning')


class AfternoonGretting:
    def greet(self):
        print('Good afternoon!')


class EveningGreeting:
    def greet(self):
        print('Good evening')


class GreetingFactory:
    def create_greeting(self, time_of_day):
        if time_of_day == 'morning':
            return MorningGreeting()
        elif time_of_day == 'afternoon':
            return AfternoonGretting()
        elif time_of_day == 'evening':
            return EveningGreeting()
        else:
            raise Exception('Unknown time of day!')


greeting_factory = GreetingFactory()
morning_greeting = greeting_factory.create_greeting('morning')

# Outputs: Good morning! Let's have a great day ahead.
morning_greeting.greet()
afternoon_greeting = greeting_factory.create_greeting('afternoon')

# Outputs: Good afternoon! Hope your day is going well.
afternoon_greeting.greet()
evening_greeting = greeting_factory.create_greeting('evening')

# Outputs: Good evening! Time to relax after a long day.
evening_greeting.greet()


#  Builder Pattern

class ReportBuilder:
    def __init__(self):
        self.report = {'title': '', 'date': '', 'content': ''}

    def set_title(self, title):
        self.report['title'] = title
        return self

    def set_date(self, date):
        self.report['date'] = date
        return self

    def set_content(self, content):
        self.report['content'] = content
        return self

    def build(self):
        return self.report


# Using the builder to create a report
builder = ReportBuilder()
report = builder.set_title('Annual Report') \
    .set_date('2024-03-23') \
    .set_content('This is the content of the annual report.') \
    .build()

print(f'Report Details: {report}')
