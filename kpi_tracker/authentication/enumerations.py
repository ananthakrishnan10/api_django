from enum import Enum, unique


@unique
class UserRoleEnum(Enum):
    admin = 0
    staff = 1

    def __str__(self):
        return self.name
