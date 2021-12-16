class Packet:
    def __init__(self, code=None, binary=None):
        if code is None:
            self.code = None
            self.binary = binary
        else:
            self.code = code
            self.binary = self.convert_to_binary()
        self.version, self.type_id, self.rest = self.decode()
        if self.type_id == 4:
            self.literal, self.remaining = self.read_literal()
            self.subpackets = []
        else:
            self.literal = None
            self.length_type_id = int(self.rest[0])
            self.subpackets, self.remaining = self.read_subpackets()

        self.version_sum = self.compute_version_sum()
        self.value = self.evaluate()

    def convert_to_binary(self):
        binary_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                       '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                       'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
        return ''.join([binary_dict[char] for char in self.code])

    def decode(self):
        version = int(self.binary[:3], base=2)
        type_id = int(self.binary[3:6], base=2)
        rest = self.binary[6:]
        return version, type_id, rest

    def read_literal(self):
        four_bits_list = []
        num_groups = 0
        while True:
            five_bits = self.rest[num_groups*5:(num_groups + 1)*5]
            four_bits_list.append(five_bits[1:])
            if five_bits[0] == '1':
                num_groups += 1
                pass
            elif five_bits[0] == '0':
                break
        binary_str = ''.join(four_bits_list)
        remaining = self.rest[(num_groups + 1) * 5:]
        if remaining and ('1' not in remaining):
            remaining = ''
        return int(binary_str, base=2), remaining

    def read_subpackets(self):
        subpackets = []
        if self.length_type_id == 0:
            bit_length = int(self.rest[1:16], base=2)
            binary_str = self.rest[16:16 + bit_length]
            remaining = self.rest[16 + bit_length:]
            while True:
                packet = Packet(binary=binary_str)
                subpackets.append(packet)
                binary_str = packet.remaining
                if not binary_str:
                    break
        elif self.length_type_id == 1:
            subpacket_count = int(self.rest[1:12], base=2)
            binary_str = self.rest[12:]
            for num in range(subpacket_count):
                packet = Packet(binary=binary_str)
                subpackets.append(packet)
                binary_str = packet.remaining
            remaining = binary_str
        if remaining and ('1' not in remaining):
            remaining = ''
        return subpackets, remaining

    def compute_version_sum(self):
        return self.version + sum(packet.version_sum for packet in self.subpackets)

    def evaluate(self):
        if self.type_id == 4:
            return self.literal
        elif self.type_id == 0:
            return sum(subpacket.value for subpacket in self.subpackets)
        elif self.type_id == 1:
            prod = 1
            for subpacket in self.subpackets:
                prod *= subpacket.value
            return prod
        elif self.type_id == 2:
            return min(subpacket.value for subpacket in self.subpackets)
        elif self.type_id == 3:
            return max(subpacket.value for subpacket in self.subpackets)
        elif self.type_id == 5:
            return int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.type_id == 6:
            return int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.type_id == 7:
            return int(self.subpackets[0].value == self.subpackets[1].value)


if __name__ == '__main__':
    with open('data/day_16_input.txt', 'r') as f:
        data = f.read().strip()

    packet = Packet(data)

    part_1 = packet.version_sum
    part_2 = packet.value

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
