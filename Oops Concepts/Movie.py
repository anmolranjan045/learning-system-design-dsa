class Movie:
    def __init__(self, name: str, total_seats: int, ticket_price: float) -> None:
        self.movie_name = name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0
    
    def book_ticket(self, num_tickets:str) -> None:
        if(self.total_seats - self.booked_seats >= num_tickets):
            cost = self.ticket_price * num_tickets
            self.booked_seats += num_tickets
            print(f'Tickets booked. Total amount to be paid: {cost}')
        else:
            print(f'Sorry, not enough seats available')
    
    def show_status(self) -> None:
        print(f'Movie Name: {self.movie_name}')
        print(f'Remaining Seats: {self.total_seats - self.booked_seats}')
        print(f'Seats Available: {self.booked_seats}')
        
movie = Movie("Krish", 100, 499)
movie.show_status()
movie.book_ticket(70)
movie.show_status()
movie.book_ticket(70)