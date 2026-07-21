# 🚀 SalesPipe CRM - Setup Guide

Complete step-by-step guide to get up and running with SalesPipe CRM.

## Prerequisites

- Modern web browser (Chrome, Safari, Firefox, Edge)
- Python 3.6+ (for bulk import script, optional)
- Your Excel file with leads (if using bulk import)

## Installation

### Step 1: Extract Files

```bash
unzip salespipe-crm.zip
cd salespipe-crm
```

### Step 2: Open the CRM

**Option A: Direct Open**
1. Find `CRM/SalesPipe_CRM.html`
2. Double-click to open in your browser
3. Application loads immediately

**Option B: Via Browser**
1. Open your browser
2. Press Ctrl+O (Windows) or Cmd+O (Mac)
3. Select `CRM/SalesPipe_CRM.html`
4. Click Open

## Data Import

### Option 1: Python Script (14,529 Leads)

**Prerequisites:**
- Python 3.6+
- Pandas library

**Steps:**

```bash
# 1. Ensure you have your Excel file
# Place: data/leads-10772054-300.xlsx

# 2. Install pandas (if needed)
pip install pandas

# 3. Run the import script
cd scripts
python3 crm_bulk_import.py

# 4. Output: crm_imported_data.json
# 5. Copy output to CRM folder
cp crm_imported_data.json ../CRM/

# 6. Open CRM in browser
# 7. Click "Import" button
# 8. Select crm_imported_data.json
```

### Option 2: CSV Files

**Manual Import:**

1. Open `CRM/SalesPipe_CRM.html`
2. Go to "Contacts" tab
3. Look for import option
4. Upload `data/pipedrive_persons.csv` first
5. Then upload `data/pipedrive_deals.csv`

**Note:** CSV import requires manual field mapping in the CRM

### Option 3: Manual Entry

1. Click "+ New Deal" button
2. Fill in:
   - Deal Title
   - Select Contact (or create new)
   - Choose Stage
   - Enter Value
   - Assign Owner
3. Click "Save Deal"

## First Time Setup

### Step 1: Add Your Team

```
1. Click "Contacts" tab
2. Click "+ Add Contact"
3. Enter contact info:
   - Name (required)
   - Email
   - Phone
   - Organization
4. Save
```

### Step 2: Add Your First Deal

```
1. Click "+ New Deal" (top right)
2. Enter:
   - Deal Title: "Acme Corp - Annual License"
   - Contact: Select from list
   - Stage: Choose (Lead, SQL, etc.)
   - Value: $50,000
3. Save
```

### Step 3: View Dashboard

```
1. Click "Dashboard" in sidebar
2. See metrics update in real-time:
   - Total Deals
   - Pipeline Value
   - Contact Count
   - Average Deal Size
   - Stage breakdown chart
```

## Using the CRM

### Dashboard
- **Real-time metrics** of your sales pipeline
- **Stage breakdown** showing where deals are
- **Pipeline value** total across all stages

### Deals Tab
- **View all deals** in table format
- **Track progress** through sales pipeline
- **See deal values** and assigned owner

### Contacts Tab
- **Store customer info** (name, email, phone, company)
- **Link deals** to contacts
- **See deal count** per contact

### Activities Tab
- **Log interactions** (calls, emails, meetings)
- **Timestamp** all activities
- **Track customer engagement**

### Reports Tab
- **Pipeline analysis** by stage
- **Revenue forecasting**
- **Team performance** metrics

### Export Tab
- **CSV Export** - Download all deals
- **JSON Backup** - Full data backup
- **Restore anytime** from backup

## Configuration

### Custom Fields

Add custom fields for your business:

1. Click "Fields" in sidebar
2. Click "+ Add Field"
3. Choose:
   - Field name (e.g., "Budget")
   - Type (Text, Number, Date, Dropdown)
   - Apply to (Deals, Contacts, Both)
4. Save

### Automation Rules

Set up automatic actions:

1. Click "Automation" in sidebar
2. Click "+ Create Rule"
3. Set:
   - When: (Deal created, Stage changed, etc.)
   - Then: (Send notification, Auto-assign, etc.)
4. Save and toggle On/Off

### Pipeline Stages

Default stages:
- Lead - New contact
- MQL - Marketing qualified
- SQL - Sales qualified
- SAL - Sales accepted
- Opportunity - Active deal
- Negotiation - Final stage
- Closed Won - Won deal
- Closed Lost - Lost deal

## Data Backup

### Regular Backups

```
1. Click "Export" tab
2. Click "Full Backup"
3. File downloads: backup-1234567890.json
4. Save to safe location
```

### Restore from Backup

```
1. Open backup-xxxx.json in text editor
2. Copy all content
3. Import via CRM import feature
4. Data restores completely
```

## Troubleshooting

### CRM Won't Open
- Ensure you're using a modern browser
- Try a different browser
- Check if JavaScript is enabled

### Data Not Saving
- Check browser storage is enabled
- Clear browser cache
- Try incognito/private mode
- Check browser console for errors

### Python Import Script Error
- Ensure pandas is installed: `pip install pandas`
- Check Excel file path is correct
- Verify Python version: `python3 --version`
- Run with: `python3 crm_bulk_import.py`

### Lost Data
- Check browser developer tools → Application → Local Storage
- Look for "salespipe-crm" key
- Can restore from backup JSON file

## Performance Tips

- **Archive old deals** to keep performance snappy
- **Export regularly** to backup data
- **Clear browser cache** monthly
- **Use latest browser** for best performance

## Privacy & Security

- ✅ **No data sent to servers** - Everything stays local
- ✅ **No tracking** - No analytics
- ✅ **No login required** - Direct access
- ✅ **Export anytime** - Never locked in

## Next Steps

1. ✅ Import your 14,529 leads
2. ✅ Train your sales team
3. ✅ Start logging deals and activities
4. ✅ Set up automation rules
5. ✅ Run weekly reports
6. ✅ Export backups regularly

## Support

For issues:

1. **Check browser console** - Press F12, click Console
2. **Export data** - Backup your work
3. **Clear cache** - Try fresh load
4. **Try different browser** - Test compatibility

Need to migrate to Pipedrive later? Use CSV files included in `data/` folder.

---

**Happy selling! 🚀**
