# app.py
from flask import Flask, render_template
import shape_calculator
from unittest import main

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    rect = shape_calculator.Rectangle(5, 10)
    rect_area = rect.get_area()
    rect.set_width(3)
    rect_perimeter = rect.get_perimeter()

    sq = shape_calculator.Square(9)
    sq_area = sq.get_area()
    sq.set_side(4)
    sq_diagonal = sq.get_diagonal()

    return render_template('index.html', rect_area=rect_area, rect_perimeter=rect_perimeter,
                           sq_area=sq_area, sq_diagonal=sq_diagonal)

if __name__ == '__main__':
    app.run(debug=True)
