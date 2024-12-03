# Import necessary libraries from WPILib
from wpimath.kinematics import SwerveDrive4Kinematics, ChassisSpeeds
from wpimath.geometry import Translation2d
import math

# Define module locations relative to the robot center (in meters)
frontLeftLocation = Translation2d(x=0.3, y=0.3)  # Example coordinates
frontRightLocation = Translation2d(x=0.3, y=-0.3)
backLeftLocation = Translation2d(x=-0.3, y=0.3)
backRightLocation = Translation2d(x=-0.3, y=-0.3)

# Create the kinematics object
kinematics = SwerveDrive4Kinematics(
    frontLeftLocation,
    frontRightLocation,
    backLeftLocation,
    backRightLocation
)

# Define some test chassis speeds to simulate movement
# These values represent meters per second (vx, vy) and radians per second (omega)
test_chassis_speeds = [
    ChassisSpeeds(vx=1.0, vy=0.0, omega=0.0),    # Forward movement
    ChassisSpeeds(vx=0.0, vy=1.0, omega=0.0),    # Sideways movement
    ChassisSpeeds(vx=0.5, vy=0.5, omega=0.0),    # Diagonal movement
    ChassisSpeeds(vx=0.0, vy=0.0, omega=1.0),    # Pure rotation
    ChassisSpeeds(vx=1.0, vy=1.0, omega=1.0),    # Combined motion
]

# Test each chassis speed and print out the module states
for idx, speeds in enumerate(test_chassis_speeds):
    # Get the swerve module states for the given chassis speeds
    swerveModuleStates = kinematics.toSwerveModuleStates(speeds)

    # Print the output for each module
    print(f"ChassisSpeeds Test {idx + 1}: vx={speeds.vx:.2f} m/s, vy={speeds.vy:.2f} m/s, omega={speeds.omega:.2f} rad/s")
    for i, state in enumerate(swerveModuleStates):
        # Extract speed and angle for each swerve module
        speed = state.speed  # Corrected attribute to access speed (in m/s)
        angle = state.angle.degrees()  # Get the angle in degrees from Rotation2d object

        # Print the speed and angle for each module
        print(f"  Module {i + 1}: Speed = {speed:.2f} m/s, Angle = {angle:.2f} degrees")
    print()
