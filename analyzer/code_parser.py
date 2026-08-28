import ast


def analyze_code(code):
    try:
        tree = ast.parse(code)

        lines = len([
            line for line in code.splitlines()
            if line.strip()
        ])

        functions = 0
        loops = 0
        conditions = 0
        variables = 0

        max_loop_depth = 0

        def get_loop_depth(node, current_depth=0):
            max_depth = current_depth

            for child in ast.iter_child_nodes(node):

                if isinstance(child, (ast.For, ast.While)):
                    depth = get_loop_depth(
                        child,
                        current_depth + 1
                    )
                    max_depth = max(max_depth, depth)

                else:
                    depth = get_loop_depth(
                        child,
                        current_depth
                    )
                    max_depth = max(max_depth, depth)

            return max_depth

        max_loop_depth = get_loop_depth(tree)

        for node in ast.walk(tree):

            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
            ):
                functions += 1

            elif isinstance(node, (ast.For, ast.While)):
                loops += 1

            elif isinstance(node, ast.If):
                conditions += 1

            elif isinstance(node, ast.Assign):
                variables += 1

        # Time Complexity
        if max_loop_depth >= 3:
            time_complexity = "O(n³)"
        elif max_loop_depth == 2:
            time_complexity = "O(n²)"
        elif max_loop_depth == 1:
            time_complexity = "O(n)"
        else:
            time_complexity = "O(1)"

        # Space Complexity - basic estimation
        list_creations = 0

        for node in ast.walk(tree):
            if isinstance(node, (ast.List, ast.ListComp)):
                list_creations += 1

        if list_creations > 0:
            space_complexity = "O(n)"
        else:
            space_complexity = "O(1)"

        # Performance Issues
        issues = []

        if max_loop_depth >= 2:
            issues.append(
                "Nested loops detected. "
                "Performance may decrease for large inputs."
            )

        if max_loop_depth >= 3:
            issues.append(
                "Deeply nested loops detected. "
                "Consider optimizing the algorithm."
            )

        if list_creations > 0:
            issues.append(
                "Additional list memory usage detected."
            )

        if not issues:
            issues.append(
                "No major performance issues detected."
            )

        return {
            "lines": lines,
            "functions": functions,
            "loops": loops,
            "conditions": conditions,
            "variables": variables,
            "loop_depth": max_loop_depth,
            "time_complexity": time_complexity,
            "space_complexity": space_complexity,
            "issues": issues
        }

    except SyntaxError:
        return None