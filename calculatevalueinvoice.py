def calculateValueInvoice(data):
    total = data['income'] - data['valueInvoice']
    return {"total": total}
