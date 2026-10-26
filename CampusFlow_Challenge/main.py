from tickets import create_ticket
from storage import load_tickets, save_tickets
from ai_assistant import get_ai_suggestions
def main():
    all_tickets = load_tickets()
   
    while True:
        print("----CAMPUSFLOW TICKET CREATOR----")
        print("1. Create a ticket")
        print("2. Get AI suggestions for a ticket")
        print("3. Exit")
        choice  = input("Choose an option: ").strip()
        
        if choice == "1":
            title = input("Enter title: ").strip()
            description = input("Enter description: ").strip()
            try:
                new_ticket = create_ticket(all_tickets, title, description)
                all_tickets.append(new_ticket)
                save_tickets(all_tickets)
                print(f"Ticket {new_ticket['id']} saved successfully.")
            except ValueError as e:
                print("Validation Error:", e)
        
        elif choice == "2":
            #ask which ticket to analyze
            ticket__id = input("Enter ticket ID: ").strip().upper()

            #find the ticket
            found_ticket = None
            for each_ticket in all_tickets:
                if ticket__id == each_ticket["id"]:
                    found_ticket = each_ticket
                    break
            if found_ticket is None:
                print("Error: Ticket not found")
                continue
            
            #call the AI function now
            print("\nGetting AI suggestions....")
            suggestion = get_ai_suggestions(found_ticket["description"])

            #display the result
            print("\n---- AI SUGGESTIONS ----")
            print(suggestion)
            print("-------------------------")

        elif choice == "3":
            print("Goodbye!")
            break
    
        else:
            print("Invalid option. Try again!")
if __name__ == "__main__":
    main()