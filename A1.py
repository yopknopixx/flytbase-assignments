from flyt_python import api
import time

drone = api.navigation(timeout=120000)  # Instantiate the navigation API

# Wait for initialization
time.sleep(3)

# take off to 5m
print("Take Off!")
drone.take_off(5.0)

print("Point 1")
drone.position_set(6.5, 0, -5, relative=False)
print("Point 2")
drone.position_set(6.5, 6.5, -5, relative=False)
print("Point 3")
drone.position_set(0, 6.5, -5, relative=False)
print("Point 4")
drone.position_set(0, 0, -5, relative=False)

print("Landing")
drone.land()
