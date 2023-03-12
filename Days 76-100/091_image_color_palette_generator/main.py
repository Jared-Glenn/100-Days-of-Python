from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from colorthief import ColorThief

app = Flask(__name__)


app.config['SECRET_KEY'] = 'anything'

UPLOAD_FOLDER = "C:\\Users\\Jared\Documents\\3. Programming\\100 Days of Python\\Days 76-100\\091_image_color_palette_generator\\static\\Image"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/palette', methods=['GET', 'POST'])
def palette():
    if request.method=="POST":
        uploaded_img = request.files['uploaded-file']
        img_filename = secure_filename(uploaded_img.filename)
        uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        img_file_path = UPLOAD_FOLDER + "/" + img_filename
        updated_img_path = "/Image/" + img_filename
        
        color_thief = ColorThief(img_file_path)
        dominant_color = color_thief.get_color(quality=1)
        
        # GETTING COLORS
        first_palette = color_thief.get_palette(color_count=11)
        palette = []
        for color in first_palette:
            color = "rgb" + str(color)
            palette.append(color)
            
        # FIND INVERTED COLOR
        red_value = 255 - first_palette[0][0]
        green_value = 255 - first_palette[0][1]
        blue_value = 255 - first_palette[0][2]
        
        complementary_color = "rgb(" + str(red_value) + ", " + str(green_value) + ", " + str(blue_value) + ")"
        
        return render_template('palette_page.html', file=updated_img_path, palette=palette, complementary_color = complementary_color)
    
    else:
        return render_template(url_for(home))

if __name__ == '__main__':
    app.run(debug=True)
    
    
# "NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT NEXT "