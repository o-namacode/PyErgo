from typing import Optional


def format_money(amount: float, currency: Optional[str] = None) -> str:
    """
    Format a money amount with currency symbol.
    """
    if currency:
        return f"$ {amount:,.2f}".replace(",", ", ") + f" {currency.upper()}"
    else:
        return f"$ {amount:,.2f}".replace(",", ", ")