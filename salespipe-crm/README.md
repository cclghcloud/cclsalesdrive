# 🚀 SalesPipe CRM

A lightweight, browser-based CRM system with Pipedrive-like features. No servers, no subscriptions, all data stays with you.

**14,529 pre-loaded leads | 13,319 unique contacts | Ready to use immediately**

## ✨ Features

### Core CRM
- 📊 **Sales Dashboard** - Real-time pipeline metrics and visualization
- 💼 **Deal Management** - Track opportunities through 8 pipeline stages
- 👥 **Contact Database** - Store customer information with email and phone
- 📅 **Activity Logging** - Log calls, emails, meetings, demos, and notes
- 📈 **Sales Reports** - Pipeline analysis and revenue forecasting

### Advanced Features
- ⚙️ **Automation Rules** - Auto-assign deals, high-value alerts, follow-up tasks
- 🔧 **Custom Fields** - Add unlimited fields (text, number, date, dropdown)
- 📧 **Email Integration** - Ready for Gmail, Outlook, Slack connections
- 💾 **Data Export** - Download as CSV or JSON anytime
- 🔒 **Local Storage** - All data stays in your browser (no servers)

## 🚀 Quick Start

### 1. Open the CRM
```bash
# Download SalesPipe_CRM.html and double-click to open in your browser
# Or open via: File → Open → SalesPipe_CRM.html
```

### 2. Import Your Data
Three options:

**Option A: Python Script (Recommended)**
```bash
python3 scripts/crm_bulk_import.py
# Creates: crm_imported_data.json
# Upload to CRM via Import button
```

**Option B: CSV Files**
- Use `data/pipedrive_persons.csv` (13,319 contacts)
- Use `data/pipedrive_deals.csv` (14,529 deals)

**Option C: Manual Entry**
- Click "+ New Deal" and add deals manually
- Click "+ Add Contact" for customers

### 3. Start Using
- View dashboard metrics
- Add deals and track through pipeline
- Log customer activities
- Export backups regularly

## 📊 What's Included

| File | Purpose |
|------|---------|
| `CRM/SalesPipe_CRM.html` | Main CRM application (standalone, no installation) |
| `scripts/crm_bulk_import.py` | Python script to process 14,529 leads |
| `data/pipedrive_persons.csv` | 13,319 unique contacts |
| `data/pipedrive_deals.csv` | 14,529 sales deals |
| `docs/SETUP_GUIDE.md` | Detailed setup instructions |
| `docs/FEATURES.md` | Complete feature documentation |

## 🔄 Two-Phase Strategy

### Phase 1: Use SalesPipe CRM (Weeks 1-4)
- ✅ No cost
- ✅ Immediate access
- ✅ Full control
- ✅ Test your workflow

### Phase 2: Migrate to Pipedrive (Week 5+)
- Use `data/pipedrive_*.csv` files
- Import directly to Pipedrive
- Keep SalesPipe as backup

## 💡 Key Capabilities

### Dashboard
- Total deals count
- Pipeline value ($)
- Contact count
- Average deal size
- Stage-by-stage breakdown

### Pipeline Management
8 Standard Stages:
1. Lead - Initial contact
2. MQL - Marketing qualified
3. SQL - Sales qualified
4. SAL - Sales accepted
5. Opportunity - Active opportunity
6. Negotiation - Final stages
7. Closed Won - Successful deals
8. Closed Lost - Lost opportunities

### Data Your Data Includes
- **Contact Name** - Person's name
- **Email** - Contact email address
- **Phone** - Contact phone number
- **Organization** - Company name
- **Deal Title** - Opportunity name
- **Deal Stage** - Current pipeline stage
- **Deal Value** - Monetary amount
- **Deal Owner** - Sales representative

## 🎯 Use Cases

✅ Small sales teams (1-20 people)
✅ Startup CRM needs
✅ Local data requirements
✅ No vendor lock-in preference
✅ Quick evaluation phase
✅ Training and testing

## 🔒 Privacy & Security

- **No servers** - Data stays in your browser
- **No tracking** - No analytics or telemetry
- **No cloud sync** - Complete local control
- **Export anytime** - Never locked in
- **GDPR compliant** - No data sharing

## 📱 Browser Compatibility

✅ Chrome (latest)
✅ Safari (latest)
✅ Firefox (latest)
✅ Edge (latest)

Mobile browsers: Partial support

## 🚀 Getting Started

1. **Download** the files
2. **Open** `CRM/SalesPipe_CRM.html` in your browser
3. **Import** data (Python script or CSV)
4. **Start selling** - Add deals and track progress

## 📖 Documentation

See `docs/` folder for:
- `SETUP_GUIDE.md` - Step-by-step setup
- `FEATURES.md` - Detailed feature guide
- `MIGRATION_GUIDE.md` - How to move to Pipedrive

## 💬 Support

This is a standalone CRM. No external support needed.

For Python script issues:
- Ensure Python 3.6+
- Install pandas: `pip install pandas`
- Run: `python3 scripts/crm_bulk_import.py`

## 📄 License

MIT License - See LICENSE file

## 🎉 What's Next?

1. Extract the ZIP file
2. Open `CRM/SalesPipe_CRM.html`
3. Click "+ New Deal" to add your first opportunity
4. Import 14,529 leads via Python script
5. Share with your sales team

**Happy selling! 🚀**
