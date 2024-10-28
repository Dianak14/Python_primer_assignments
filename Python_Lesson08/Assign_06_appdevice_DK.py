#create the class SmartDevice 
class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name = "BetaTesting App"): #1. Add the default argument for install_app method
        # 2. modify install_app method to avoid duplicates in the app_list
        if app_name not in self.app_list:
            print(f"Installing {app_name}...")
            self.app_list.append(app_name)
        else:
            print(f"Error. {app_name} is already installed. ")
        return self.app_list
    
    # 3. Add delete_app method 
    def delete_app(self, app_name):
        if app_name in self.app_list:
            print(f"Deleting {app_name}...")
            self.app_list.remove(app_name)
        else:
            print(f"Error. {app_name} does not exist. ")
        return self.app_list

# 4. Create a SmartDevice object to call the functions 
device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

# 5. Use print statements to check the methods work as expected 
# Test install_app method 

print(device_a.app_list) # check that an empty list is returned
device_a.install_app("Google Maps")
print(device_a.app_list) #check that the app is now included in the list

device_a.install_app()
print(device_a.app_list) #check when no paramter is passed, the default name is added to the list

device_a.install_app("Google Maps")
print(device_a.app_list) #check that the same app cannot be installed twice 

# Test the delete_app method
device_a.delete_app("Singing App")
print(device_a.app_list) #check that an app that doesn't exist cannot be deleted

device_a.delete_app("Google Maps")
print(device_a.app_list) #check that an app can be deleted 