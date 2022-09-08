from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

drawing = svg2rlg('creepysmileman-colour.svg')
renderPM.drawToFile(drawing, 'ice.png', fmt='PNG')