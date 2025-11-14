import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define positions
col_widths = [0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # 7 columns
row_height = 0.12
start_y = 0.75  # Moved down to make room for title

# Helper function to draw cell
def draw_cell(ax, x, y, width, height, text, bg_color, text_color='black', bold=False, fontsize=11):
    rect = Rectangle((x, y), width, height, facecolor=bg_color, edgecolor='black', linewidth=1)
    ax.add_patch(rect)
    weight = 'bold' if bold else 'normal'
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', 
            fontsize=fontsize, weight=weight, color=text_color)

# Row 0: Drug names (merged cells)
current_x = 0
# Empty cell for predictor column
draw_cell(ax, current_x, start_y, col_widths[0], row_height, '', '#2C3E50', 'white', True, 12)
current_x += col_widths[0]

# Nicotine (spans 2 columns)
draw_cell(ax, current_x, start_y, col_widths[1] + col_widths[2], row_height, 
          'Nicotine', '#2C3E50', 'white', True, 12)
current_x += col_widths[1] + col_widths[2]

# Marijuana (spans 2 columns)
draw_cell(ax, current_x, start_y, col_widths[3] + col_widths[4], row_height, 
          'Marijuana', '#2C3E50', 'white', True, 12)
current_x += col_widths[3] + col_widths[4]

# Alcohol (spans 2 columns)
draw_cell(ax, current_x, start_y, col_widths[5] + col_widths[6], row_height, 
          'Alcohol', '#2C3E50', 'white', True, 12)

# Row 1: Cohort headers
headers = ['Predictor', 'Teen', 'Adult', 'Teen', 'Adult', 'Teen', 'Adult']
current_x = 0
current_y = start_y - row_height
for i, header in enumerate(headers):
    draw_cell(ax, current_x, current_y, col_widths[i], row_height, header, 
              '#34495E', 'white', True, 11)
    current_x += col_widths[i]

# Data rows
predictors = ['Zuckerman', 'Barrets', 'Delay Discounting', 'TEXI']
data = [
    ['4.6%', '0.5%', '4.9%', '9.8%', '87.9%', '79.5%'],
    ['68.6%', '25.3%', '26.8%', '55.3%', '3.7%', '8.6%'],
    ['14.1%', '23.4%', '30.8%', '11.7%', '3.9%', '0%'],
    ['12.7%', '50.8%', '37.5%', '23.2%', '4.6%', '11.9%']
]

current_y = start_y - 2 * row_height
for row_idx, (predictor, row_data) in enumerate(zip(predictors, data)):
    current_x = 0
    
    # Predictor name
    draw_cell(ax, current_x, current_y, col_widths[0], row_height, predictor, 
              '#ECF0F1', 'black', True, 11)
    current_x += col_widths[0]
    
    # Data cells
    for col_idx, value in enumerate(row_data):
        pct_value = float(value.strip('%'))
        
        # Determine color
        if pct_value >= 50:
            bg_color = '#E74C3C'
            text_color = 'white'
            bold = True
        elif pct_value >= 25:
            bg_color = '#F39C12'
            text_color = 'black'
            bold = True
        elif pct_value >= 10:
            bg_color = '#F9E79F'
            text_color = 'black'
            bold = False
        else:
            bg_color = '#FFFFFF'
            text_color = 'black'
            bold = False
        
        draw_cell(ax, current_x, current_y, col_widths[col_idx + 1], row_height, 
                  value, bg_color, text_color, bold, 11)
        current_x += col_widths[col_idx + 1]
    
    current_y -= row_height

# Add title
ax.text(0.5, 0.92, 'Shapley Value Decomposition: Variance Explained (% of R²)', 
        ha='center', va='top', fontsize=14, weight='bold', transform=ax.transAxes)

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#E74C3C', label='≥50%'),
    mpatches.Patch(facecolor='#F39C12', label='25-49%'),
    mpatches.Patch(facecolor='#F9E79F', label='10-24%'),
    mpatches.Patch(facecolor='#FFFFFF', edgecolor='black', label='<10%')
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 0.05), 
         ncol=4, frameon=False, fontsize=10)

plt.tight_layout()
plt.savefig('shapley_table.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()