"""
Database models for SecureFlow
Stores scan history for trend analysis
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Scan(db.Model):
    """
    Represents a single security scan
    """
    __tablename__ = 'scans'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    target_path = db.Column(db.String(500), nullable=False)
    
    # Summary statistics
    total_findings = db.Column(db.Integer, default=0)
    critical = db.Column(db.Integer, default=0)
    high = db.Column(db.Integer, default=0)
    medium = db.Column(db.Integer, default=0)
    low = db.Column(db.Integer, default=0)
    
    # Scanner breakdown
    semgrep_findings = db.Column(db.Integer, default=0)
    trivy_findings = db.Column(db.Integer, default=0)
    trufflehog_findings = db.Column(db.Integer, default=0)
    
    # Duration
    duration_seconds = db.Column(db.Float, default=0.0)
    
    # Store JSON file path
    report_file = db.Column(db.String(500))
    
    def __repr__(self):
        return f'<Scan {self.id}: {self.timestamp} - {self.total_findings} findings>'
    
    def to_dict(self):
        """Convert to dictionary for JSON"""
        return {
            'id': self.id,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'target_path': self.target_path,
            'total_findings': self.total_findings,
            'critical': self.critical,
            'high': self.high,
            'medium': self.medium,
            'low': self.low,
            'semgrep': self.semgrep_findings,
            'trivy': self.trivy_findings,
            'trufflehog': self.trufflehog_findings,
            'duration': self.duration_seconds
        }
