from PIL import Image
import os

def images_to_pdf(start_num, end_num, output_pdf):
    # 画像のリストを保持するリストを初期化
    images = []
    
    # 画像ファイルのパスを生成してリストに追加
    for i in range(start_num, end_num + 1):
        file_name = f"{i:04}.png"
        file_path = os.path.join("out", file_name)
        if os.path.exists(file_path):
            img = Image.open(file_path)
            images.append(img.convert('RGB'))  # PDFにはRGBモードで保存
        
    # 画像を1つのPDFに結合
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"Saved PDF: {output_pdf}")
    else:
        print("No images found to create PDF.")

if __name__ == "__main__":
    # 開始番号と終了番号を指定
    start_num = 1
    end_num = 270
    output_pdf = "output.pdf"
    
    # 画像をPDFに変換
    images_to_pdf(start_num, end_num, output_pdf)
