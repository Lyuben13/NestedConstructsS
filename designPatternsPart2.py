# # # # # # Adapter pattern
# # # # # # # class OldLogger:
# # # # # # #     def log_error(self, msg):
# # # # # # #         print(f'Error: {msg}')
# # # # # # #
# # # # # # #     def log_info(self, msg):
# # # # # # #         print(f'Info: {msg}')
# # # # # # #
# # # # # # #
# # # # # # # class NotificationSystem:
# # # # # # #     def notify(self, level, message):
# # # # # # #         pass
# # # # # # #
# # # # # # #
# # # # # # # class LoggerAdapter(NotificationSystem):
# # # # # # #     def __init__(self, logger):
# # # # # # #         self.logger = logger
# # # # # # #
# # # # # # #     def notify(self, level, message):
# # # # # # #         if level == 'error':
# # # # # # #             self.logger.log_error(message)
# # # # # # #         elif level == 'info':
# # # # # # #             self.logger.log_info(message)
# # # # # # #
# # # # # # #
# # # # # # # old_logger = OldLogger()
# # # # # # # logger_adapter = LoggerAdapter(old_logger)
# # # # # # # logger_adapter.notify('error', 'This is an error message.')
# # # # # # #
# # # # # # # logger_adapter.notify('info', 'This is an info message.')
# # # # # #
# # # # # # class OldMediaPlayer:
# # # # # #     def play_mp3(self, file):
# # # # # #         print(f'Playing MP3 file: {file}')
# # # # # #
# # # # # #
# # # # # # class AdvancedMediaPlayer:
# # # # # #     def play_mp4(self, file):
# # # # # #         print(f'Playing MP4 file: {file}')
# # # # # #
# # # # # #     def play_vlc(self, file):
# # # # # #         print(f'Playing VLC file: {file}')
# # # # # #
# # # # # #
# # # # # # class MediaAdapter:
# # # # # #     def __init__(self, file_type):
# # # # # #         self.advanced_player = AdvancedMediaPlayer()
# # # # # #         self.file_type = file_type
# # # # # #
# # # # # #     def play(self, file):
# # # # # #         if self.file_type == 'mp4':
# # # # # #             self.advanced_player.play_mp4(file)
# # # # # #         elif self.file_type == 'vlc':
# # # # # #             self.advanced_player.play_vlc(file)
# # # # # #
# # # # # #
# # # # # # class AudioPlayer:
# # # # # #     def play(self, file: str):
# # # # # #         if file.endswith('.mp3'):
# # # # # #             old_player = OldMediaPlayer()
# # # # # #             old_player.play_mp3(file)
# # # # # #         elif file.endswith('.mp4') or file.endswith('.vlc'):
# # # # # #             adapter = MediaAdapter(file.split('.')[-1])
# # # # # #             adapter.play(file)
# # # # # #         else:
# # # # # #             print('Unsupported format')
# # # # # #
# # # # # #
# # # # # # player = AudioPlayer()
# # # # # # player.play('song1.mp3')
# # # # # # player.play('video1.mp4')
# # # # # # player.play('movie1.vlc')
# # # # #
# # # # #
# # # # # # Composite Pattern
# # # # #
# # # # # class FileSystemComponent:
# # # # #     def __init__(self, name):
# # # # #         self.name = name
# # # # #
# # # # #     def display(self):
# # # # #         pass
# # # # #
# # # # #
# # # # # class File(FileSystemComponent):
# # # # #     def __init__(self, name, size):
# # # # #         super().__init__(name)
# # # # #         self.size = size
# # # # #
# # # # #     def display(self):
# # # # #         print(f'File: {self.name}, Size: {self.size}')
# # # # #
# # # # #
# # # # # class Folder(FileSystemComponent):
# # # # #     def __init__(self, name):
# # # # #         super().__init__(name)
# # # # #         self.children = []
# # # # #
# # # # #     def add(self, component):
# # # # #         self.children.append(component)
# # # # #
# # # # #     def display(self):
# # # # #         print(f'Folder: {self.name}')
# # # # #         for child in self.children:
# # # # #             child.display()
# # # # #
# # # # #
# # # # # root_folder = Folder("Root")
# # # # # folder_A = Folder("Folder A")
# # # # # file_A1 = File("File A1", "10KB")
# # # # # file_A2 = File("File A2", "20KB")
# # # # # folder_B = Folder("Folder B")
# # # # # file_B1 = File("File B1", "30KB")
# # # # #
# # # # # folder_A.add(file_A1)
# # # # # folder_A.add(file_A2)
# # # # # folder_B.add(file_B1)
# # # # # root_folder.add(folder_A)
# # # # # root_folder.add(folder_B)
# # # # #
# # # # # root_folder.display()
# # # #
# # # # # 4. Proxy Pattern
# # # #
# # # # class IUserManagement:
# # # #     def create_user(self, name):
# # # #         pass
# # # #
# # # #     def delete_user(self, name):
# # # #         pass
# # # #
# # # #
# # # # class UserManagement(IUserManagement):
# # # #     def create_user(self, name):
# # # #         print(f'User {name} created.')
# # # #
# # # #     def delete_user(self, name):
# # # #         print(f'User {name} deleted.')
# # # #
# # # #
# # # # class LoggingUserManagementProxy(IUserManagement):
# # # #     def __init__(self):
# # # #         self.user_management = UserManagement()
# # # #
# # # #     def create_user(self, name):
# # # #         print(f'Logging: Creating user {name}.')
# # # #         self.user_management.create_user(name)
# # # #
# # # #     def delete_user(self, name):
# # # #         print(f'Logging: Deleting user {name}.')
# # # #         self.user_management.delete_user(name)
# # # #
# # # #
# # # # user_management_proxy = LoggingUserManagementProxy()
# # # #
# # # # user_management_proxy.create_user('Alice')
# # # #
# # # # user_management_proxy.delete_user('Alice')
# # #
# # #
# # # class Image:
# # #     def display(self):
# # #         raise NotImplementedError(f'Should be overridden')
# # #
# # #
# # # class RealImage(Image):
# # #     def __init__(self, filename: str):
# # #         self.filename = filename
# # #         self.load_from_disk()
# # #
# # #     def load_from_disk(self):
# # #         print(f'Loading: {self.filename}')
# # #
# # #     def display(self):
# # #         print(f'Displaying {self.filename}')
# # #
# # #
# # # class ProxyImage(Image):
# # #     def __init__(self, filename: str):
# # #         self.filename = filename
# # #         self.real_image = None
# # #
# # #     def display(self):
# # #         if self.real_image is None:
# # #             self.real_image = RealImage(self.filename)
# # #         self.real_image.display()
# # #
# # #
# # # img1 = ProxyImage('image1.png')
# # # img2 = ProxyImage('image2.jpg')
# # #
# # # img1.display()
# # # img2.display()
# # # img1.display()
# # #
# # # # 5. Flyweight Pattern
# #
# # class Circle:
# #     def __init__(self, color):
# #         self.color = color
# #
# #     def draw(self, x, y):
# #         print(f'Drawing a {self.color} circle at ({x},{y}).')
# #
# #
# # class CircleFactory:
# #     def __init__(self):
# #         self.circles = {}
# #
# #     def get_circle(self, color):
# #         if color not in self.circles:
# #             self.circles[color] = Circle(color)
# #             print(f'Creating a circle of color: {color}')
# #         return self.circles[color]
# #
# #
# # factory = CircleFactory()
# # colors = ['red', 'green', 'blue', 'red', 'blue', 'blue']
# #
# # for index, color in enumerate(colors):
# #     circle = factory.get_circle(color)
# #     circle.draw(index * 10, index * 15)
#
# # Bridge Pattern
#
# class Device:
#     def is_enabled(self):
#         pass
#
#     def enable(self):
#         pass
#
#     def disable(self):
#         pass
#
#     def get_volume(self):
#         pass
#
#     def set_volume(self, volume):
#         pass
#
#
# class TV(Device):
#     def __init__(self):
#         self.enabled = False
#         self.volume = 10  # Default volume
#
#     def is_enabled(self):
#         return self.enabled
#
#     def enable(self):
#         self.enabled = True
#
#     def disable(self):
#         self.enabled = False
#
#     def get_volume(self):
#         return self.volume
#
#     def set_volume(self, volume):
#         self.volume = volume
#
#
# class Radio(Device):
#     pass
#
#
# class RemoteControl:
#     def __init__(self, device):
#         self.device = device
#
#     def toggle_power(self):
#         if self.device.is_enabled():
#             self.device.disable()
#             print('Device turned off')
#
#         else:
#             self.device.enable()
#             print('Device turned on')
#
#     def volume_down(self):
#         self.device.set_volume(self.device.get_volume() - 1)
#         print(f'Volume set to {self.device.get_volume()}')
#
#     def volume_up(self):
#         self.device.set_volume(self.device.get_volume() + 1)
#         print(f'Volume set to {self.device.get_volume()}')
#
#
# tv = TV()
# remote = RemoteControl(tv)
#
# remote.toggle_power()
#
# remote.volume_up()

#
# class Device:
#     def power_on(self):
#         raise NotImplementedError
#
#     def power_off(self):
#         raise NotImplementedError
#
#     def set_volume(self):
#         raise NotImplementedError
#
#
# class RemoteControl:
#     def __init__(self, device: Device):
#         self.device = device
#
#     def turn_on(self):
#         self.device.power_on()
#
#     def turn_off(self):
#         self.device.power_off()
#
#
# class AdvancedRemoteControl(RemoteControl):
#     def mute(self):
#         self.device.set_volume(0)
#
#
# class TV(Device):
#     def power_on(self):
#         print('TV is turned on')
#
#     def power_off(self):
#         print('TV turned off')
#
#     def set_volume(self, volume):
#         print(f'TV volume is set to {volume}')
#
#
# class Radio(Device):
#     def power_on(self):
#         print('Radio is turned on')
#
#     def power_off(self):
#         print('Radio is turned off')
#
#     def set_volume(self, volume):
#         print(f'Radio volume is set to  {volume}')
#
# class SmartTV(Device):
#
#     def power_on(self):
#         print('SmartTV is turned on')
#
#     def power_off(self):
#         print('TV turned off')
#
#     def set_volume(self, volume):
#         print(f'SmartTV volume is set to {volume}')
#
# # tv = TV
# # basic_remote = RemoteControl(tv)
# # basic_remote.turn_on()
# # basic_remote.turn_off()
#
#
#
#
# radio = Radio()
# advanced_remote = AdvancedRemoteControl(radio)
# advanced_remote.turn_on()
# advanced_remote.mute()

# Component
# class TextComponent:
#     def __init__(self, text):
#         self.text = text
#
#     def get_text(self):
#         return self.text
#
#
# # Decorator
# class TextDecorator:
#     def __init__(self, text_component):
#         self.text_component = text_component
#
#     def get_text(self):
#         return self.text_component.get_text()
#
#
# # Concrete Decorators
# class BoldDecorator(TextDecorator):
#     def get_text(self):
#         return f"<b>{super().get_text()}</b>"
#
#
# class ItalicDecorator(TextDecorator):
#     def get_text(self):
#         return f"<i>{super().get_text()}</i>"
#
#
# simple_text = TextComponent("Hello, world!")
#
# print(simple_text.get_text())
# bold_text = BoldDecorator(simple_text)
#
# print(bold_text.get_text())
# italic_text = ItalicDecorator(simple_text)
#
# print(italic_text.get_text())

class Coffee:
    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class BasicCoffee(Coffee):
    def const(self):
        return 5

    def description(self):
        return 'Basic Coffee'


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ', Milk'


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + ', Sugar'


coffee = BasicCoffee()

print(f'{coffee.description()}; {coffee.const()}')

coffee_with_milk = MilkDecorator(coffee)
print(f'{coffee_with_milk.description()}, {coffee_with_milk.cost()}')

coffee_milk_sugar = SugarDecorator(coffee_with_milk)
