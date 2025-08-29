# Border Killing Trend Analysis in Bangladesh

This repository contains a comprehensive analysis of border killing incidents between Bangladesh and India by the Border Security Force (BSF) from 1971 to 2023.

## 📊 Project Overview

The project analyzes patterns and trends in border killings, examining the relationship between ruling parties in both countries and the frequency of incidents. The analysis provides insights into:

- Total killings by ruling party in India (BJP vs Congress)
- Total killings by ruling party in Bangladesh (BAL vs BNP vs Others)
- Average killings per year by political periods
- Temporal trends and patterns over 50+ years

## 🗂️ Repository Structure

```
├── src/
│   ├── analysis/
│   │   └── border_killings_analysis.py    # Main optimized analysis script
│   └── Border_Killing_inBD_byBSF_Prediction.ipynb  # Jupyter notebook analysis
├── data/
│   ├── border-inc.xlsx                     # Main dataset
│   └── avg values based on Rulling Parties.xlsx
├── docs/
│   └── SQLQuery1.sql                       # SQL queries for data processing
├── archive/
│   ├── generated_files/                    # Generated plots and HTML files
│   └── duplicate_files/                    # Legacy analysis scripts
└── plots/                                  # Generated visualization outputs
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Required packages (see requirements.txt)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/saajiidi/Border-Killing-Trend-in-Bangladesh.git
cd Border-Killing-Trend-in-Bangladesh
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Option 1: Run the optimized Python script
```bash
python src/analysis/border_killings_analysis.py
```

#### Option 2: Use Jupyter Notebook
```bash
jupyter notebook src/Border_Killing_inBD_byBSF_Prediction.ipynb
```

## 📈 Analysis Features

The main analysis script (`border_killings_analysis.py`) provides:

- **Comprehensive Data Loading**: Automatic path resolution and data cleaning
- **Summary Statistics**: Basic overview of the dataset
- **Party-wise Analysis**: Killings by ruling parties in both countries
- **Average Calculations**: Per-year averages by political periods
- **Trend Analysis**: Time series visualization with trend lines
- **Automated Reporting**: Complete analysis with optional plot saving

### Key Functions

```python
from src.analysis.border_killings_analysis import BorderKillingsAnalyzer

# Initialize analyzer
analyzer = BorderKillingsAnalyzer()

# Generate comprehensive report
analyzer.generate_comprehensive_report(save_plots=True)

# Individual analyses
analyzer.analyze_by_ruling_party_india()
analyzer.analyze_by_ruling_party_bangladesh()
analyzer.plot_average_killings_comparison()
analyzer.plot_trend_over_time()
```

## 📊 Data Sources

- **Primary Dataset**: `data/border-inc.xlsx`
- **Time Period**: 1971-2023
- **Key Variables**: Year, Killed, Injured, Ruling Party (BD), Ruling Party (India)

## 🔍 Key Findings

The analysis reveals significant patterns in border killings:

1. **Political Correlation**: Different ruling parties show varying incident rates
2. **Temporal Trends**: Clear patterns emerge over different political periods
3. **Bilateral Impact**: Both countries' political situations affect incident rates

## 🛠️ Technical Improvements

This repository has been optimized with:

- ✅ **Consolidated Code**: Single optimized script replacing multiple duplicates
- ✅ **Dynamic Paths**: No more hardcoded Windows paths
- ✅ **Proper Structure**: Organized directories for data, source, docs, and archives
- ✅ **Error Handling**: Robust data loading and processing
- ✅ **Documentation**: Comprehensive README and code comments
- ✅ **Dependencies**: Clear requirements specification

## 📁 Archive

The `archive/` directory contains:
- Legacy analysis scripts with hardcoded paths
- Generated files (plots, HTML exports)
- Duplicate data files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is available under the MIT License.

## 📧 Contact

For questions or collaboration opportunities, please open an issue in this repository.

---

**Note**: This analysis is for research and educational purposes. The data reflects documented incidents and should be interpreted within appropriate historical and political contexts.
