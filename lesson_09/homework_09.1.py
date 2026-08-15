class Romb:

    def __init__(self, side_a, angle_a: int | float = None, angle_b: int | float =None):

        # Validate if at least one angle provided
        if not (angle_a or angle_b):
            raise ValueError("At least one angle(angle_a or angle_b) must be set!")

        # If both angles provided - check their sum to == 180
        if angle_a and angle_b and angle_a != 180 - angle_b:
            raise ValueError("Sum of angles must be 180 degrees!")

        self.side_a = side_a
        self.angle_a = angle_a or 180 - angle_b
        self.angle_b = angle_b or 180 - angle_a

    def __setattr__(self, name, value):
        angles = ["angle_a", "angle_b"]

        # Validation for "side_a" value
        if name == "side_a":
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("Romb side must be a positive number!")
            else:
                self.__dict__[name] = value

        # Validation for "angle_a" and "angle_b" values
        elif name in angles:
            if not isinstance(value, (int, float)) or not 0 < value < 180:
                raise ValueError(f"Wrong '{name}' value: Romb angle must be a numeric value between 0 and 180!")
            else:
                self.__dict__[name] = value
                # Re-calculate opposite angle
                angles.remove(name)
                self.__dict__[angles[0]] = 180 - value
        # Do not allow extra parameters except for side_a', 'angle_a' and 'angle_b'
        else:
            raise KeyError("Romb can only have 'side_a', 'angle_a' and 'angle_b' parameters!")

    def __eq__(self, other):
        if isinstance(other, Romb):
            return self.side_a == other.side_a and self.angle_a == other.angle_a and self.angle_b == other.angle_b
        else:
            raise ValueError("Can compare only with other rombs!")

    def __str__(self):
        return f"Romb has side={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b}"

# Create instance of Romb setting side and one of angles
my_romb_1 = Romb(side_a =3.5, angle_b = 44, angle_a = 136)
print(my_romb_1)

# Change created romb angles aand check opposite angle adjustment
my_romb_1.angle_a = 100
print(my_romb_1)

setattr(my_romb_1, "angle_b", 40)
print(my_romb_1)

setattr(my_romb_1, "angle_a", 123.5)
print(my_romb_1)

### Example of two rombs comparison:
# my_romb_2 = Romb(3.5, 30, 150)
# print(my_romb_1 == my_romb_2)
