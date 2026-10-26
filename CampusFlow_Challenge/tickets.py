def next_ticket_id(ticket_list):
    current_highest_id = 0
    for tickets in ticket_list:
        ticket_id = tickets["id"]
        num_part = int(ticket_id[1:])
        if num_part > current_highest_id:
            current_highest_id = num_part
    next_id = current_highest_id + 1
    return f"T{next_id:03d}"

def create_ticket(existing_tickets, title, description):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    if not description or not description.strip():
        raise ValueError("Description cannot be empty, MUST be detailed.")
    
    ticket_id = next_ticket_id(existing_tickets)

    return {
        "id": ticket_id,
        "title": title.strip(),
        "description": description.strip()
    }