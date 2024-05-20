from PIL import Image
import os
import glob

def extract_lightwarp_lines_from_directory(directory):
    dds_files = glob.glob(os.path.join(directory, "*dyt.dds"))
    output_directory = os.path.join(directory, "DYT")
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for input_path in dds_files:
        with Image.open(input_path) as img:
            if img.size != (128,128):
                print(f"Skipping {input_path}: Image size is not 128x128")
                continue
            
            texture_name = os.path.splitext(os.path.basename(input_path))[0]
            set_number = 0
            print(f"Extracting lightwarp lines from {texture_name}")
            
            y = 0
            while y < 128:
                black_area_check = img.crop((0,y,128,y +5))
                
                if is_pure_black(black_area_check):
                    print(f"Reached end of lightwarp lines in {texture_name} at y={y}")
                    print()
                    break
                
                lightwarp_line = img.crop((0,y,128,y +4))
                set_number += 1
                output_path = os.path.join(output_directory,f"{texture_name}_{set_number}.png")
                lightwarp_line.save(output_path)
                print(f"Found lightwarp line in {texture_name} at y={y}, saving as {texture_name}_{set_number}.png")

                color_pixel = lightwarp_line.getpixel((120,1))[:3]
                color_text_path = os.path.join(output_directory, f"{texture_name}_{set_number}.txt")
                
                with open(color_text_path,'w') as color_file:
                    color_file.write(f"\"$color2\" \"{{{color_pixel[0]} {color_pixel[1]} {color_pixel[2]}}}\"")
                
                print(f"Saved color {color_pixel} from {texture_name} at y={y} to {color_text_path}")
                print()

                y += 16

def is_pure_black(img):
    for pixel in img.getdata():
        if pixel[:3] != (0,0,0):
            return False
    return True

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Checking for Xenoverse 2 DYT files in {script_directory}...")
    extract_lightwarp_lines_from_directory(script_directory)
    print(f"Finished extracting Xenoverse 2 color data from directory...")
