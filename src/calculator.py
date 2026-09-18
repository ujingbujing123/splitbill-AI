from typing import Dict, List
from src.extractor import ReceiptData

def calculate_split(
    receipt: ReceiptData,
    item_assignments: Dict[int, List[str]]  # index_item: [nama_orang1, nama_orang2]
) -> Dict[str, float]:
    """
    Menghitung total tagihan per orang termasuk pajak & service fee secara proporsional.
    """
    person_subtotal = {}

    # Hitung porsi subtotal per orang
    for idx, item in enumerate(receipt.items):
        assigned_people = item_assignments.get(idx, [])
        if not assigned_people:
            continue
        
        split_price = item.total_price / len(assigned_people)
        for person in assigned_people:
            person_subtotal[person] = person_subtotal.get(person, 0.0) + split_price

    total_extra_fees = receipt.tax + receipt.service_charge + receipt.other_fees
    results = {}

    # Bagi ekstra fee secara proporsional terhadap subtotal individu
    for person, subtotal in person_subtotal.items():
        if receipt.subtotal > 0:
            proportion = subtotal / receipt.subtotal
        else:
            proportion = 0
            
        extra_fee_share = total_extra_fees * proportion
        results[person] = round(subtotal + extra_fee_share, 2)

    return results