def P5_wer(ref, test):
    # สร้างตารางต้นทุน
    m, n = len(ref), len(test)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # กำหนดต้นทุนเริ่มต้น
    for i in range(m + 1):
        dp[i][0] = i  # การลบทั้งหมด
    for j in range(n + 1):
        dp[0][j] = j  # การแทรกทั้งหมด

    # เติมตารางด้วยการคำนวณค่า WER
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if ref[i - 1] == test[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # การลบ
                dp[i][j - 1] + 1,  # การแทรก
                dp[i - 1][j - 1] + cost  # การแทนที่
            )

    # ค่าต้นทุนขั้นต่ำในการเปลี่ยน ref เป็น test
    min_operations = dp[m][n]
    wer = min_operations / len(ref)
    
    return wer, min_operations

# ทดสอบฟังก์ชัน
if __name__ == '__main__':
    wer, n = P5_wer("grit", "greet")
    print("wer = {:.3f}, n = {}".format(wer, n))
