#P4
def krill_consumption(feeding, whales):
    total_consumption = 0
    
    # วนลูปผ่านแต่ละชนิดของวาฬใน feeding dictionary
    for whale_type, daily_diet in feeding.items():
        if whale_type in whales:
            # คำนวณการบริโภคคริลสำหรับวาฬชนิดนี้และเพิ่มใน total_consumption
            total_consumption += daily_diet * whales[whale_type]
    
    return total_consumption

feeding = {'Humpback whale': 2000, 'Gray whale': 1500, 'Bowhead whale': 
2500, 'Blue whale': 3600} 
whales = {'Bowhead whale': 80000}

if __name__ == "__main__":
    total_consum = krill_consumption(feeding, whales)
    print('Estimate daily consumption: %d kg of krill' % total_consum)
