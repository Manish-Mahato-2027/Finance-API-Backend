# Utility functions

def format_currency(amount):
    """Format amount as currency string"""
    return f"${amount:,.2f}"


def calculate_percentage(part, total):
    """Calculate percentage"""
    if total == 0:
        return 0
    return round((part / total) * 100, 2)