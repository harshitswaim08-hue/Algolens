import ast


def analyze_quality(code):
    try:
        tree = ast.parse(code)

        score = 100
        issues = []
        suggestions = []

        function_count = 0
        condition_count = 0
        loop_count = 0

        lines = len([
            line for line in code.splitlines()
            if line.strip()
        ])

        max_loop_depth = 0

        # ---------- LOOP DEPTH ----------

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

        # ---------- AST ANALYSIS ----------

        for node in ast.walk(tree):

            # Functions
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
            ):

                function_count += 1

                if hasattr(node, "lineno") and hasattr(node, "end_lineno"):

                    function_length = (
                        node.end_lineno - node.lineno + 1
                    )

                    if function_length > 20:

                        score -= 10

                        issues.append(
                            "Long function detected."
                        )

                        suggestions.append(
                            "Break long functions into smaller "
                            "and more focused functions."
                        )

            # Loops
            elif isinstance(node, (ast.For, ast.While)):

                loop_count += 1

            # Conditions
            elif isinstance(node, ast.If):

                condition_count += 1

        # ---------- NESTED LOOP ----------

        if max_loop_depth >= 2:

            score -= 10

            issues.append(
                "Nested loops detected."
            )

            suggestions.append(
                "Consider reducing nested iterations "
                "to improve performance."
            )

        # ---------- DEEPLY NESTED LOOP ----------

        if max_loop_depth >= 3:

            score -= 10

            issues.append(
                "Deeply nested loops detected."
            )

            suggestions.append(
                "Consider using a more efficient algorithm "
                "to reduce loop nesting."
            )

        # ---------- TOO MANY CONDITIONS ----------

        if condition_count > 5:

            score -= 10

            issues.append(
                "Too many conditional statements detected."
            )

            suggestions.append(
                "Simplify complex conditional logic."
            )

        # ---------- TOO MANY LOOPS ----------

        if loop_count > 3:

            score -= 10

            issues.append(
                "Multiple loops detected."
            )

            suggestions.append(
                "Review loops and look for optimization opportunities."
            )

        # ---------- LONG CODE ----------

        if lines > 50:

            score -= 10

            issues.append(
                "Large amount of code detected."
            )

            suggestions.append(
                "Split the code into smaller modules "
                "or functions."
            )

        # ---------- NO FUNCTIONS ----------

        if function_count == 0:

            score -= 5

            issues.append(
                "No functions detected."
            )

            suggestions.append(
                "Use functions to improve code organization "
                "and reusability."
            )

        # ---------- DEFAULT ----------

        if not issues:

            issues.append(
                "No major code quality issues detected."
            )

        if not suggestions:

            suggestions.append(
                "Code structure looks good."
            )

        # Keep score between 0 and 100
        score = max(0, min(score, 100))

        return {
            "score": score,
            "functions": function_count,
            "conditions": condition_count,
            "loops": loop_count,
            "lines": lines,
            "loop_depth": max_loop_depth,
            "issues": issues,
            "suggestions": suggestions
        }

    except SyntaxError:
        return None