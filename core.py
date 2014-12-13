# Ethan Busbee
# Rocketski Core

# Rocketski is a library meant to simplify calculations for rocketry.
# I'm mainly coding this just to see if I can.

import traceback


class Rocketski(object):
    gravities = {"Earth": 9.81}  # The idea is to have stock celestial bodies and allow adding more

    def __init__(self):
        pass

    def getTWR(self, thrust = 1, mass = 1, gravity = 9.81):
        if self._checkTWRInputs(thrust = thrust, mass = mass, gravity = gravity) is False:
            raise Exception("TWR inputs were not all valid!")

        weight = mass * gravity  # YAY PHYSICS
        return thrust / weight  # YAY MATH

    def getTargetPayload(self, TWR = 1, thrust = 1, gravity = 9.81):
        pass


    def _checkTWRInputs(self, TWR = 1, thrust = 1, mass = 1, gravity = 9.81):
        try:
            if TWR < 0: raise Exception("TWR must be positive or zero!")
            if thrust < 0: raise Exception("Thrust must be positive or zero!")
            if mass <= 0: raise Exception("Weight must be positive!")
            if gravity <= 0: raise Exception("Gravity must be positive!")
        except:
            print "\n\n" + str(traceback.format_exc())
            return False

        return True
