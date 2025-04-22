# Pokémon

Một trò chơi Pokémon đơn giản được phát triển trên Python với thư viện Pygame.

## Giới thiệu

Đây là một trò chơi có giao diện thân thiện với người dùng. Trò chơi cho phép người chơi chọn 1 trong 3 chế độ là đấu truyền thông, đấu với bot tập luyện. Người chơi sẽ phải chọn 2 cặp hình giống nhau sao cho đường đi giữa 2 hình đó không được vượt quá 3 cạnh trên 1 bảng có kích thước 12x9. Mục tiêu cuối cùng là trên bảng sẽ không còn 1 pokémon nào.

## Các thành viên

- Mai Xuân Doanh - 221230767
- Trần Văn Dũng  - 221230773
- Nguyễn Văn Hải - 221230824

## Công nghệ sử dụng

- Python

## Cách cài đặt

1. Clone repository này về máy
```bash
git clone https://github.com/doanhXmai/pokemon.git
``` 
2. Mở thư mục dự án trên pycharm
3. tìm đến file main.py và run file

## Cấu trúc dự án
```
pokemon/
├── assests/                        # Thư mục chứa tài nguyên của game
│   ├── fonts/                      # Thư mục chứ kiểu chữ
│   │   └── timesnewroman.ttf       # Kiểu chữ times new roman
│   ├── images/                     # Thư mục chứa ảnh
│   │   ├── avt.png                 # Ảnh đại diện
│   │   ├── ...                     # ...
│   │   ├── background{i}.jpg       # Các ảnh về nền
│   │   └── pieces{i}.png           # Các ảnh về pokémon
│   └── sounds/                     # Thư mục chứa âm thanh
│       ├── click.wav               # Âm thanh khi nhấn vào 1 nút hoặc pokémon
│       ├── ...                     # ...
│       └── matched.wav             # Âm thanh khi nối
├── bot/                            # Thứ mục chứa các cài đặt của bot
│   └── core/                       # 
│       └── bot.py                  # logic của bot
├── core/                           #
│   ├── button/                     # Thư mục chứa các cấu hình của nút
│   │   ├── btnhint.py              # Nút gợi ý
│   │   ├── btnpause.py             # Nút tạm dừng
│   │   ├── btnrestartandback.py    # 2 nút restart and back
│   │   ├── btnshuffle.py           # Nút đảo
│   │   └── tile.py                 # Nút tượng trưng cho pokémon
│   ├── playerHUD/                  # Thư mục chứa giao diện người chơi
│   │   └── avatarscore.py          # Giao diện người chơi
│   ├── processor/                  # Bộ xử lý
│   │   ├── BFS.py                  # Thuật toán BFS dùng để tìm đường đi hợp lệ
│   │   ├── connect.py              # Kiểm tra có nối được không và vẽ đường đi giữa 2 pokémon
│   │   ├── generate.py             # Sinh ngẫu nhiên các pokémon lên bảng
│   │   └── hint.py                 # Hàm gợi ý
│   ├── screens/                    # Thư mục chứa các giao diện
│   │   ├── boards/                 # Thư mục chứa các giao diện về bảng chơi
│   │   │   ├── boardBot.py         # Giao diện đấu với bot
│   │   │   ├── boardsolo.py        # Giao diện chơi đơn
│   │   │   └── boardtranning.py    # Giao diện huấn luyện
│   │   └── menu/                   # Thư mục chứa các menu tuỳ chọn
│   │       ├── menugameover.py     # Menu khi bảng đấu với bot hết pokémon
│   │       ├── menulevel.py        # Menu chọn option để chơi
│   │       ├── menulose.py         # Menu khi thua
│   │       ├── menupase.py         # Menu khi bấm tạm dừng
│   │       ├── menuwin.py          # Menu khi chiến thắng
│   │       └── menustart.py        # Menu khi bắt đầu chạy game
│   ├── sound/                      # 
│   │   ├── soundmanager.py         # Quản lý âm thanh
│   │   └── sound.py                # Xử lý âm thanh
│   ├── config.py                   # Các thông số không được thay đổi của game
│   └── setting.py                  # Các thông số có thể thay đổi của game
├── main.py                         # File dùng để chay game
├── requirements.txt                # File dùng để tự import các thư viện của game
└── README.md                       # File này
```

## Cách chơi

1. Mở trò chơi trong pycharm
2. Chọn chế độ chơi
3. chọn các cặp pokémon giống nhau sao cho đường đi giữa chúng không bị vượt quá 3 đường nối
