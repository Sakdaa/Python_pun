from collections import deque

def is_valid_state(m1, c1, m2, c2):
    if (m1 >= c1 or m1 == 0) and (m2 >= c2 or m2 == 0):
        return True
    return False

def get_possible_actions():
    return [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

def P4_crossriver(initial):
    m_total, c_total = initial[0] + initial[2], initial[1] + initial[3]
    goal = (0, 0, m_total, c_total, 0)

    queue = deque([(initial, [])])
    visited = set()

    while queue:
        (m1, c1, m2, c2, boat), path = queue.popleft()

        if (m1, c1, m2, c2, boat) == goal:
            return path

        visited.add((m1, c1, m2, c2, boat))

        for action in get_possible_actions():
            m, c = action

            if boat == 1:  
                new_m1, new_c1 = m1 - m, c1 - c
                new_m2, new_c2 = m2 + m, c2 + c
                new_boat = 0
            else:  
                new_m1, new_c1 = m1 + m, c1 + c
                new_m2, new_c2 = m2 - m, c2 - c
                new_boat = 1

            if 0 <= new_m1 <= m_total and 0 <= new_c1 <= c_total and 0 <= new_m2 <= m_total and 0 <= new_c2 <= c_total:
                if is_valid_state(new_m1, new_c1, new_m2, new_c2):
                    new_state = (new_m1, new_c1, new_m2, new_c2, new_boat)
                    if new_state not in visited:
                        queue.append((new_state, path + [action]))

    return None