import re

# Dữ liệu mẫu bạn đã cung cấp
data = """
- congdac09@gmail.com
- --------------------[shared indicator privated]------------------
- 【The☯Take】:  https://www.tradingview.com/script/eIdB8hnQ-The-Take/
- ☯: https://www.tradingview.com/script/k04PsyvB/
- Alert: https://www.tradingview.com/script/8huOUpbV-Alert-multi-symbols-at-specific-timeframe-in-N-day-look-back/
- ------------------------------------------------------------------
- --------------------------[list symbol]----------------------------
- list symbols: https://www.tradingview.com/watchlists/63910864/
- default: https://www.tradingview.com/chart/
- 
- ---------------------------[1m]-------------------------------------
- Forex: https://www.tradingview.com/chart/JedvVjKg/
- Euro:  https://www.tradingview.com/chart/3noHzaYd/
- Asia:  https://www.tradingview.com/chart/jhSv8alA/
- Stock: https://www.tradingview.com/chart/6cRyXnSV/
- Stock-US: https://www.tradingview.com/chart/cC86mBDK/
- Coin:  https://www.tradingview.com/chart/wYNYz2MP/
-
- ---------------------------[15m]-------------------------------------
- Forex: https://www.tradingview.com/chart/O1oZXV8m/
- Euro:  https://www.tradingview.com/chart/HLDm6cAz/
- Asia:  https://www.tradingview.com/chart/vxMDnj6k/
- Metal: https://www.tradingview.com/chart/Q6c01kWD/
- Soft: https://www.tradingview.com/chart/6tuWK8zz/
- Stock: https://www.tradingview.com/chart/jQK6fklD/
- Stock-US: https://www.tradingview.com/chart/UjcRkLKW/
- Coin: https://www.tradingview.com/chart/y9E01I7B/
-
- ---------------------------[1H]-------------------------------------
- Forex: https://www.tradingview.com/chart/k1VfmKBP/
- Euro:  https://www.tradingview.com/chart/XYXkB44r/
- Asia:  https://www.tradingview.com/chart/oyM37JXH/
- Metal: https://www.tradingview.com/chart/T3fmeW19/
- Soft: https://www.tradingview.com/chart/cE5wzffR/
- Stock: https://www.tradingview.com/chart/IWX8z3Vk/
- Stock-US: https://www.tradingview.com/chart/DLnGwd0C/
- Stock_VN1: https://www.tradingview.com/chart/dDiG5zNU/
- Stock_VN2: https://www.tradingview.com/chart/6QGN2pds/
- Coin: https://www.tradingview.com/chart/2Q2GSRgw/
- 
- ---------------------------[4H]-------------------------------------
- Forex: https://www.tradingview.com/chart/4Bsts75O/
- Euro:  https://www.tradingview.com/chart/XUXjnim7/
- Asia:  https://www.tradingview.com/chart/tdB1AZNb/
- Metal: https://www.tradingview.com/chart/bJzWn9aC/
- Soft: https://www.tradingview.com/chart/fNZ5Reb9/
- Stock: https://www.tradingview.com/chart/kA26TkJY/
- Stock-US: https://www.tradingview.com/chart/Lmd4Kf7w/
- Stock_VN1: https://www.tradingview.com/chart/kAPtZG5E/
- Stock_VN2: https://www.tradingview.com/chart/Y8jmfcrd/
- Coin: https://www.tradingview.com/chart/WRiPbJFL/
-
- ---------------------------[1D]-------------------------------------
- Forex: https://www.tradingview.com/chart/L6hVfumd/
- Euro:  https://www.tradingview.com/chart/iU8BSQTY/
- Asia:  https://www.tradingview.com/chart/htyC3uBy/
- Metal: https://www.tradingview.com/chart/Arb13gYe/
- Soft: https://www.tradingview.com/chart/ZJ10CRZL/
- Stock: https://www.tradingview.com/chart/SBCSEDiP/
- Stock-US: https://www.tradingview.com/chart/wkHKptOl/
- Stock_VN1: https://www.tradingview.com/chart/e9vpVmd2/
- Stock_VN2: https://www.tradingview.com/chart/sGBC6Cly/
- Coin: https://www.tradingview.com/chart/znlFN4yp/
-
- ---------------------------[1W]-------------------------------------
- Forex: https://www.tradingview.com/chart/apS1i8Nf/
- Euro:  https://www.tradingview.com/chart/5kx0wfpN/
- Asia:  https://www.tradingview.com/chart/RsPslYK6/
- Metal: https://www.tradingview.com/chart/Cof71cZk/
- Soft: https://www.tradingview.com/chart/zYQlrqdV/
- Stock: https://www.tradingview.com/chart/b1neWJNS/
- Stock-US: https://www.tradingview.com/chart/vmHJBe1H/
- Stock_VN1: https://www.tradingview.com/chart/SXkpedqg/
- Stock_VN2: https://www.tradingview.com/chart/rr5VWCbL/
- Coin: https://www.tradingview.com/chart/57FtXlAM/
-
- ---------------------------[1MN]-------------------------------------
- Forex: https://www.tradingview.com/chart/QmPdaCFm/
- Euro:  https://www.tradingview.com/chart/LymnVVci/
- Asia:  https://www.tradingview.com/chart/rFW19vBi/
- Metal: https://www.tradingview.com/chart/hXIEu4ls/
- Soft: https://www.tradingview.com/chart/M9HBOA0P/
- Stock: https://www.tradingview.com/chart/l9Rs32N5/
- Stock-US: https://www.tradingview.com/chart/h7MFU7A9/
- Stock_VN1: https://www.tradingview.com/chart/D9jq2ufo/
- Stock_VN2: https://www.tradingview.com/chart/BG62pNrf/
- Coin: https://www.tradingview.com/chart/fvLZAbZq/
-
- ---------------------------[1Y]-------------------------------------
- Forex: https://www.tradingview.com/chart/ktaIufpt/
- Euro: https://www.tradingview.com/chart/hhtAV8Gu/
- Asia: https://www.tradingview.com/chart/vLuNjSqE/
- Metal: https://www.tradingview.com/chart/ilOcsZlB/
- Soft: https://www.tradingview.com/chart/gUhqeteB/
- Stock: https://www.tradingview.com/chart/xgdECXjm/
- Stock-US:  https://www.tradingview.com/chart/HzKyMK8B/
- Stock_VN1: https://www.tradingview.com/chart/5SFtTVMs/
- Stock_VN2: https://www.tradingview.com/chart/Rrc1p9ED/
- Coin: https://www.tradingview.com/chart/MP347lHp/
-
- ----------------------------[general]-------------------------------
- DXY_US500_BTC_VN30_1W-1H: https://www.tradingview.com/chart/FbuuVpji/
- DXY_US500_BTC_VN30_1H-1m: https://www.tradingview.com/chart/bnQKq357/
- US500_BTC_XAU_OIL_1W-1H: https://www.tradingview.com/chart/QVONaRWO/
- US500_BTC_XAU_OIL_1H-1m: https://www.tradingview.com/chart/ej0q1u40/
- DXY: https://www.tradingview.com/chart/ECJFFGNy/
- JXY: https://www.tradingview.com/chart/LGSiDGmD/
- EXY: https://www.tradingview.com/chart/syc5GVlY/
- USD_EUR_JPY: https://www.tradingview.com/chart/GyOZgYWZ/
-
-
- AUS200: https://www.tradingview.com/chart/gV1zppLj/
- HK50: https://www.tradingview.com/chart/ez4iW5rl/
- CHINA50: https://www.tradingview.com/chart/SVtd1JNI/
- UK100: https://www.tradingview.com/chart/kOMalY4t/
- GER40: https://www.tradingview.com/chart/7ggA5SBt/
- JPN225: https://www.tradingview.com/chart/xXIEBmBH/
- VN30: https://www.tradingview.com/chart/8sK1pFNf/
- VNINDEX: https://www.tradingview.com/chart/msx0G3i0/
- US30: https://www.tradingview.com/chart/O98o3tgq/
- US500: https://www.tradingview.com/chart/xovr4TIS/
- Oil: https://www.tradingview.com/chart/qhnKAlNz/
- Silver: https://www.tradingview.com/chart/zbokCqf1/
- Gold: https://www.tradingview.com/chart/vFXRA4vt/
- BNB: https://www.tradingview.com/chart/yFH5TJqj/
- ETH: https://www.tradingview.com/chart/yc56kTHN/
- BTC: https://www.tradingview.com/chart/ihJOIy6E/
-
-
- Coffee: https://www.tradingview.com/chart/zCHSsu3f/
- Cotton: https://www.tradingview.com/chart/Zmcbz1GU/
- Sugar: https://www.tradingview.com/chart/mHJBrPVe/
- Soybeans: https://www.tradingview.com/chart/lAQlBhS5/
- Cocoa: https://www.tradingview.com/chart/1bPePKBe/
- RighRice: https://www.tradingview.com/chart/wxqMNjZx/
- Corn: https://www.tradingview.com/chart/kgMXyAoV/
- SoyMeal: https://www.tradingview.com/chart/yYM57BpF/
- SoyOil: https://www.tradingview.com/chart/Gd2w9gtG/
-
-
- Platium, XPT: https://www.tradingview.com/chart/hSE66E1U/
- Alu, Aluminium: https://www.tradingview.com/chart/ksshX5mp/
- Copper: https://www.tradingview.com/chart/QjlXAx0w/
- Nickel: https://www.tradingview.com/chart/aYkzfMJV/
- Lead: https://www.tradingview.com/chart/fW8sLoUv/
- Zinc: https://www.tradingview.com/chart/ttDhYvGj/

"""

# Hàm trích xuất bookmark từ dữ liệu
def extract_bookmarks(data):
    bookmarks = {}
    
    # Tìm tất cả các subfolder trong dấu [xxx]
    folder_pattern = re.compile(r'---\[(.*?)\]---')
    folder_matches = folder_pattern.findall(data)

    # Lặp qua từng subfolder
    for folder in folder_matches:
        # Tìm các mục trong subfolder
        folder_data_pattern = re.compile(r'---\[' + re.escape(folder) + r'\]---(.*?)(?=---\[|\Z)', re.DOTALL)
        folder_data = folder_data_pattern.search(data).group(1).strip()

        # Tìm các mục name:link
        link_pattern = re.compile(r'(\S+):\s*(https?://\S+)')
        links = link_pattern.findall(folder_data)

        # Lưu vào dict
        bookmarks[folder] = [{"Name": name, "Link": link} for name, link in links]

    return bookmarks

# Hàm tạo file bookmark
def generate_bookmark_file(bookmarks_data):
    header = '''
    <!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!-- This is an automatically generated file.
         It will be read and overwritten.
         DO NOT EDIT! -->
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>
        <DT><H3 ADD_DATE="1730285454" LAST_MODIFIED="1730721852" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks bar</H3>
        <DL><p>
    '''
    
    botder = '''
        </DL><p>
    </DL><p>
    '''
    
    bookmark_in_subfolder_template = '''
        <DT><H3 ADD_DATE="1730285467" LAST_MODIFIED="0">{NameFolder}</H3>
        <DL><p>
            {Links}
        </DL><p>
    '''
    
    bookmark_template = '''
        <DT><A HREF="{Link}" ADD_DATE="1728961208" ICON="">{Name}</A>
    '''

    # Tạo nội dung bookmark từ dữ liệu
    bookmark_file_content = header
    for folder, bookmarks in bookmarks_data.items():
        links_content = "".join([bookmark_template.format(Name=bookmark["Name"], Link=bookmark["Link"]) for bookmark in bookmarks])
        bookmark_file_content += bookmark_in_subfolder_template.format(NameFolder=folder, Links=links_content)
    
    bookmark_file_content += botder
    return bookmark_file_content

# Trích xuất dữ liệu bookmark từ mẫu dữ liệu
bookmarks_data = extract_bookmarks(data)

# Tạo file bookmark HTML
bookmark_file_content = generate_bookmark_file(bookmarks_data)

# Lưu vào file import.html
with open('import.html', 'w', encoding='utf-8') as f:
    f.write(bookmark_file_content)

print("Bookmarks saved to import.html")
