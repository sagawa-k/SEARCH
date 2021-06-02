import pandas as pd



# 検索ツール
def search():
  df = pd.read_csv("./source.csv")
  source = list(df["name"])

  while True:
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    if word in source:
      print("「{0}」が見つかりました。".format(word))
    else:
      print("「{0}」が見つかりませんでした。".format(word))
      is_add_name = input("名前を追加登録しますか？(0:しない 1:する)　＞＞　")
      if is_add_name == "1":
        source.append(word)

        df = pd.DataFrame(source, columns=["name"])
        df.to_csv("./source.csv", encoding = "utf_8")
        print(source)

    is_end = input("検索を終了しますか？(0:しない 1:する)　＞＞　")
    if is_end == "1":
      break

if __name__ == "__main__":
  search()