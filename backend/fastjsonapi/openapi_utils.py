from copy import deepcopy


def stabilize(openapi):
    openapi = deepcopy(openapi)
    stabilize_paths(openapi["paths"])
    return openapi


def stabilize_paths(paths):
    for path in paths.values():
        for operation in path.values():
            stabilize_operation(operation)


def stabilize_operation(operation):
    if "parameters" in operation:
        operation["parameters"] = sorted(
            operation["parameters"],
            key=lambda parameter: (parameter["in"], parameter["name"]),
        )
