# Zoom Attendance Tracker

**Draw.io**: [Workflow Diagram](https://drive.google.com/file/d/1_N7xQqpITmObizHcJ7MeuGtOqFcDpEAd/view)

![Workflow Diagram](./zoom-attendance-workflow.png)

## Project Overview
The **Zoom Attendance Tracker** is an automated system designed to simplify and enhance attendance tracking and student engagement monitoring for online Zoom sessions. By extracting attendance logs directly from Zoom, the system generates detailed attendance reports and participation metrics, allowing educators to identify students who may need additional support.

This project helps educators save time, ensure accuracy in attendance records, and track student participation with minimal manual effort.

## Key Features
1. **Automated Attendance Tracking**:
   - Extracts attendance data from Zoom automatically after each session.
   - Generates daily, weekly, and monthly attendance reports.
   - Provides an easy-to-access and accurate attendance history.

2. **Participation Metrics**:
   - Tracks student engagement through session duration.
   - Calculates metrics for active participation, late entry, and early exit.
   - Provides insight into student behavior and engagement in each session.

3. **Interactive Dashboard**:
   - A visual interface displaying attendance trends and individual performance.
   - Utilizes charts and heatmaps for comparative analysis.
   - Offers a quick overview of class performance.

4. **Notifications and Alerts**:
   - Sends automatic notifications to students with low attendance or poor participation.
   - Alerts educators about students at risk of disengagement, enabling timely intervention.

## Working Flow

### 1. **Data Extraction**:
   - **Step 1**: After each Zoom session, the system connects to the Zoom API and extracts attendance logs (participant names, join times, leave times, total time attended).
   - **Step 2**: The attendance logs are stored in a structured database for easy access and future reference.

### 2. **Report Generation**:
   - **Step 3**: Based on the stored data, the system generates:
     - **Daily reports**: For attendance in individual sessions.
     - **Weekly reports**: Aggregated attendance for the entire week.
     - **Monthly reports**: Comprehensive attendance overview for the month.

### 3. **Participation Scoring**:
   - **Step 4**: The system calculates participation metrics:
     - **Late Entry**: Students who join after a predefined threshold.
     - **Early Exit**: Students who leave before the session ends.
     - **Active Participation**: Total time present in the session.

### 4. **Dashboard Visualization**:
   - **Step 5**: The participation and attendance data are visualized using charts and heatmaps:
     - **Attendance trends** over time.
     - **Individual performance** comparisons.
     - **Class participation breakdowns** to highlight any anomalies or consistent trends.

### 5. **Notifications and Alerts**:
   - **Step 6**: The system continuously monitors attendance and participation data.
     - Students with **low attendance or engagement** receive automated alerts via email or in-app notifications.
     - Educators are notified if any students are at risk of disengagement, allowing for early intervention.

### Workflow Diagram
For a detailed view of the project’s workflow, you can refer to the **[Workflow Diagram](https://drive.google.com/file/d/1_N7xQqpITmObizHcJ7MeuGtOqFcDpEAd/view?usp=sharing)**, which illustrates the complete process from data extraction to report generation and alerting.

## Technologies Used
- **Framework**: Django (for backend and web application)
- **Frontend**: JavaScript, HTML, CSS, Bootstrap (for the interactive dashboard)
- **Database**: MySQL (for storing attendance data)
- **APIs**: Zoom API (for attendance data extraction)
- **Visualization**: Plotly

