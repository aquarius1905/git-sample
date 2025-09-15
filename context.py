class MyContext:
    def __enter__(self):
        print("開始時の処理")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("終了時の処理")

with MyContext() as ctx:
    print("中の処理")