def vehicle_details(vehicle_no,owner_name,vehicle_type,year_of_manufacture):
    result=(
        f"Vehicle Number: {vehicle_no}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle_Type: {vehicle_type}\n"
        f"Year Of Manufacture: {year_of_manufacture}\n"
    )
    return result
if __name__=="__main__":
  vehicle_no="KA25P3505"
  owner_name="priya"
  vehicle_type="car"
  year_of_manufacture="2008"  
  print(vehicle_details(vehicle_no,owner_name,vehicle_type,year_of_manufacture))
