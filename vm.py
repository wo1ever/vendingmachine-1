class VendingMachine:
   def __init__(self):
       self._change = 0

   def run(self, raw):
       tokens = raw.split(” “)
       cmd, params = tokens[0], tokens[1:]

       # if 와 elif는 중간에 띄어쓰지 않는다.

       if cmd == “잔액“:
           return “잔액은 ” + str(self._change) + “원입니다”
       elif cmd == “동전“:
           # known_coins = [“10”, “50", “100”, “500"]
           known_coins = “10,50,100,500”.split(“,”)

           coin = params[0]
           if coin not in known_coins:
               return “알 수 없는 동전입니다”
           self._change += int(coin)
           return coin + “원을 넣었습니다”

       elif cmd == “음료“:
           known_beverage = “커피”
           price = 150

           beverage = params[0]
           if beverage != known_beverage:
               return “알 수 없는 음료입니다”
           if self._change < price:
               return “잔액이 부족합니다”
           self._change = self._change - price
           return beverage + “가 나왔습니다”
       else:
           return “알 수 없는 명령입니다”



# class VendingMachine:  # 타입을 만든다 # 메세지는 인스턴스에게 보내진다.
#     def __init__(self):  # 이닛은 벤딩머신 클래스가 호출되는 순간 실행된다. self는 지금 만들어진 인스턴스를 말함
#         self._change = 0  # VendingMachine  에 change라는 변수가 생기고 값이 0이다.
#                           # 중간에 _ 이 들어가면 쓰지 말라는 럿임
#
#     def run(self, raw):  # v1 첫번째 벤딩머신이 self로 담기고, 동전 100 이 raw에 담긴다.
#
#         tokens = raw.split(” “)
#         cmd, params = tokens[0], tokens[1:]
#
#         if cmd == “잔액“:
#             return “잔액은 ” + str(self._change) + “원입니다”
#
#         elif cmd == “동전“:
#             coin = params[0]
#             self._change = int(coin) + change
#             return coin + “원을 넣었습니다”
#
#         else :
#             return “알 수 없는 명령 입니다”

       # 인터페이스로 바꾸거나 번역할때 a 와 b 가 같은것으로 처리되는가? 그렇다면 중복이다!

# v1 = VendingMachine()
# v2 = VendingMachine()
# v1.run(“동전 100”)
