# 🏙️ Urban Flood Risk Mapping Tool

An interactive Python + Streamlit application that estimates urban flood risk using rainfall data and land use information. Built using the SCS Curve Number method, the tool allows users to simulate runoff and visualize flood-prone areas on a map.

## 🚀 Live Demo  
👉 [Launch the App](https://urban_flood_tool.streamlit.app) 

## 📦 Features
- Upload land use polygons (GeoJSON)
- Upload Curve Number (CN) table (CSV)
- Input custom rainfall (in mm)
- Runoff estimation using **SCS Curve Number Method**
- Interactive flood risk map (low vs high runoff)
- Color-coded output and data overlay

## 📁 Project Structure
```
urban_flood_tool/
├── app.py                     # Streamlit application code
├── requirements.txt           # Python dependencies
└── data/
    ├── sample_landuse.geojson     # Sample land use polygons
    └── curve_number_table.csv     # Sample CN lookup table
```

## 📥 How to Use

### 1. Clone the Repo
```bash
git clone https://github.com/kapase16/urban_flood_tool.git
cd urban_flood_tool
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App Locally
```bash
streamlit run app.py
```

## 📊 Input File Formats

### `curve_number_table.csv`
| land_use     | CN  |
|--------------|-----|
| Residential  | 85  |
| Park         | 65  |
| Commercial   | 92  |
| Industrial   | 90  |

### `sample_landuse.geojson`
A GeoJSON file with polygons, each having a `"land_use"` property.

## ⚙️ Methods Used

Uses the **SCS Curve Number Method**:

\[
Q = \begin{cases}
0, & P \leq 0.2S \\
\frac{(P - 0.2S)^2}{(P + 0.8S)}, & P > 0.2S
\end{cases}
\quad where \quad S = \frac{25400}{CN} - 254
\]

## 🧑‍💻 Author
**Yogesh Kapase**  
📧 kapaseyogesh16@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/yk16/)
