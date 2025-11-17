import matplotlib.pyplot as plt
import numpy as np

# Model coefficients from your output
intercept = -1.07038
b_alcohol = 6.29777
b_age = 0.05186
b_interaction = -0.32056

# Representative ages
age_teen = 16.34  # -1 SD from your simple slopes
age_adult = 19.76  # +1 SD from your simple slopes

# Alcohol use levels
alcohol_use = np.array([0, 1])  # Low (0) vs High (1)

# Calculate predicted values using the full model:
# zuckerman.z = intercept + b_alcohol*alcohol + b_age*age + b_interaction*alcohol*age

# For teens (age 16.34)
teens_ss = intercept + b_alcohol*alcohol_use + b_age*age_teen + b_interaction*alcohol_use*age_teen

# For adults (age 19.76)
adults_ss = intercept + b_alcohol*alcohol_use + b_age*age_adult + b_interaction*alcohol_use*age_adult

# Create figure
fig, ax = plt.subplots(figsize=(10, 7))

# Plot
ax.plot(alcohol_use, teens_ss, 'o-', linewidth=3, markersize=12, 
         color='#e74c3c', label='(Age 15-18)', alpha=0.9)
ax.plot(alcohol_use, adults_ss, 's-', linewidth=3, markersize=12,
         color='#3498db', label='(Age 19+)', alpha=0.9)

ax.set_xlabel('Alcohol Use', fontsize=13, weight='bold')
ax.set_ylabel('Sensation Seeking (z-score)', fontsize=13, weight='bold')
ax.set_title('Age × Alcohol Use Interaction on Sensation Seeking', 
              fontsize=14, weight='bold', pad=15)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Low', 'High'], fontsize=12)
ax.legend(loc='upper left', fontsize=12, framealpha=0.95)
ax.grid(True, alpha=0.3)

# Add horizontal line at 0 (sample mean)
ax.axhline(y=0, color='gray', linestyle=':', linewidth=1, alpha=0.5)

plt.tight_layout()
plt.savefig('age_moderation_figure.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
plt.show()

print("Figure saved as 'age_moderation_figure.png'")