"""
Enhanced PDF Report Generator for SecureFlow
Includes detailed findings with fix recommendations
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime

class PDFReportGenerator:
    def __init__(self, report_data, output_path, semgrep_findings=None, trivy_findings=None, trufflehog_findings=None):
        self.report = report_data
        self.output = output_path
        self.semgrep = semgrep_findings or []
        self.trivy = trivy_findings or []
        self.trufflehog = trufflehog_findings or []
        
        self.doc = SimpleDocTemplate(
            output_path, 
            pagesize=letter,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=30
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        self.create_custom_styles()
    
    def create_custom_styles(self):
        """Create custom text styles"""
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            textColor=colors.HexColor('#6366f1'),
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        self.section_style = ParagraphStyle(
            'SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#4f46e5'),
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        )
        
        self.subsection_style = ParagraphStyle(
            'SubsectionHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            textColor=colors.HexColor('#6366f1'),
            spaceAfter=8,
            spaceBefore=10,
            fontName='Helvetica-Bold'
        )
        
        self.finding_title_style = ParagraphStyle(
            'FindingTitle',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#1f2937'),
            fontName='Helvetica-Bold',
            spaceAfter=4
        )
        
        self.code_style = ParagraphStyle(
            'Code',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            textColor=colors.HexColor('#374151'),
            leftIndent=10,
            spaceAfter=4
        )
    
    def add_title_page(self):
        """Cover page"""
        title = Paragraph("SecureFlow Security Report", self.title_style)
        self.story.append(title)
        self.story.append(Spacer(1, 0.3*inch))
        
        scan_date = datetime.now().strftime('%B %d, %Y at %H:%M')
        subtitle = Paragraph(f"<font size=14 color='#6b7280'>Generated on {scan_date}</font>", self.styles['Normal'])
        subtitle.alignment = TA_CENTER
        self.story.append(subtitle)
        self.story.append(Spacer(1, 0.5*inch))
        
        # Summary box
        summary = f"""
        <para align=center>
        <b><font size=12>Security Assessment Summary</font></b><br/>
        <font size=10>Automated security scanning results using:<br/>
        Semgrep • Trivy • TruffleHog</font>
        </para>
        """
        self.story.append(Paragraph(summary, self.styles['Normal']))
        self.story.append(PageBreak())
    
    def add_executive_summary(self):
        """Summary statistics"""
        header = Paragraph("Executive Summary", self.section_style)
        self.story.append(header)
        
        summary_data = [
            ['Metric', 'Count', 'Status'],
            [
                'Total Findings', 
                str(self.report.get('total_findings', 0)),
                '⚠️ Action Required' if self.report.get('total_findings', 0) > 0 else '✅ Clean'
            ],
            ['Critical Severity', str(self.report.get('by_severity', {}).get('CRITICAL', 0)), '🔴 Immediate'],
            ['High Severity', str(self.report.get('by_severity', {}).get('HIGH', 0)), '🟠 Urgent'],
            ['Medium Severity', str(self.report.get('by_severity', {}).get('MEDIUM', 0)), '🟡 Important'],
            ['Low Severity', str(self.report.get('by_severity', {}).get('LOW', 0)), '🟢 Monitor'],
        ]
        
        table = Table(summary_data, colWidths=[2.5*inch, 1.5*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6366f1')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#f3f4f6')),
            ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#fee2e2')),
            ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#ffedd5')),
            ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#fef9c3')),
            ('BACKGROUND', (0, 5), (-1, 5), colors.HexColor('#dcfce7')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#d1d5db')),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        self.story.append(table)
        self.story.append(Spacer(1, 0.3*inch))
    
    def add_scanner_breakdown(self):
        """Scanner statistics"""
        header = Paragraph("Findings by Scanner", self.section_style)
        self.story.append(header)
        
        scanner_data = [['Scanner', 'Type', 'Findings']]
        for scanner_name, scanner_info in self.report.get('by_scanner', {}).items():
            scanner_data.append([
                scanner_name.title(),
                scanner_info.get('type', 'Unknown'),
                str(scanner_info.get('findings', 0))
            ])
        
        table = Table(scanner_data, colWidths=[2*inch, 2.5*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4f46e5')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        self.story.append(table)
        self.story.append(PageBreak())
    
    def add_semgrep_details(self):
        """Detailed Semgrep findings"""
        if not self.semgrep:
            return
        
        header = Paragraph(f"Semgrep Code Analysis ({len(self.semgrep)} findings)", self.section_style)
        self.story.append(header)
        
        # Show top 15 findings
        for i, finding in enumerate(self.semgrep[:15], 1):
            # Finding title
            severity_color = '#dc2626' if finding['severity'] == 'ERROR' else '#ea580c'
            title_text = f"<b>{i}. {finding['severity']}: {finding['rule_id'][:60]}</b>"
            title = Paragraph(title_text, self.finding_title_style)
            self.story.append(title)
            
            # Details table
            details_data = [
                ['File:', finding['file']],
                ['Line:', str(finding['line'])],
                ['Category:', finding['category']],
                ['Issue:', finding['message'][:100]]
            ]
            
            details_table = Table(details_data, colWidths=[1*inch, 5*inch])
            details_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d1d5db')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ]))
            
            self.story.append(details_table)
            
            # Fix recommendation
            fix_text = self._get_fix_recommendation(finding['rule_id'])
            fix = Paragraph(f"<b>Fix:</b> {fix_text}", self.code_style)
            self.story.append(fix)
            self.story.append(Spacer(1, 0.15*inch))
        
        if len(self.semgrep) > 15:
            more = Paragraph(f"<i>... and {len(self.semgrep) - 15} more findings</i>", self.styles['Normal'])
            self.story.append(more)
        
        self.story.append(PageBreak())
    
    def add_trivy_details(self):
        """Detailed Trivy findings"""
        if not self.trivy:
            return
        
        header = Paragraph(f"Trivy Dependency Vulnerabilities ({len(self.trivy)} CVEs)", self.section_style)
        self.story.append(header)
        
        for i, vuln in enumerate(self.trivy[:15], 1):
            severity_color = '#dc2626' if vuln['severity'] == 'CRITICAL' else '#ea580c'
            title_text = f"<b>{i}. {vuln['severity']}: {vuln['cve_id']}</b>"
            title = Paragraph(title_text, self.finding_title_style)
            self.story.append(title)
            
            details_data = [
                ['Package:', vuln['package']],
                ['Installed:', vuln['installed_version']],
                ['Fixed In:', vuln['fixed_version'] if vuln['fixed_version'] else 'Not available'],
                ['Issue:', vuln['title'][:80]]
            ]
            
            details_table = Table(details_data, colWidths=[1*inch, 5*inch])
            details_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f3f4f6')),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d1d5db')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ]))
            
            self.story.append(details_table)
            
            if vuln['fixed_version']:
                fix_cmd = f"pip install {vuln['package']}=={vuln['fixed_version'].split(',')[0].strip()}"
                fix = Paragraph(f"<b>Fix:</b> <font name='Courier'>{fix_cmd}</font>", self.code_style)
                self.story.append(fix)
            
            self.story.append(Spacer(1, 0.15*inch))
        
        if len(self.trivy) > 15:
            more = Paragraph(f"<i>... and {len(self.trivy) - 15} more CVEs</i>", self.styles['Normal'])
            self.story.append(more)
        
        self.story.append(PageBreak())
    
    def add_trufflehog_details(self):
        """Detailed TruffleHog findings"""
        if not self.trufflehog:
            return
        
        header = Paragraph(f"TruffleHog Secret Detection ({len(self.trufflehog)} secrets)", self.section_style)
        self.story.append(header)
        
        for i, secret in enumerate(self.trufflehog, 1):
            title_text = f"<b>{i}. SECRET: {secret['reason']}</b>"
            title = Paragraph(title_text, self.finding_title_style)
            self.story.append(title)
            
            details_data = [
                ['File:', secret['filepath']],
                ['Type:', secret['reason']],
                ['Date:', secret['date']],
            ]
            
            details_table = Table(details_data, colWidths=[1*inch, 5*inch])
            details_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#fee2e2')),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#fca5a5')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ]))
            
            self.story.append(details_table)
            
            fix_steps = """1. Remove secret from code
2. Add to .env file
3. Add .env to .gitignore
4. Use os.getenv() to access
5. Rotate the leaked secret immediately"""
            fix = Paragraph(f"<b>Fix Steps:</b><br/>{fix_steps}", self.code_style)
            self.story.append(fix)
            self.story.append(Spacer(1, 0.15*inch))
        
        self.story.append(PageBreak())
    
    def _get_fix_recommendation(self, rule_id):
        """Get fix recommendation based on rule"""
        rule_lower = rule_id.lower()
        
        if 'sql' in rule_lower or 'injection' in rule_lower:
            return "Use parameterized queries: cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))"
        elif 'eval' in rule_lower:
            return "Never use eval() on user input. Use ast.literal_eval() for safe parsing."
        elif 'command' in rule_lower or 'os-system' in rule_lower:
            return "Use subprocess with list args: subprocess.run(['cmd', arg], capture_output=True)"
        elif 'secret' in rule_lower or 'api-key' in rule_lower:
            return "Move to environment variables: os.getenv('API_KEY'). Add to .env file."
        elif 'xss' in rule_lower or 'html' in rule_lower:
            return "Escape user input before rendering HTML. Use template auto-escaping."
        elif 'path' in rule_lower or 'traversal' in rule_lower:
            return "Validate paths with os.path.realpath() and check against allowed directories."
        else:
            return "Review OWASP guidelines for remediation best practices."
    
    def add_footer(self):
        """Add disclaimer"""
        footer_text = """
        <para align=center>
        <font size=8 color='#9ca3af'>
        <b>Generated by SecureFlow v2.0</b><br/>
        This report is based on automated scanning and may contain false positives.<br/>
        Manual verification recommended for all findings.<br/>
        GitHub: https://github.com/Kali-ai007/SecureFlow
        </font>
        </para>
        """
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(Paragraph(footer_text, self.styles['Normal']))
    
    def generate(self):
        """Build complete PDF"""
        print(f"📄 Generating detailed PDF report: {self.output}")
        
        self.add_title_page()
        self.add_executive_summary()
        self.add_scanner_breakdown()
        self.add_semgrep_details()
        self.add_trivy_details()
        self.add_trufflehog_details()
        self.add_footer()
        
        self.doc.build(self.story)
        print(f"✅ Detailed PDF generated with {len(self.semgrep) + len(self.trivy) + len(self.trufflehog)} findings!")
        return self.output
