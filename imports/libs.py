from PIL import Image

def open_file(p_file_path):
    img = Image.open(p_file_path, "r")
    img.load()
    return img

def convert(p_file_path, p_new_width, p_file_name, p_new_file_name):
    img = open_file(p_file_path)
    
    width, height = img.size
    small_img = img.resize((int(p_new_width), int((p_new_width / width) * height)), Image.BILINEAR)
    final_img = small_img.resize(img.size, Image.NEAREST)
    
    new_path = p_file_path.replace(p_file_name, p_new_file_name)
    
    img.show("old_image")
    final_img.show("new_image")
    final_img.save(new_path)
    