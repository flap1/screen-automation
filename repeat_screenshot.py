import pyautogui
import argparse
import time
import os

def take_screenshots(start_num, count, region, click_position, sleep_time):
    # outディレクトリを作成
    output_dir = "out"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i in range(count):
        # ファイル名を生成（0001.pngの形式）
        file_name = f"{start_num + i:04}.png"
        file_path = os.path.join(output_dir, file_name)
        
        # スクリーンショットを撮る
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(file_path)
        print(f"Saved screenshot: {file_path}")
        
        # 指定された位置をクリック
        pyautogui.click(click_position)
        print(f"Clicked at position: {click_position}")
        
        # 次の操作の前にスリープ
        time.sleep(sleep_time)

if __name__ == "__main__":
    # コマンドライン引数を解析
    parser = argparse.ArgumentParser(description="Take repeated screenshots and click specified location.")
    parser.add_argument('--start_num', type=int, required=True, help="Starting number for screenshot filenames (e.g., 1 for 0001.png)")
    parser.add_argument('--count', type=int, required=True, help="Number of screenshots to take")
    parser.add_argument('--region', type=int, nargs=4, default=[393, 0, 3054, 2160], help="Region to capture (x, y, width, height) [default: 395 0 3052 2180]")
    parser.add_argument('--click_position', type=int, nargs=2, default=[3770, 1068], help="Position to click (x, y) [default: 3770 1068]")
    parser.add_argument('--sleep_time', type=float, default=0.5, help="Time to sleep between actions in seconds (default: 1.0)")
    
    args = parser.parse_args()
    
    # スクリーンショットを撮り、クリックする処理を繰り返す
    take_screenshots(args.start_num, args.count, tuple(args.region), tuple(args.click_position), args.sleep_time)
