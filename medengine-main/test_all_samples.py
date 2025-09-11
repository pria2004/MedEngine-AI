#!/usr/bin/env python3
"""
Test script for all 10 sample patient files
"""
import sys
sys.path.insert(0, r'c:\Users\ADMIN\OneDrive\Desktop\medengine-main\backend')

from predict import HospitalReadmissionPredictor
import pandas as pd
import os

def test_sample_file(filename, description):
    """Test a sample CSV file and show results"""
    print(f"\n{'='*60}")
    print(f"🏥 TESTING: {description}")
    print(f"📄 FILE: {filename}")
    print('='*60)
    
    try:
        # Load the CSV file
        df = pd.read_csv(filename)
        print(f"📊 Loaded {len(df)} patients from {filename}")
        
        # Convert to list of dictionaries
        patients = df.to_dict('records')
        
        # Initialize predictor
        predictor = HospitalReadmissionPredictor()
        
        # Make predictions
        results = predictor.predict_batch(patients, threshold=0.4)
        
        print(f"\n🎯 PREDICTION RESULTS:")
        print("-" * 50)
        
        high_risk_count = 0
        medium_risk_count = 0
        low_risk_count = 0
        
        for i, result in enumerate(results):
            if 'error' not in result:
                prob = result['probabilities']['readmitted']
                prediction = result['predictions']['custom_threshold_0.4']['result']
                risk_level = result['risk_assessment']['risk_level']
                
                print(f"Patient {i+1:2d}: {prob*100:5.1f}% | {prediction:15s} | {risk_level}")
                
                if prob >= 0.7:
                    high_risk_count += 1
                elif prob >= 0.4:
                    medium_risk_count += 1
                else:
                    low_risk_count += 1
            else:
                print(f"Patient {i+1:2d}: ERROR - {result['error']}")
        
        print(f"\n📈 SUMMARY:")
        print(f"   High Risk (≥70%):    {high_risk_count} patients")
        print(f"   Medium Risk (40-69%): {medium_risk_count} patients") 
        print(f"   Low Risk (<40%):      {low_risk_count} patients")
        
    except Exception as e:
        print(f"❌ ERROR testing {filename}: {e}")

def main():
    """Test all sample files"""
    os.chdir(r'c:\Users\ADMIN\OneDrive\Desktop\medengine-main')
    
    sample_files = [
        ("sample_patients_high_risk.csv", "High Risk Cardiac & Diabetes Patients"),
        ("sample_patients_low_risk.csv", "Low Risk Young Patients"),
        ("sample_patients_medium_risk.csv", "Medium Risk Mixed Patients"),
        ("sample_patients_diabetes_cardiac.csv", "Elderly Diabetes & Cardiac"),
        ("sample_patients_emergency_respiratory.csv", "Emergency & Respiratory Cases"),
        ("sample_patients_surgery.csv", "Surgical Patients"),
        ("sample_patients_young_healthy.csv", "Young Healthy Patients"),
        ("sample_patients_elderly_complex.csv", "Elderly Complex Cases"),
        ("sample_patients_mixed_diagnosis.csv", "Mixed Diagnosis Patients"),
        ("sample_patients_comprehensive.csv", "Comprehensive Test Cases")
    ]
    
    print("🚀 MEDENGINE ML MODEL TESTING")
    print("Testing 10 different patient scenarios...")
    
    for filename, description in sample_files:
        test_sample_file(filename, description)
    
    print(f"\n{'='*60}")
    print("✅ ALL TESTS COMPLETED!")
    print("='*60")

if __name__ == "__main__":
    main()
