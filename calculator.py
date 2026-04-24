#First_project
def add(x, y):
    """Qo'shish funksiyasi"""
    return x + y

def subtract(x, y):
    """Ayirish funksiyasi"""
    return x - y

def multiply(x, y):
    """Ko'paytirish funksiyasi"""
    return x * y

def divide(x, y):
    """Bo'lish funksiyasi (Nolga bo'lishni tekshiradi)"""
    if y == 0:
        return "Xato! Nolga bo'lish mumkin emas."
    return x / y

def main():
    print("--- Python Kalkulyatoriga Xush Kelibsiz! ---")
    print("Amallar:")
    print("1. Qo'shish (+)")
    print("2. Ayirish (-)")
    print("3. Ko'paytirish (*)")
    print("4. Bo'lish (/)")

    while True:
        # Foydalanuvchi tanlovini olish
        choice = input("Amalni tanlang (1/2/3/4) yoki chiqish uchun 'q' bosing: ")

        # Chiqish tekshiruvi
        if choice.lower() == 'q':
            print("Dastur tugatildi. Sog' bo'ling!")
            break

        # Tanlov to'g'riligini tekshirish
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Birinchi sonni kiriting: "))
                num2 = float(input("Ikkinchi sonni kiriting: "))
            except ValueError:
                print("Xato! Iltimos, faqat son kiriting.")
                continue

            # Hisoblash va natijani chiqarish
            if choice == '1':
                print(f"Natija: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Natija: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Natija: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str): # Agar xato matni qaytsa
                    print(result)
                else:
                    print(f"Natija: {num1} / {num2} = {result}")
            
            print("-" * 20) # Ajratuvchi chiziq

        else:
            print("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()
