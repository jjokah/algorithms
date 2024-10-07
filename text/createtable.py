table = [
    ["M", "Possibilities", "addition"],
    ["1", "512", "what"],
    ["2", "250912", "the"],
    ["3", "1815264", "fuck"],
]

def print_table(data):
    # Define the width for columns
    col_widths = [max(len(str(item)) for item in col) + 2 for col in zip(*data)]
    
    # Helper function to print lines
    def print_line(left, middle, right, line):
        print(left + middle.join([line * width for width in col_widths]) + right)
    
    # Print top border
    print_line("┌", "┬", "┐", "─")
    
    # Print headers
    for i, row in enumerate(data):
        print("│" + "│".join(f' {str(item).ljust(col_widths[j] - 2)} ' for j, item in enumerate(row)) + "│")
        if i == 0:
            # Print separator after header
            print_line("├", "┼", "┤", "─")
    
    # Print rows
    for row in data[1:]:
        print("│" + "│".join(f' {str(item).ljust(col_widths[j] - 2)} ' for j, item in enumerate(row)) + "│")
    
    # Print bottom border
    print_line("└", "┴", "┘", "─")

# Call the function to print the table
print_table(table)

