import time
import board
import pwmio

# Create a PWM object for the robot's left motor
left_motor = pwmio.PWMOut(board.D18, frequency=50)

# Create a PWM object for the robot's right motor
right_motor = pwmio.PWMOut(board.D13, frequency=50)

# Set the speed of the robot's left motor
left_motor.duty_cycle = 1000

# Set the speed of the robot's right motor
right_motor.duty_cycle = 1000

# Move the robot forward
left_motor.duty_cycle = 2000
right_motor.duty_cycle = 2000

# Wait for 2 seconds
time.sleep(2)

# Move the robot backward
left_motor.duty_cycle = 1000
right_motor.duty_cycle = 1000

# Wait for 2 seconds
time.sleep(2)

# Stop the robot
left_motor.duty_cycle = 0
right_motor.duty_cycle = 0
