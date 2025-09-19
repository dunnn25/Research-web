from pyvi import ViTokenizer

def tim_kiem_tu(van_ban,tu_can_tim):

    van_ban_tach = ViTokenizer.tokenize(van_ban)

    van_ban_lower = van_ban_tach.lower()
    tu_can_tim_lower = tu_can_tim.lower()

    tu_can_tim_da_chuan_hoa = tu_can_tim_lower.replace(" ","_")

    words = van_ban_lower.split()

    if tu_can_tim_da_chuan_hoa in words:
        return True
    else:
        return False

d =  "Đây là văn bản cần kiểm tra"
t = "kiểm tra"

if tim_kiem_tu(d,t):
    print(f"Từ {t} có trong văn bản")
else:
    print(f"Từ {t} không có trong văn bản")
