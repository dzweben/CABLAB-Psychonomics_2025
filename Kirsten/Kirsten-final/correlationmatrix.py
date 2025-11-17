import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define positions
col_widths = [0.22, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]
row_height = 0.12
start_y = 0.70

# Helper function (larger fonts!)
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
# HEADER ROW 0 (substance categories)
# ------------------------------

current_x = 0
draw_cell(ax, current_x, start_y, col_widths[0], row_height,
          '', '#2C3E50', 'white', True, fontsize=18)
current_x += col_widths[0]

draw_cell(ax, current_x, start_y, col_widths[1] + col_widths[2], row_height,
          'Alcohol', '#2C3E50', 'white', True, fontsize=22)
current_x += col_widths[1] + col_widths[2]

draw_cell(ax, current_x, start_y, col_widths[3] + col_widths[4], row_height,
          'Marijuana', '#2C3E50', 'white', True, fontsize=22)
current_x += col_widths[3] + col_widths[4]

draw_cell(ax, current_x, start_y, col_widths[5] + col_widths[6], row_height,
          'Nicotine', '#2C3E50', 'white', True, fontsize=22)

# ------------------------------
# HEADER ROW 1 (teen/adult)
# ------------------------------

headers = ['Cognitive Measure', 'Teen', 'Adult', 'Teen', 'Adult', 'Teen', 'Adult']
current_x = 0
current_y = start_y - row_height

for i, header in enumerate(headers):
    draw_cell(ax, current_x, current_y, col_widths[i], row_height,
              header, '#34495E', 'white', True, fontsize=18)
    current_x += col_widths[i]

# ------------------------------
# DATA
# ------------------------------

cognitive_measures = [
    'Executive Function',
    'Impulsivity',
    'Sensation Seeking',
    'Delay Discounting'
]

data = [
    ['-0.14', '-0.07', '-0.05', '-0.31***', '0.07', '-0.21*'],
    ['0.05', '0.04', '0.10', '0.44***', '0.11', '0.19*'],
    ['0.37**', '0.19*', '0.17', '0.19*', '0.01', '0.02'],
    ['0.09', '-0.04', '0.16', '0.11', '0.00', '-0.15']
]

# Colors based on effect size + significance
def get_color_for_corr(value_str):
    value = value_str.replace('*', '')
    try:
        val = float(value)
        abs_val = abs(val)
        is_sig = '*' in value_str
        
        if is_sig and abs_val >= 0.30:   # red
            return ('#E74C3C', 'white', True)
        elif is_sig and abs_val >= 0.15: # orange
            return ('#F39C12', 'black', True)
        elif abs_val >= 0.10:            # yellow
            return ('#F9E79F', 'black', False)
        else:                            # white
            return ('#FFFFFF', 'black', False)
    except:
        return ('#FFFFFF', 'black', False)

# ------------------------------
# DRAW DATA ROWS
# ------------------------------

current_y = start_y - 2 * row_height

for measure, row_data in zip(cognitive_measures, data):
    current_x = 0
    
    # Left label
    draw_cell(ax, current_x, current_y, col_widths[0], row_height,
              measure, '#ECF0F1', 'black', True, fontsize=18)
    current_x += col_widths[0]
    
    # Data entries
    for i, value in enumerate(row_data):
        bg_color, text_color, bold = get_color_for_corr(value)
        draw_cell(ax, current_x, current_y, col_widths[i+1], row_height,
                  value, bg_color, text_color, bold, fontsize=20)
        current_x += col_widths[i+1]
    
    current_y -= row_height

# ------------------------------
# TITLE
# ------------------------------

ax.text(
    0.5, 0.90,
    'Correlations: Substance Use × Cognitive Measures by Age Group',
    ha='center', va='top',
    fontsize=26, weight='bold',
    transform=ax.transAxes
)

# ------------------------------
# LEGEND — final correct position
# ------------------------------

legend_elements = [
    mpatches.Patch(facecolor='#E74C3C', label='|r| ≥ .30*'),
    mpatches.Patch(facecolor='#F39C12', label='|r| ≥ .15*'),
    mpatches.Patch(facecolor='#F9E79F', label='|r| ≥ .10'),
    mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='|r| < .10')
]

ax.legend(
    handles=legend_elements,
    loc='upper center',
    # place the legend directly under the table (just below the lowest data row)
    # 'upper center' means the legend's top-center will be anchored at this y
    bbox_to_anchor=(0.5, 0.095),
    ncol=4,
    frameon=False,
    fontsize=14
)

# ------------------------------
# SIGNIFICANCE FOOTNOTE — spaced properly
# ------------------------------

ax.text(
    # put the significance footnote below the legend
    0.5, 0.02,
    '*** p < .001, ** p < .01, * p < .05',
    ha='center', va='bottom',
    fontsize=13, style='italic',
    transform=ax.transAxes
)

# Extra bottom space so nothing clips
plt.subplots_adjust(bottom=0.04)

plt.savefig('correlation_table_large_fonts.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Correlation table with large fonts saved!")
