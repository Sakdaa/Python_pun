from mama_turtle import road, find_pol
import math

def brunelleschi_lamp(vx, vy, x0, y0, h, d, logfile='log.txt'):


    b_point = (x0, y0)
    e_point = (vx, vy)
    L, alpha = find_pol(b_point, e_point, rad=True)
    
    # 2. คำนวณมุม beta
    beta = math.pi - alpha

    # 3. คำนวณ H และ tau
    H = (L - d) * math.sin(beta)
    tau = (L - d) * math.cos(beta)
    
    # 4. หามุม theta จากด้านบนของเสาหลอดไฟอ้างอิง (x0, y0 + h) ไปยัง (vx, vy)
    top_point = (x0, y0 + h)
    L_top, theta = find_pol(top_point, e_point, rad=True)
    
    # 5. คำนวณมุม phi
    phi = math.pi - theta

    # 6. คำนวณ h'
    h_prime = H - tau * math.tan(phi)
    
    # บันทึกข้อมูลการคำนวณลงในไฟล์ล็อก
    inp_msg = "Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, " + \
              "height={:.2f}, d={:.2f}.\n"
    inp_msg = inp_msg.format(vx, vy, x0, y0, h, d)

    calc_msg = "Calc: L = {:.2f}, beta = {:.2f}, " + \
        "H = {:.2f}, tau = {:.2f}, phi = {:.2f}, " + \
        "h' = {:.2f}.\n"
    calc_msg = calc_msg.format(L, beta, H, tau, phi, h_prime)
    with open(logfile, 'a') as f:
        f.write(inp_msg)
        f.write(calc_msg)
    
    return h_prime

if __name__ == '__main__':
    r = road() 
    vx, vy = 0, 75
    x, y = 100, -100 
    height = 40 
    d = 0 
    res = brunelleschi_lamp(vx, vy, x, y, height, d) 
    print('Ans =', res)

    # r.draw_road()
    # r.draw_lamp_posts(brunelleschi_lamp)

    # input('enter to exit')
