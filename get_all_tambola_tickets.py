from tambola_ticket import TambolaTicket
import math
from fastapi import HTTPException

def get_all_tambola_tickets(page = 1, page_limit = 2):
    offset = (page - 1) * page_limit * 6
    query = TambolaTicket.select()
    total_count = query.count() // 6
    data = list(query.order_by(TambolaTicket.set_id, TambolaTicket.ticket_number).dicts().offset(offset).limit(page_limit * 6))
    
    tickets = {}
    total_tickets = len(data)
    try:
        for i in range(page_limit):
            if 6 * i >= total_tickets:
                continue
            first_ticket = data[6*i]
            set_id = first_ticket["set_id"]
            curr_set = [{"1": [eval(first_ticket["row1"]), eval(first_ticket["row2"]), eval(first_ticket["row3"])]}]
            for num in range(1,6):
                next_ticket = data[6*i + num]
                curr_set.append({str(num+1): [eval(next_ticket["row1"]), eval(next_ticket["row2"]), eval(next_ticket["row3"])]})
            tickets[set_id] = curr_set
    except Exception as e:
        raise HTTPException(status_code=500, detail="Data in databse is not proper")

    pagination = {
        "page": page, 
        "page_limit": page_limit, 
        "total": math.ceil(total_count / page_limit), 
        "total_count": total_count
        }

    return tickets | pagination