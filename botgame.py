import pyautogui as pg
import time

# Point(x=1456, y=775) น้ำจิ้ม
# Point(x=779, y=837) เริ่มเกม


def grill():
    pg.moveTo(427, 611)
    pg.dragTo(826, 274, 1)  # ลากเนื้อ1
    pg.moveTo(561, 645)
    pg.dragTo(1041, 263, 1)  # ลากเนื้อ2
    pg.moveTo(611, 715)
    pg.dragTo(1224, 288, 1)  # ลากเนื้อ3
    pg.moveTo(642, 779)
    pg.dragTo(904, 387, 1)  # ลากเนื้อ4
    pg.moveTo(590, 824)
    pg.dragTo(1259, 387, 1)  # ลากเนื้อ5
    pg.moveTo(522, 779)
    pg.dragTo(1116, 456, 1)  # ลากเนื้อ6


def remeat():
    pg.click(826, 274)  # กลับเนื้อ1
    time.sleep(1)
    pg.click(1041, 263)  # กลับเนื้อ2
    time.sleep(1)
    pg.click(1224, 290)  # กลับเนื้อ3
    time.sleep(1)
    pg.click(904, 387)  # กลับเนื้อ4
    time.sleep(1)
    pg.click(1259, 387)  # กลับเนื้อ5
    time.sleep(1)
    pg.click(1116, 456)  # กลับเนื้อ6


def sauce():
    pg.moveTo(826, 274)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม1
    pg.moveTo(1041, 263)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม2
    pg.moveTo(1224, 288)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม3
    pg.moveTo(904, 387)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม4
    pg.moveTo(1259, 387)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม5
    pg.moveTo(1116, 456)
    pg.dragTo(1469, 772, 1)  # ลากเนื้อใส่น้ำจิ้ม6


def grill2():
    pg.moveTo(420, 722)
    pg.dragTo(826, 274, 1)  # ลากเนื้อ1
    pg.moveTo(357, 690)
    pg.dragTo(1041, 263, 1)  # ลากเนื้อ2
    pg.moveTo(289, 739)
    pg.dragTo(1224, 288, 1)  # ลากเนื้อ3
    pg.moveTo(366, 792)
    pg.dragTo(904, 387, 1)  # ลากเนื้อ4
    pg.moveTo(424, 855)
    pg.dragTo(1259, 387, 1)  # ลากเนื้อ5
    pg.moveTo(271, 820)
    pg.dragTo(1116, 456, 1)  # ลากเนื้อ6


pg.click(779, 837) # เริ่มเกม
for i in range(2):
    grill()
    remeat()
    sauce()
    grill2()
    remeat()
    sauce()







