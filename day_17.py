from collections import defaultdict


class Launcher:
    def __init__(self, data):
        self.x_min, self.x_max, self.y_min, self.y_max = self.parse_input(data)

    def get_time_range_for_x(self, v_x):
        """When is the probe in the correct x position?
        Also, does the x position get stuck within the right range?"""
        time_step = 0
        x = 0
        good_times = []
        while (x <= self.x_max) and (v_x > 0):
            x += v_x
            v_x -= 1
            time_step += 1
            if self.x_min <= x <= self.x_max:
                good_times.append(time_step)
        stopped = ((v_x == 0) and (self.x_min <= x <= self.x_max))
        return good_times, stopped

    def get_time_range_for_y(self, v_y):
        """When is the probe in the correct y position?"""
        time_step = 0
        y = 0
        good_times = []
        while y >= self.y_min:
            y += v_y
            v_y -= 1
            time_step += 1
            if self.y_min <= y <= self.y_max:
                good_times.append(time_step)
        return good_times

    def test_initial_velocity(self, v_x, v_y):
        x_times, stopped = self.get_time_range_for_x(v_x)
        y_times = self.get_time_range_for_y(v_y)
        if stopped:
            return y_times and (max(y_times) >= min(x_times))
        else:
            return bool(set(x_times).intersection(y_times))

    def find_highest_point(self):
        """Assuming that the x range contains a number of the form
        n * (n + 1) / 2, and that y_min is small enough,
        you can reach the range if your initial velocity is (n, -y_min - 1)."""
        return (-self.y_min - 1) * (-self.y_min) // 2

    def count_possible_velocities(self):
        x_good_times_dict = {v_x: self.get_time_range_for_x(v_x)
                             for v_x in range(1, self.x_max + 1)
                             if self.get_time_range_for_x(v_x)[0]}
        y_good_times_dict = {v_y: self.get_time_range_for_y(v_y)
                             for v_y in range(self.y_min, -self.y_min)
                             if self.get_time_range_for_y(v_y)}
        # Highest time step where the probe can be in the range is -2 * y_min
        # Keep track of how many initial velocities put the probe in the right position
        x_reverse_dict = defaultdict(list)
        y_reverse_dict = defaultdict(list)
        for v_x, (time_list, stopped) in x_good_times_dict.items():
            for time in time_list:
                x_reverse_dict[time].append(v_x)
            if stopped:
                for time in range(max(time_list) + 1, -2 * self.y_min + 1):
                    x_reverse_dict[time].append(v_x)
        for v_y, time_list in y_good_times_dict.items():
            for time in time_list:
                y_reverse_dict[time].append(v_y)

        velocities_by_time = [set((v_x, v_y) for v_x in x_reverse_dict[time]
                                  for v_y in y_reverse_dict[time])
                              for time in range(-2 * self.y_min + 1)]
        return len(set.union(*velocities_by_time))

    @staticmethod
    def parse_input(data):
        x_part, y_part = data.split(',')
        x_numbers = x_part.split('=')[1]
        y_numbers = y_part.split('=')[1]
        x_min, x_max = x_numbers.split('..')
        y_min, y_max = y_numbers.split('..')
        return int(x_min), int(x_max), int(y_min), int(y_max)


if __name__ == '__main__':
    with open('data/day_17_input.txt', 'r') as f:
        data = f.read()
    launcher = Launcher(data)

    part_1 = launcher.find_highest_point()
    part_2 = launcher.count_possible_velocities()

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
