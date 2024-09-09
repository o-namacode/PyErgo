from typing import Optional, Union


def format_money(amount: Union[str, float], currency: Optional[str] = None) -> str:
    """
    Format a money amount with currency symbol.
    """

    # Allow exception to be raised if conversion fails
    if isinstance(amount, str):
        amount = float(amount)  # Convert string to float

    if not isinstance(amount, (int, float)):
        raise ValueError("Invalid amount type")

    if currency:
        return f"$ {amount:,.2f}".replace(",", ", ") + f" {currency.upper()}"
    else:
        return f"$ {amount:,.2f}".replace(",", ", ")