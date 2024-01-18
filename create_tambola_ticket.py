import random
from tambola_ticket import TambolaTicket
from fastapi import HTTPException
from helpers import *

def add_tickets_to_database(final_tickets):
    set_id = get_unique_set_id()
    generated_tickets = {}
    try:
        for i, ticket in enumerate(final_tickets):
            params = {
                "set_id": str(set_id),
                "ticket_number": i + 1,
                "row1": str(ticket[0]),
                "row2": str(ticket[1]),
                "row3": str(ticket[2]),
            }
            tambola_object = TambolaTicket(**params)
            tambola_object.save()
            generated_tickets[str(tambola_object.id)] = ticket
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error while adding tickets in database")
    return generated_tickets

def generate_tambola_ticket_set():
    col_vals = [[10*y + x for x in range(10)] for y in range(9)]
    col_vals[0].pop(0)
    col_vals[-1].append(90)

    all_tics = [[[] for _ in range(9)] for _ in range(6)]

    for i in range(9):
        col = col_vals[i]
        for j in range(6):
            random_index = random.randrange(len(col))
            all_tics[j][i].append(col.pop(random_index))

    random_index = random.randrange(len(col_vals[8]))
    all_tics[random.randrange(6)][8].append(col_vals[8].pop(random_index))

    for i in range(3):
        for j in range(9):
            col = col_vals[j]
            if not len(col):
                continue
            random_index = random.randrange(len(col))
            random_number = col[random_index]

            found = 1
            while found:
                tic = all_tics[random.randrange(6)]

                if numofelement(tic) != 15 and len(tic[j]) != 2:
                    found = 0
                    tic[j].append(random_number)
                    col.pop(random_index)

    for j in range(9):
        col = col_vals[j]
        if not len(col):
            continue
        random_index = random.randrange(len(col))
        random_number = col[random_index]

        found = 1
        while found:
            tic = all_tics[random.randrange(6)]

            if numofelement(tic) != 15 and len(tic[j]) != 3:
                found = 0
                tic[j].append(random_number)
                col.pop(random_index)

    if numofelement(col_vals):
        raise HTTPException(status_code=500, detail="All numbers from 0 to 90 are not used while generating the set. Try Again")

    for i in range(6):
        for j in range(9):
            all_tics[i][j].sort()

    final_tickets = generate_final_tickecs(all_tics)

    # for ticket in final_tickets:
    #     for row in ticket:
    #         print(row)
    #     print("  ")
                
    for ticket in final_tickets:
        if TambolaTicket.select().where(
            TambolaTicket.row1 == str(ticket[0]),
            TambolaTicket.row2 == str(ticket[1]),
            TambolaTicket.row3 == str(ticket[2]),
        ).exists():
            return generate_tambola_ticket_set()

    generated_tickets = add_tickets_to_database(final_tickets)

    return generated_tickets