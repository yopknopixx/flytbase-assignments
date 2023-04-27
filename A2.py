from flyt_python import api
import time

drone = api.navigation(timeout=120000)  # Instantiate the navigation API

# Wait for initialization
time.sleep(3)

# take off to 5m
print("Take Off!")
drone.take_off(10.0)

print("Point 1")
drone.position_set(10, 5, -10, relative=False)
print("Point 2")
drone.position_set(0, 10, -10, relative=False)
print("Point 3")
drone.position_set(0, 0, -10, relative=False)

print("Landing")
drone.land()
