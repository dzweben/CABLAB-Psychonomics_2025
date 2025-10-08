# Psychonomics 2025 — Repository README
**Owner:** Daniel (Danny) Zweben  
**Labs:** CABLab / SDN Lab, Temple University  
**Conference:** Psychonomics 2025 (Denver)  

This repo contains **two independent analysis tracks** plus shared scoring pipelines:

- **Kirsten — Substance Use & Cognition (teens vs. young adults)**  
- **Megan — Digital Immersion, Executive Functioning, and Health (youth)**  
- **Shared scoring** for TEXI (executive functioning) and ARSQ (rejection sensitivity), and the YRBS-derived **substance PCA** dataset used by **Kirsten**.  
- **Danny** — abstract and submission materials.


---
<img src="images/icon.png" alt="icon" width="820">

## Directory Layout

```
Psychonomics_2025/
├─ arsqdata/
│  ├─ arsq_coding.Rmd
│  ├─ arsq_coding_2000.Rmd
│  ├─ arsq-rawcode.csv
│  ├─ 2000_arsq-rawcode_z.csv
│  └─ arsq-rawcode_z.csv
│
├─ texi-data/
│  ├─ texi-psychonom.Rmd
│  ├─ texi-psychon.csv
│  ├─ 2000texi.csv
│  └─ 3000texi.csv
│
├─ yrbsdata/
│  ├─ Risk_Project.Rmd
│  ├─ SA-scores-200-psychonomics copy.Rmd
│  ├─ SA-scores-3000-psychonomics.Rmd
│  └─ substance_scores.csv
│
├─ taskdata/
│  ├─ taskdata_2000.csv
│  └─ task_data_1000.csv
│
├─ Kirsten/
│  ├─ Kirsten-final/
│  │  └─ k_final.Rmd
│  ├─ Kirsten Results.docx
│  └─ Kirsten_Abstract-Psychonom.docx
│
├─ Megan/
│  ├─ stsscoring.Rmd
│  ├─ des-starts.Rmd
│  ├─ screen_time_data.csv
│  ├─ sts.xlsx
│  ├─ projectprep/
│  │  ├─ megan-psychonom-data-prep.Rmd
│  │  ├─ Lina-scored-data.csv
│  │  ├─ projectdata-start.csv
│  │  ├─ streamroomuse.csv
│  │  ├─ sleepdata.csv
│  │  └─ task-data.csv
│  └─ final/
│     ├─ megdawg-Psychonomics.Rmd
│     ├─ final-items.csv
│     ├─ Megan Abstract.docx
│     └─ MeganPsychonomics-analyses.docx
│
├─ Danny/
│  └─ Danny-Abstract-Psychonom.docx
│
└─ LItesubstanceabuse.csv
```

---

## Shared Scoring Pipelines

### 1) `texi-data/` — TEXI (Executive Functioning)
**Script:** `texi-psychonom.Rmd`  
**Input:** `texi-psychon.csv` (REDCap export)  
**Steps:**
- Map `record_id → PID`; fill missing PIDs from non-missing rows.
- Reverse-score items so **higher = better EF**.
- Compute `texi_total`; cohort-standardize:
  - `2000texi.csv` for PID 2000–2999 (teens)
  - `3000texi.csv` for PID 3000–3999 (adults)
**Outputs:** `PID`, `texi_total`, `texi_total.z`

---

### 2) `arsqdata/` — ARSQ (Rejection Sensitivity)
**Scripts:** `arsq_coding_2000.Rmd`, `arsq_coding.Rmd`  
**Input:** `arsq-rawcode.csv`  
**Steps:**
- Filter `redcap_event_name == "visit_1_y1_arm_1"`.
- Compute ARSQ concern×expectation composite across nine scenarios; create `arsq.score`.
- Z-score by cohort and export:
  - Teens → `2000_arsq-rawcode_z.csv`
  - Adults → `arsq-rawcode_z.csv`
**Outputs:** `PID`, `arsq.score`, `arsq_zscore`

---

### 3) `yrbsdata/` — Substance Use PCA (for Kirsten)
**Scripts:** `Risk_Project.Rmd`, `SA-scores-200-psychonomics copy.Rmd`, `SA-scores-3000-psychonomics.Rmd`  
**Input:** `substance_scores.csv` is produced here.  
**Steps (summarized from code):**
- Clean PIDs, keep valid REDCap event rows.
- Build frequency sets and **z-score** items.
- **PCA scores**:
  - **Alcohol:** `yrbs_alcfreq`, `yrbs_alccount`, `yrbs_alc45freq`
  - **Marijuana:** `yrbs_mjuse`, `yrbs_mjfreq`
  - **Nicotine:** `yrbs_cig_days`, `yrbs_cig_day_freq`, `yrbs_vape_days`, `yrbs_cigars`, `yrbs_tobacdays`
- Create `drug_use_ever` indicator.
- Join behavioral/self-report data (TEXI, Barretts, Zuckerman, Delay Discounting, tasks, ARSQ).
- Flip signs so larger values = worse control where appropriate; drop |z|>3 outliers.
- Save merged master: **`LItesubstanceabuse.csv`**

---

## Kirsten — Substance Use & Cognition (Independent Track)

**Location:** `Kirsten/Kirsten-final/k_final.Rmd`  
**Data:** `LItesubstanceabuse.csv` (+ cohort splits by age)  

### Analytic Steps
1. **Cohort split:**  
   - Teens: `df2k` (≈ PID 2000–2999, ages 15–17)  
   - Adults: `df3k` (≥18)
2. **Zero‑order correlations** among:
   - Substance PCA scores (`alcohol_pca_score`, `marijuana_pca_score`, `nicotine_pca_score`),  
   - Cognitive variables (`delay_discounting_indiff_z`, `texi_total.z`, `barrets.z`, `zuckerman.z`),  
   - `drug_use_ever`, `Flanker_Z`, `rpi.z`, `participant_age`.
3. **Median splits** to define *high vs. low* user categories for alcohol/weed/nicotine.
4. **MANCOVA + FDR‑corrected ANCOVAs** for group × age effects on cognitive outcomes.
5. **Shapley value decomposition** for each cohort and substance to quantify the %R² contributed by the cognitive predictors.
6. **Simple slopes** when age moderates alcohol–sensation seeking (`interactions::sim_slopes`).

### Key Results (from the code & results docs)
- **Weed:** Multivariate effect present; high-use group shows **higher impulsivity**, **lower EF**, **higher sensation seeking**. Effects **consistent across age**.  
- **Alcohol:** **Age‑moderated** association with **sensation seeking**; stronger in younger participants.  
- **Nicotine:** No reliable multivariate or univariate effects.  
- **Shapley (adults):** Sensation seeking (Zuckerman) explains the largest share of variance in composite use; Delay Discounting, Barretts, and TEXI contribute smaller portions.

**Supporting files:** `Kirsten Results.docx`, `Kirsten_Abstract-Psychonom.docx`

---

## Megan — Digital Immersion, EF, and Health (Independent Track)

**Location:** `Megan/`

### A) Objective Phone Data Cleaning
**Script:** `Megan/stsscoring.Rmd`  
**Input:** `Megan/sas-data/sts.csv`  
- Compute 10th‑percentile cutoffs across months for minutes, pickups, notifications.
- Set monthly triplets to `NA` **only if all three** are below cutoff (invalid sync).
- Create per‑participant means: `avg_minutes_clean`, `avg_pickups_clean`, `avg_notifs_clean`.
- QC flags ensure participants aren’t fully wiped.  
- **Output:** `Megan/screen_time_data.csv`

### B) Project Prep & Digital PCA
**Script:** `Megan/projectprep/megan-psychonom-data-prep.Rmd`  
- Merge REDCap baseline, stream/room, cleaned screen data, EF metrics (from `Lina-scored-data.csv`).
- Z‑score all inputs (except IDs/demographics).  
- **Digital immersion PCA** from: Streaming composite, Time‑on‑app, Phone checking, Public updates, Devices‑in‑room → `screen_behavior_pca_score`.
- Add tasks (Go/No‑Go d′, Flanker), self‑report (Barretts, Zuckerman, SAS), and health (sleep, body health).  
- Remove |z|>3 outliers.  
- **Output:** `Megan/final/final-items.csv`

### C) Final Analyses
**Script:** `Megan/final/megdawg-Psychonomics.Rmd`  
- Correlations (EF, impulsivity, health, age, digital indices).  
- **Mediation**: Screen → Sleep/Body Health → Barretts & TEXI (bootstrapped).  
- **MANCOVA/ANCOVA**: SAS class & objective use class × Sleep/Body Health predicting EF/impulsivity (age covariate).  
- **Output write‑up:** `MeganPsychonomics-analyses.docx`

---

## Danny — Abstract
**Location:** `Danny/Danny-Abstract-Psychonom.docx`  
Written abstract for the conference; no code.

---

## Master Data Artifacts
- **`LItesubstanceabuse.csv`** — Master table for **Kirsten** (substance PCA + cognition).  
- **`Megan/final/final-items.csv`** — Master table for **Megan** (digital indices + EF/health).  
- **`texi-data/2000texi.csv`, `3000texi.csv`** — TEXI z‑scores by cohort.  
- **`arsqdata/2000_arsq-rawcode_z.csv`, `arsq-rawcode_z.csv`** — ARSQ z‑scores by cohort.

---

## Dependencies (R ≥ 4.3)
```
tidyverse
dplyr
ggplot2
Hmisc
mediation
car
broom
knitr
kableExtra
ShapleyValue
psych
readr
```

---

## Reproducibility & Run Order

### A) Kirsten track (Substance & Cognition)
```r
# Set base directory used in scripts
base_dir <- "/Users/dannyzweben/Desktop/CABLAB_Files/Psychonomics_2025"
setwd(base_dir)

# Build substance PCA + merged table
rmarkdown::render("yrbsdata/Risk_Project.Rmd")         # produces LItesubstanceabuse.csv
# (If needed) Re-run cohort-specific scoring
rmarkdown::render("yrbsdata/SA-scores-200-psychonomics copy.Rmd")
rmarkdown::render("yrbsdata/SA-scores-3000-psychonomics.Rmd")

# Ensure TEXI/ARSQ are up to date
rmarkdown::render("texi-data/texi-psychonom.Rmd")
rmarkdown::render("arsqdata/arsq_coding_2000.Rmd")
rmarkdown::render("arsqdata/arsq_coding.Rmd")

# Main analysis
rmarkdown::render("Kirsten/Kirsten-final/k_final.Rmd")
```

### B) Megan track (Digital, EF, Health)
```r
base_dir <- "/Users/dannyzweben/Desktop/CABLAB_Files/Psychonomics_2025"
setwd(base_dir)

# Objective screen data cleaning
rmarkdown::render("Megan/stsscoring.Rmd")

# Merge, PCA, prep
rmarkdown::render("Megan/projectprep/megan-psychonom-data-prep.Rmd")

# Final analyses (correlation, mediation, MANCOVA)
rmarkdown::render("Megan/final/megdawg-Psychonomics.Rmd")
```

---

## Variable Quick Reference
- **Substance DVs (Kirsten):** `alcohol_pca_score`, `marijuana_pca_score`, `nicotine_pca_score`, `drug_use_ever`
- **Cognition (shared):** `texi_total.z`, `barrets.z`, `zuckerman.z`, `delay_discounting_indiff_z`, `Flanker_Z`, `rpi.z`
- **Digital (Megan):** `screen_behavior_pca_score`, `avg_minutes_clean.z`, `avg_pickups_clean.z`, `avg_notifs_clean.z`, `sas.z`
- **Health (Megan):** `sleep_composite.z`, `bodyhealth.z`
- **Demographics:** `PID`, `participant_age`

---

**Maintainer:** Danny Zweben  
**Status:** Ready for replication and poster figure generation.
