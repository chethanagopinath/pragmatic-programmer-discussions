# designing a small address book database using a straightforward binary
# representation in your language of choice
import struct


class AddressBook:
    """Class representing a address"""

    FORMAT = "20s10s15s20s"

    def __init__(self, name: str, phone: str, city: str, directions: str):
        self.name = name
        self.phone = phone
        self.city = city
        self.directions = directions

    def represent_binary(self):
        # padding since binary requires fixed length strings
        name_bytes = self.name.encode("utf-8").ljust(20, b"\x00")
        phone_bytes = self.phone.encode("utf-8").ljust(10, b"\x00")
        city_bytes = self.city.encode("utf-8").ljust(15, b"\x00")
        directions_bytes = self.directions.encode("utf-8").ljust(20, b"\x00")

        return struct.pack(
            self.FORMAT, name_bytes, phone_bytes, city_bytes, directions_bytes
        )

    def represent_json(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "city": self.city,
            "directions": self.directions,
        }


if __name__ == "__main__":
    # Adding directions field for newer data meant I need to modify previous data
    # Which is interesting for binary - could keep an updated timestamp but if its all in binary, its just not understandable
    # Also directions can vary a lot, so thats difficult to predict and pad for accordingly, if its over the limit, the field's val gets truncated
    ab = AddressBook(
        name="Chethana",
        phone="6073450377",
        city="Milpitas",
        directions="directions to reach address but I'm not sure if this will work since I just gave 20",
    )

    print(f"Binary {ab.represent_binary()}")
    print(f"JSON {ab.represent_json()}")
