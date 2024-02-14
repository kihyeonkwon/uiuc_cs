def print_towers(towers):
    for i, tower in enumerate(towers):
        print(f"Rod {i+1}: {tower}")

def move_disk(towers, source, target):
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"\nMove disk {disk} from Rod {source+1} to Rod {target+1}")
    print_towers(towers)

def tower_of_hanoi(n, source, target, auxiliary, towers):
    if n == 1:
        move_disk(towers, source, target)
        return
    tower_of_hanoi(n-1, source, auxiliary, target, towers)
    move_disk(towers, source, target)
    tower_of_hanoi(n-1, auxiliary, target, source, towers)

n = 3  # 원반의 수
towers = [list(range(n, 0, -1)), [], []]  # 초기 타워 상태: 첫 번째 타워에 n개의 원반, 나머지는 비어 있음

print("Initial Towers:")
print_towers(towers)
tower_of_hanoi(n, 0, 2, 1, towers)
