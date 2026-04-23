class UserService:
    def login(self, user_name: str, password: str) -> dict:
        print(f'[UserService] Logging in: {user_name}')
        return {'user_id': "U123", 'name': user_name}
    
    def get_profile(self, user_id: str) -> dict:
        print(f'[UserService] Getting profile for: {user_id}')
        return {'user_id': user_id,  'name': "Rahul", 'address': 'Mumbai'}
    
class OrderService:
    def get_orders(self, user_id: str) -> list:
        print(f'[OrderService] Getting orders for: {user_id}')
        return [
            {'order_id': 'ORD-1', 'total': 1500},
            {'order_id': 'ORD-2', 'total': 2000},
        ]

class ApiGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()
    
    def get_orders(self, user_id: str):
        self.__order_service.get_orders(user_id)
    
    def login(self, username: str, password: str):
        self.__user_service.login(username, password)
    
    def get_profile(self, user_id: str):
        self.__user_service.get_profile(user_id)
    
    def get_all_details(self, user_name: str, password: str, user_id):
        self.__user_service.get_profile(user_id)
        self.__user_service.login(user_name, password)
        self.__order_service.get_orders(user_id)
        
        
api_gateway = ApiGateway()
api_gateway.get_all_details('anmolranjan045', '123', 'U123')