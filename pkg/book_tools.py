import json


def read_books(file_name: str) -> list:
    """讀取 JSON 書籍資料並回傳。

    參數:
        file_name (str): 要讀取的 JSON 檔案路徑。

    回傳:
        list: 包含多筆書籍字典 (dict) 的串列。
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def write_books(books: list, file_name: str) -> None:
    """將書籍資料寫入 JSON 檔案。

    參數:
        books (list): 書籍資料串列。
        file_name (str): 要匯出的 JSON 檔案路徑。

    回傳:
        None
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
        print(f"已匯出 {len(books)} 筆書籍資料至 {file_name}。")
    except OSError as error:
        print(f"檔案寫入失敗，無法匯出資料：{error}")


def search_books(books: list, keyword: str) -> list:
    """依書名關鍵字查詢書籍並回傳結果。

    參數:
        books (list): 書籍資料串列。
        keyword (str): 書名查詢關鍵字（不區分英文大小寫）。

    回傳:
        list: 符合關鍵字的書籍串列。
    """
    lower_keyword = keyword.lower()
    return [
        book for book in books
        if lower_keyword in book["title"].lower()
    ]


def show_books(books: list) -> None:
    """顯示書籍資料。

    參數:
        books (list): 要顯示的書籍資料串列。

    回傳:
        None
    """
    if not books:
        print("目前沒有書籍資料。")
        return

    print(f"{'編號':>4}  {'書籍編號':<8}  {'書名':<16}  {'作者':<8}  {'價格':>6}  {'狀態'}")
    for index, book in enumerate(books, 1):
        status = "已借出" if book["borrowed"] else "可借閱"
        print(
            f"{index:>4}  {book['id']:<10}  {book['title']:<16}  "
            f"{book['author']:<8}  {book['price']:>8,}  {status}"
        )


def add_book(books: list) -> None:
    """依序輸入欄位並新增一筆書籍資料至串列中。

    參數:
        books (list): 目前的書籍資料串列。

    回傳:
        None
    """
    while True:
        book_id = input("請輸入書籍編號：").strip()
        if not book_id:
            print("書籍編號不可為空白，請重新輸入。")
            continue

        is_duplicate = False
        for book in books:
            if book["id"] == book_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("書籍編號已存在，請重新輸入。")
        else:
            break

    while True:
        title = input("請輸入書名：").strip()
        if title:
            break
        print("書名不可為空白，請重新輸入。")

    while True:
        author = input("請輸入作者：").strip()
        if author:
            break
        print("作者不可為空白，請重新輸入。")

    while True:
        price_str = input("請輸入價格：").strip()
        try:
            price = int(price_str)
            if price > 0:
                break
            print("價格須為大於 0 的整數，請重新輸入。")
        except ValueError:
            print("價格須為大於 0 的整數，請重新輸入。")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "price": price,
        "borrowed": False
    }
    books.append(new_book)
    print("新增成功。")


def toggle_book_status(books: list) -> None:
    """輸入書籍編號以切換該書的借閱狀態。

    參數:
        books (list): 目前的書籍資料串列。

    回傳:
        None
    """
    target_id = input("請輸入書籍編號：").strip()
    for book in books:
        if book["id"] == target_id:
            book["borrowed"] = not book["borrowed"]
            status = "已借出" if book["borrowed"] else "可借閱"
            print(f"「{book['title']}」的狀態已變更為：{status}")
            return

    print("查無此書籍編號。")


def show_last_three_and_stats(books: list) -> None:
    """顯示最後 3 筆書籍與全部書籍的統計資訊。

    參數:
        books (list): 目前的書籍資料串列。

    回傳:
        None
    """
    if not books:
        print("目前沒有書籍資料。")
        return

    print("\n--- 最後 3 筆書籍 ---")
    last_three = books[-3:]
    show_books(last_three)

    total_count = len(books)
    borrowed_count = sum(1 for book in books if book["borrowed"])
    available_count = total_count - borrowed_count
    total_price = sum(book["price"] for book in books)
    avg_price = total_price / total_count

    print("\n--- 書籍統計 ---")
    print(f"書籍總數：{total_count}")
    print(f"可借閱：{available_count}")
    print(f"已借出：{borrowed_count}")
    print(f"價格合計：{total_price:,} 元")
    print(f"平均價格：{avg_price:.2f} 元")