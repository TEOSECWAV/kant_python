# 초기 상품 나열
# 리스트 {상품명, 가격, 재고}
# 맨앞 번호 자동 생성, 번호 +=1

# 상품명 
# 가격(끝에 "원" 붙이기, :3 단위,)
# 재고 끝에 "개" 붙이기, 재고가 0일시 "품절" 

# 장바구니 타이틀 출력
def show_title():    
    print("-"*55)
    print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
    print("-"*55)

    print ("선택: 1")

class Item:
    def __init__(self,num,name,price,stock):
        self.num = num
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self,):
        self.bucket = []

    def add_item(self, item):
        self.bucket.append({item})

    def remove_item(self, name):
        for item in self.bucket:
            if item["name"] == name:
                self.bucket.remove(item)
                return
            print("장바구니에 없는 상품입니다.")

    def total(self):
        return sum(item["price"] for item in self.bucket)
    
    def discount(self, percent):
        """정률 할인 후 금액 반환 (장바구니 내용은 그대로)"""
        return int(self.total() * (1 - percent/100))

def show_items(items):
    for item in items:
        if item.stock == 0:
            stock_text = "품절"
        else:
            stock_text = f"재고 {item.stock}개"
        print(f"{item.num}. {item.name} {item.price:,}원 ({stock_text})")

def find_item(items, num):
    for item in items:
        if item.num == num:
            return item
    return None

items = [
    Item(1, "무선 이어폰", 89000, 3),
    Item(2, "텀블러", 15000, 10),
    Item(3, "보조배터리", 32000, 5),
    Item(4, "마우스패드", 9000, 0),
    Item(5, "USB 허브", 18000, 4),
]

cart = ShoppingCart()
show_title()
show_items(items)

# print ("선택: 2")
#     while True:
#         def ask_number():
#             print("상품 번호를 입력하시오.")
#             answer = input("번호를 선택하세요 : ").strip()
#             if item.stock > 0:
#                 print(f"상품 번호: {ask_number}")
#             else:
#                 print("품절된 상품입니다.")
#             return int(answer)



