# Wilson's Multi-Asset Research

An AI-powered investment research system that produces institutional-grade PDF briefings using Claude Code.

## Architecture

The system uses a **modular pipeline** rather than a monolithic prompt. A thin constitution (always loaded) provides core rules and routing. Analytical modules are loaded on demand per task. A working brief carries findings between stages.

```
CLAUDE.md (constitution — always loaded)
  ↓ reads state files
  ↓ classifies task → loads relevant modules
  ↓ research (web search)
  ↓ analyse (per module → working brief)
  ↓ synthesise (resolve tensions, draft thesis)
  ↓ produce (load production module → LaTeX → PDF)
  ↓ post-run (update state files)
```

## Files

### Core

| File | Purpose |
|---|---|
| `CLAUDE.md` | **Constitution** — core rules, routing table, connection map. Always loaded. |
| `modules/macro.md` | Macro & economic context framework |
| `modules/equities.md` | Equity analysis framework |
| `modules/fixed-income.md` | Rates, credit, yield curve |
| `modules/alternatives.md` | Commodities, crypto, REITs |
| `modules/fx.md` | Currency analysis |
| `modules/derivatives.md` | Hedging, vol, risk management |
| `modules/thematic.md` | Thematic & secular analysis |
| `modules/cross-asset.md` | Cross-asset synthesis & relative value |
| `modules/company.md` | Single company deep dive (Damodaran-style) |
| `modules/scenarios.md` | Scenario framework & Key Indicators to Watch |
| `modules/production.md` | Output format, LaTeX, charts, build process |
| `templates/working_brief.md` | Working brief template — copied per run |

### State Files (persistent, updated after each report)

| File | Purpose |
|---|---|
| `wilson_house_view.md` | Macro regime, key levels, themes, conviction changelog, interaction effects |
| `wilson_preferences.md` | Standing instructions, style preferences, feedback |
| `wilson_watchlist.md` | Tracked companies and themes with catalyst dates |
| `QUESTIONS.md` | Open questions pipeline |
| `log/_index.md` | Research audit trail |

### Production Assets (rarely changed)

| File | Purpose |
|---|---|
| `wilson-report.cls` | LaTeX document class — all branding |
| `wilson_latex_template.tex` | Report content skeleton — copy per report |
| `wilson_charts.py` | Matplotlib brand styling helper |
| `scripts/build_report.sh` | Compile, retry, error reporting |
| `wilson_test_plan.md` | Stress tests for validation |

## How to Use

**Direct request:** "Run a report on European defence equities"
→ Constitution routes to thematic + equities + scenarios + production → Full PDF

**Company deep-dive:** "Deep dive on Rheinmetall"
→ Constitution routes to company + relevant sector + scenarios + production → Full PDF

**Open-ended:** "What's interesting right now?"
→ Constitution + state files only → Theme Radar (3–5 cards) → you pick → full report

**Revision:** Upload .tex + "raise the bull case probability to 40%"
→ Surgical edit and recompile

## Why Modular?

- **Better attention:** The agent only has ~300 lines of instruction at peak, not 800. Data integrity rules stay salient.
- **Deeper modules:** Each module can be richer without bloating unrelated tasks.
- **Clean production:** Analysis and formatting don't compete for attention.
- **Easy iteration:** Weak equity reports? Edit one file. Chart styling issues? Edit one file.
- **Scales:** New module = new file + routing entry.

## Key Guardrails

- Every number sourced from web search (never fabricated)
- Evidence quality tagged: **Measured** → **Inferred** → **Speculative**
- Source tiers: Tier 1 (primary) → Tier 2 (secondary) → Tier 3 (signal detection only)
- Actively searches for disconfirming evidence; steelmans the opposing view
- Falsification criteria in every report
- AI hypotheses separated into labelled appendix
- Working brief carries cross-domain connections between modules
- House view updated after every report (append, never overwrite)

## Output

PDFs: `YYYY-MM-DD-[topic]-[asset-class].pdf`
Reports in `reports/`, charts in `figures/`, log entries in `log/`.
