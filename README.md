# X Profile Opener

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Automation-Script-22D3EE?style=for-the-badge" alt="Automation" />
  <img src="https://img.shields.io/badge/OS-Webbrowser-Greeen?style=for-the-badge" alt="Webbrowser" />
</p>

A lightweight, efficient Python automation utility designed to iterate through a targeted list of X (Twitter) profiles directly from a CSV dataset. By listening for low-level global OS keypresses, it allows developers or data auditors to fast-review user profiles without manually copy-pasting links, while tracking progress through live system auditing files.

---

## Core Features

* **Smart Data Integration**: Seamlessly parses raw CSV spreadsheets, targeting handles listed under the `screen_name` column.
* **Global Hardware Hotkeys**: Run the script in the background and cycle through links using customizable, single-key commands.
* **Persistent Telemetry Logs**: Automatically creates and updates a flat text file (`history_log.txt`) that logs exactly when and which profiles were processed, complete with high-precision system timestamps.
* **Software Debouncing Logic**: Built-in state timers prevent hardware stutter from opening duplicated browser tabs with a single key press.
* **Low-Overhead Footprint**: Uses optimized polling sleep loops to run with near-zero CPU and resource utilization.

---

## Prerequisites & Setup

This automation utility requires **Python 3.x** and a couple of external dependencies. 

### 1. Install Dependencies
Open your development terminal and run:

pip install pandas keyboard

### 2. Prepare Your Dataset
Ensure your source data file is saved as file_csv.csv in the root directory. The file must contain a column named exactly screen_name:

```
id,screen_name,location
1,elonmusk,Texas
2,nasa,Space
```

## Controls
P - Next Profile
ESC - Terminate

## Technical Implementation Details
Data Management (pandas): Utilizes DataFrame vector analysis to process massive sheets instantly.
Native Interfacing (webbrowser): Connects directly to your operating system's default browser runtime configurations without requiring heavy webdriver installations (like Selenium).
System Optimization: Implements a 0.01 cooldown so you pc do not explode.
