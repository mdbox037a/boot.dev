class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        sword1 = self.sword_type
        sword2 = other.sword_type

        if sword1 == "bronze" and sword2 == "bronze":
            return Sword("iron")
        elif sword1 == "iron" and sword2 == "iron":
            return Sword("steel")
        else:
            raise Exception("cannot craft")
