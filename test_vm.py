from vm import VendingMachine


def test_초기_잔액은_0원():
   m = VendingMachine()
   assert "잔액은 0원입니다" == m.run("잔액")

def test_동전_넣고_잔액_검사():
   m = VendingMachine()
   assert "100원을 넣었습니다" == m.run("동전 100")
   assert "잔액은 100원입니다" == m.run("잔액")

def test_잔액_누적():
   m = VendingMachine()
   m.run("동전 100")
   m.run("동전 100")
   assert "잔액은 200원입니다" == m.run("잔액")

def test_음료_뽑기():
   m = VendingMachine()
   m.run("동전 500")
   assert "커피가 나왔습니다" == m.run("음료 커피")
   assert "잔액은 350원입니다" == m.run("잔액")
   assert "우유가 나왔습니다" == m.run("음료 우유")
   assert "잔액은 150원입니다" == m.run("잔액")

def test_모르는_음료_뽑기():
   m = VendingMachine()
   m.run("동전 500")
   assert "알 수 없는 음료입니다" == m.run("음료 맥주")
   assert "잔액은 500원입니다" == m.run("잔액")

def test_동전이_부족한_상황에서_음료_뽑기():
   m = VendingMachine()
   m.run("동전 100")
   assert "잔액이 부족합니다" == m.run("음료 커피")
   assert "잔액은 100원입니다" == m.run("잔액")

def test_unknown_command():
   m = VendingMachine()
   assert "알 수 없는 명령입니다" == m.run("웅앵")

def test_valid_coins():
   m = VendingMachine()
   valid_coins = ["10", "50", "100", "500"]
   for coin in valid_coins:
       assert coin + "원을 넣었습니다" == m.run("동전 " + coin)

def test_10():
   m = VendingMachine()
   assert "10원을 넣었습니다" == m.run("동전 10")

def test_50():
   m = VendingMachine()
   assert "50원을 넣었습니다" == m.run("동전 50")

def test_100():
   m = VendingMachine()
   assert "100원을 넣었습니다" == m.run("동전 100")

def test_500():
   m = VendingMachine()
   assert "500원을 넣었습니다" == m.run("동전 500")

def test_invalid_coin():
   m = VendingMachine()
   assert "알 수 없는 동전입니다" == m.run("동전 999")

def test_동전반환():
    m = VendingMachine()
    m.run("동전 670")
    assert "500원 1개, 100원 1개, 50원 1개, 10원 2개" == m.run("반환")
    assert "잔액이 없습니다" == m.run("잔액")





# from vm import VendingMachine
#
# # 최대한 쪼개서 해야 한다. 하나의 def 안에 첫번째 assert가 깨지면 아래것은 테스트를 못하기 때문이다.
#
# def test_initial_change_should_be_zero():
#     m = VendingMachine()  # 벤딩머신의 새로운 인스턴스가 생긴다. (VendingMachine은 개념이다. 이것의 실체인 인스턴스를 만들어놓고 써야 한다. 그냥 VendingMachine.run 은 쓸 수 없다. )
#     assert "잔액은 0원입니다" == m.run(“잔액“)
#
# def test_insert_coin_and_check():
#     m = VendingMachine()
#     assert “100원을 넣었습니다" == run(“동전 100")
#     assert “잔액은 100원입니다” == run(“잔액“)
#
# def test_accumulation_of_change():
#     m = VendingMachine()
#     run(“동전 100”)
#     run(“동전 100")
#     assert “잔액은 200원입니다” == run(“잔액“)
#
# def test_mola():
#     m = VendingMachine()
#     assert “알 수 없는 명령 입니다” == run(“우애웅“)
