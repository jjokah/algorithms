def generate_unicode_table(data):
    if not data or not data[0]:
        return "No data provided"

    # Get the number of rows and columns
    rows = len(data)
    cols = len(data[0])

    # Find the maximum width for each column
    col_widths = [max(len(str(data[row][col])) for row in range(rows)) for col in range(cols)]

    # Unicode box characters
    top_left = "┌"
    top_right = "┐"
    bottom_left = "└"
    bottom_right = "┘"
    horizontal = "─"
    vertical = "│"
    t_down = "┬"
    t_up = "┴"
    t_right = "├"
    t_left = "┤"
    cross = "┼"

    # Generate the table
    table = []

    # Top border
    table.append(top_left + t_down.join(horizontal * (width + 2) for width in col_widths) + top_right)

    # Data rows
    for i, row in enumerate(data):
        cell_data = vertical + vertical.join(f" {str(cell).ljust(col_widths[j])} " for j, cell in enumerate(row)) + vertical
        table.append(cell_data)
        
        # Add separator row if not the last row
        if i < rows - 1:
            separator = t_right + cross.join(horizontal * (width + 2) for width in col_widths) + t_left
            table.append(separator)

    # Bottom border
    table.append(bottom_left + t_up.join(horizontal * (width + 2) for width in col_widths) + bottom_right)

    return "\n".join(table)

# Example usage
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "London"]
]

print(generate_unicode_table(data))
