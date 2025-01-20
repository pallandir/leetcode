from collections import defaultdict


facts = ["1 m = 3 ft", "1 ft = 12 in", "1 h = 60 min", "1 min = 60 s"]
questions = [
    "2 h to s",  # Valid: Convert 2 hours to seconds
    "3 min to in",  # Invalid: Convert minutes to inches
]


def parse_facts(facts) -> dict:
    units_map = defaultdict(dict)
    for fact in facts:
        left_operand, right_operand = fact.split("=")
        left_value, left_unit = left_operand.strip().split()
        right_value, right_unit = right_operand.strip().split()
        left_value, right_value = float(left_value), float(right_value)

        units_map[left_unit][right_unit] = right_value / left_value
        units_map[right_unit][left_unit] = left_value / right_value
    return units_map


def from_unit_to_unit_path(from_unit, to_unit, units_graph) -> int | None:
    queue = [(from_unit, 1)]
    visited = set()

    while queue:
        current_unit, conv_factor = queue.pop(0)

        if current_unit == to_unit:
            return conv_factor
        visited.add(current_unit)

        for next_unit, next_factor in units_graph[current_unit].items():
            if next_unit not in visited:
                queue.append((next_unit, conv_factor * next_factor))
    return None


def convert(from_unit, to_unit, value, units_map) -> int | str:
    try:
        conversion_factor = from_unit_to_unit_path(from_unit, to_unit, units_map)
        return value * conversion_factor
    except (ValueError, TypeError, KeyError) as conversion_error:
        return f"Invalid conversion : {conversion_error}"
        # raise ValueError(f"Invalid conversion : {conversion_error}") #better way but not required here to have a cleaner output


if __name__ == "__main__":
    for question in questions:
        value, from_unit, _, to_unit = question.strip().split()
        units_val_graph = dict(parse_facts(facts))
        response = convert(from_unit, to_unit, float(value), units_val_graph)
        print(f"{question} = {response}")
