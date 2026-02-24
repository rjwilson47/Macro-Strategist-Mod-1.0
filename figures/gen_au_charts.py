"""
Generate charts for Australian Economic Outlook report — February 2026
"""
import sys
sys.path.insert(0, '/home/user/Macro-Strategist-Mod-1.0')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from wilson_charts import BRAND, wilson_style

# ─────────────────────────────────────────────────
# Chart 1: Australia CPI & Trimmed Mean Inflation
# ─────────────────────────────────────────────────
months = ['Jun\n2025', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec\n2025']
cpi_yoy = [1.9, 2.7, 2.7, 2.7, 3.0, 3.4, 3.8]
trimmed = [3.0, 2.8, 2.8, 3.0, 3.1, 3.2, 3.4]  # Quarterly interpolated to monthly where available

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(months, cpi_yoy, color=BRAND['bear'], marker='o', markersize=5, linewidth=2.2, label='Headline CPI YoY')
ax.plot(months, trimmed, color=BRAND['navy'], marker='s', markersize=5, linewidth=2.2, label='Trimmed Mean YoY')
ax.axhspan(2.0, 3.0, color=BRAND['bull'], alpha=0.08, label='RBA Target Band (2-3%)')
ax.axhline(y=2.5, color=BRAND['bull'], linestyle=':', linewidth=0.8, alpha=0.4)

ax.annotate('Headline surges\nto 3.8%', xy=(6, 3.8), xytext=(4.2, 4.3),
            fontsize=7, fontfamily='serif', color=BRAND['bear'],
            arrowprops=dict(arrowstyle='->', color=BRAND['bear'], lw=0.8))

wilson_style(ax, title='Australia: CPI Inflation Re-Accelerates',
             ylabel='YoY %',
             source='ABS, as of Dec 2025')
ax.set_ylim(1.5, 4.8)
ax.legend(loc='upper left', fontsize=7.5, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/au-econ-inflation.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 1: Inflation — done")


# ─────────────────────────────────────────────────
# Chart 2: RBA Cash Rate Path
# ─────────────────────────────────────────────────
dates = ['Feb\n2025', 'May', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan\n2026', 'Feb']
cash_rate = [4.10, 3.85, 3.60, 3.60, 3.60, 3.60, 3.60, 3.60, 3.85]

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.step(dates, cash_rate, where='post', color=BRAND['navy'], linewidth=2.5)
ax.fill_between(range(len(dates)), cash_rate, alpha=0.08, step='post', color=BRAND['navy'])

# Highlight the U-turn
ax.annotate('RBA hikes +25bp\n(first since Nov 2023)',
            xy=(8, 3.85), xytext=(5.5, 4.2),
            fontsize=7, fontfamily='serif', color=BRAND['bear'], fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=BRAND['bear'], lw=1.0))

# Market-implied path
future_dates_x = [8, 8.5]
future_rates = [3.85, 4.10]
ax.plot(future_dates_x, future_rates, color=BRAND['amber'], linestyle='--', linewidth=1.5,
        marker='D', markersize=4, label='Market-implied (May 2026)')

wilson_style(ax, title='RBA Cash Rate: The U-Turn',
             ylabel='Cash Rate Target (%)',
             source='RBA, market pricing as of 21 Feb 2026')
ax.set_ylim(3.3, 4.5)
ax.legend(loc='upper right', fontsize=7.5, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/au-econ-rba-rate.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 2: RBA rate path — done")


# ─────────────────────────────────────────────────
# Chart 3: Labour Market (Employment + Unemployment)
# ─────────────────────────────────────────────────
months_lab = ['Jul\n2025', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan\n2026']
emp_change = [58.2, 42.6, 64.1, -4.7, 90.5, 68.5, 17.8]  # thousands
unemp_rate = [4.2, 4.2, 4.1, 4.1, 4.2, 4.1, 4.1]  # Based on trend data

fig, ax1 = plt.subplots(figsize=(8, 4.5))
colors_bar = [BRAND['navy'] if v >= 0 else BRAND['bear'] for v in emp_change]
bars = ax1.bar(months_lab, emp_change, color=colors_bar, width=0.5, alpha=0.8, label='Employment Change (000s, LHS)')
for bar, val in zip(bars, emp_change):
    ypos = bar.get_height() + 2 if val >= 0 else bar.get_height() - 6
    ax1.text(bar.get_x() + bar.get_width()/2, ypos,
             f'{val:+.1f}K', ha='center', va='bottom' if val >= 0 else 'top',
             fontsize=7, fontfamily='serif', color=BRAND['dark_text'])

ax2 = ax1.twinx()
ax2.plot(months_lab, unemp_rate, color=BRAND['bear'], marker='D', markersize=5,
         linewidth=2, label='Unemployment Rate (%, RHS)')
ax2.set_ylabel('Unemployment Rate (%)', fontsize=9, color=BRAND['bear'], fontfamily='serif')
ax2.tick_params(axis='y', colors=BRAND['bear'], labelsize=8)
ax2.set_ylim(3.7, 4.6)

wilson_style(ax1, title='Australia: Labour Market Remains Tight',
             ylabel='Employment Change (000s)',
             source='ABS, as of Jan 2026')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=7.5, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/au-econ-labor.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 3: Labour market — done")


# ─────────────────────────────────────────────────
# Chart 4: Commodity Export Mix (Iron Ore, Gold, Copper)
# ─────────────────────────────────────────────────
commodities = ['Iron Ore', 'Gold', 'LNG', 'Copper', 'Coal']
fy2025 = [116, 37, 52, 13, 35]  # A$B approximate
fy2026e = [114, 56, 48, 15, 30]  # A$B approximate

x = np.arange(len(commodities))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))
bars1 = ax.bar(x - width/2, fy2025, width, label='FY2024-25', color=BRAND['mid_grey'], alpha=0.6)
bars2 = ax.bar(x + width/2, fy2026e, width, label='FY2025-26E', color=BRAND['navy'])

for bar, val in zip(bars1, fy2025):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'${val}B', ha='center', va='bottom', fontsize=7, fontfamily='serif', color=BRAND['mid_grey'])
for bar, val in zip(bars2, fy2026e):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'${val}B', ha='center', va='bottom', fontsize=7, fontfamily='serif', color=BRAND['navy'], fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(commodities, fontsize=9, fontfamily='serif')

# Annotate gold surge
ax.annotate('Gold +51%', xy=(1 + width/2, 56), xytext=(2.0, 62),
            fontsize=8, fontfamily='serif', color=BRAND['gold'], fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=BRAND['gold'], lw=1.0))

wilson_style(ax, title='Australia: Commodity Export Earnings Shifting',
             ylabel='Export Earnings (A$B)',
             source='DISER Resources & Energy Quarterly, Dec 2025')
ax.set_ylim(0, 130)
ax.legend(loc='upper right', fontsize=8, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/au-econ-commodities.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 4: Commodity exports — done")


# ─────────────────────────────────────────────────
# Chart 5: Key Macro Snapshot (Horizontal Bar)
# ─────────────────────────────────────────────────
categories = ['CPI YoY', 'Trimmed Mean\nYoY', 'RBA Cash\nRate', '10Y ACGB\nYield',
              'Unemployment\nRate', 'AUD/USD', 'ASX 200\nFwd P/E']
current =     [3.8,  3.4,  3.85, 4.74, 4.1,  70.5,  20.9]
year_ago =    [2.4,  3.2,  4.35, 4.30, 4.2,  64.3,  17.5]

fig, ax = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(categories))
ax.barh(y_pos - 0.15, current, height=0.3, color=BRAND['navy'], label='Current (Feb 2026)', zorder=3)
ax.barh(y_pos + 0.15, year_ago, height=0.3, color=BRAND['mid_grey'], alpha=0.5, label='Year Ago (Feb 2025)', zorder=3)
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=9, fontfamily='serif')
ax.invert_yaxis()

for i, (c, ya) in enumerate(zip(current, year_ago)):
    fmt = '.1f'
    ax.text(c + max(current)*0.02, i - 0.15, f'{c:{fmt}}', va='center', fontsize=7.5,
            fontfamily='serif', color=BRAND['navy'], fontweight='bold')
    ax.text(ya + max(current)*0.02, i + 0.15, f'{ya:{fmt}}', va='center', fontsize=7.5,
            fontfamily='serif', color=BRAND['mid_grey'])

wilson_style(ax, title='Australia Macro Snapshot: Current vs Year Ago',
             source='ABS, RBA, ASX, as of Feb 2026')
ax.legend(loc='lower right', fontsize=8, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/au-econ-snapshot.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 5: Macro snapshot — done")

print("\nAll Australian charts generated successfully.")
