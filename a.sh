#!/bin/bash

#C:\Users\userName\.bashrc
#source D:/02_Git/MT5/a.sh
#=============================================================[begin copy MT5]==============================================================================
# Định nghĩa màu cho log
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Đường dẫn cơ bản đến thư mục Users
base_path="/c/Users"

copy() {
	# Kiểm tra tùy chọn -d
	delete_before_copy=false
	while getopts "d" opt; do
		case $opt in
			d)
				delete_before_copy=true
				;;
			*)
				echo -e "${RED}Usage: $0 [-d]${NC}"
				exit 1
				;;
		esac
	done

	echo -e "${BLUE}Starting folder search and file management...${NC}"

	# Tìm và xử lý các thư mục cần thiết trong AppData/Roaming/MetaQuotes/Terminal
	find "$base_path" -type d -path "*/AppData/Roaming/MetaQuotes/Terminal/*" | grep -E "/(MQL5/Experts|MQL5/Indicators|MQL5/Files|MQL5/Profiles/Charts|MQL5/Profiles/Templates)$" | while read -r folder; do
		echo -e "${CYAN}Processing folder: ${folder}${NC}"
		
		# Kiểm tra nếu folder tồn tại, nếu không, báo lỗi
		if [ -d "$folder" ]; then
			# Xóa tất cả các file và thư mục con bên trong mỗi thư mục tìm được nếu -d được truyền vào
			if $delete_before_copy; then
				echo -e "${YELLOW}Clearing existing contents in $folder...${NC}"
				rm -rf "$folder"/* || echo -e "${RED}Failed to clear contents in ${folder}${NC}"
				echo -e "${GREEN}Cleared contents in ${folder}${NC}"
			else
				echo -e "${YELLOW}Skipping clearing contents in $folder.${NC}"
			fi

			# Sao chép nội dung từ các thư mục gốc vào đúng thư mục tương ứng
			case "$folder" in
				*/MQL5/Experts)
					echo -e "${YELLOW}Copying files from ./RunningFile_EA to $folder...${NC}"
					cp -r ./RunningFile_EA/* "$folder" || echo -e "${RED}Failed to copy files to ${folder}${NC}"
					echo -e "${GREEN}Copied files to $folder${NC}"
					;;
				*/MQL5/Indicators)
					echo -e "${YELLOW}Copying files from ./RunningFile_Indicator to $folder...${NC}"
					cp -r ./RunningFile_Indicator/* "$folder" || echo -e "${RED}Failed to copy files to ${folder}${NC}"
					echo -e "${GREEN}Copied files to $folder${NC}"
					;;
				*/MQL5/Files)
					echo -e "${YELLOW}Copying files from ./File to $folder...${NC}"
					cp -r ./File/* "$folder" || echo -e "${RED}Failed to copy files to ${folder}${NC}"
					echo -e "${GREEN}Copied files to $folder${NC}"
					;;
				*/MQL5/Profiles/Charts)
					echo -e "${YELLOW}Copying files from ./Profile to $folder...${NC}"
					cp -r ./Profile/* "$folder" || echo -e "${RED}Failed to copy files to ${folder}${NC}"
					echo -e "${GREEN}Copied files to $folder${NC}"
					;;
				*/MQL5/Profiles/Templates)
					echo -e "${YELLOW}Copying files from ./Template to $folder...${NC}"
					cp -r ./Template/* "$folder" || echo -e "${RED}Failed to copy files to ${folder}${NC}"
					echo -e "${GREEN}Copied files to $folder${NC}"
					;;
			esac
		else
			echo -e "${RED}Folder ${folder} does not exist or cannot be accessed.${NC}"
		fi
		
		echo -e "${CYAN}Finished processing ${folder}${NC}"
		echo ""
	done

	echo -e "${BLUE}All folders processed successfully.${NC}"

}

delete_history_chart() {
	find "$base_path" -type d -path "*/AppData/Roaming/MetaQuotes/Terminal/*" | grep -E "/(history|ticks)$" | while read dir; do
		# In ra thông tin về thư mục đang xử lý
		echo "Processing directory: $dir"
		
		# Tìm tất cả các file trong thư mục đó và in ra
		find "$dir" -type f -print
		
		# Xóa tất cả các file trong thư mục history và ticks
		echo "Deleting files in: $dir"
		find "$dir" -type f -exec rm -f {} \;
		
	done

}
#=============================================================[end copy MT5]==========================================================================



#=============================================================[begin 7zip with password]==============================================================================
echo -e "${YELLOW}    ====[7z, C:\Program Files\7-Zip\7z.exe]====> [zipFile][zipFolder][uzip] <folder/zip file>  <password> =============> ${NC}"
# Đường dẫn đến 7z.exe trên Windows
sevenzip="C:\\Program Files\\7-Zip\\7z.exe"

zipFile() {
  unset folder
  unset password  
  # Nếu không có đủ 2 tham số, yêu cầu người dùng nhập lần lượt tham số 1 và 2
  if [ $# -ne 2 ]; then
    echo -e "${YELLOW}Usage: zipFile <folder with all file> <password>${NC}"
    
    # Kiểm tra nếu tham số đầu tiên chưa có (folder), yêu cầu nhập
    if [ -z "$folder" ]; then
      read -p "Enter folder name path: " folder
    fi
    
    # Kiểm tra nếu tham số thứ hai chưa có (password), yêu cầu nhập
    if [ -z "$password" ]; then
      read -sp "Enter password: " password
      echo  # Để xuống dòng sau khi nhập mật khẩu
    fi
  else
    # Nếu có đủ 2 tham số từ dòng lệnh, gán chúng cho folder và password
    folder=$1
    password=$2
  fi

  if [ ! -d "$folder" ]; then
    echo -e "${RED}Directory $folder does not exist!${NC}"
    return 1
  fi

  # Duyệt qua tất cả các tệp trong thư mục và thư mục con, bỏ qua các thư mục chứa .git
  find "$folder" -type d -name ".git" -prune -o -type f ! -name ".*" | while read -r file; do
    # Lấy tên file mà không bao gồm đường dẫn thư mục
    basefile=$(basename "$file")
    dir=$(dirname "$file")

    # Tạo thư mục tạm để chứa file (chỉ dùng để nén)
    temp_dir=$(mktemp -d)

    # Sao chép file vào thư mục tạm
    cp "$file" "$temp_dir/"

    # Tạo tên file zip tại thư mục chứa tệp
    zip_file="$dir/$basefile.zip"

    echo -e "${CYAN}Zipping: $file into $zip_file${NC}"

    encrypted_password=$(encrype "$basefile")
    combined_password="$password$encrypted_password"
    #echo -e "${BLUE}$basefile $combined_password${NC}"
    # Nén file trong thư mục tạm, chỉ nén file mà không có đường dẫn thư mục
    "$sevenzip" a -p"$combined_password" "$zip_file" "$temp_dir/$basefile" -sdel -mx=9 -mem=AES256 -bb0 > /dev/null 2>&1

    # Kiểm tra nếu file zip đã được tạo thành công
    if [ -f "$zip_file" ]; then
      echo -e "${GREEN}Zipped and deleted: $file -> $zip_file${NC}"
      # Sau khi nén thành công, xóa file gốc
      rm -f "$file"
    else
      echo -e "${RED}Failed to zip: $file${NC}"
    fi

    # Xóa thư mục tạm
    rm -rf "$temp_dir"
  done

  echo -e "${GREEN}All files in $folder have been zipped and deleted.${NC}"

  # Di chuyển vào thư mục gốc
  cd "$folder" || exit 1  # Kiểm tra có vào được thư mục không

  # Tạo thư mục $folder trong thư mục hiện tại
  mkdir -p "$folder"  # Sử dụng -p để đảm bảo thư mục được tạo nếu chưa có

  # Liệt kê tất cả các file và thư mục trong thư mục hiện tại, bỏ qua .git và thư mục hiện tại ($folder)
  ls -1 | grep -v '/\.git/' | grep -v "$folder" | \
    xargs -I {} cp -r ./{} ./"$folder"

  # Tạo file zip từ thư mục mới tạo mà không cần mật khẩu
  echo -e "${CYAN}Zipping the folder $folder${NC}"
  encrypted_password=$(encrype "$folder")
  combined_password="$password$encrypted_password"  
  "$sevenzip" a -p"$combined_password" "$folder.zip" "$folder" -sdel -mx=9 -mem=AES256 -bb0 > /dev/null 2>&1

  # Kiểm tra xem file zip có được tạo thành công không
  if [ -f "$folder.zip" ]; then
    echo -e "${GREEN}Zipped and deleted folder: $folder -> $folder.zip${NC}"
  else
    echo -e "${RED}Failed to zip folder: $folder${NC}"
  fi

  # Xóa thư mục mới tạo sau khi zip
  rm -rf "$folder"

  # Quay lại thư mục gốc
  cd ../
}

zipFolder() {
  unset folder
  unset password  
  if [ $# -ne 2 ]; then
    echo -e "${YELLOW}Usage: zipFolder <only folder> <password>${NC}"
    
    # Kiểm tra nếu tham số đầu tiên chưa có (folder), yêu cầu nhập
    if [ -z "$folder" ]; then
      read -p "Enter folder name path: " folder
    fi
    
    # Kiểm tra nếu tham số thứ hai chưa có (password), yêu cầu nhập
    if [ -z "$password" ]; then
      read -sp "Enter password: " password
      echo  # Để xuống dòng sau khi nhập mật khẩu
    fi
  else
    # Nếu có đủ 2 tham số từ dòng lệnh, gán chúng cho folder và password
    folder=$1
    password=$2
  fi

  if [ ! -d "$folder" ]; then
    echo -e "${RED}Directory $folder does not exist!${NC}"
    return 1
  fi

  # Di chuyển vào thư mục gốc
  cd "$folder" || exit 1  # Kiểm tra có vào được thư mục không

  # Tạo thư mục $folder trong thư mục hiện tại
  mkdir -p "$folder"  # Sử dụng -p để đảm bảo thư mục được tạo nếu chưa có

  # Liệt kê tất cả các file và thư mục trong thư mục hiện tại, bỏ qua .git và thư mục hiện tại ($folder)
  ls -1 | grep -v '/\.git/' | grep -v "$folder" | \
    xargs -I {} cp -r ./{} ./"$folder"

  # Tạo file zip từ thư mục mới tạo mà không cần mật khẩu
  echo -e "${CYAN}Zipping the folder $folder${NC}"
  encrypted_password=$(encrype "$folder")
  combined_password="$password$encrypted_password"   
  "$sevenzip" a -p"$combined_password" "$folder.zip" "$folder" -sdel -mx=9 -mem=AES256 -bb0 > /dev/null 2>&1

  # Kiểm tra xem file zip có được tạo thành công không
  if [ -f "$folder.zip" ]; then
    echo -e "${GREEN}Zipped and deleted folder: $folder -> $folder.zip${NC}"
  else
    echo -e "${RED}Failed to zip folder: $folder${NC}"
  fi

  # Xóa thư mục mới tạo sau khi zip
  rm -rf "$folder"

  # Quay lại thư mục gốc
  cd ../
}

uzip() {
  unset folder
  unset password  
  # Kiểm tra xem có đúng 2 tham số không: <folder> <password>
  if [ $# -ne 2 ]; then
    echo -e "${YELLOW}Usage: uzip <folder/file> <password>${NC}"
    
    # Kiểm tra nếu tham số đầu tiên chưa có (folder), yêu cầu nhập
    if [ -z "$folder" ]; then
      read -p "Enter folder name path OR a .zip file " folder
    fi
    # Kiểm tra nếu tham số thứ hai chưa có (password), yêu cầu nhập
    if [ -z "$password" ]; then
      read -sp "Enter password: " password
      echo  # Để xuống dòng sau khi nhập mật khẩu
    fi
  else
    # Nếu có đủ 2 tham số từ dòng lệnh, gán chúng cho folder và password
    file_=$1          # Đây là file hoặc folder
    password=$2       # Mật khẩu giải nén
    folder=$1         # Thư mục đích sau khi giải nén (ban đầu giống tên file)
  fi
  file_=$folder

  # Kiểm tra nếu param1 là file .zip
  if [ -f "$file_" ] && [[ "$file_" == *.zip ]]; then
    echo -e "${CYAN}$file_ is a zip file!${NC}"
    folder="${file_%.*}"  # Tạo thư mục giải nén từ tên file (cắt phần mở rộng .zip)
    
    # Giải nén vào thư mục
    mkdir -p "$folder"  # Tạo thư mục nếu chưa tồn tại
    encrypted_password=$(encrype "$folder")
    combined_password="$password$encrypted_password"       
    "$sevenzip" x -p"$combined_password" "$file_" -o"$folder" -y -bb0 > /dev/null 2>&1
  elif [ -d "$file_" ]; then
    # Nếu param1 là thư mục, chỉ cần in thông báo và bỏ qua
    echo -e "${CYAN}$file_ is a folder, skipping extraction.${NC}"
  else
    # Nếu không phải file hoặc thư mục hợp lệ
    echo -e "${RED}$file_ is neither a valid file nor a folder!${NC}"
    return 1
  fi

  # Duyệt qua tất cả các tệp zip trong thư mục và thư mục con
  find "$folder" -type f -name "*.zip" | while read -r zipfile; do
    # Lấy thư mục chứa file zip
    dir=$(dirname "$zipfile")

    echo -e "${CYAN}Unzipping: $zipfile into $dir${NC}"
    fileNotPath=$(basename "$zipfile" .zip)
    encrypted_password=$(encrype "$fileNotPath")
    combined_password="$password$encrypted_password" 
    #echo $fileNotPath $combined_password
    # Giải nén với mật khẩu vào thư mục chứa file zip mà không tạo thư mục con
    "$sevenzip" x -p"$combined_password" "$zipfile" -o"$dir" -y -bb0 > /dev/null 2>&1

    # Kiểm tra xem giải nén có thành công không
    if [ $? -eq 0 ]; then
      echo -e "${GREEN}Unzipped and deleting: $zipfile${NC}"
      rm -f "$zipfile"  # Xóa file zip sau khi giải nén thành công
    else
      echo -e "${RED}Failed to unzip: $zipfile${NC}"
    fi
  done

  echo -e "${GREEN}All zip files in $folder have been unzipped and deleted.${NC}"

  if [ -f "$param1" ]; then
    cd ../
  fi  
}



# Hàm mã hóa chuỗi
encrype() {
    local string_in="$1"
    string_in="${string_in:0:36}"
    local encoded=""
    local key=""

    # Vòng lặp qua từng ký tự trong chuỗi đầu vào
    for i in $(seq 0 $((${#string_in} - 1))); do
        local char="${string_in:i:1}"
        local ascii=$(printf "%d" "'$char")  # Lấy mã ASCII của ký tự
        local encoded_char=$(( (ascii * (i + 1)) % 62 ))  # Mã hóa với phần dư 62
        encoded+="$encoded_char"
    done
    
    # Chuyển chuỗi encoded thành mảng các số
    local numbers=()
    for (( i=0; i<${#encoded}; i++ )); do
        local digit="${encoded:i:1}"
        numbers+=($digit)
    done

    # Xử lý các số và chuyển thành ký tự số, chữ cái in hoa hoặc chữ cái thường
    for number in "${numbers[@]}"; do
        local mod=$((number % 62))
        if (( mod < 10 )); then
            key+="$mod"  # Số 0-9
        elif (( mod < 36 )); then
            key+=$(printf "\\$(printf '%03o' $((mod + 55)))")  # Chữ in hoa A-Z
        else
            key+=$(printf "\\$(printf '%03o' $((mod + 61)))")  # Chữ thường a-z
        fi
    done

    # Giới hạn độ dài mã thành 255 ký tự
    key="${key:0:255}"

    echo -e "${RED} $key ${NC}"
}

#=============================================================[end 7zip with password]==============================================================================



metaWord() {
    local keyWords=()
    local keyPass=""
    local sum_ascii=0
    local ascii_keyPass=()
    local fileWord=""
    # Nhập mật khẩu

    read -p "Enter the path to the input file: " fileWord
    if [[ ! -f "$fileWord" ]]; then
        echo "Error: File not found."
        echo -e "${RED} ref: /d/02_Git/MT5/Meta_words.txt  ${NC}"
        return 1
    fi

    read -s -p  "Input password to gen Words for Meta: " keyPass

    mapfile -t keyWords < $fileWord

    # Tính tổng ASCII của các ký tự trong mật khẩu
    for (( i=0; i<${#keyPass}; i++ )); do
        ascii_value=$(printf "%d" "'${keyPass:$i:1}")
        ascii_keyPass+=($ascii_value)
        ((sum_ascii+=ascii_value))
    done

    # Điều chỉnh sum_ascii nếu cần
    if (( sum_ascii > ${#keyWords[@]}/2 )); then
        sum_ascii=$((sum_ascii / 2))
    fi

    # Sắp xếp ASCII tăng và giảm
    IFS=$'\n' sorted_increase=($(printf "%s\n" "${ascii_keyPass[@]}" | sort -n))
    IFS=$'\n' sorted_decrease=($(printf "%s\n" "${ascii_keyPass[@]}" | sort -nr))

    local key=()

    # Thêm từ theo thứ tự giảm dần
    for ascii in "${sorted_decrease[@]}"; do
        index=$((sum_ascii - ascii))
        if (( index >= 0 && index < ${#keyWords[@]} )); then
            key+=("${keyWords[index]}")
        fi
    done

    # Thêm từ theo thứ tự tăng dần
    for ascii in "${sorted_increase[@]}"; do
        index=$((sum_ascii + ascii))
        if (( index >= 0 && index < ${#keyWords[@]} )); then
            key+=("${keyWords[index]}")
        fi
    done

    # In kết quả
    echo "   "
    echo -e "${RED}"
    echo "${key[*]}"
    echo -e "${NC}"
}

keyCharacter=(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!#$%&()*+[]^{}~:;<=>?@"
)

# Hàm tính tổng ASCII của chuỗi
calculate_sum_ascii() {
    local input_string="$1"
    local sum=0
    for ((i=0; i<${#input_string}; i++)); do
        sum=$((sum + $(printf "%d" "$(printf '%d' "'${input_string:i:1}")")))
    done
    #echo "$sum"
}

# Hàm sinh password
passWord() {
    read -s -p "Input password to gen password: " keyPass

    local sum_ascii
    sum_ascii=$(calculate_sum_ascii "$keyPass")

    local key=""
    local count=0

    for ((i=0; i<${#keyPass}; i++)); do
        local char=${keyPass:i:1}
        local genKey=$(( $(printf "%d" "$(printf '%d' "'${char}")") + sum_ascii ))

        while ((genKey >= ${#keyCharacter[count]})); do
            local temp="$genKey"
            genKey=0
            for ((j=0; j<${#temp}; j++)); do
                genKey=$((genKey + ${temp:j:1}))
            done
        done

        key+="${keyCharacter[count]:genKey:1}"
        count=$((count + 1))
        if ((count >= ${#keyCharacter[@]})); then
            count=0
        fi
    done

    echo -e "${RED} $key ${NC}"
}

