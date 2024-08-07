

class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def print_value(self):
        print(self.value)

    def to_octal(self):
        new_value: str = ""
        temp = abs(self.value)
        while temp > 7:
            new_value = str(temp % 8) + new_value
            temp //= 8
        if self.value < 0:
            return '-' + str(temp) + new_value
        return str(temp) + new_value

    def to_bin(self):
        new_value: str = ""
        temp = abs(self.value)
        while temp > 1:
            new_value = str(temp % 2) + new_value
            temp //= 2
        if self.value < 0:
            return '-' + str(temp) + new_value
        return (str(temp)+ new_value)

    def to_hexadecimal(self):
        decimals = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F')
        new_value: str = ""
        temp = abs(self.value)
        while temp > 15:
            new_value = decimals[temp % 16] + new_value
            temp //= 16
        if self.value < 0:
            return '-' + decimals[temp] + new_value
        return decimals[temp] + new_value
