from tickets import create_ticket
from storage import load_tickets, save_tickets

def main():
    tickets = load_tickets()
    while True:
        print("----CAMPUSFLOW TICKET CREATOR----")
        print("1. Create a ticket")
        print("2. Exit")
        choice  = input("Choose an option: ").strip()
        
        if choice == "1":
            title = input("Enter title: ").strip()
            description = input("Enter description: ").strip()
            try:
                new_ticket = create_ticket([], title, description)
                tickets.append(new_ticket)
                save_tickets(tickets)
                print(f"Ticket {new_ticket['id']} saved successfully.")
            except ValueError as e:
                print("Validation Error:", e)
        elif choice == "2":
            print("Goodbye!")
            break
    
        else:
            print("Invalid option. Try again!")
if __name__ == "__main__":
    main()