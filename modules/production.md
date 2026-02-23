# Module: Production

**Load this module last, only when analysis and synthesis are complete.**

This module covers: report structure, LaTeX compilation, chart generation, error handling, and output naming.

---

## Output Format: Structured Research Briefing

Every report follows this structure. Sections expand or contract based on relevance.

```
TITLE: [Descriptive title]
DATE: [Current date]
CLASSIFICATION: [Research type]
HORIZON: [Tactical / Strategic / Secular / Combined]
ASSET CLASS(ES): [List]

EXECUTIVE SUMMARY
Four lines, same structure every report:
1. THE VIEW: Direction + asset + conviction + horizon
2. THE EVIDENCE: Single most compelling data point
3. THE RISK: What would make this call wrong
4. THE EXPRESSION: How to implement — instruments + hedge

1. MACRO CONTEXT
2. CORE ANALYSIS
   2.1 Valuation Assessment
   2.2 Cycle Positioning
   2.3 Sentiment & Positioning
   [Sub-sections adapted to topic]
   For thematic equity: Key Names to Watch table, Earnings Themes
3. SCENARIO ANALYSIS (bull/base/bear table)
4. CROSS-ASSET IMPLICATIONS
5. RISKS TO THE VIEW
6. KEY INDICATORS TO WATCH (table with thresholds)
7. ACTIONABLE CONCLUSIONS
   Direction + conviction + instruments + hedges + falsification criteria

APPENDIX: AI-GENERATED HYPOTHESES (if applicable)
OPEN QUESTIONS (2–3 specific, investigable questions)
SOURCES (all sources with dates and URLs)
```

**Optional "What's Next?" section:** At the end of a full report, you may append a mini Theme Radar (1–2 cards) flagging adjacent themes the user might want to explore next. This aids report continuity and surfaces follow-on investigations.

---

## Style & Tone

- **Write for experts.** No explaining what P/E ratios are.
- **Be opinionated.** Clear view + evidence + transparent reasoning. Fence-sitting helps no one.
- **Quantify.** "Equities look cheap" is weak. "S&P 500 fwd P/E of 20.8x at 72nd percentile, ERP of 1.2% at 8th percentile" is useful.
- **Cross-reference signals.** When value + cycle + sentiment align = high conviction. When they conflict, explain the tension and which signal you weight more.
- **Concise but thorough.** Every sentence adds information. Cut filler, keep nuance.
- **No generic caveats.** Skip "past performance..." and "consult your advisor."
- **Analytical sections close with "So what?"** — positioning implication, not summary.
- **Contextual sections** (Macro, Risks) close with a **bridge** — why this context matters for what follows.

### Length Targets

| Report Type | Body Text | Charts |
|---|---|---|
| Tactical Trade Idea | ~2,000 words max | 1–2 |
| Single Asset / Thematic Deep Dive | ~4,500 words max | 2–4 |
| Cross-Asset / Macro Review | ~4,500 words max | 3–5 |
| Company Deep Dive | ~4,500 words max | 2–4 |

These are ceilings, not targets. A tight 800-word tactical idea with one chart is better than a padded 2,000-word one.

---

## LaTeX Template & Branding

All reports use **`wilson-report.cls`**. Start with `\documentclass{wilson-report}`. Use **`wilson_latex_template.tex`** as the content skeleton — copy and replace placeholders.

### Custom Commands (defined in .cls)

| Command | Usage |
|---|---|
| `\maketitlepage{Title}{Classification}{Assets}{Horizon}` | Title page |
| `\execsummary{...}` | Executive summary box |
| `\conviction{H}` / `\conviction{M}` / `\conviction{L}` | Conviction badges |
| `\overweight` / `\underweight` / `\neutralweight` | Direction badges |
| `\keyinsight{...}` | Callout box (do not overuse) |
| `\staledata{date}` | Stale data flag |
| `\aihypothesis{...}` | Dashed-border box for AI inferences |
| `\bullrow` / `\baserow` / `\bearrow` | Scenario table row colours |
| `\signoff` | End-of-report branding |

### Template Rules

- **Never modify `wilson-report.cls`.**
- Update PDF metadata in `\hypersetup`: `pdftitle`, `pdfsubject`, `pdfkeywords`.
- **Required elements:** title page, executive summary, Key Indicators table, Open Questions, Sources, `\signoff`.
- **Table columns:** Use `m{}` (vertically centered) types, not `l` or `c`.
- Include charts as PDF figures.
- Do not add packages without reason.

### Build Process

Compile with: **`bash scripts/build_report.sh reports/{file}.tex`**

The script handles two-pass xelatex, error detection with log parsing, retry (up to 3 attempts). If it fails, it reports the error.

### LaTeX Sanitisation

Before writing to `.tex`, escape: `&` → `\&`, `%` → `\%`, `$` → `\$`, `#` → `\#`, `_` → `\_`. Financial data frequently contains these.

---

## Charts & Visualisations

Include charts wherever quantitative data supports a visual narrative. Do not force charts when data is insufficient.

### When to Chart

- Valuation time series (P/E, CAPE, ERP over time)
- Performance comparison (relative returns)
- Yield curves (current vs 3m ago vs 1y ago)
- Macro indicators (PMI, inflation trends)
- Positioning / flows (CFTC, cumulative fund flows)
- Scenario payoff (return distribution)
- Correlation (rolling)
- Earnings (revisions, EPS growth, margins)

### Chart Generation

1. Use **Python with matplotlib**.
2. Use **`wilson_charts.py`** for brand styling — `BRAND` colour dict + `wilson_style()` function.
3. Style: clean, minimal, white background, light grey grid, serif fonts, source in small grey text below chart.
4. Save as PDF: `plt.savefig('figures/{slug}-{chart-name}.pdf', bbox_inches='tight', dpi=150)`
5. Include in LaTeX:
```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.95\textwidth]{figures/{slug}-{chart-name}.pdf}
  \caption{Caption. Source: [source], as of [date].}
\end{figure}
```

### Chart Data Rules

- **Only chart sourced data.** Two data points = annotated comparison (bar/dot). Line charts need 4+ points. Scatter needs 6+.
- If a valuable chart lacks data, note: *"A chart of [X] would be informative here, but data was unavailable."*

---

## Output Naming

PDFs: **`YYYY-MM-DD-[topic]-[asset-class].pdf`**

Asset class tags: `equity`, `fixed-income`, `multi-asset`, `economic`, `commodities`, `fx`, `thematic`, `company`, `secular`

---

## Error Handling

### Search Failure
After 3 failed queries for a data point: flag inline as *"[DATA UNAVAILABLE — searched: query1, query2, query3]"* and continue. A report with marked gaps > no report.

### LaTeX Failure
The build script retries 3 times. If it still fails, it reports the error. Fix the `.tex` and re-run. Common issues: unescaped special characters, missing figure files, unclosed environments.

---

## Report Versioning

- **Surgical edits** (changing probabilities, updating data): Edit existing `.tex` and recompile.
- **Structural revision** (new thesis, different focus): Regenerate from scratch, reference prior report for reusable data.
- When user provides a previous `.tex` for revision, default to surgical edits.

---

## Source URLs

In the Sources section, include clickable URLs: `\href{URL}{Source Name}`. Keep body text clean — inline citations are source name + date only.
