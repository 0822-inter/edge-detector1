import cv2
import sys
import numpy as np


def main():
    # 画像を読み込む（ファイル名: input.jpg）
    img = cv2.imread('input.jpg')

    if img is None:
        print("エラー: input.jpg が見つかりません。フォルダに画像を入れてください。")
        sys.exit(1)

    # 白黒（グレースケール）に変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 輪郭抽出（Canny法という有名なアルゴリズム）
    edges = cv2.Canny(gray, 100, 200)

    # エッジのみを赤で表示し、それ以外は黒にする
    colored = np.zeros_like(img)
    colored[edges != 0] = (0, 0, 255)

    # 結果を保存
    cv2.imwrite('output.jpg', colored)
    print("変換完了！ output.jpg を作成しました。")


if __name__ == "__main__":
    main()
