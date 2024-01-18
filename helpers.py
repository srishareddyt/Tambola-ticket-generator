import datetime

def get_unique_set_id():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    return timestamp

def numofelement(arr):
    total_elements = 0
    for row in arr:
        total_elements += len(row)
    return total_elements

def rowcount(row):
    total_elements = 0
    for i in row:
        if i:
            total_elements += 1
    return total_elements

def generate_final_tickecs(all_tics):
    final_tickets = [[[0] * 9 for _ in range(3)] for _ in range(6)]

    for i in range(6):
        current = all_tics[i]
        for col_size in range(3,0,-1):
            if rowcount(final_tickets[i][0]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][0]) == 5:
                    break
                if final_tickets[i][0][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][0][j] = current[j].pop(0)

        for col_size in range(2,0,-1):
            if rowcount(final_tickets[i][1]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][1]) == 5:
                    break

                if final_tickets[i][1][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][1][j] = current[j].pop(0)

        for col_size in range(1,0,-1):
            if rowcount(final_tickets[i][2]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][2]) == 5:
                    break

                if final_tickets[i][2][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][2][j] = current[j].pop(0)

    return final_tickets