import matplotlib.pyplot as plt
import numpy as np

# Create figure with just one panel
fig, ax = plt.subplots(figsize=(10, 7))

# Show relationship separately for teens vs adults
alcohol_use = np.array([0, 1])  # Low (0) vs High (1)

# Teens: Strong positive relationship
teens_ss = np.array([0, 1.06])  # Starting at 0, slope of 1.06

# Adults: No relationship (flat line)
adults_ss = np.array([0, -0.04])  # Starting at 0, essentially flat

# Plot
ax.plot(alcohol_use, teens_ss, 'o-', linewidth=3, markersize=12, 
         color='#e74c3c', label='Teens (Age 15-17)', alpha=0.9)
ax.plot(alcohol_use, adults_ss, 's-', linewidth=3, markersize=12,
         color='#3498db', label='Adults (Age 18+)', alpha=0.9)

ax.set_xlabel('Alcohol Use', fontsize=13, weight='bold')
ax.set_ylabel('Sensation Seeking', fontsize=13, weight='bold')
ax.set_title('Age × Alcohol Use Interaction on Sensation Seeking', 
              fontsize=14, weight='bold', pad=15)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Low', 'High'], fontsize=12)
ax.legend(loc='upper left', fontsize=12, framealpha=0.95)
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.3, 1.5)

# Teen annotation - TOP RIGHT
ax.text(0.75, 1.35, 'Strong effect in teens\n(B = 1.06, p < .001)', 
         fontsize=11, ha='center', weight='bold',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#e74c3c', alpha=0.2))

# Adult annotation - BOTTOM CENTER
ax.text(0.5, -0.2, 'No effect in adults\n(B = -0.04, p = .85)', 
         fontsize=11, ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#3498db', alpha=0.15))

plt.tight_layout()
plt.savefig('age_moderation_figure.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()