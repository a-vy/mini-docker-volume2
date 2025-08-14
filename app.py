import time

turn = 0
while True:
    turn += 1
    with open("data/out.txt", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] turn={turn}\n")
    time.sleep(2)
