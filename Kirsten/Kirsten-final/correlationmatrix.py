import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define positions
col_widths = [0.22, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]  # 7 columns
row_height = 0.12
start_y = 0.68

# Helper function to draw cell
def draw_cell(ax, x, y, width, height, text, bg_color, text_color='black', bold=False, fontsize=11):
    rect = Rectangle((x, y), width, height, facecolor=bg_color, edgecolor='black', linewidth=1)
    ax.add_patch(rect)
    weight = 'bold' if bold else 'normal'
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
            fontsize=fontsize, weight=weight, color=text_color)

# Row 0: Substance names (merged cells)
current_x = 0
draw_cell(ax, current_x, start_y, col_widths[0], row_height, '', '#2C3E50', 'white', True, 12)
current_x += col_widths[0]

draw_cell(ax, current_x, start_y, col_widths[1] + col_widths[2], row_height, 
          'Alcohol', '#2C3E50', 'white', True, 12)
current_x += col_widths[1] + col_widths[2]

draw_cell(ax, current_x, start_y, col_widths[3] + col_widths[4], row_height, 
          'Marijuana', '#2C3E50', 'white', True, 12)
current_x += col_widths[3] + col_widths[4]

draw_cell(ax, current_x, start_y, col_widths[5] + col_widths[6], row_height, 
          'Nicotine', '#2C3E50', 'white', True, 12)

# Row 1: Cohort headers
headers = ['Cognitive Measure', 'Teen', 'Adult', 'Teen', 'Adult', 'Teen', 'Adult']
current_x = 0
current_y = start_y - row_height
for i, header in enumerate(headers):
    draw_cell(ax, current_x, current_y, col_widths[i], row_height, header, 
              '#34495E', 'white', True, 10)
    current_x += col_widths[i]

# Data rows
cognitive_measures = ['Executive Function', 'Impulsivity', 'Sensation Seeking', 'Delay Discounting']
data = [
    ['-0.14', '-0.07', '-0.05', '-0.31***', '0.07', '-0.21*'],
    ['0.05', '0.04', '0.10', '0.44***', '0.11', '0.19*'],
    ['0.37**', '0.19*', '0.17', '0.19*', '0.01', '0.02'],
    ['0.09', '-0.04', '0.16', '0.11', '0.00', '-0.15']
]

def get_color_for_corr(value_str):
    value = value_str.replace('*', '')
    try:
        val = float(value)
        abs_val = abs(val)
        is_sig = '*' in value_str
        
        if is_sig and abs_val >= 0.3:
            return ('#E74C3C', 'white', True)
        elif is_sig and abs_val >= 0.15:
            return ('#F39C12', 'black', True)
        elif abs_val >= 0.1:
            return ('#F9E79F', 'black', False)
        else:
            return ('#FFFFFF', 'black', False)
    except:
        return ('#FFFFFF', 'black', False)

current_y = start_y - 2 * row_height
for row_idx, (measure, row_data) in enumerate(zip(cognitive_measures, data)):
    current_x = 0
    draw_cell(ax, current_x, current_y, col_widths[0], row_height, measure, 
              '#ECF0F1', 'black', True, 10)
    current_x += col_widths[0]
    
    for col_idx, value in enumerate(row_data):
        bg_color, text_color, bold = get_color_for_corr(value)
        draw_cell(ax, current_x, current_y, col_widths[col_idx + 1], row_height, 
                  value, bg_color, text_color, bold, 10)
        current_x += col_widths[col_idx + 1]
    
    current_y -= row_height

# Title
ax.text(0.5, 0.88, 'Correlations: Substance Use × Cognitive Measures by Age Group', 
        ha='center', va='top', fontsize=14, weight='bold', transform=ax.transAxes)

# Legend - simplified
legend_elements = [
    mpatches.Patch(facecolor='#E74C3C', label='|r| ≥ .30*'),
    mpatches.Patch(facecolor='#F39C12', label='|r| ≥ .15*'),
    mpatches.Patch(facecolor='#F9E79F', label='|r| ≥ .10'),
    mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='|r| < .10')
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0.03), 
         ncol=4, frameon=False, fontsize=10)

# Significance note
ax.text(0.5, 0.0, '*** p < .001, ** p < .01, * p < .05', 
        ha='center', va='bottom', fontsize=10, style='italic', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('correlation_table.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
print("Correlation table saved!")