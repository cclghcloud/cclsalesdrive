#!/usr/bin/env python3
"""
SalesPipe CRM - Bulk Import Script
Converts 14,529 leads from Excel into CRM-ready JSON format
"""

import json
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("Installing pandas...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "--break-system-packages"])
    import pandas as pd

def main():
    input_file = '../data/leads-10772054-300.xlsx'
    output_file = 'crm_imported_data.json'
    
    if not Path(input_file).exists():
        print(f"❌ Error: {input_file} not found")
        print("   Place your Excel file at: data/leads-10772054-300.xlsx")
        sys.exit(1)
    
    try:
        print("🚀 Starting bulk import...\n")
        print(f"📂 Reading {input_file}...")
        
        df = pd.read_excel(input_file)
        total_rows = len(df)
        print(f"✓ Loaded {total_rows:,} rows\n")
        
        print("Processing data...")
        contacts = {}
        deals = []
        stage_counts = {}
        stage_values = {}
        
        for idx, row in df.iterrows():
            if idx % 2000 == 0:
                print(f"  {idx:,}/{total_rows:,}...")
            
            contact_name = str(row.get('Contact person', '')).strip() if pd.notna(row.get('Contact person')) else ''
            if not contact_name or contact_name == 'nan':
                continue
            
            if contact_name not in contacts:
                contacts[contact_name] = {
                    'id': str(len(contacts) + 1),
                    'name': contact_name,
                    'email': str(row.get('Email', '')).strip() if pd.notna(row.get('Email')) and str(row.get('Email')) != 'nan' else '',
                    'phone': str(row.get('Phone Number', '')).strip() if pd.notna(row.get('Phone Number')) and str(row.get('Phone Number')) != 'nan' else '',
                    'organization': str(row.get('Organization', '')).strip() if pd.notna(row.get('Organization')) and str(row.get('Organization')) != 'nan' else ''
                }
            
            stage = str(row.get('Lead Stage', 'Lead')).strip() if pd.notna(row.get('Lead Stage')) else 'Lead'
            if not stage or stage == 'nan':
                stage = 'Lead'
            
            try:
                deal_value = float(row.get('Value', 0)) if pd.notna(row.get('Value')) else 0
            except:
                deal_value = 0
            
            deal = {
                'id': str(row.get('ID', f'd-{idx}')) if pd.notna(row.get('ID')) else f'd-{idx}',
                'title': str(row.get('Title', f'Deal from {contact_name}')).strip() if pd.notna(row.get('Title')) else f'Deal from {contact_name}',
                'contactId': contacts[contact_name]['id'],
                'stage': stage,
                'value': deal_value,
                'owner': str(row.get('Owner', '')).strip() if pd.notna(row.get('Owner')) and str(row.get('Owner')) != 'nan' else ''
            }
            
            deals.append(deal)
            stage_counts[stage] = stage_counts.get(stage, 0) + 1
            stage_values[stage] = stage_values.get(stage, 0) + deal_value
        
        contacts_list = list(contacts.values())
        total_value = sum(d['value'] for d in deals)
        
        crm_data = {
            'contacts': contacts_list,
            'deals': deals,
            'metadata': {
                'totalContacts': len(contacts_list),
                'totalDeals': len(deals),
                'totalValue': total_value,
                'dealsWithValue': sum(1 for d in deals if d['value'] > 0),
                'stageBreakdown': stage_counts,
                'stageValues': stage_values
            }
        }
        
        with open(output_file, 'w') as f:
            json.dump(crm_data, f, indent=2)
        
        print("\n" + "="*70)
        print("✅ IMPORT SUCCESSFUL!")
        print("="*70)
        
        print(f"\n📊 Summary:")
        print(f"   Contacts: {len(contacts_list):,}")
        print(f"   Deals: {len(deals):,}")
        print(f"   Pipeline Value: ${total_value:,.2f}")
        print(f"   Deals with Values: {crm_data['metadata']['dealsWithValue']:,}")
        
        print(f"\n📈 By Stage:")
        for stage in sorted(stage_counts.keys()):
            count = stage_counts[stage]
            value = stage_values.get(stage, 0)
            print(f"   {stage:25} │ {count:6,} deals │ ${value:>15,.2f}")
        
        print(f"\n📁 Output: {output_file}")
        print(f"\n🚀 Next Step:")
        print(f"   1. Open CRM/SalesPipe_CRM.html in your browser")
        print(f"   2. Click 'Import' button")
        print(f"   3. Select {output_file}")
        print(f"   4. Click 'Confirm'")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
