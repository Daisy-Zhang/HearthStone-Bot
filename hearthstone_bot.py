import pyautogui
import time

def checkturn(turn, state):#check if it is my turn
	temp = state.getpixel((1216, 421))
	if temp[2] == 0:
		turn = True
	else:
		turn = False
	return turn

def passturn(turn):#end my turn
	pyautogui.moveTo(1201, 397, duration = 0.25)
	pyautogui.click()
	turn = False
	return turn

def hero_power():#stable shot
	pyautogui.moveTo(856, 655, duration = 0.25)
	pyautogui.click()

def search_game():#start to search opponent
	pyautogui.moveTo(1096, 721, duration = 0.25)
	pyautogui.click()


def start_game():#check your cards in the beginning
	pyautogui.moveTo(722, 712, duration = 0.25)
	pyautogui.click()

def game_over():#finish the battle and click
	pyautogui.click()

def play_cards():#play your minions
	for i in range(8):
		pyautogui.moveTo(480 + 60 * i, 850, duration = 0.25)
		pyautogui.dragRel(0, -250, duration = 0.25)

def check_taunt():#check if there is an enemy minion with taunt
	state_now = pyautogui.screenshot()
	point_for_this = state_now.getpixel((970, 550))
	if point_for_this == (55, 52, 48, 255):
		print("taunt found")
		return 1
	else:
		return 0

def taunt_policy(x, y):#the policy when there is an enemy minion with taunt
	for i in range(6):
		pyautogui.moveTo(x, y, duration = 0.15)
		pyautogui.dragTo(437 + 115 * i, 375, duration = 0.25)
		pyautogui.moveTo(x, y, duration = 0.15)
		pyautogui.click()

	for i in range(7):
		pyautogui.moveTo(x, y, duration = 0.15)
		pyautogui.dragTo(363 + 115 * i, 375, duration = 0.25)
		pyautogui.moveTo(x, y, duration = 0.15)
		pyautogui.click()


def attack():#odd or even enemy minions's situation
	for i in range(6):
		pyautogui.moveTo(437 + 115 * i, 490, duration = 0.15)
		pyautogui.dragTo(714, 168, duration = 0.25)
		pyautogui.moveTo(437 + 115 * i, 490, duration = 0.15)
		pyautogui.click()
		time.sleep(1.2)
		if check_taunt() == 1:
			taunt_policy(437 + 115 * i, 490)

	for i in range(7):
		pyautogui.moveTo(363 + 115 * i, 490, duration = 0.15)
		pyautogui.dragTo(714, 168, duration = 0.25)
		pyautogui.moveTo(363 + 115 * i, 490, duration = 0.15)
		pyautogui.click()
		time.sleep(1.2)
		if check_taunt() == 1:
			taunt_policy(363 + 115 * i, 490)

def win_or_lose(point):#check if the battle is over
	state_now = pyautogui.screenshot()
	point_now = state_now.getpixel((499, 585))
	#print (point_now)
	localtime = time.asctime(time.localtime(time.time()))
	#print (localtime)
	delta = abs(point_now[0] - point[0]) + abs(point_now[1] - point[1]) + abs(point_now[2] - point[2]) + abs(point_now[3] - point[3])
	if delta < 150:
		return 0
	else:
		return 1

if __name__ == '__main__':
	turn = False
	time.sleep(5)
	start_game()
	print("game start!")
	time.sleep(8)
	state = pyautogui.screenshot()
	win_lose_point = state.getpixel((499, 585))
	while True:
		time.sleep(2)
		state = pyautogui.screenshot()
		turn = checkturn(turn, state)
		if turn:
			print("my turn")
			play_cards()
			print("play cards already")
			attack()
			print("attack already")
			hero_power()
			print("hero power already")
			turn = passturn(turn)
			print("end my turn")
		else:
			print("enemy's turn")
		if win_or_lose(win_lose_point) == 1:
			print("game over!")
			break
		else:
			continue
	pyautogui.click()
	
