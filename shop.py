class Customer:
    def __init__(self, name, grade = "basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += amount * 0.08  # 구매액의 8% 적립

    def get_discount_rate(self):
        if self.grade == "vip":
            return 0.1  # vip 고객은 10% 할인
        return 0.03  # 기본 고객은 3% 할인

    def get_discount(self):
        if self.grade == "vip":
            return 0.1 # vip 고객은 10% 할인
        return 0.03# 기본 고객은 3퍼 할인

    def summary(self):
        return f"[{self.grade}]{self.name} (포인트: {self.points})"



class Order:
     def __init__(self, order_id, customer, items=None):
        self.order_id = order_id
        self.customer = customer          
        self.items = items or []  # 튜플의 리스트 예시: [(상품명, 가격)]
 
     def add_item(self, name , price):
        self.items.append((name, price))
 
     def total_price(self):
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))
  
     def pay(self):
        total = self.total_price()
        self.customer.add_points(total)
        return total


# 검증 코드
if __name__ == "__main__": #주의:그냥 name 이라고 쓰면 에러남
    park = Customer("박지우", "vip")
    Lee = Customer("이기쁨")

    order1 = Order("주문번호1", park, [("라떼", 5500), ("초코쿠키", 4200)])
    order2 = Order("주문번호2", Lee)
    order2.add_item("아메리카노", 4500)
    order3 = Order("주문번호3", park, [("베이글", 6800)])

    for order in (order1, order2, order3):
        total = order.pay()
        print(f"[{order.order_id}] {order.customer.name}님의 결제 금액: {total:,}원입니다.")
 
    print(park.summary())
    print(Lee.summary())