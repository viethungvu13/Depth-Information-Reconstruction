def get_valid_input(prompt, valid_options):
    """
    Yêu cầu người dùng nhập giá trị hợp lệ dựa trên danh sách valid_options.
    Nếu nhập không hợp lệ, yêu cầu nhập lại.
    
    Tham số:
      prompt: thông báo yêu cầu nhập.
      valid_options: danh sách các giá trị hợp lệ (phải là chữ thường).
    
    Trả về:
      Giá trị hợp lệ mà người dùng nhập.
    """
    while True:
        try:
            value = input(prompt).strip().lower()
            if value in valid_options:
                return value
            else:
                raise ValueError("Invalid input")
        except ValueError as ve:
            print("Error: You can only enter the following values:", valid_options, "\nPlease re-enter.")
