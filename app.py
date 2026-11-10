from pkg.book_tools import (
    add_book,
    read_books,
    search_books,
    show_books,
    show_last_three_and_stats,
    toggle_book_status,
    write_books,
)


def main() -> None:
    """簡易書籍管理系統主程式。"""
    input_file = "books.json"
    output_file = "output.json"

    try:
        books = read_books(input_file)
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {input_file}，程式即將結束。")
        return
    except ValueError:
        print(f"錯誤：{input_file} 的 JSON 格式不正確，程式即將結束。")
        return
    except OSError as error:
        print(f"錯誤：讀取 {input_file} 時發生檔案系統錯誤（{error}），程式即將結束。")
        return

    while True:
        print("\n--- 簡易書籍管理系統 ---")
        print("1. 顯示全部書籍")
        print("2. 新增書籍")
        print("3. 查詢書籍")
        print("4. 變更借閱狀態")
        print("5. 顯示最後 3 筆書籍與統計")
        print("6. 匯出書籍資料")
        print("7. 離開系統")
        print("------------------------")

        choice = input("請選擇功能：").strip()

        if choice == "1":
            print("\n--- 全部書籍 ---")
            show_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            while True:
                keyword = input("請輸入書名關鍵字：").strip()
                if keyword:
                    break
                print("關鍵字不可為空白，請重新輸入。")

            results = search_books(books, keyword)
            if results:
                print("\n--- 查詢結果 ---")
                show_books(results)
            else:
                print("查無符合的書籍。")
        elif choice == "4":
            toggle_book_status(books)
        elif choice == "5":
            show_last_three_and_stats(books)
        elif choice == "6":
            write_books(books, output_file)
        elif choice == "7":
            print("系統已退出。")
            break
        else:
            print("無效的選項，請輸入 1 到 7 之間的數字。")


if __name__ == "__main__":
    main()