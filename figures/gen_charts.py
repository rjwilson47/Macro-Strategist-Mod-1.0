"""
Generate charts for US Economic Outlook report — February 2026
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
# Chart 1: US GDP Growth (Quarterly, Annualised)
# ─────────────────────────────────────────────────
quarters = ['Q1\n2024', 'Q2\n2024', 'Q3\n2024', 'Q4\n2024',
            'Q1\n2025', 'Q2\n2025', 'Q3\n2025', 'Q4\n2025',
            'Q1\n2026E']
gdp_growth = [1.4, 3.0, 2.8, 2.4, 2.3, 3.1, 4.4, 1.4, 3.1]

fig, ax = plt.subplots(figsize=(8, 4.5))
colors = [BRAND['navy'] if v >= 2.0 else BRAND['bear'] if v < 1.0 else BRAND['amber'] for v in gdp_growth]
colors[-1] = BRAND['accent']  # GDPNow estimate
bars = ax.bar(quarters, gdp_growth, color=colors, width=0.6, edgecolor='white', linewidth=0.5)

for bar, val in zip(bars, gdp_growth):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.08,
            f'{val:.1f}%', ha='center', va='bottom', fontsize=8, fontfamily='serif',
            color=BRAND['dark_text'], fontweight='bold')

ax.axhline(y=2.0, color=BRAND['mid_grey'], linestyle='--', linewidth=0.8, alpha=0.6)
ax.text(8.4, 2.05, 'Trend (~2%)', fontsize=7, color=BRAND['mid_grey'], fontfamily='serif', va='bottom')

wilson_style(ax, title='US Real GDP Growth (Quarterly, Annualised %)',
             source='BEA, Atlanta Fed GDPNow (Q1 2026E), as of 20 Feb 2026')
ax.set_ylim(0, 5.2)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f%%'))
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/us-econ-gdp-growth.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 1: GDP growth — done")


# ─────────────────────────────────────────────────
# Chart 2: ISM PMI Manufacturing vs Services
# ─────────────────────────────────────────────────
months = ['Jul\n2025', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan\n2026']
ism_mfg =  [48.5, 47.2, 47.0, 46.8, 48.3, 47.9, 52.6]
ism_svc =  [52.7, 51.5, 54.0, 53.2, 52.8, 53.8, 53.8]

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(months, ism_mfg, color=BRAND['navy'], marker='o', markersize=5, linewidth=2, label='Manufacturing')
ax.plot(months, ism_svc, color=BRAND['accent'], marker='s', markersize=5, linewidth=2, label='Services')
ax.axhline(y=50, color=BRAND['bear'], linestyle='--', linewidth=1, alpha=0.5)
ax.text(6.1, 50.3, '50 = Expansion/Contraction', fontsize=7, color=BRAND['bear'],
        fontfamily='serif', alpha=0.7)

ax.annotate('Mfg breaks\ninto expansion', xy=(6, 52.6), xytext=(4.5, 54.5),
            fontsize=7, fontfamily='serif', color=BRAND['navy'],
            arrowprops=dict(arrowstyle='->', color=BRAND['navy'], lw=0.8))

wilson_style(ax, title='ISM PMI: Manufacturing vs Services',
             ylabel='PMI Index',
             source='ISM, as of Jan 2026')
ax.set_ylim(44, 57)
ax.legend(loc='lower left', fontsize=8, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/us-econ-ism-pmi.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 2: ISM PMI — done")


# ─────────────────────────────────────────────────
# Chart 3: Labor Market Dashboard (NFP + Unemployment)
# ─────────────────────────────────────────────────
months_nfp = ['Jul\n2025', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan\n2026']
nfp = [178, 143, 224, 75, 41, 48, 130]
unemp = [4.2, 4.2, 4.1, 4.1, 4.2, 4.3, 4.3]

fig, ax1 = plt.subplots(figsize=(8, 4.5))
bars = ax1.bar(months_nfp, nfp, color=BRAND['navy'], width=0.5, alpha=0.8, label='NFP (000s, LHS)')
for bar, val in zip(bars, nfp):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
             f'{val}K', ha='center', va='bottom', fontsize=7, fontfamily='serif',
             color=BRAND['dark_text'])

ax2 = ax1.twinx()
ax2.plot(months_nfp, unemp, color=BRAND['bear'], marker='D', markersize=5,
         linewidth=2, label='Unemployment Rate (%, RHS)')
ax2.set_ylabel('Unemployment Rate (%)', fontsize=9, color=BRAND['bear'], fontfamily='serif')
ax2.tick_params(axis='y', colors=BRAND['bear'], labelsize=8)
ax2.set_ylim(3.8, 4.6)

wilson_style(ax1, title='US Labor Market: Nonfarm Payrolls & Unemployment Rate',
             ylabel='NFP Change (000s)',
             source='BLS, as of Jan 2026')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=7.5, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/us-econ-labor.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 3: Labor market — done")


# ─────────────────────────────────────────────────
# Chart 4: Key Macro Snapshot (Horizontal Bar)
# ─────────────────────────────────────────────────
categories = ['CPI YoY', 'Core CPI YoY', 'Fed Funds\n(Upper)', '10Y Yield',
              'DXY', 'HY OAS (bps)', 'VIX']
current =     [2.4,  2.5,  3.75, 4.09,  97.8,  288,  20.0]
year_ago =    [3.1,  3.2,  4.50, 4.43, 106.1,  340,  14.5]

fig, ax = plt.subplots(figsize=(8, 5))
y_pos = np.arange(len(categories))
ax.barh(y_pos - 0.15, current, height=0.3, color=BRAND['navy'], label='Current (Feb 2026)', zorder=3)
ax.barh(y_pos + 0.15, year_ago, height=0.3, color=BRAND['mid_grey'], alpha=0.5, label='Year Ago (Feb 2025)', zorder=3)
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=9, fontfamily='serif')
ax.invert_yaxis()

for i, (c, ya) in enumerate(zip(current, year_ago)):
    fmt = '.0f' if c > 50 else '.1f' if c > 10 else '.1f'
    ax.text(c + max(current)*0.02, i - 0.15, f'{c:{fmt}}', va='center', fontsize=7.5,
            fontfamily='serif', color=BRAND['navy'], fontweight='bold')
    ax.text(ya + max(current)*0.02, i + 0.15, f'{ya:{fmt}}', va='center', fontsize=7.5,
            fontfamily='serif', color=BRAND['mid_grey'])

wilson_style(ax, title='US Macro Snapshot: Current vs Year Ago',
             source='BLS, Fed, FRED, ICE BofA, as of Feb 2026')
ax.legend(loc='lower right', fontsize=8, framealpha=0.9)
plt.tight_layout()
plt.savefig('/home/user/Macro-Strategist-Mod-1.0/figures/us-econ-snapshot.pdf',
            bbox_inches='tight', dpi=150)
plt.close()
print("Chart 4: Macro snapshot — done")

print("\nAll charts generated successfully.")
