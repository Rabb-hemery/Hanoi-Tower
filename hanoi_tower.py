def hanoi_solver(n):
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    moves = []

    def format_state():
        return f"{rods['A']} {rods['B']} {rods['C']}"
    moves.append(format_state())

    def move_disk(disks, source, target, auxiliary):
        if disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            moves.append(format_state())
        else:
            move_disk(disks - 1, source, auxiliary, target)
            disk = rods[source].pop()
            rods[target].append(disk)
            moves.append(format_state())
            move_disk(disks - 1, auxiliary, target, source)

    move_disk(n, 'A', 'C', 'B')
    return "\n".join(moves)

if __name__ == "__main__":
    print(hanoi_solver(3))
