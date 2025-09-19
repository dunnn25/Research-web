def tim_kiem_tu(van_ban, tu_can_tim):
    van_ban_lower = van_ban.lower()
    tu_tim_lower = tu_can_tim.lower()

    # words = van_ban_lower.split()
    if tu_tim_lower in van_ban_lower:
        return  True
    else:
        return False


d = " Đây là một tài liệu mẫu dùng để kiểm tra chức năng tìm kiếm từ trong văn bản"
t = "kiểm tra"

if tim_kiem_tu(d,t):
    print(f"Từ {t} có mặt trong văn bản")
else:
    print(f"Tu {t} không có trong văn bản")
