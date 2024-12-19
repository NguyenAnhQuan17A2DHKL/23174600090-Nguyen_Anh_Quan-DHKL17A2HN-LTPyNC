import json
from datetime import datetime

# Danh sách giao dịch mẫu
transactions = [
    {"type": "gold", "amount": 100, "price": 5000},
    {"type": "money", "amount": 200, "price": 1000},
    {"type": "gold", "amount": 50, "price": 2500},
    {"type": "money", "amount": 300, "price": 1500}
]

def save_transactions_to_json(transactions):
    # Lấy thông tin ngày hiện tại theo định dạng: nam-thang-ngay-gio-phut-giay
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{current_time}.json"
    
    # Lưu danh sách các giao dịch vào tệp JSON
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(transactions, json_file, ensure_ascii=False, indent=4)
    
    print(f"Dữ liệu giao dịch đã được ghi vào tệp {file_name}")

def main():
    while True:
        # Hiển thị các giao dịch hiện tại
        print("Danh sách giao dịch hiện tại:")
        for transaction in transactions:
            print(transaction)
        
        # Hỏi người dùng có muốn tiếp tục giao dịch không
        cont = input("Bạn có muốn tiếp tục giao dịch không? (1: Có, 0: Không): ")
        if cont == "0":
            break
        
        # Thêm giao dịch mới
        type = input("Nhập loại giao dịch (gold/money): ")
        amount = float(input("Nhập số lượng: "))
        price = float(input("Nhập giá: "))
        transactions.append({"type": type, "amount": amount, "price": price})
    
    # Hỏi người dùng có muốn ghi vào tệp không
    save = input("Bạn có muốn ghi dữ liệu giao dịch vào tệp không? (1: Có, 0: Không): ")
    if save == "1":
        save_transactions_to_json(transactions)
    else:
        print("Dữ liệu giao dịch không được ghi vào tệp.")

if __name__ == "__main__":
    main()
