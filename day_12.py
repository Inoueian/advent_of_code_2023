from collections import defaultdict


class CaveSystem:
    def __init__(self, lines):
        self.neighbor_dict = defaultdict(list)
        for line in lines:
            cave_0, cave_1 = line.split('-')
            self.neighbor_dict[cave_0].append(cave_1)
            self.neighbor_dict[cave_1].append(cave_0)

    def create_path(self, choices, small_cave_twice=False):
        """Choices keeps track of choices made in the previous path,
        by recording the index of the cave that was chosen in each step."""
        path = ['start']
        new_choices = []
        current = 'start'
        twice_flag = small_cave_twice
        while True:
            if current == 'end':
                break
            success = False
            neighbors = self.neighbor_dict[current]
            if choices:
                if len(choices) > 1:
                    choice = choices.pop(0)
                    current = neighbors[choice]
                    if (current in path) and (current == current.lower()):
                        twice_flag = False
                    path.append(current)
                    new_choices.append(choice)
                    success = True
                else:
                    last_choice = choices.pop(0)
                    for choice, neighbor in enumerate(neighbors):
                        if choice <= last_choice:
                            continue
                        elif (neighbor == neighbor.lower()) and (neighbor in path):
                            if twice_flag and (neighbor not in ('start', 'end')):
                                new_choices.append(choice)
                                path.append(neighbor)
                                current = neighbor
                                success = True
                                twice_flag = False
                                break
                            else:
                                continue
                        else:
                            new_choices.append(choice)
                            path.append(neighbor)
                            current = neighbor
                            success = True
                            break
            else:
                for choice, neighbor in enumerate(neighbors):
                    if (neighbor == neighbor.lower()) and (neighbor in path):
                        if twice_flag and (neighbor not in ('start', 'end')):
                            new_choices.append(choice)
                            path.append(neighbor)
                            current = neighbor
                            success = True
                            twice_flag = False
                            break
                        else:
                            continue
                    else:
                        new_choices.append(choice)
                        path.append(neighbor)
                        current = neighbor
                        success = True
                        break
            # backtrack
            if not success:
                failed_cave = path.pop()
                if (failed_cave in path) and (failed_cave == failed_cave.lower()):
                    twice_flag = True
                if not new_choices:
                    return [], []
                current = path[-1]
                last_choice = new_choices.pop()
                choices = [last_choice]
        return new_choices, path

    def find_all_paths(self, small_cave_twice=False):
        paths = []
        choices = []
        while True:
            choices, path = self.create_path(choices, small_cave_twice=small_cave_twice)
            if path:
                paths.append(path)
            else:
                break
        return paths


if __name__ == '__main__':
    with open('data/day_12_input.txt', 'r') as f:
        data = f.read().strip()
    lines = data.split('\n')

    caves = CaveSystem(lines)
    paths_1 = caves.find_all_paths(small_cave_twice=False)
    part_1 = len(paths_1)

    caves = CaveSystem(lines)
    paths_2 = caves.find_all_paths(small_cave_twice=True)
    part_2 = len(paths_2)

    print(f'Part 1 answer: {part_1}')
    print(f'Part 2 answer: {part_2}')
