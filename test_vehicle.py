from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        "vehicle_no: KA25P3505\n"
        "owner_name: priya\n"
        "vehicle_type: car\n"
        "year_of_manufacture: 2008\n"
    )
    assert vehile_details("KA25P3505","priya","car",2008) == expected_output
