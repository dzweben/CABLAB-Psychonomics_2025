import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define column widths
col_widths = [0.20, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]  
row_height = 0.12
start_y = 0.75  

# Helper function (larger default fontsize!)
def draw_cell(ax, x, y, width, height, text, bg_color,
              text_color='black', bold=False, fontsize=18):
    rect = Rectangle((x, y), width, height, facecolor=bg_color,
                     edgecolor='black', linewidth=1)
    ax.add_patch(rect)
    ax.text(
        x + width/2, y + height/2, text,
        ha='center', va='center',
        fontsize=fontsize,
        weight='bold' if bold else 'normal',
        color=text_color
    )

# ------------------------------
# HEADER ROWS
# ------------------------------

current_x = 0

# Empty top-left corner
draw_cell(ax, current_x, start_y, col_widths[0], row_height,
          '', '#2C3E50', 'white', True, fontsize=18)
current_x += col_widths[0]

# Alcohol (2 columns)
draw_cell(ax, current_x, start_y, col_widths[1] + col_widths[2], row_height,
          'Alcohol', '#2C3E50', 'white', True, fontsize=22)
current_x += col_widths[1] + col_widths[2]

# Marijuana (2 columns)
draw_cell(ax, current_x, start_y, col_widths[3] + col_widths[4], row_height,
          'Marijuana', '#2C3E50', 'white', True, fontsize=22)
current_x += col_widths[3] + col_widths[4]

# Nicotine (2 columns)
draw_cell(ax, current_x, start_y, col_widths[5] + col_widths[6], row_height,
          'Nicotine', '#2C3E50', 'white', True, fontsize=22)

# Row 1: Teen / Adult
headers = [
    "Cognitive Measure",
    "Teen", "Adult",
    "Teen", "Adult",
    "Teen", "Adult"
]

current_x = 0
current_y = start_y - row_height

for i, h in enumerate(headers):
    draw_cell(ax, current_x, current_y, col_widths[i], row_height,
              h, '#34495E', 'white', True, fontsize=18)
    current_x += col_widths[i]

# ------------------------------
# FIXED ROW ORDER
# ------------------------------

measures = [
    "Executive Function",
    "Impulsivity",
    "Sensation Seeking",
    "Delay Discounting"
]

# ------------------------------
# VALUES: Alcohol (T/A), Marijuana (T/A), Nicotine (T/A)
# ------------------------------

data = [
    ['4.6%', '11.9%', '37.5%', '23.2%', '12.7%', '50.8%'],
    ['3.7%', '8.6%', '26.8%', '55.3%', '68.6%', '25.3%'],
    ['87.9%', '79.5%', '4.9%', '9.8%', '4.6%', '0.5%'],
    ['3.9%', '0%', '30.8%', '11.7%', '14.1%', '23.4%']
]

# ------------------------------
# COLOR CODING FUNCTION
# ------------------------------

def color_for_pct(p):
    p = float(p.replace('%', ''))
    if p >= 50:
        return '#E74C3C', 'white', True
    elif p >= 25:
        return '#F39C12', 'black', True
    elif p >= 10:
        return '#F9E79F', 'black', False
    else:
        return '#FFFFFF', 'black', False

# ------------------------------
# DRAW DATA ROWS
# ------------------------------

current_y = start_y - 2 * row_height

for measure, row_values in zip(measures, data):
    current_x = 0

    # Left label
    draw_cell(ax, current_x, current_y, col_widths[0], row_height,
              measure, '#ECF0F1', 'black', True, fontsize=18)
    current_x += col_widths[0]

    # Data cells (larger numbers: 20pt)
    for i, val in enumerate(row_values):
        bg, text_c, bold = color_for_pct(val)
        draw_cell(ax, current_x, current_y, col_widths[i+1], row_height,
                  val, bg, text_c, bold, fontsize=20)
        current_x += col_widths[i+1]

    current_y -= row_height

# ------------------------------
# TITLE + LEGEND
# ------------------------------

ax.text(0.5, 0.92,
        'Shapley Value Decomposition: Variance Explained (% of R²)',
        ha='center', va='top',
        fontsize=24, weight='bold',
        transform=ax.transAxes)

legend_elements = [
    mpatches.Patch(facecolor='#E74C3C', label='≥ 50%'),
    mpatches.Patch(facecolor='#F39C12', label='25–49%'),
    mpatches.Patch(facecolor='#F9E79F', label='10–24%'),
    mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='< 10%')
]

ax.legend(
    handles=legend_elements, loc='upper left',
    bbox_to_anchor=(0, 0.04), frameon=False,
    ncol=4, fontsize=16
)

plt.tight_layout()
plt.savefig('shapley_table_large_fonts.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
